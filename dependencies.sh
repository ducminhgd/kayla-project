#!/usr/bin/env bash
apt-get update
add-apt-repository -y ppa:deadsnakes/ppa
apt-get update
apt-get install -y gcc-4.8
apt-get install -y bash-completion
apt-get install -y python-dev
apt-get install -y python2.7-dev
apt-get install -y python3.6-dev
apt-get install -y python-pip
apt-get install -y python-virtualenv

