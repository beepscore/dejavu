# Purpose
Record info about using dejavu.

# References
forked from
https://github.com/bcollazo/dejavu

## PyAudio with USB audio interface
### Recording multiple microphones in python
Scarlett audio interface and PyAudio
https://stackoverflow.com/questions/25620285/recording-multiple-microphones-in-python

### python2.7 on Raspberry Pi 3 - Pyaudio Input overflowed
Raspberry Pi 3 Model B and Focusrite Scarlett 2i2 USB Sound Card
https://stackoverflow.com/questions/38042875/python2-7-on-raspberry-pi-3-pyaudio-input-overflowed

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

## Select live audio input source
Selecting live audio input from an audio interface instead of from microphone gives a cleaner signal without room noise.
If using macOS and an audio interface, go to System Preferences / Sound / Input.
Select the interface e.g. Scarlett 2i4 USB.
Note I haven't tried running Dejavu on Raspberry Pi Raspbian yet, and haven't selected an audio input source.

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
Ok to delete contents of results directory.

## data/config.json
may contain a json dictionary e.g.

    {"DATABASE_URL": "results/test.db"}

Ways to run:
Can run recognize_audio.py
If no database exists it will make a new one, I think in-memory sqlite.

    conda activate <environment>
    
    python3 recognize_audio.py

example output:

    2019-04-20 15:01:55 DEBUG    <module> line:101 dburl: sqlite://
    2019-04-20 15:01:55 INFO     _fingerprint_worker line:184 Fingerprinting channel 1/2 for data/commercial_mp3/google-help-german-woman.mp3
    2019-04-20 15:01:55 INFO     _fingerprint_worker line:184 Fingerprinting channel 1/2 for data/commercial_mp3/aleve-proven-better.mp3
    ...

    2019-04-20 15:02:49 DEBUG    recognize_audio_from_a_file line:48
        filename_containing_audio_to_match: data/commercial_mp3/chantix.mp3,
        match_dict_json: {"song_id": 14, "song_name": "chantix", "confidence": 43335,
        "offset": 0, "offset_seconds": 0.0,
        "file_sha1": "7050797273712b325559706c4d6878594238583866486d4b4371493d0a",
        "match_time": 12.952589988708496}

    2019-04-20 21:01:40 DEBUG    recognize_audio_from_microphone line:79
        From mic with 5 seconds we recognized: {"song_id": 13, "song_name": "chantix", "confidence": 376,
        "offset": 525, "offset_seconds": 24.38095,
        "file_sha1": "7050797273712b325559706c4d6878594238583866486d4b4371493d0a"}


