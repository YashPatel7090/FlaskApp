from flask import Flask, render_template, url_for

Finance = Flask(__name__)

@Finance.route('/')
def home():
    return render_template('home.html')



if __name__ == "__main__":
    Finance.run(debug=True)

