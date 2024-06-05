from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reviews.db'
db = SQLAlchemy(app)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    rate = db.Column(db.Integer)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reviews', methods=['GET', 'POST'])
def reviews():
    if request.method == 'POST':
        text = request.form['text']
        rate = int(request.form['rate'])
        review = Review(text=text, rate=rate)
        db.session.add(review)
        db.session.commit()
        return redirect(url_for('reviews'))
    reviews = Review.query.all()
    return render_template('reviews.html', reviews=reviews)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)