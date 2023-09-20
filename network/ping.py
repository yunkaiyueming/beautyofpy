#coding=utf8

import subprocess
import re

p = subprocess.Popen(["ping.exe", 'www.baidu.com'],
  stdin = subprocess.PIPE,
  stdout = subprocess.PIPE,
  stderr = subprocess.PIPE,
  shell = True)
out = p.stdout.read()
regex = re.compile("最短 = (\d+)ms, 最长 = (\d+)ms, 平均 = (\d+)ms", re.IGNORECASE)
print regex.findall(out)