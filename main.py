from joke import Joke
import os

def joke(request):
    j = Joke()
    return j.GetJokePair()
