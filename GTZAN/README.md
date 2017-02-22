# GTZANデータセット

## genresフォルダに解凍
- 音楽データセット [GTZAN Genre Collection](http://marsyasweb.appspot.com/download/data_sets/)

## au2wav.py
- 音楽ファイルを.auから.wav形式に変換する

## spectrogram.py
- GTZAN genresの音楽データからスペクトログラム画像を作成する
- 画像のパスファイル(train.txt, test.txt)を作る(Caffe用)

## Caffe学習用のLMDBを作成する
```
$ $CAFFE_DIR/built/tools/convert_imageset -resize_height=256 -resize_width=256 -shuffle -gray ./ train.txt gtzan_train_lmdb
$ $CAFFE_DIR/built/tools/convert_imageset -resize_height=256 -resize_width=256 -shuffle -gray ./ test.txt gtzan_test_lmdb
```
