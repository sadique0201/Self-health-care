# main.py

from flask import Flask, render_template

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route for user login and registration
@app.route('/login')
def login():
    return render_template('login.html')

# Route for displaying user profile
@app.route('/profile/<username>')
def profile(username):
    # Fetch user data from your database or other sources
    # Example: user = get_user_by_username(username)
    # Render the profile template with user data
    return render_template('profile.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)
