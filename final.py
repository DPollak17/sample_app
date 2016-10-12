from flask import Flask, render_template, request
import giphypop

g = giphypop.Giphy()
results = g.search('cats') # returns a list of objects
for result in results:
    print(result.media_url)
    print(result.url)

@app.route('/')
def index():
    ...

@app.route('/results')
def results():
    ...

@app.route('/about')
def about():
    ...

{% for result in results %}
    {{ result.media_url }}
    {{ result.url }}
{% endfor %}

<img src="[Media Url goes here]">

http://media0.giphy.com/media/26uf9IAZN7JvvYbwA/giphy.gif # Media (image) Url
http://giphy.com/gifs/love-cat-cats-26uf9IAZN7JvvYbwA # GIF Url
http://media1.giphy.com/media/26uf5hiFbD0DdZdGo/giphy.gif
http://giphy.com/gifs/cat-judgemental-judgey-26uf5hiFbD0DdZdGo