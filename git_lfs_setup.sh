#!/bin/bash

cd /

apt-get install software-properties-common -y
add-apt-repository ppa:git-core/ppa -y
apt-get install curl -y
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
apt-get install git-lfs -y
git lfs install