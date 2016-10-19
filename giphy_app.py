import os
from flask import Flask, render_template, request
import giphypop
app = Flask(__name__)


#Defines function to pull the GIFs
def get_gif(search_term):
    g = giphypop.Giphy()
    results = g.search(search_term) # returns a list of objects    
    for result in results:
        print(result.media_url)
        print(result.url)


#creates the index page
@app.route('/')
def index():
    name = request.values.get('name', "Friends")
    greeting = "Hello, {}!".format(name)
    return render_template('index.html', greeting=greeting)


#creates the results page

@app.route('/results')
def results():
    gif = request.values.get('gif')
    gifs = ["One", "Two", "Three"]
    return render_template('results.html', gifs=gifs)



#creates the about page

@app.route('/about')
def about():
    return render_template('about.html')

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
