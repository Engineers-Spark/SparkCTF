import angr
import sys
import claripy

sys.set_int_max_str_digits(9999999)

p = angr.Project("./rusty_flag_checker/target/sparkctf/rusty_flag_checker")

input_size = 35  # size in bytes
stdin = claripy.BVS('stdin', input_size * 8)  # 8 bits per byte

newline = claripy.BVV(b'\n')
stdin_with_newline = claripy.Concat(stdin, newline)

state = p.factory.full_init_state(stdin=stdin_with_newline)
state.options.add(angr.options.BYPASS_UNSUPPORTED_SYSCALL)

for i in range(input_size):
    byte = stdin.get_byte(i)
    state.solver.add(byte > 0x20, byte <= 0x7E)
    state.solver.add(byte != ord("\\"))


sm = p.factory.simulation_manager(state)
sm.use_technique(angr.exploration_techniques.dfs.DFS())

dep = 0
while len(sm.active) > 0:
  dep += 1
  sm.step()
  print(dep, sm, len(sm.deadended + sm.active))
  for s in sm.deadended + sm.active:
    stdin = s.posix.dumps(0)    
    stdout = s.posix.dumps(1)
    print(stdout)
    print(stdin)
    if stdin and (b"Well done" in stdout):
      print(stdin)
      exit()