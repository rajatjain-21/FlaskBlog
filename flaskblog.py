from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'Rajat Jain',
        'title': 'The Journey',
        'content': 'Blog Posted',
        'date_ppsted': 'April 20, 2018'
    },
    {
        'author': 'Nishtha Jain',
        'title': 'The Journey 2',
        'content': 'Second Blog Posted',
        'date_ppsted': 'April 21, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title="My truth")


if __name__ == "__main__":
    app.run(debug=True)
