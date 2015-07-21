#!../flask/bin/python
from flask import render_template
from app import truecross
from app import app
from .forms import WordForm

@app.route('/', methods=['GET','POST'])
@app.route('/home', methods=['GET','POST'])
def home():
	word_search = []
	form = WordForm()
	if form.validate_on_submit():
		word_search, hints = truecross.create_from_list(form.word_field.data.split(','))
		word_search = word_search.get_grid()
		print(word_search)
		print(hints)
	return render_template("home.html",
                           form=form,
                           puzzle=word_search)
