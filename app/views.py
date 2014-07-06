from flask import render_template #Jinja2 templating engine
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = { 'nickname': 'iconix' } # fake user
	#user = {}
	posts = [ # fake array of posts
		{ 
			'author': { 'nickname': 'John' }, 
			'body': 'Beautiful day in Seattle!' 
		},
		{ 
			'author': { 'nickname': 'Susan' }, 
			'body': 'The Avengers movie was so cool!' 
		}
	]
	return render_template("index.html",
		title = 'Home',
		user = user,
		posts = posts)
