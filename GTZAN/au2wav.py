'''
GTZAN Genre Collection
convert *.au to *.wav
'''

import os

dirname = 'genres'
genres = ['blues', 'classical', 'country', 'disco', 'hiphop',
          'jazz', 'metal', 'pop', 'reggae', 'rock']

for g in genres:
    for i in range(100):
        src = os.path.join(dirname, g, g + ".%05d.au" % i)
        dst = os.path.join(dirname, g, g + ".%05d.wav" % i)
        command = 'sox ' + src + ' ' + dst
        os.system(command)
