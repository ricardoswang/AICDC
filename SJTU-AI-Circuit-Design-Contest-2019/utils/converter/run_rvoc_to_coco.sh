#!/usr/bin/env bash 

pip3 install -r requirements.txt

rm ./IR.py

cp ./rvoc.txt ./IR.py

sed -i '' -e '1i \
stuff = \\' ./IR.py

python3 ./Rvoc_to_coco.py
