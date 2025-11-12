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

url_prefix = "/toy-computer"
# url_prefix = "/"

# register javascript in mimetypes
mimetypes.add_type('text/javascript', '.js')


def serialize_operand(operand):
    """Serialize an operand to JSON-compatible dict with all fields."""
    from internal.computer.operand import Operand

    if operand is None:
        return None

    if not isinstance(operand, Operand):
        raise TypeError("must be an Operand class instance")

    return {
        "tp": operand.tp.name,  # Convert enum to string (Reg/Mem/Imm/Str)
        "reg": operand.reg,
        "offset": operand.offset,
        "immVal": operand.immVal,
        "text": operand.text
    }


def serialize_operation(op):
    """Serialize an operation to JSON-compatible dict."""

    # Get operation type name
    op_type = type(op).__name__.lower()

    # Base result with common fields
    result = {
        "addr": op.addr,
        "type": op_type,
        "labels": op.labels,
        "p1": serialize_operand(op.p1),
        "p2": serialize_operand(op.p2),
        "action": op.action,
        "target": op.target,
    }

    # Add operation-specific fields
    from internal.computer.operations import Dump
    if isinstance(op, Dump):
        result["cnt"] = op.cnt

    return result


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


@app.post(url_prefix + "/api/compile")
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
        from internal.grammar.compiler import Compiler
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


# Mount SvelteKit static files if the directory exists
frontend_build_dir = Path(__file__).parent.parent / "web_frontend" / "build"
if frontend_build_dir.exists():
    app.mount(url_prefix, StaticFiles(directory=str(frontend_build_dir), html=True), "static")


@app.get(url_prefix + '/favicon.ico')
async def favicon():
    # Serve the favicon.png from build directory
    favicon_path = frontend_build_dir / "favicon.png"
    if favicon_path.exists():
        return FileResponse(path=str(favicon_path), media_type="image/png")
    return JSONResponse({"error": "Not found"}, status_code=404)


if __name__ == "__main__":
    app_name = "webserver:app"
    uvicorn.run(app_name,
                host="127.0.0.1",
                port=22000,
                log_level="debug",
                reload=True,
                )
