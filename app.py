from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Simulated database (list to store registrations)
registrations = []

@app.route('/')
def home():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    registrations.append({'name': name, 'email': email})
    return redirect(url_for('success'))

@app.route('/success')
def success():
    return 'Registration successful! <a href="/">Back</a>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)