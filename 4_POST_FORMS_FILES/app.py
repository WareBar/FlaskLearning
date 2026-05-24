from flask import Flask, render_template, request
import pandas as pd


app = Flask(__name__, template_folder="templates")


@app.route("/", methods=["GET","POST"])
def index():
    return render_template("index.html")




# login function, validates data
@app.route("/login", methods=["POST"])
def login():
    # static credentials
    true_email = "barryadam615@gmail.com"
    true_password = "admin123"


    # data from the form data
    form_email = request.form.get("email", "")
    form_password = request.form.get("password","")

    print(request.form)

    # remove trailing emptry space then compare value
    if true_email.strip() == form_email.strip() and true_password.strip() == form_password.strip():
        return "Success", 200
    else:
        return "Failed", 403



@app.route("/file_upload", methods=["POST"])
def file_upload():
    # request has many things inside, if expecting files then request.files, if expecting json then requiest.json 
    file = request.files["file"]
    print(file)
    if file.content_type == "text/plain":
        return file.read().decode()
    elif file.content_type == "vnd.openxmlformats-officedocument" or file.content_type == "application/vnd.ms-excel":
        df = pd.read_excel(file)
        return df.to_html()

    return ''


if __name__ == "__main__":
    app.run(
        debug=True, port=8000, host="0.0.0.0",
    )

