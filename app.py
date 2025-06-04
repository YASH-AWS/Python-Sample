from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return "Welcome to the Flask App deployed via Azure Function App!"

# About route
@app.route('/about')
def about():
    return "This is a sample 'About' page."

# Contact form (basic GET/POST)
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        message = request.form.get('message')
        return f"Thanks {name}, your message was received!"
    return '''
        <form method="post">
            Name: <input name="name"><br>
            Message: <textarea name="message"></textarea><br>
            <input type="submit">
        </form>
    '''

# Custom 404
@app.errorhandler(404)
def not_found(e):
    return "Page not found.", 404
