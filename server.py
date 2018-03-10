from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'lkajdf;lakjdf'

@app.route('/')
def index():
	if 'myNumber' not in session:
		session['myNumber'] = random.randrange(1,101)
	if 'guess' not in session:
		session['game_status'] = "Can you guess my number?"
		session['style'] = 'green'
	return render_template('index.html')

@app.route('/process', methods=['POST'])
def game():
	session['guess']=request.form['guess']
	guess = int(session['guess'])
	session.modified = True
	
	if guess == session['myNumber']:
		session['game_status'] = "That's right!"
		session['style'] = 'green'
	elif guess < session['myNumber']:
		session['game_status'] = "Too low..."
		session['style'] = 'red'
	elif guess > session['myNumber']:
		session['game_status'] = "Too high..."
		session['style'] = 'red'
	return redirect('/')

@app.route('/clear', methods=['POST'])
def clear_session():
	print('pushed clear button')
	session.clear()
	return redirect('/')

app.run(debug=True)