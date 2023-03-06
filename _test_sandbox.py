
#!/usr/bin/python3.8

from sandbox import Sandbox

s = Sandbox()

# cmd ="""
# print("Hello test sandbox")
# """


# Prevent file writing? How?
# we can put "open" builtin function in a blacklist
# So that the attacker cannot write to file. (1)
# but what if it is encrypted. (2)
# cmd_write_file = """
# open("example.txt", "w").write("open run")
# """

# s.execute(cmd_write_file)

# # (1)
# cmd_builtin_open = """
# func = __builtins__["open"]
# func("example.txt", "w").write("meow >>")
# """
# s.execute(cmd_builtin_open)


# # (2)
# encrypted_cmd_builtin_open = """
# func = __builtins__["open"]
# func("example.txt", "w").write("meow >>")
# """
# s.execute(encrypted_cmd_builtin_open)

def random_string(size):
    import string, random
    return ''.join([string.ascii_letters[random.randint(0, 51)] for x in range(size)])

import unittest
#python3 -m unittest -v _test_sandbox.py


class TestSandbox(unittest.TestCase):
    def setUp(self):
        import os.path
        if not os.path.exists("example.txt"):
            fp = open('example.txt', 'x')
            fp.close()

    def test_open_function(self):
        s = Sandbox()
        #rs = random_string(8)
        cmd_write_file = """
open("example.txt", "w").write(">> random_string")
"""
        with self.assertRaises(NameError):
            s.execute(cmd_write_file)
    
    def test_builtin_open(self):
        s = Sandbox()
        #rs = random_string(8)
        cmd_builtin_open = """
func = __builtins__["open"]
func("example.txt", "w").write(">> random_string")
"""
        with self.assertRaises(KeyError):
            s.execute(cmd_builtin_open)


    def test_encrypted_builtin_open(self):
        s = Sandbox()
        #rs = random_string(8)
        cmd_builtin_open = """
        # https://docs.python.org/3/library/codecs.html#text-transforms
import codecs
func = __builtins__[codecs.decode("bcra", 'rot_13')]
func("example.txt", "w").write(">> random_string")
"""
        with self.assertRaises(KeyError):
            s.execute(cmd_builtin_open)


    def test_os_package(self):
        s = Sandbox()
        cmd = """
import os
fd = os.open("example.txt", os.O_RDWR|os.O_CREAT)
os.write(fd, bytes(">> import os unsecure", 'utf-8'))
"""
        # with self.assertRaises(KeyError):
        #     s.execute(cmd)
        s.execute(cmd)