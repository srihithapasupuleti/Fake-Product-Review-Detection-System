from flask import Flask, request, render_template, flash, redirect, url_for
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import sys
import Sentiment_website_integration

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'dc98a1dff26acf9dac338188cfb512b5199944ea3f317ea1'


@app.route('/')
def my_form():
    return render_template('product_details.html')

@app.route('/success/<name>') 
def success(name): 
    result = Sentiment_website_integration.run_sentiment_analysis(name)
    print('Hello world!', file=sys.stderr)
    print(result, file=sys.stderr)
    return result

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['nm']
    processed_text = text.upper()
    return redirect(url_for('success',name = text)) 




if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)