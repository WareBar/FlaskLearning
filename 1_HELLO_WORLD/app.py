from flask import Flask


# create the application
app = Flask(__name__)



# routes
@app.route("/")
def index():
    return "<h1>HELLO WORLD</h1>" #returning html tag
    # return "Hello World"        #returning plain text


# run the app both in localhost and in private id address
if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=8000
    )