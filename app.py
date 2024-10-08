from flask import Flask, request, render_template
import re

app = Flask(__name__)

def check_password_strength(password):
    # Initialize strength to 0
    strength = 0

    # Check password length
    if len(password) >= 8:
        strength += 1

    # Check for uppercase letter
    if re.search(r'[A-Z]', password):
        strength += 1

    # Check for lowercase letter
    if re.search(r'[a-z]', password):
        strength += 1

    # Check for digit
    if re.search(r'[0-9]', password):
        strength += 1

    # Check for special character
    if re.search(r'[\W_]', password):
        strength += 1

    # Check for very weak password
    if len(password) < 10 and re.search(r'[0-9]', password) and not re.search(r'[\W_]', password):
        strength = 0  # Set strength to 0 for very weak password

    print(f"Password: {password}, Strength: {strength}")  # Debug statement
    return strength

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    password = request.form['password']
    strength = check_password_strength(password)
    return render_template('result.html', strength=strength)

if __name__ == '__main__':
    app.run(debug=True)