from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# After importing Flask this then creates the object, defines the views, and starts the server.


# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    print(db)
    form = LoginForm()
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'bclauser' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

    
# This starts the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)

