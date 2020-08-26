from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
from starlette.routing import Route
from dev_help.endpoints.videos import Videos, Video


async def homepage(request):
    return JSONResponse({"hello": "world"})


middleware = [Middleware(CORSMiddleware, allow_origins=["*"])]

app = Starlette(
    debug=True,
    routes=[
        Route("/", homepage),
        Route("/videos", Videos),
        Route("/videos/{filename}", Video),
    ],
    middleware=middleware,
)
