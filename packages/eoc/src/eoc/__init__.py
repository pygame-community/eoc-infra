import click
import os
import eoclib


@click.group()
def main():
    """EOC CLI tool"""
    pass


@main.command()
@click.argument("path", type=click.Path(exists=True))
def run(path):
    """Run EOC analysis on a Python file or directory"""
    if os.path.isfile(path):
        if not path.endswith(".py"):
            raise click.BadParameter("File must be a Python file (.py extension)")
        # TODO: Handle single file analysis
    elif os.path.isdir(path):
        init_path = os.path.join(path, "__init__.py")
        if not os.path.exists(init_path):
            raise click.BadParameter("Directory must contain an __init__.py file")
        # TODO: Handle directory analysis
    else:
        raise click.BadParameter("Path must be a file or directory")


if __name__ == "__main__":
    main()
