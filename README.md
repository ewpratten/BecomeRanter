# BecomeRanter
An LSTM based python script for creating devrant posts based on the style and content of other users.

## Requirements
You must have the following installed:
```
python3.6
pip3
```

## Installation
After cloning the repo, run the following:
```bash
pip3 install textgenrnn tensorflow numpy pandas keras
```

## Creating a HDF5 file
just run this:
```bash
python3 createhdf5frominput.py
```
and make sure you have your input data in the "input.txt" file.
<br>
for more options try
```bash
python3 createhdf5frominput.py -h
```