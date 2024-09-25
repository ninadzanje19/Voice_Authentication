from feature_extraction import *
from address import *
from database import *

def detection(test_voice, data_voice):
    result = similarity_percentage(test_voice, data_voice)
    if result >= 90:
        for key, value in result.items():
            if value == result:
                print("The voice belongs to " + str(key))
                break
    else:
        for key, value in result.items():
            if value == result:
                print("The voice does not belongs to " + str(key))

