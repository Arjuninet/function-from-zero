import wikipedia
import click


def get_summary(name, length=1):
    """Fetches a summary of the given topic from Wikipedia."""
    return wikipedia.summary(name, sentences=length)


@click.command()
@click.option(
    "--name",
    prompt="Enter the topic name to scrape from Wikipedia",
    help="Scrap on Wikipedia.",
)
def search_wikipedia(name):
    result = get_summary(name)
    click.echo(click.style(result, fg="yellow", bg="black", bold=True))


if __name__ == "__main__":
    search_wikipedia()
