import typer
from builds.python_build import Build


def main(name: str = typer.Option(..., "-build")):
    build = Build(name)
    build.build_project()
    

if __name__ == "__main__":
    typer.run(main)