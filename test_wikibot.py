from wikibot import search_wikipedia
from click.testing import CliRunner


# def test_search_wikipedia():
#     assert "Microsoft" in get_summary("Microsoft")


def test_get_summary():
    runner = CliRunner()
    result = runner.invoke(search_wikipedia, ["--name", "Microsoft"])
    assert result.exit_code == 0
    assert "Microsoft" in result.output
