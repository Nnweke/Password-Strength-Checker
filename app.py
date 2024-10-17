import os
import re
from flask import Flask, render_template, request

app = Flask(__name__)

def check_password_strength(password):
    strength = 0
    suggestions = []

    # Check for length
    if len(password) >= 8:
        strength += 1
    else:
        suggestions.append("Password should be at least 8 characters long.")

    # Check for digit
    if re.search(r'[0-9]', password):
        strength += 1
    else:
        suggestions.append("Password should contain at least one digit.")

    # Check for uppercase letter
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        suggestions.append("Password should contain at least one uppercase letter.")

    # Check for lowercase letter
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        suggestions.append("Password should contain at least one lowercase letter.")

    # Check for special character
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        suggestions.append("Password should contain at least one special character.")

    if strength <= 2:
        return "Weak", suggestions
    elif strength == 3 or strength == 4:
        return "Medium", suggestions
    else:
        return "Strong", suggestions

@app.route('/', methods=['GET', 'POST'])
def index():
    strength = None
    suggestions = []
    if request.method == 'POST':
        password = request.form['password']
        strength, suggestions = check_password_strength(password)
    return render_template('index.html', strength=strength, suggestions=suggestions)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)