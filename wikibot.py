import wikipedia
import click

@click.command()
@click.option('--name', prompt='Enter the topic name to scrape from Wikipedia',
              help='Scrap on Wikipedia.')
def search_wikipedia(name="Facebook", length=1):
    result = wikipedia.summary(name, sentences=length)
    click.echo(click.style(result, fg='yellow', bg='black', bold=True))

if __name__ == "__main__":
    search_wikipedia()