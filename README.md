# Kivy 1.11.1 Basics

Based on source: [https://kivy.org/doc/stable-1.11.1/guide/basic.html]

## Install

**NOTE:** The script is only tested on Ubuntu 22.04. The package may be different when using another version of Linux kernel.

Install Python3.7

```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.7 python3.7-dev python3.7-venv -y
```

Install OpenCV

```bash
sudo apt install -y python3-opencv
```

If `gstreamer` is needed (This is NOT required on Linux [https://kivy.org/doc/stable/gettingstarted/installation.html#installing-kivy-s-dependencies]):

```bash
sudo apt install -y libgstreamer-opencv1.0-0 libgstreamer1.0-0 libgstreamer1.0-dev 
```

Install SDL2 on Linux

```bash
sudo apt install -y libsdl2-2.0-0 libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev
```

Create virtual environment

```bash
python3.7 -m venv venv
. ./venv/bin/activate
pip install --upgrade pip

# Avoid using the broken pre-build wheel
pip install --no-binary=kivy kivy==1.11.1

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
8. Handle exception when camera is not connected
9. Xbox controller
