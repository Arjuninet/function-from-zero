import wikipedia

def search_wikipedia(query="Facebook", length=1):
    result = wikipedia.summary(query, sentences=length)
    return result
