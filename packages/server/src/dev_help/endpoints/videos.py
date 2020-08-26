from starlette.endpoints import HTTPEndpoint
from starlette.requests import Request
from starlette.responses import JSONResponse, StreamingResponse
from starlette.exceptions import HTTPException
from dev_help import settings
import aiofiles


class Videos(HTTPEndpoint):
    """HTTP methods for API endpoint /videos."""

    async def get(self, request: Request) -> JSONResponse:
        """Get filenames for all videos."""
        files = [{"filename": path.name} for path in settings.VIDEOS_PATH.iterdir()]
        return JSONResponse(files)

    async def post(self, request: Request) -> JSONResponse:
        """Add new video."""
        form = await request.form()
        filename = form["upload_video"].filename
        contents = await form["upload_video"].read()
        async with aiofiles.open(
            f"{settings.VIDEOS_PATH}/{filename}", "wb"
        ) as new_video:
            written_bytes = await new_video.write(contents)
            if written_bytes != len(contents):
                raise HTTPException(
                    status_code=400, contents="Couldn't save video file to server."
                )
        return JSONResponse({"filename": filename}, status_code=201)


class Video(HTTPEndpoint):
    """HTTP methods for API endpoint /videos/{filename}."""

    async def get(self, request: Request) -> StreamingResponse:
        """Get single video as streamed response"""
        filename = request.path_params["filename"]
        path_to_video = settings.VIDEOS_PATH / filename
        if not path_to_video:
            raise HTTPException(status_code=404)

        async def video_generator(path_to_file: str, blocksize: int = 1024 * 256):
            async with aiofiles.open(path_to_file, mode="rb") as file:
                while chunk := await file.read(blocksize):
                    yield chunk

        return StreamingResponse(
            video_generator(str(path_to_video)), media_type="video/mp4"
        )
