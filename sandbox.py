#!/usr/bin/env python3

# chmod +x sandbox.py
# ./sandbox


# Will fail
# BLK_LIST = (
#     "open"
# )

WT_LIST = [
'__name__', '__doc__', '__package__', '__loader__', '__spec__', '__build_class__', '__import__', 'abs', 'all', 
'any', 'ascii', 'bin', 'callable', 'chr', 'compile', 'delattr', 'dir', 'divmod', 'format', 'getattr', 'globals'
, 'hasattr', 'hash', 'hex', 'id', 'input', 'isinstance', 'issubclass', 'iter', 'len', 'locals', 'max', 'min', 
'next', 'oct', 'ord', 'pow', 'print', 'repr', 'round', 'setattr', 'sorted', 'sum', 'vars', 'None', 'Ellipsis', 'NotImplemented', 
'False', 'True', 'bool', 'memoryview', 'bytearray', 'bytes', 'classmethod', 'complex', 'dict', 'enumerate', 'filter', 'float', 'frozenset', 
'property', 'int', 'list', 'map', 'object', 'range', 'reversed', 'set', 'slice', 'staticmethod', 'str', 'super', 
'tuple', 'type', 'zip', '__debug__', 'BaseException', 'Exception', 'TypeError', 'StopAsyncIteration', 'StopIteration', 
'GeneratorExit', 'SystemExit', 'KeyboardInterrupt', 'ImportError', 'ModuleNotFoundError', 'OSError', 'EnvironmentError',
'IOError', 'EOFError', 'RuntimeError', 'RecursionError', 'NotImplementedError', 'NameError', 'UnboundLocalError', 'AttributeError', 
'SyntaxError', 'IndentationError', 'TabError', 'LookupError', 'IndexError', 'KeyError', 'ValueError', 'UnicodeError', 'UnicodeEncodeError', 
'UnicodeDecodeError', 'UnicodeTranslateError', 'AssertionError', 'ArithmeticError', 'FloatingPointError', 'OverflowError', 'ZeroDivisionError', 
'SystemError', 'ReferenceError', 'BufferError', 'MemoryError', 'Warning', 'UserWarning', 'DeprecationWarning', 'PendingDeprecationWarning', 
'SyntaxWarning', 'RuntimeWarning', 'FutureWarning', 'ImportWarning', 'UnicodeWarning', 'BytesWarning', 'ResourceWarning', 'ConnectionError', 
'BlockingIOError', 'BrokenPipeError', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionRefusedError', 'ConnectionResetError', 
'FileExistsError', 'FileNotFoundError', 'IsADirectoryError', 'NotADirectoryError', 'InterruptedError', 'PermissionError',
'ProcessLookupError', 'TimeoutError', 'copyright', 'credits', 'license', 'help', '_', 'exec',
# BLOCK
#'open', 'eval', 'quit' , 'exit',
]


class Sandbox(object):
    def __init__(self):
        pass
    
    def safe_builtins_cmd(self, _builtins):
        for function in list(_builtins):
            if function not in WT_LIST:
                del _builtins[function]

    def execute(self, cmd):
        # https://github.com/vstinner/pysandbox/blob/master/sandbox/sandbox_class.py#L99
        origin_globals = globals()
        _builtins = origin_globals["__builtins__"]
        # generate safe builtins dict
        self.safe_builtins_cmd(_builtins)
        exec(cmd, origin_globals)
    


