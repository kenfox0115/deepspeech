#!/bin/bash

cd /

git clone https://github.com/mozilla/DeepSpeech
cd Deepspeech
git lfs fetch
git lfs checkout
apt-get install python-pip -y
pip install --upgrade pip
pip install -r /DeepSpeech/requirements.txt
pip install tensorflow
pip install deepspeech
cd /DeepSpeech/native_client
python /DeepSpeech/util/taskcluster.py --target .