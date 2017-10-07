from flask import Flask, render_template, request, session, redirect, url_for

test_username = "user"
test_password = "passwrd"

app = Flask(__name__)
app.secret_key = "secret"

@app.route('/', methods=["GET"])
def root():

    #logs user out of session
    if 'logout' in request.args.keys():
        session.pop('username')

    # if user is in session, take him/her to welcome page
    if 'username' in session.keys():
        return redirect(url_for("response", name=session['username']))

    # if new session, go to login page
    return render_template("root.html", error="" )


@app.route('/welcome', methods=["GET", "POST"])
def response():
    if request.args['username'] == test_username and request.args['password'] == test_password:
        session['username'] = request.args['username']
        return render_template("welcome.html", name=request.args["username"])
    
    elif request.args['username'] != test_username:
        return redirect(url_for("root", error="Bad username."))
    
    elif request.args['password'] != test_password:
        return redirect(url_for("root", error="Bad password."))

    return redirect(url_for("root", error="You should not get to this point." ))

if __name__ == '__main__':
	app.debug = True
	app.run()
