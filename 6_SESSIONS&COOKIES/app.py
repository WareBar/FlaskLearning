from flask import Flask, render_template, session, make_response, request, flash

"""
Use Cookies if we want to keep the data on the client side
Use Session if we want to keep the data on the server side
-for security reason, for something sensitive we keep it to server side



Sessions
Use a session when we want to maintain data across requests for a particular user.
In Flask, the default session is actually stored client-side in a signed cookie.
Flask signs the session cookie so the server can detect if it has been tampered with.
The user generally cannot modify the session data without invalidating the signature, assuming the secret key is kept secure.
For truly sensitive or large data, use a server-side session store such as Redis or a database.
Any Flask route/function handling that user's request can access:

session["username"]

Cookies
Use cookies when we want to store data on the client/browser side.
The browser stores the cookie and sends it back to the server with requests.
Cookies are not inherently secure because the client can inspect and potentially modify them.
Avoid storing sensitive information directly in cookies.

"""


# Create the Flask app instance and point it to the folder containing HTML templates
app = Flask("__name__", template_folder='templates')

# In order to use session-based storage, Flask needs a secret key to sign the session cookie.
# This key is used to cryptographically sign (not encrypt) the session data,
# so Flask can detect if the cookie has been tampered with on the client side.
app.secret_key = '2343sdf34'


@app.route("/")
def index():
    # Home page route, simply renders the index template with no extra data
    return render_template('index.html')


@app.route("/set_data")
def set_data():
    """
    a session data is a sensitve information that the user can't see or change
    """
    # Store values in the session dict; Flask will sign and send this as a cookie
    session['name'] = 'Mike'
    session['other'] = 'hello world'
    # Confirm to the user that the session data was set
    return render_template('index.html', message='Session data set')

@app.route("/get_data")
def get_data():
    # Check that both expected keys exist in the session before trying to read them
    if 'name' in session.keys() and 'other' in session.keys():
        name = session['name']
        other = session['other']
        # Display the retrieved session values back to the user
        return render_template('index.html', message=f'Name: {name}, Other: {other}')
    else:
        # No session data found (e.g., session was never set or was cleared)
        return render_template('index.html', message='Session not found')


@app.route('/clean_session')
def clean_session():
    # Remove all data stored in the session for this user
    session.clear()
    return render_template('index.html', message='Session Cleared')


@app.route('/set_cookie')
def set_cookie():
    # Build the response object first so we can attach a cookie to it
    response = make_response(render_template('index.html', message='Cookie data set'))
    # Set a plain cookie on the client's browser (not signed/encrypted like session data)
    response.set_cookie('cookie_name','cookie_valuess')
    return response

@app.route('/get_cookie')
def get_cookie():
    # when a client send a request, the cookie is always present, but thats uncertain for the value inside
    if request.cookies.keys():    
        # NOTE: this grabs the cookie *names*, not their values (likely a bug -
        # probably meant request.cookies.get('cookie_name') to fetch the actual value)
        cookie_value = request.cookies.keys()
        return render_template('index.html',message=f'Cookie value: {cookie_value}')
    else:
        # No cookies were sent with the request at all
        return render_template('index.html', message=f'Cookie value not found')

@app.route("/remove_cookie")
def remove_cookie():
    # to remove a cookie, we just set or let it expire so it instantly disappear
    response = make_response(render_template('index.html', message='Cookie data set'))
    # Setting expires=0 tells the browser to treat the cookie as already expired,
    # causing it to delete the cookie immediately
    response.set_cookie('cookie_name', expires=0)
    return response


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        # Just show the login form on a normal page visit
        return render_template('login.html')
    else:
        # Hardcoded "user database" for demo purposes only (not secure for real use)
        user = {
            'username':'barry',
            'password':'adam'
        }

        # Pull submitted credentials from the login form
        username = request.form['username']
        password = request.form['password']

        # Compare submitted credentials (stripped of whitespace) against the stored user
        if  user['username'].strip() == username.strip() and user['password'].strip() == password.strip():
            # flash() stores a one-time message in the session to show on the next rendered page
            flash('Successful Login!')
            return render_template('index.html', messages="")
        else:
            flash('Login Failed!')
            return render_template('index.html', messages="")



if __name__ == "__main__":
    # Run the development server, accessible on all network interfaces, port 8000,
    # with debug mode on (auto-reload + detailed error pages - don't use in production)
    app.run(
        debug=True, port=8000, host="0.0.0.0",
    )