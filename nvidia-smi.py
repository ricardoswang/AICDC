#!/usr/bin/env python

import os
import re
import time
import requests
import datetime
import subprocess

update_freq = 1
threshold = 200

issue_index = 2

first_time = False

token = os.getenv('GITHUB_TOKEN')

assert(token)

header = {
    'Authorization': 'token %s' % token
}


def send_message(msg: str):
    rs = requests.post(
        'https://api.github.com/repos/ricardoswang/AICDC/issues/%d/comments' % (issue_index), json={
            "body": msg
        }, headers=header)


while True:

    cont_0 = os.popen("nvidia-smi -q --id=0").readlines()
    cont_1 = os.popen("nvidia-smi -q --id=1").readlines()

    timestamp = datetime.datetime.now()

    cont_0_mem = 0
    cont_1_mem = 0

    for line in cont_0:
        line = line.strip()
        if 'Used GPU Memory' in line:
            tokens = [k for k in re.split(':|MiB', line) if k.strip() != '']
            cont_0_mem += int(tokens[-1].strip())

    for line in cont_1:
        line = line.strip()
        if 'Used GPU Memory' in line:
            tokens = [k for k in re.split(':|MiB', line) if k.strip() != '']
            cont_1_mem += int(tokens[-1].strip())

    message = """
    Core #0 memory usage: %d MiB
    Core #1 memory usage: %d MiB

    Update time: %s
    """ % (cont_0_mem, cont_1_mem, timestamp.strftime(r'%Y.%m.%d %H:%M:%S'))

    print(message)

    if first_time:
        try:
            send_message("[normal routinely notification]\n" + message)
            first_time = False
        except:
            print("failed to send [normal routinely notification] message.")

    elif cont_0_mem < threshold and cont_1_mem < threshold:

        # 开始缺德
        try:
            subprocess.Popen(['./start_train.sh'])
        except:
            pass

        while True:
            # os.system('./start_train.sh')
            try:
                send_message(
                    "[resource free!]\nmaking an preempting attempt.\n" + message)
                break
            except:
                print(
                    "failed to send [normal routinely notification] message.")

        exit(0)
    elif timestamp.minute == 0 or timestamp.minute == 30:
        try:
            send_message("[normal routinely notification]\n" + message)
            time.sleep(60.0)
        except:
            print("failed to send [normal routinely notification] message.")

    time.sleep(update_freq)
