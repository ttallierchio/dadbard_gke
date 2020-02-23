from fastapi import FastAPI
from joke import Joke
import os
app = FastAPI()


@app.get('/api/joke')
def get():
    j = Joke()
    return j.GetJokePair()

@app.get('/api/os_environ')
def get():
    l = os.environ
    return l