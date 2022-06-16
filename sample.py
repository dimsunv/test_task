#!usr/bin/python3
# -*- coding: UTF-8 -*-

import subprocess
import os


message = subprocess.getoutput('cat /etc/*release')
print(message)
