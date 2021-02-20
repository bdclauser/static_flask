from flask import Flask, render_template

app = Flask(__name__)

# After importing Flask this then creates the object, defines the views, and starts the server.

@app.route('/') # home
def home():
    return "Hello, World!"

@app.route('/welcome') # home/welcome
def welcome():
    return render_template('welcome.html') # renders welcome.html

# This starts the server with the 'run()' method
if __name__=='__main__':
    app.run(debug=True)

