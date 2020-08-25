import nox

locations = "src", "tests", "noxfile.py"


@nox.session(python=["3.8"])
def lint_check(session):
    session.install("flake8", "flake8-black")
    session.run("flake8", *locations)


@nox.session(python="3.8")
def format_check(session):
    session.install("black")
    session.run("black", *locations, "--check")
