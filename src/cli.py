"""Console script for homecredit_default_classification."""
import homecredit_default_classification

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for homecredit_default_classification."""
    console.print("Replace this message by putting your code into "
               "homecredit_default_classification.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    


if __name__ == "__main__":
    app()
