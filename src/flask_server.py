# app.py
from flask import Flask, jsonify, request, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, TextAreaField
from wtforms.validators import DataRequired, Email, Optional

# local imports
from business.services.snippet_service import SnippetService

app = Flask(__name__, template_folder="presentation/templates", static_folder="presentation/static")
app.config['SECRET_KEY'] = 'mysecretkey'  # Needed for CSRF protection

# Create a WTForm class for the form
class MyForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')

# Root route
@app.route('/', methods=['GET', 'POST'])
def home_page():
    form = MyForm()
    # If the form is submitted and validated
    if form.validate_on_submit():
        # Extract the form data
        username = form.username.data
        email = form.email.data

        # Flash a message (Flask's messaging system)
        flash(f"Form submitted successfully! Username: {username}, Email: {email}")

        # Redirect to avoid form resubmission issues
        return redirect(url_for('home_page'))

    return render_template("dashboard.html", form=form)


class SnippetForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    description = TextAreaField('description', validators=[Optional()])
    code = TextAreaField('code', validators=[Optional()])
    tags = FieldList(StringField('tag'), validators=[Optional()], min_entries=1)
    links = FieldList(StringField('link'), validators=[Optional()], min_entries=1)
    submit = SubmitField('Submit')

@app.route('/snippets', methods=['GET', 'POST'])
def snippet_page():
    snip_form = SnippetForm()

    if snip_form.validate_on_submit():
        # Extract the form data
        title = snip_form.title.data
        description = snip_form.description.data
        code = snip_form.code.data
        tags = snip_form.tags.data
        links = snip_form.links.data
        SnippetService.create_snippet(title=title, description=description, code=code, tags=tags, links=links)

        return redirect(url_for('snippet_page'))

    snippets = SnippetService.read_all_snippets()
    return render_template("snippets.html", snippets=snippets, snippet_form=snip_form)

@app.route('/snippet/<id>', methods=['GET', 'POST'])
def snippet_update_page(id):
    snippet = SnippetService.read_one_by_id(id)
    
    if not snippet:
        return render_template("not_found.html")
    
    snip_form = SnippetForm()
    snip_form.title.data = snippet['title']
    snip_form.description.data = snippet['description']
    snip_form.code.data = snippet['code']
    for idx, tag in enumerate(snippet['tags']):
        if idx > 0: # because by default there is one entry
            snip_form.tags.append_entry()
        snip_form.tags[idx].data = tag
    # snip_form.links.data = snippet['links']
    for idx, link in enumerate(snippet['links']):
        if idx > 0: # because by default there is one entry
            snip_form.links.append_entry()
        snip_form.links[idx].data = link

    return render_template("snippet_update.html", snippet_form=snip_form)

# Simple API route for demonstration
@app.route('/api/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'Developer')  # Get the 'name' from query parameters
    return jsonify({"message": f"Hello, {name}!"})

# Run the server
if __name__ == '__main__':
    app.run(debug=True)
