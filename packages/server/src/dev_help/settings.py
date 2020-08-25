from starlette.config import Config
from pathlib import Path

config = Config()

# 1) Set path for videos folder
VIDEOS_PATH = Path(__file__).parent / "data" / "videos"
