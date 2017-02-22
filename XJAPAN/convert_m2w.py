# coding: utf-8
"""
dirname内のmp3ファイルをwav形式に変換する
"""
import os

dirname = 'X'
files = os.listdir(dirname)

for file in files:
    command = 'sox ' + os.path.join(dirname, file) + ' -c 1 -r 22050 ' + \
              os.path.join(dirname, file[:-4] + '.wav')
    os.system(command)
