#!flas/bin/python
from flask import render_template
from app import app
from .forms import WordForm

@app.route('/', methods=['GET','POST'])
@app.route('/home', methods=['GET','POST'])
def home():
    words = []
    form = WordForm()
    if form.validate_on_submit():
        words.append(form.word_field.data)
        print(words)
    return render_template("home.html",
                           form=form,
                           word=words)
