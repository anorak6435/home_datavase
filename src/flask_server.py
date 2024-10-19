# app.py
from flask import Flask, jsonify, request, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

app = Flask(__name__, template_folder="presentation/templates")
app.config['SECRET_KEY'] = 'mysecretkey'  # Needed for CSRF protection

# Create a WTForm class for the form
class MyForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')

# Root route
@app.route('/', methods=['GET', 'POST'])
def home():
    form = MyForm()

    # If the form is submitted and validated
    if form.validate_on_submit():
        # Extract the form data
        username = form.username.data
        email = form.email.data

        # Flash a message (Flask's messaging system)
        flash(f"Form submitted successfully! Username: {username}, Email: {email}")

        # Redirect to avoid form resubmission issues
        return redirect(url_for('home'))

    return render_template("dashboard.html", form=form)

# Simple API route for demonstration
@app.route('/api/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'Developer')  # Get the 'name' from query parameters
    return jsonify({"message": f"Hello, {name}!"})

# Run the server
if __name__ == '__main__':
    app.run(debug=True)
