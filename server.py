from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'yesican'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    print(request.form)
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('display_info.html')

@app.route('/home')
def return_home():
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)