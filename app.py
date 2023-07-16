from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author':'Corey Schafer',
        'title':'blog post 1',
        'content': 'first post content',
        'date_posted':'April 20, 2018'
    },
    {
        'author':'Shayan Waqar',
        'title':'blog post 2',
        'content':'second post content',
        'date_posted':'July 16, 2023'
    }
]

'''
FLASK
route	Flask route
frt	    Render template
routegp	Flask route with GET, POST
routep	Flask route POST only

JINJA2
fvar    {{Name var}}
ffor	Flask for
fif	    Flask if
fife	Flask ife
felif	Flask elif
'''


@app.route("/")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='title')

if __name__ == '__main__':
    app.run(debug=True)