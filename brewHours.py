from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    users = [ 'Mike','Tim','John', 'Chris' ]
    return render_template('index.html', title='Welcome', members=users)

app.run(host='0.0.0.0', port=81)