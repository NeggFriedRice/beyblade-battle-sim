import time, sys, subprocess

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)

def delay_print_slow(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.03)

def clear_screen():
    subprocess.call(['tput', 'reset']) 