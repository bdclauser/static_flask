from flask import Flask, render_template, url_for, request

app = Flask(__name__)

# After importing Flask this then creates the object, defines the views, and starts the server.


@app.route('/')  # home
def home():
    return "Hello, World! Hey!"


@app.route('/welcome')  # home/welcome
def welcome():
    return render_template('welcome.html')  # renders welcome.html


# This starts the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)


# Route for handling the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != error = 'Invalid Credentials. Please try again.'
        else:
            return redirecte(url_for('home')
                             )
    return render_template('login.html', error=error)
