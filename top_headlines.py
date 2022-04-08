
import requests
from flask import Flask, render_template
from secret import API_KEY

app = Flask(__name__)

@app.route('/')

def homepage():
    return render_template('homepage.html')


@app.route('/headlines/<name>')

def headline(name):
    news_api = requests.get(f'https://api.nytimes.com/svc/topstories/v2/technology.json?api-key={API_KEY}')
    result = news_api.json()
    top_stories = []
    for i in result['results']:
        top_stories.append(i['title'])
        
    return render_template('top_headlines.html', tech_stories = top_stories[:5], name = name)

@app.route('/<name>')

def name(name):
    return render_template('name.html', name = name)

@app.route('/link/<name>')

def link(name):
    news_api = requests.get(f'https://api.nytimes.com/svc/topstories/v2/technology.json?api-key={API_KEY}')
    result = news_api.json()
    urls = []
    for i in result['results']:
        urls.append(i['url'])
    return render_template('urls.html', url = urls, name = name)




if __name__ == '__main__':
    print('start nytimes app', app.name)
    app.run(debug=True)



