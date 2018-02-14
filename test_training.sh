#!/bin/sh
set -xe
if [ ! -f DeepSpeech.py ]; then
    echo "Please make sure you run this from DeepSpeech's top level directory."
    exit 1
fi;

python -u DeepSpeech.py \
  --train_files data/kftest01/kftest01.csv \
  --dev_files data/kftest01/kftest01.csv \
  --test_files data/kftest01/kftest01.csv \
  ----initialize_from_frozen_model /mnt/hgfs/shared/models/output_graph.pb
  --train_batch_size 1 \
  --dev_batch_size 1 \
  --test_batch_size 1 \
  --n_hidden 494 \
  --epoch 50 \
  --checkpoint_dir \
  "$@"
