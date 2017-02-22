# coding: utf-8
'''
GTZAN
スペクトログラムの画像(256x256)のデータセットを作る
画像のパスファイル(train.txt, test.txt)を作る(Caffe用)
trimsec秒間を１秒ずつずらしながら切り出す
(データ量を疑似的に(30-trimsec+1)倍に増やす)
1/testraioがテストデータ
'''

import os

trimsec = 20        # 20秒間切り出す
testratio = 10      # 1/10がテストデータ

dirname = 'genres'
genres = ['blues', 'classical', 'country', 'disco', 'hiphop',
          'jazz', 'metal', 'pop', 'reggae', 'rock']

train = open('train.txt', 'w')
test = open('test.txt', 'w')

# Output Directories
spectrogram = 'spectrogram'
if not os.path.isdir(spectrogram):
    os.mkdir(spectrogram)
if not os.path.isdir(os.path.join(spectrogram, 'train')):
    os.mkdir(os.path.join(spectrogram, 'train'))
if not os.path.isdir(os.path.join(spectrogram, 'test')):
    os.mkdir(os.path.join(spectrogram, 'test'))

n = 0   # Genre label
for g in genres:
    if not os.path.isdir(os.path.join(spectrogram, 'train', g)):
        os.mkdir(os.path.join(spectrogram, 'train', g))

    if not os.path.isdir(os.path.join(spectrogram, 'test', g)):
        os.mkdir(os.path.join(spectrogram, 'test', g))

    for i in range(100):
        src = os.path.join(dirname, g, g + ".%05d.wav" % i)
        for j in range(30 - trimsec + 1):
            if i % testratio == 0:      # Test Data
                dst = os.path.join(spectrogram, 'test', g,
                                   g + "%05d_%d.png" % (i, j))
                test.write(dst + ' ' + str(n) + '\n')
            else:                       # Training Data
                dst = os.path.join(spectrogram, 'train', g,
                                   g + "%05d_%d.png" % (i, j))
                train.write(dst + ' ' + str(n) + '\n')

            command = 'sox ' + src + \
                      ' -n trim %d %d spectrogram ' % (j, trimsec) + \
                      '-x 256 -y 256 -m -r -o ' + dst
            os.system(command)

    n += 1

train.close()
test.close()
