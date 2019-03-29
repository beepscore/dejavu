# Purpose
Record info about using dejavu.

# Reference
forked from
https://github.com/bcollazo/dejavu

# Results

## TODO

## Install dependencies
https://github.com/worldveil/dejavu/blob/master/INSTALLATION.md

ffmpeg for converting audio files to .wav format
matplotlib, used for spectrograms and plotting
MySQLdb for interfacing with MySQL databases
numpy for taking the FFT of audio signals
pydub, a Python ffmpeg wrapper
scipy, used in peak finding algorithms
yaudio for grabbing audio from microphone

### convert wav to mp3

    ffmpeg -i a.wav -f mp3 a.mp3

### Put files in mp3 directory

### ./test_dejavu.sh
This makes a temporary sqlite file

    $ chmod u+x ./test_dejavu.sh
    $ ./test_dejavu.sh

### database
check sqlite schema

#### create database (how to set up schema?)

#### set environment variable for database



