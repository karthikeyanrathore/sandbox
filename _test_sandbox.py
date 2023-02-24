
#!/usr/bin/python3.8

from sandbox import Sandbox

s = Sandbox()
cmd ="""
print("Hello test sandbox")
"""


# Prevent file writing? How?
# we can put "open" builtin function in a blacklist
# So that the attacker cannot write to file. (1)
# but what if it is encrypted. (2)
cmd_write_file = """
open("example.txt", "w").write("jailbreak")
"""


# (1)
cmd_builtin_open = """
func = __builtins__["open"]
func("example.txt", "w").write("meow >>")
"""
s.execute(cmd_builtin_open)

