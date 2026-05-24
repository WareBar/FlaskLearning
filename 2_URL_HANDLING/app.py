from flask import Flask, request


# create the application
app = Flask(__name__)



# routes
@app.route("/")
def index():
    return "wows"    #returning plain text


# routes always start with "/"
@app.route("/hello")
def hello():
    return "Hello World"

# this is called URL PROCESSOR
# it process the url
@app.route("/greet/<name>")
def greet(name):
    return f"Hello {name}"
 


# DYNAMIC URL
"""datas passed from url are automatically string, so to use it for math, convert into integer"""
@app.route("/add/<int:number1>/<int:number2>")
def add(number1, number2):
    return f"{number1} + {number2} = {number1 + number2}"


# URL PARAMETERS
"""
datas lived inside the "request"
datas are passed after the '?' key, like url?name='barry' 

unlike in django, no need to include 'request' inside the url function, it automatically lives or connected
just import request from flask

! from flask import request

"""
@app.route("/handle_url_params")
def handle_params():
    # request arguments are dictionary
    greeting = request.args.get("greeting", "") # it can also be request.args['greeting]
    name = request.args.get("name","") # noticed the  "" empty string after name?, it a fallback when the specified arguments do not exist in request
    return f"{greeting}, {name}"


"""
Methods

we can passed that into app.route to specify what the route can do, either only returns datas or accept data from forms
typing '/example/ at the browser when methods=["POST"] will return Method not allowed  error, since now the url can now only communicate through POST method

if you want to support both, just add "GET" inside the methods list to support hybrid methods allowed, methods=["GET","POST"]
 

GET = used when you want to return information if the url was hit
POST = used to process data passed to the url
DELETE = used when you want to delete a specific data instance
PUT/PATCH = used when you want to update the data of a specific item

"""
@app.route("/example", methods=["GET","POST"])
def request_method_handling():
    return f'THIS IS {request.method} REQUEST URL'



"""
Status code can be returns as a second value

return data, code


200(means OK) is the default status code for GET request
"""
@app.route('/url_status_code')
def url_status_code():
    return 'HELLO THIS IS THE STATYS CODE', 200



# run the app in localhost
if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=8000
    )