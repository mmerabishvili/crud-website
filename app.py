from flask import Flask, render_template, request

# Create a Flask application instance
app = Flask(__name__)

# Define routes for the application

# Home route
@app.route('/')
def home():
    return render_template('index.html', company_name="Marketing Company", course_name="Marketing Course", price=100, description="This is a marketing course that teaches you how to market your products effectively.")

# About route
@app.route('/about')
def about():
    return render_template('about.html')

# Contact route
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    # Handle form submission and validation
    error = None
    success = False
    success_message = ""
    
    if request.method == 'POST':
        # Get form data and validate it
        first_name = request.form.get('first_name', "").strip()
        last_name = request.form.get('last_name', "").strip()
        email = request.form.get('email', "").strip()
        phone = request.form.get('phone', "").strip()

        # check if any of the fields are empty
        if not first_name or not last_name or not email or not phone:
            error = "All fields are required."

        elif len(first_name) > 100 or len(last_name) > 100 or len(email) > 100 or len(phone) > 20:
            error = "Input exceeds maximum length."

        elif not email or "@" not in email:
            error = "Invalid email address."
            
        else:
            success = True
            success_message = "Thank you for contacting us! We will get back to you shortly."

        print("ERROR:", error)
    return render_template('contact.html', error=error, success=success, success_message=success_message)