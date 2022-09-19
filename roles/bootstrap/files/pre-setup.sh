#!/usr/bin/env bash

cd /opt
sudo wget https://www.python.org/ftp/python/3.8.8/Python-3.8.8.tgz
sudo tar xzf Python-3.8.8.tgz
cd Python-3.8.8
sudo ./configure --enable-optimizations
sudo make altinstall
sudo touch /home/ec2-user/bootstrapped.txt