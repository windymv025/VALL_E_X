from fastapi import FastAPI, HTTPException
from typing import List

from server.constants import support_languages
from server.objects import Language

app = FastAPI()


@app.get("/support-languages", response_model=List[Language])
def get_languages():
    return support_languages




if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
