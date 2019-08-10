# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import subprocess
import time


def solve():
    cmd='bash shadowsocks-libev-update.sh'
    subprocess.call(cmd, shell=True)


if __name__ == '__main__':
    cnt = 1
    while (cnt):
        solve()
        time.sleep(10)
        cnt -= 1

