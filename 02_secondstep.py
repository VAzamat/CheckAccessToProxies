#!/usr/bin/env python3

#https://www.youtube.com/shorts/1E9lAYmhnVQ

import subprocess
import threading
import time
import os
import random


os.system('rm -f prooven_proxies_yt.dat')

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



proxies = []
proxies += open("prooven_proxies.dat").read(-1).split("\n")[:-1]
print( proxies)


bash_commands_list = [
]

for i,proxy in enumerate(proxies):
 url = "https://www.youtube.com/shorts/1E9lAYmhnVQ"
 delay = i % 30
 bash_commands_list.append(
 f'sleep {i} && source ./env/bin/activate && yt-dlp --js-runtimes node -f 139 --proxy "{proxy}"  --socket-timeout 60 --retries 20  --output "/dev/null" "{url}" > /dev/null && [[ "$?" == "0" ]]   &&  echo {proxy} >> prooven_proxies_yt.dat'
 )

print( bash_commands_list )

# Create and start a thread for each command
for bash_command in bash_commands_list:
    # Target function is run_command, arguments are passed as a tuple
    t = threading.Thread(target=run_command, args=(bash_command,))
    t.start()

