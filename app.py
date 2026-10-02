from flask import Flask, render_template

app = Flask(__name__)

# This tells Flask what to show when you visit the main web address
@app.route('/')
def home():
    return render_template('index.html')

# This starts the local web server when you run this file
if __name__ == '__main__':
    app.run(debug=True)
