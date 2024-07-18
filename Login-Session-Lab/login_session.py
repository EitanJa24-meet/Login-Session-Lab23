from flask import Flask, render_template, request, url_for, redirect
from flask import session as login_session

app = Flask(__name__,
template_folder='templates',
static_folder='static')

app.config['SECRET_KEY'] = 'Your_secret_string'

@app.route('/home', methods=['GET', 'POST'])
def home():
	try:
		if request.method == "POST":
			Name = request.form["name"]
			Quote = request.form["quote"]
			Age = request.form["age"]
			login_session['name'] = Name
			login_session['quote']  = Quote
			login_session['age'] = Age
			print(login_session)
			return redirect(url_for('thanks'))
		else:	
			return render_template("home.html")
	except:
		return redirect(url_for('error'))

	
@app.route('/error', methods=['GET', 'POST'])
def error():
	return render_template("error.html")


@app.route('/thanks', methods=['GET', 'POST'])
def thanks():
	return render_template("thanks.html")

@app.route('/display', methods=['GET', 'POST'])
def display():
	return render_template("display.html")



if __name__ == '__main__':
	app.run(debug=True)

