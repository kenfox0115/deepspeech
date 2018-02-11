#!/bin/bash

#apt
apt-get update
apt-get upgrade

#git
apt-get install software-properties-common -y
add-apt-repository ppa:git-core/ppa -y
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
apt-get install git-lfs -y
git lfs install

#DeepSpeech
git clone https://github.com/mozilla/DeepSpeech
cd Deepspeech
git lfs fetch
git lfs checkout
apt-get install python-pip -y
pip install tensorflow
pip install deepspeech
python util/taskcluster.py --target .
