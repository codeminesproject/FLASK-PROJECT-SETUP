"""
install flask in a system: pip install flask

render_template is used to get all text from html and render on browser

"""

from flask import Flask,render_template

# create object of Flask
obj = Flask(__name__)

@obj.route("/index")
def home():
    return render_template("index.html")


# run flask on web browser
if __name__=="__main__":
    obj.run()