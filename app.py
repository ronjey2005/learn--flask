from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import EmailModule

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:CaitlynClarise0711@localhost/height_collector'
db = SQLAlchemy(app)


class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)
    email_ = db.Column(db.String(120), unique=True)
    height_ = db.Column(db.Integer)

    def __init__(self, email_, height_):
        print(f"--- email: {email_}")
        print(f"--- height: {height_}")
        self.email_ = email_
        self.height_ = height_

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
        print(db.session.query(Data))
        print(db.session.query(Data).filter(Data.email_ == email).count())
        #if(db.session.query(Data).filter(Data.email_ == email).count() == 0):
        data = Data(email, height)
        db.session.add(data)
        db.session.commit()

        EmailMod = EmailModule(email,height)
        EmailMod.send_email()

        return render_template('success.html')
        #return render_template('index.html' , text="already exist!")

if __name__ == "__main__":
    app.run(debug=True)
