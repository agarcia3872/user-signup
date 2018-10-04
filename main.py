from flask import Flask, request, redirect, render_template
import getpass

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/validate-fields", methods=["POST"])
def validate_fields():
    username = request.form['username']
    password = request.form['password']
    verify_passwd = request.form['verify-passwd']
    email = request.form['email']
    isError = False
    error_string = "/?" 

    if not username:
        error1 = "That's not a valid username"
        error_string = error_string + "error1=" + error1 + "&"
        isError = True
        #return redirect("/?error=" + error)
    if not password or len(password) < 3 or len(password) > 20 or " " in password:
        error2 = "That's not a valid password"
        error_string = error_string + "error2=" + error2 + "&"
        isError = True
       # return redirect("/?error=" + error)
    if not verify_passwd or verify_passwd == " " or password != verify_passwd:
        error3 = "Passwords do not match"
        error_string = error_string + "error3=" + error3 + "&"
        isError = True
        #return redirect("/?error=" + error)
    if '@' not in email or '.' not in email or len(email) < 3 or len(email) > 20 or " " in email:
        error4 = "That's not a valid email"
        error_string = error_string + "error4=" + error4 + "&"
        isError= True
    if isError == True:
        return redirect(error_string)
    else:
        return render_template('welcome.html', username=username)

@app.route("/")
def index():
    encoded_error1 = request.args.get("error1")
    encoded_error2 = request.args.get("error2")
    encoded_error3 = request.args.get("error3")
    encoded_error4 = request.args.get("error4")
    return render_template('user-signup.html', error1=encoded_error1, error2=encoded_error2, error3=encoded_error3, error4=encoded_error4)

app.run()