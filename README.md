# Kivy 1.11.1 Basics

Based on source: [https://kivy.org/doc/stable-1.11.1/guide/basic.html]

## Install

```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.7 python3.7-dev python3.7-venv -y

python3.7 -m venv venv
. ./venv/bin/activate
pip install -r requirements.txt
```

## Get started

```bash
python ./venv/share/kivy-examples/camera/main.py
```

If it crashes, try:

```bash
pip install opencv-python
```

## List of examples

1. Hello world (`Label`)
2. Build a login dialog (`GridLayout`)
3. Using properties
4. Kv script: `Button`
5. Kv script: `AsyncImage`
6. Kv script: Inherent classes
7. Kv script: zip file (sequence of images) as background
