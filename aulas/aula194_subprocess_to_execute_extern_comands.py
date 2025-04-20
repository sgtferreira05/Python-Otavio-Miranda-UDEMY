# Using subprocess to execute external commands
# Subprocess is a module in Python that allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes.
# It is a powerful tool for executing external commands and interacting with them.
# The most simple way to use subprocess is to call the subprocess.run() function, which runs a command in a new process and waits for it to finish.
# Main function to execute external commands
#  stdout, stdin and stderr -> standard output, standard input and standard error
# capture_output -> capture the output of the command
# text -> return the output as a string instead of bytes
# shell -> run the command through the shell
# executable -> specify the shell to use
# check -> raise an exception if the command returns a non-zero exit code
# Return:
# stdout, stderr, returncode and args
# Important: the codfication of the output is in bytes, so it is necessary to decode it to utf-8 #in Windows try to use cp1252 or cp850 if utf-8 does not work
# examples commands:
# Windows: ping 127.0.0.1
# Linux/Mac: ping 127.0.0.1 -c 4

import subprocess
import sys

# Sys.platform = linux, darwin, win32, cygwin, os2emx, os2, os390, osf1, freebsd, sunos5, hpux, aix3, irix6, m68k
# sys.platform = 'win32' -> Windows
print(sys.platform)

cmd = ['ping', '127.0.0.1', '-c', '4']
encoding = 'utf-8'
system = sys.platform
if system == 'win32':
    cmd = ['cmd', '/c', 'dir', 'D:\\']
    encoding = 'cp850'


proc = (subprocess.run(
    cmd, capture_output=True,
      text=True, encoding=encoding,
))
print()
# print(proc)
# print(proc.stdout.decode('cp1252'))
# print(proc.stdout.decode('cp850'))
print(proc.stdout)

# print(proc.stderr)
# print(proc.returncode)
# print(proc.args)