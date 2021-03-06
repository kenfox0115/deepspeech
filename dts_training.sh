#!/bin/sh
set -xe
if [ ! -f DeepSpeech.py ]; then
    echo "Please make sure you run this from DeepSpeech's top level directory."
    exit 1
fi;

python -u DeepSpeech.py \
  --train_files /home/ken/deepspeech/mnt/hgfs/shared/training_data/wav/dts_traning.csv \
  --dev_files /home/ken/deepspeech/mnt/hgfs/shared/training_data/wav/dts_traning.csv \
  --test_files /home/ken/deepspeech/mnt/hgfs/shared/training_data/wav/dts_traning.csv \
  --alphabet_config_path /DeepSpeech/models/alphabet.txt 
  --initialize_from_frozen_model /DeepSpeech/models/output_graph.pb
  --train_batch_size 1 \
  --dev_batch_size 1 \
  --test_batch_size 1 \
  --n_hidden 494 \
  --epoch 50 \
  --validation_step 5 \
  --checkpoint_dir /home/ken/deepspeech/checkpoint/ \
  "$@"



