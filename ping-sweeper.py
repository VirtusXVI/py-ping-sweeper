import sys;
import subprocess;
import platform;
import threading;

result = [];
threads = [];

def ping(target, param, i):
    ip = target[:-1] + str(i);
    output = subprocess.run(
        ["ping", param, "2", ip],
        ## this 2 lines are used to prevent the output print of the ping command
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    if output.returncode == 0:
        print(f"Host up: {ip}")
        result.append(output);

def pre_script():
    if len(sys.argv) < 2:
        print("Usage: python ping-sweeper.py <subnet-address>");
        sys.exit(1);

    script();

def script():
    param = "-n" if platform.system().lower() == "windows" else "-c" ## this detects the host OS and modifies the params accodingly(Linux uses '-c', Windows uses '-n')
    target = sys.argv[1] ## Subnet used for the scan
    for i in range(0, 256):
        t = threading.Thread(target=ping, args=(target, param, i));
        threads.append(t);
    for t in threads:
        t.start(); ## start the threads.
    for t in threads:
        t.join(); ## wait for all the threads to end.


pre_script();