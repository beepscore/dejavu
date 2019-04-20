from __future__ import absolute_import
from __future__ import print_function
import json
import os
import logging
import warnings
warnings.filterwarnings("ignore")

from dejavu import Dejavu
from dejavu.recognize import FileRecognizer, MicrophoneRecognizer

# Reference example.py


def config_environment_variable_database_url_from_file(filename):
    """
    Reads configuration file, may set environment variable DATABASE_URL.
    https://stackoverflow.com/questions/5627425/what-is-a-good-way-to-handle-exceptions-when-trying-to-read-a-file-in-python
    Alternatively could set a python variable.
    :param filename: a json file that may contain a dictionary with key "DATABASE_URL"
    """
    try:
        with open(filename) as f:
            config_dict = json.load(f)
            db_url_from_file = config_dict.get('DATABASE_URL')
            if db_url_from_file is not None:
                os.environ['DATABASE_URL'] = db_url_from_file

    except IOError:
        # e.g. file doesn't exist
        print("Could not read file: " + filename)


if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)

    config_environment_variable_database_url_from_file('data/config.json')

    dburl = os.getenv('DATABASE_URL', default='sqlite://')
    print('dburl', dburl)
    djv = Dejavu(dburl=dburl)

    # Fingerprint all the mp3's in the directory we give it
    # this may take several seconds per file
    djv.fingerprint_directory("mp3", [".mp3"])

    # Recognize audio from a file
    # filename_containing_audio_to_match = 'mp3/Sean-Fournier--Falling-For-You.mp3'
    # filename_containing_audio_to_match = 'mp3/chantix.mp3'
    # match_dict = djv.recognize(FileRecognizer, filename_containing_audio_to_match)
    # match_dict_json = json.dumps(match_dict)
    # print('filename_containing_audio_to_match: {0}, match_dict_json: {1}\n'
    #       .format(filename_containing_audio_to_match, match_dict_json))
    # example output
    # filename_containing_audio_to_match: mp3/chantix.mp3,
    # match_dict_json: {"song_id": 12, "song_name": "chantix", "confidence": 43335,
    # "offset": 0, "offset_seconds": 0.0,
    # "file_sha1": "7050797273712b325559706c4d6878594238583866486d4b4371493d0a",
    # "match_time": 11.098071813583374}

    # Alternatively recognize audio from your microphone for 'secs' seconds
    secs = 5
    match_dict = djv.recognize(MicrophoneRecognizer, seconds=secs)
    if match_dict is None:
        print("Nothing recognized -- did you play the song out loud so your mic could hear it? :)")
    else:
        match_dict_json = json.dumps(match_dict)
        print('From mic with {0} seconds we recognized: {1}\n'.format(secs, match_dict_json))
        # example output
        # From mic with 5 seconds we recognized:
        # {"song_id": 5, "song_name": "sandals", "confidence": 186,
        # "offset": 14, "offset_seconds": 0.65016,
        # "file_sha1": "39595175712f5051494768766b4f444338774174324952736773773d0a"}
