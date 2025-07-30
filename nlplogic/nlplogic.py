from textblob import TextBlob
import wikipedia

def search_wikipedia(query):
    """Search Wikipedia"""
    try:
        results = wikipedia.search(query)
        if results:
            page = wikipedia.page(results[0])
            return page.summary
        else:
            return "No results found."
    except Exception as e:
        return str(e)

def summary_wikipedia(query):
    """Get summary from wikipedia"""
    