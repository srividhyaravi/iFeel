from flask import Flask, flash, redirect, render_template, request, session, abort
import cgi
from sentiment_analysis import get_tweets

app = Flask(__name__)
 
@app.route('/')
def my_form():
    return render_template('index1.html')

@app.route('/',methods = ['POST'])
def result():
      result = request.form['twitter']
      get_tweets(result)
      return render_template("result.html",result = result)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000,debug=True)
