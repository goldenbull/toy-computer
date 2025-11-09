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
from internal.grammar.compiler import Compiler

# url_prefix = "/toy-computer"
url_prefix = "/"

# register javascript in mimetypes
mimetypes.add_type('text/javascript', '.js')

# setup HTTP services
api = FastAPI()


def serialize_operand(operand):
    """Serialize an operand to JSON-compatible dict."""
    from internal.computer.operand import Reg, Mem, Imm, Str

    if isinstance(operand, Reg):
        return {
            "type": "reg",
            "value": operand.reg
        }
    elif isinstance(operand, Mem):
        return {
            "type": "mem",
            "reg": operand.reg,
            "offset": operand.offset
        }
    elif isinstance(operand, Imm):
        return {
            "type": "imm",
            "value": operand.val
        }
    elif isinstance(operand, Str):
        return {
            "type": "str",
            "value": operand.text
        }
    else:
        return {
            "type": "unknown",
            "value": str(operand)
        }


def serialize_operation(op):
    """Serialize an operation to JSON-compatible dict."""
    from internal.computer.operations import (
        Move, Add, Sub, Mul, Div, Cmp, Jump, Call, Ret,
        Push, Pop, Input, Print, Rand, Dump, Pause, Halt, Nop
    )

    # Get operation type name
    op_type = type(op).__name__.lower()

    # Serialize based on operation type
    result = {
        "addr": op.addr,
        "type": op_type,
        "labels": op.labels if hasattr(op, 'labels') else []
    }

    # Add operands based on operation type
    if isinstance(op, (Move, Add, Sub, Cmp)):
        result["operands"] = [serialize_operand(op.p1), serialize_operand(op.p2)]
    elif isinstance(op, (Mul, Div)):
        result["operands"] = [serialize_operand(op.p1)]
    elif isinstance(op, Jump):
        result["action"] = op.action
        result["target"] = op.target
        result["operands"] = []
    elif isinstance(op, Call):
        result["target"] = op.target
        result["operands"] = []
    elif isinstance(op, Ret):
        result["operands"] = []
    elif isinstance(op, Push):
        result["action"] = op.action
        result["operands"] = [serialize_operand(op.p1)] if op.p1 else []
    elif isinstance(op, Pop):
        result["action"] = op.action
        result["operands"] = [serialize_operand(op.p1)] if op.p1 else []
    elif isinstance(op, Input):
        result["operands"] = [serialize_operand(op.p1)]
    elif isinstance(op, Print):
        result["action"] = op.action
        result["operands"] = [serialize_operand(op.p1)] if op.p1 else []
    elif isinstance(op, Rand):
        result["operands"] = [serialize_operand(op.p1), serialize_operand(op.p2)]
    elif isinstance(op, Dump):
        if op.p1 is not None:
            result["operands"] = [serialize_operand(op.p1), {"type": "imm", "value": op.p2}]
        else:
            result["operands"] = [{"type": "imm", "value": op.p1_val}, {"type": "imm", "value": op.p2}]
    elif isinstance(op, (Pause, Halt, Nop)):
        result["operands"] = []
    else:
        # Unknown operation type - try to serialize any p1, p2 attributes
        result["operands"] = []
        if hasattr(op, 'p1') and op.p1 is not None:
            result["operands"].append(serialize_operand(op.p1))
        if hasattr(op, 'p2') and op.p2 is not None:
            result["operands"].append(serialize_operand(op.p2))

    return result


@api.post("/sourcecode")
async def post_sourcecode(request: Request):
    """
    Parse assembly source code and return structured operations and labels.

    Request body: { "sourceCode": "assembly code here..." }

    Returns:
    {
        "success": true,
        "operations": [...],
        "labels": {...}
    }
    or
    {
        "success": false,
        "error": "error message"
    }
    """
    try:
        body = await request.json()
        source_code = body.get("sourceCode", "")

        # Compile the source code
        result = Compiler.compile(source_code)

        # Serialize operations to JSON
        operations = []
        for op in result.ops:
            operations.append(serialize_operation(op))

        return JSONResponse({
            "success": True,
            "operations": operations,
            "labels": result.labels_tbl
        })

    except Exception as e:
        return JSONResponse({
            "success": False,
            "error": str(e)
        })


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
app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])

# Mount API endpoints
app.mount("/api", api)

# Mount static files if the directory exists
if Path("./html").exists():
    app.mount(url_prefix, StaticFiles(directory="./html", html=True), "static")


@app.get('/favicon.ico')
async def favicon():
    if Path("html/pc.ico").exists():
        return FileResponse(path="html/pc.ico")
    return JSONResponse({"error": "Not found"}, status_code=404)


if __name__ == "__main__":
    app_name = "webserver:app"
    uvicorn.run(app_name,
                host="127.0.0.1",
                port=22000,
                log_level="debug",
                reload=True,
                )
