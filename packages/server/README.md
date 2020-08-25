# Server

![Server code style check](https://github.com/otahontas/dev-help/workflows/Server%20code%20style%20check/badge.svg)

Server for dev-help, built with `starlette` and `python 3.8+`.

## Install
Requirements: `poetry`
- Install python version 3.8+ 
- Run `poetry install`
- If you can't install python 3.8+ globally, you can do following:
  - install pyenv
  - install 3.8.x with pyenv
  - run `pyenv local 3.8.x` in this folder
  - Ensure poetry uses python 3.8 by running `poetry env use 3.8.x`

## Running
Run server with hot reload enabled by launching shell script `./start_server.sh`. Server launches on port 8000 by default.

## Linting and code formatting

Code should be formatted with `black` code formatter and linted with `flake8`. We have configured `nox` environment and github actions to do the checks for code styles.

It is recommended to add black and flake8 formatting to your editor of choice.
