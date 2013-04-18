from flask import Flask, render_template, request
#from rapid import (top_articles, search_articles, insert_article)
from recommendationEngine import random_movie
app = Flask(__name__, static_folder="../static", static_url_path="/static")

@app.route('/' ,methods=["GET", "POST"])
def index():
    #articles = top_articles()
    movie = random_movie()
    rats = {}
    if request.method == "POST":
        return do_submit(movie, rats)
    else:
        return render_template('myindex.jinja2.html',
    page_submit="active", movie=movie)

    #return render_template('myindex.jinja2.html', rows = movies)

@app.route('/about/')
def about():
    return render_template('about.jinja2.html')


def do_submit(movie, rats):
    print "movie", movie
    form = request.form
    print "len", len(form.values()[0])
    rating = 0 
    #if form.values() = 
    if len(form.values()[0]) ==0: 
        return render_template('myindex.jinja2.html', page_submit="active",movie=movie)      
    else:
        rating = eval(form.values()[0])
        print rating
        
        rats[movie['title']] = rating
        #submission = form['rating']
        #print submission
        print rats
        return render_template('myindex.jinja2.html', page_submit="active",movie=movie)   
    
# @app.route('/search/<query>')
# def search(query):
#     articles = search_articles(query)
#     return render_template('index.jinja2.html', 
#                            query=query, 
#                            articles=articles)

# @app.route('/submit/', methods=["GET", "POST"])
# def submit():
#     if request.method == "POST":
#         return do_submit()
#     else:
#         return render_template('submit.jinja2.html')

# def do_submit():
#     # article = Article(title=title, link=link)
#     # insert_article(article)
#     article = insert_article()
#     return render_template("inserted.jinja2.html", article=article)

def run_devserver():
    app.run(debug=True)

if __name__ == "__main__":
    run_devserver()
