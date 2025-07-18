# -*- coding: utf-8 -*-

import logging
import base64
import mimetypes
from contextlib import asynccontextmanager
from pathlib import Path
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import FileResponse, PlainTextResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import json

secure_prefix = "/toy-computer"

# register javascript in mimetypes
mimetypes.add_type('text/javascript', '.js')

# setup HTTP services
api = FastAPI()


@api.post("/sourcecode")
async def post_sourcecode(src: str):
    return "running"


@asynccontextmanager
async def lifespan(app: FastAPI):
    # config logs
    log_fmt = '%(asctime)s.%(msecs)03d,[%(levelname)s],%(filename)s:%(lineno)04d,pid=%(process)05d, %(message)s'
    log_datefmt = "%Y-%m-%d %H:%M:%S"
    formatter = logging.Formatter(log_fmt, log_datefmt)
    sh = logging.StreamHandler()
    sh.setLevel(logging.DEBUG)
    sh.setFormatter(formatter)
    logging.root.handlers.clear()
    logging.root.addHandler(sh)
    logging.root.setLevel(logging.DEBUG)
    logging.info("=========== startup ============")
    yield


app = FastAPI(lifespan=lifespan)
app.add_middleware(GZipMiddleware, minimum_size=1000)
# app.add_middleware(CORSMiddleware,
#                    allow_origins=["*"],
#                    allow_credentials=True,
#                    allow_methods=["*"],
#                    allow_headers=["*"])

app.mount(secure_prefix, StaticFiles(directory="./html", html=True), "static")


@app.get('/favicon.ico')
async def favicon():
    return FileResponse(path="html/pc.ico")


if __name__ == "__main__":
    app_name = "webserver:app"
    uvicorn.run(app_name,
                host="127.0.0.1",
                port=22000,
                log_level="debug",
                reload=True,
                log_config="uvicorn_log.yaml",
                )
