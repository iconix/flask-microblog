from flask import render_template #Jinja2 templating engine
from flask import flash, redirect
from app import app
from forms import LoginForm

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

@app.route('/login', methods = ['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for OpenId="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
		return redirect('/index')
	return render_template('login.html',
		title = 'Sign In',
		form = form,
		providers = app.config['OPENID_PROVIDERS'])