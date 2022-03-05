from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/success', methods=["POST"])
def success():
    if(request.method == 'POST'):
        email = request.form['email_name']
        height = request.form['height_name']
        print(f"email: {email}")
        print(f"height: {height}")
        return render_template('success.html')

if __name__ == "__main__":
    app.run(debug=True)
