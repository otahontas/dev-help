from starlette.endpoints import HTTPEndpoint
from starlette.responses import PlainTextResponse
from dev_help import settings

class Videos(HTTPEndpoint):
    async def get(self, request):
        return PlainTextResponse(f"{settings.VIDEOS_PATH}")

# async def file_gen(file_name, blocksize=1024 * 256):
#     async with aiofiles.open(file_name, mode="rb") as file_like:
#         chunk = await file_like.read(blocksize)
#         while chunk:
#             yield chunk
#             chunk = await file_like.read(blocksize)
#
# async def video(request):
#     videopath = Path(__file__).parent.parent.parent / "data" / "edgedb_python.mp4"
#     return StreamingResponse(file_gen(str(videopath)), media_type="video/mp4")
