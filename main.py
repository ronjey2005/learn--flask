from flask import Flask, render_template

App_learnFlask = Flask(__name__)

@App_learnFlask.route('/')
def home():
    return render_template('home.html')

@App_learnFlask.route('/about/')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    App_learnFlask.run(debug=True)
