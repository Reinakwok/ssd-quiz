from flask import Flask, render_template, request, redirect, url_for, session
import re

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/search', methods=['POST'])
def search():
    search_term = request.form['search_term']
    
    # Validate the input to prevent XSS and SQL Injection attacks
    if is_xss_attack(search_term):
        return redirect(url_for('home', message='Invalid input: Potential XSS attack detected. Please try again.'))
    
    if is_sql_injection(search_term):
        return redirect(url_for('home', message='Invalid input: Potential SQL injection detected. Please try again.'))
    
    return render_template('result.html', search_term=search_term)

def is_xss_attack(input_text):
    # Basic validation for XSS attack
    xss_patterns = ['<', '>', 'script', 'alert', '&', ';']
    return any(pattern in input_text.lower() for pattern in xss_patterns)

def is_sql_injection(input_text):
    # Basic validation for SQL injection
    sql_patterns = ['\'', '--', '/*', '*/', 'or ', 'and ', 'select ', 'insert ', 'update ', 'delete ', 'drop ']
    return any(pattern in input_text.lower() for pattern in sql_patterns)

if __name__ == '__main__':
    app.run(debug=True)
