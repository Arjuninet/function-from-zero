from wikibot import search_wikipedia

def test_search_wikipedia():
    assert "Microsoft" in search_wikipedia("Microsoft")