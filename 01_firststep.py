#!/usr/bin/env python3

import subprocess
import threading
import time
import os
import random


os.system('rm -f prooven_proxies.dat')

def run_command(cmd):
    """Function to execute a bash command using Popen in a thread."""
    print(f"Starting command: {cmd}")
    try:
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()
        print(f"Finished command: {cmd}")
        print(f"STDOUT for '{cmd}':\n{stdout}")
        if stderr:
            print(f"STDERR for '{cmd}':\n{stderr}")
    except Exception as e:
        print(f"Error running command '{cmd}': {e}")

bash_commands_list = [
    f'rm -f socks5.txt && curl -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (K HTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36" -sL https://cdn.jsdelivr.net/gh/proxifly/free-proxy-list@main/proxies/protocols/socks5/data.txt -o socks5.txt',
    f'rm -f socks4.txt && curl -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (K HTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36" -sL https://cdn.jsdelivr.net/gh/proxifly/free-proxy-list@main/proxies/protocols/socks4/data.txt -o socks4.txt'
]

threads = []

# Create and start a thread for each command
for bash_command in bash_commands_list:
    # Target function is run_command, arguments are passed as a tuple
    t = threading.Thread(target=run_command, args=(bash_command,))
    t.start()
    threads.append(t)

# Wait for all threads to complete
for t in threads:
    t.join()


proxies = []
proxies += open("socks5.txt").read(-1).split("\n")[0:200]
proxies += open("socks4.txt").read(-1).split("\n")[0:200]
print( proxies)

bash_commands_list = [
]

for i,proxy in enumerate(proxies):
 delay = random.randint(2,20)
 bash_commands_list.append(
 f'sleep {delay} && curl --silent --connect-timeout 60 --output /dev/null --proxy "{proxy}" "http://example.com/{i}" && [[ "$?" == "0" ]]  && echo {proxy} >> prooven_proxies.dat'
 )



# Create and start a thread for each command
for bash_command in bash_commands_list:
    # Target function is run_command, arguments are passed as a tuple
    t = threading.Thread(target=run_command, args=(bash_command,))
    t.start()

