import numpy
def random_movie():
    movies = [
        {"title": "Deer Hunter"},{"title":"GoodFellas"}
        ]
    i = numpy.int(numpy.random.rand()*60)
    print i

    movies = movies * 30

    return movies[i]

def search_articles(query):
    return []

def insert_article(article):
    return False
