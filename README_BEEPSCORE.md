# Purpose
Record info about using dejavu.

# Reference
forked from
https://github.com/bcollazo/dejavu

# Results

## Install dependencies
https://github.com/worldveil/dejavu/blob/master/INSTALLATION.md

### ffmpeg
for converting audio files to .wav format
on macOS

    brew install ffmpeg

### matplotlib
used for spectrograms and plotting

### MySQLdb
for interfacing with MySQL databases

### numpy
for taking the FFT of audio signals

### pydub
a Python ffmpeg wrapper

### scipy
used in peak finding algorithms

### pyaudio
for grabbing audio from microphone

### sqlalchemy

### sqlalchemy_utils
https://sqlalchemy-utils.readthedocs.io/en/latest/installation.html

#### package name contains dash
    sqlalchemy-utils

#### import name contains underscore
import sqlalchemy_utils

## Activate conda environment
If using Anaconda.

    conda activate <my_environment>
    conda activate remy_python

## Install audio files

### convert wav to mp3

    ffmpeg -i a.wav -f mp3 a.mp3

### put audio files in mp3 directory

## ./test_dejavu.sh
Optional step. Running test_dejavu.sh makes a temporary sqlite file

    $ chmod u+x ./test_dejavu.sh
    $ ./test_dejavu.sh

## database
check sqlite schema

#### create database (how to set up schema?)

#### set environment variable for database

---
To run test

    ./test_dejavu.sh

This populates results directory including test.db

## data/config.json
may contain a json dictionary e.g.

    {"DATABASE_URL": "results/test.db"}

Ways to run:
Can run recognize_audio.py
If no database exists it will make a new one, I think in-memory.

    python3 recognize_audio.py

    INFO:dejavu:Fingerprinting channel 1/2 for mp3/google-help-german-woman.mp3
    INFO:dejavu:Fingerprinting channel 1/2 for mp3/aleve-proven-better.mp3
    INFO:dejavu:Fingerprinting channel 1/2 for mp3/volvo-birds.mp3
    ...

    From file we recognized: {'song_id': 12, 'song_name': 'chantix', 'confidence': 43335,
    'offset': 0, 'offset_seconds': 0.0,
    'file_sha1': '7050797273712b325559706c4d6878594238583866486d4b4371493d0a', 'match_time': 10.400582075119019}

Ok to delete contents of results directory.


