#!/bin/bash

cd /

apt-get update
apt-get upgrade -y

apt-get install ffmpeg -y

apt-get install software-properties-common -y
add-apt-repository ppa:git-core/ppa -y
apt-get install curl -y
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
apt-get install git-lfs -y
git lfs install


git clone https://github.com/mozilla/DeepSpeech
cd Deepspeech
git lfs fetch
git lfs checkout
apt-get install python-pip -y
pip install --upgrade pip
pip install -r /DeepSpeech/requirements.txt
pip uninstall tensorflow -y
pip install 'tensorflow-gpu==1.6.0' -y
pip install deepspeech-gpu
pip install --upgrade deepspeech-gpu
cd /DeepSpeech/native_client
python /DeepSpeech/util/taskcluster.py --target .
