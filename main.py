from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
  # return 'Hello World!'
    return render_template('index.html', name='ee')

@app.route('/week/<week>/add/<dish>')
def add_dish(week='next', dish=1):
    # return 'Parameters %s - %s' % (week, dish)
    return render_template('add.html', week=week, dish=dish)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.debug = True
    app.run(None, 4000)
