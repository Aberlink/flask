from flask import Flask, render_template, url_for

app = Flask(__name__)


posts = [
    {'author': 'michal', 'title': 'blog post 1', 'content': 'first post', 'date_posted': 'june'},
    {'author': 'kasia', 'title': 'blog post 2', 'content': 'second post', 'date_posted': 'july'}
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
