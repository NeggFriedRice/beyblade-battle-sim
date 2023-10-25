import time
import sys
import subprocess


# Delay print function
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)


# Delay print function but slower
def delay_print_slow(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.03)


# Clear screen function
def clear_screen():
    subprocess.call(['tput', 'reset'])
