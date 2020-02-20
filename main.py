from fastapi import FastAPI
from joke import Joke
app = FastAPI()


@app.get('/api/joke')
def get():
    j = Joke()
    return j.GetJokePair()