from flask import Flask, render_template


app =  Flask(__name__, template_folder="templates")


"""

"render_templates" function, accepts the the name of the templates and can accept variables
which can be used to dynamically show content into the HTML files/templates

in which can be display in the html by wrapping the value to "{{ value }}" curly braces

"""
@app.route("/")
def index():
    content_to_show2 = "HELLO PO FROM VARIABLE"
    content_to_show1 = "HELLO FROM ANOTHER VARIBLE"
    myContents = ['A',"B","CA","E","F"]

    # passed the html to render when this url is hit and pass the data to render  to template
    return render_template('index.html', value1=content_to_show1, value2=content_to_show2, myContents=myContents)


"""
Filters, basically a utility function for html templates

"""
@app.route("/filters")
def filters():
    text = "hello world"
    return render_template("filters.html", text=text)


# creating custom filter
# utility for reversing a string
@app.template_filter("reverse_string")
def reverse_string(s):
    return s[::-1]



if __name__ == "__main__":
    app.run(
        debug=True,
        port=8000,
        host="0.0.0.0"
    )