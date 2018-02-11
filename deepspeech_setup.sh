#apt
sudo apt-get update
sudo apt-get upgrade

#git
sudo apt-get install software-properties-common -y
sudo add-apt-repository ppa:git-core/ppa -y
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
sudo apt-get install git-lfs -y
git lfs install

#DeepSpeech
sudo git clone https://github.com/mozilla/DeepSpeech
cd Deepspeech
git lfs fetch
git lfs checkout
sudo apt-get install python-pip -y
sudo pip install tensorflow
sudo pip install deepspeech
python util/taskcluster.py --target .
