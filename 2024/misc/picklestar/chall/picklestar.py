import pickle
import pickletools
from blacklist import BLACKLISTED_OPCODES

def check(obj):
    status = True
    opcodes=[]
    for i in pickletools.genops(obj):
        opcode = i[0]
        opcodes.append(opcode.name)
    for name in opcodes:
        if name in BLACKLISTED_OPCODES:
            status = False
    return status


while True:
    p = bytes.fromhex(input('Gimme pickles: '))
    
    if len(p) > 20:
        print('Nope!')
        exit()

    if not check(p):
        print('Forbidden pickle!!')
        exit()
    
    print(pickle.loads(p))