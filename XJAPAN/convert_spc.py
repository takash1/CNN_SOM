# coding: utf-8
"""
$ python convert_spc.py [input] [start]

[input]の[start]秒から20秒間
トリミング&スペクトログラム画像を作成する
sox [input] [output] trim [start] [end]
sox [input] -n trim [start] 20 spectrogram -x 256 -y 256 -m -r -o [output]
"""
import os
import sys

argvs = sys.argv

if len(argvs) != 3:
    print 'Wrong number of arguments'

dst_trim = 'trim/'
if not os.path.isdir(dst_trim):
    os.mkdir(dst_trim)

dst_img = 'spc/'
if not os.path.isdir(dst_img):
    os.mkdir(dst_img)

command_trim = 'sox ' + argvs[1] + ' ' + \
               dst_trim + argvs[1][6:-4] + '_trim20.wav' + \
               ' trim ' + argvs[2] + ' 20'

command_img = 'sox ' + argvs[1] + ' -n trim ' + argvs[2] + \
               ' 20 spectrogram -x 256 -y 256 -m -r -o ' + \
               dst_img + argvs[1][6:-4] + '.png'

os.system(command_trim)
os.system(command_img)
