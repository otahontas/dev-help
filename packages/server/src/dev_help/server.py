import aiofiles
from starlette.applications import Starlette
<<<<<<< HEAD
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse, FileResponse, StreamingResponse
from starlette.routing import Route
from pathlib import Path


async def file_gen(file_name, blocksize=1024 * 256):
    async with aiofiles.open(file_name, mode="rb") as file_like:
        chunk = await file_like.read(blocksize)
        while chunk:
            yield chunk
            chunk = await file_like.read(blocksize)

async def video(request):
    videopath = Path(__file__).parent.parent.parent / "data" / "edgedb_python.mp4"
    return StreamingResponse(file_gen(str(videopath)), media_type="video/mp4")

async def homepage(request):
    return JSONResponse({'hello': 'world'})

middleware = [
    Middleware(CORSMiddleware, allow_origins=['*'])
]

app = Starlette(debug=True, routes=[
    Route('/', homepage),
    Route('/video', video),
], middleware=middleware)
