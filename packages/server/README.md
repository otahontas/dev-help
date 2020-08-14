# Codeer server 

Backend for coreer, built with `starlette` running on `python 3.8+`.

## Install
Requirements: `poetry`
- Install python version 3.8+ 
- Run poetry install
- If you can't install python 3.8+ globally, you can do following:
  - install pyenv
  - install 3.8.x with pyenv
  - run `pyenv local 3.8.x` in this folder
  - Ensure poetry uses python 3.8 by running `poetry env use 3.8.x`

## Running
Run server with `poetry run codeer-server`, server starts at port 5000
