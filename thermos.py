from flask import Flask, render_template, url_for, request, redirect, flash
from datetime import datetime

from logging import DEBUG
class User:
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname

    def initials(self):
        return "{}.{}.".format(self.firstname[0],self.lastname[0])

app = Flask(__name__)
app.logger.setLevel(DEBUG)
app.config['SECRET_KEY'] = '5MS0\xa5\xf5\x03qb\xbd+\x80\x12\x13\xcd\xa3.A\xbd|\x07\xd5b\xf6'

bookmarks = []
def store_bookmarks(url):
    bookmarks.append(dict(
        url = url,
        user = "reindert",
        date = datetime.utcnow()
    ))

def new_bookmarks(num):
    return sorted(bookmarks, key = lambda bm: bm['date'], reverse = True)[:num]

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', Title = "My learning", user = User("Siva","Kumar"),new_bookmarks=new_bookmarks(5))

@app.route('/add',methods = ['GET','POST'])
def add():
    if request.method == "POST":
        url = request.form['url']
        store_bookmarks(url)
        app.logger.debug('URL stored')
        flash("Stored bookmark '{}'".format(url))
        return redirect(url_for('index'))
    return render_template('add.html', Title = "My learning", user = User("Siva","Kumar"))

if __name__ == "__main__":
    app.run(debug=True)