from flask import Flask, flash, redirect, render_template, request, session, abort
import cgi
from extract_tweets import get_tweets

app = Flask(__name__)
 
@app.route('/')
def my_form():
    return render_template('index1.html')

@app.route('/',methods = ['POST'])
def result():
      result = request.form['twitter']
      sad_score_list = get_tweets(result)
      labels = ["January","February","March","April","May","June","July","August"]
      return render_template("result.html", values=sad_score_list, labels=labels)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=1234,debug=True)
