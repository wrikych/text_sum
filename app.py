from flask import Flask, render_template, url_for, request, redirect 
from helpers import *

app = Flask(__name__) 

@app.route('/') 
def index(): 
    return render_template('index.html')

@app.route('/wiki', methods=['GET','POST'])
def wiki():
    return render_template('wiki.html')

@app.route('/text', methods=['GET','POST'])
def text():
    return render_template('text.html')

@app.route('/wiki_results', methods=['GET','POST']) 
def wiki_results(): 
    input_text = request.form['url'] 
    input_sents = int(request.form['num_sents']) 
    sentences = wiki_to_sents(input_text, num_sents=input_sents) ## Old function 
    return render_template('wiki_results.html', sentences = sentences) 

@app.route('/text_results', methods=['GET','POST']) 
def text_results(): 
    input_text = request.form['text'] 
    input_sents = int(request.form['num_sents']) 
    sentences = text_to_sents(input_text, num_sents=input_sents) ## Old function 
    return render_template('text_results.html', sentences = sentences) 

if __name__ == "__main__": 
    app.run(debug=True)