#!/bin/sh
poetry run uvicorn dev_help.server:app --reload --port 5000
