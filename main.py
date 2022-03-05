from flask import Flask, render_template, request

App_learnFlask = Flask(__name__)

@App_learnFlask.route('/')
def home():
    return render_template('home.html')

@App_learnFlask.route('/about/')
def about():
    return render_template('about.html')

@App_learnFlask.route('/success', methods=["POST"])
def success():
    if(request.method == 'POST'):
        email = request.form['email_name']
        height = request.form['height_name']
        print(f"email: {email}")
        print(f"height: {height}")
        return render_template('success.html')

if __name__ == "__main__":
    App_learnFlask.run(debug=True)
