from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', company_name="Marketing Company", course_name="Marketing Course", price=100, description="This is a marketing course that teaches you how to market your products effectively.")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')