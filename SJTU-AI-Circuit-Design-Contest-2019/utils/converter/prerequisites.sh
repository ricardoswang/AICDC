#!/usr/bin/env bash 

rm ./train_list.py

cp ./train_list.txt ./train_list.py

sed -i '' -e '1i \
stuff = \\' ./train_list.py