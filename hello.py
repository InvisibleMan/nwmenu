from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
  # return 'Hello World!'
    return render_template('index.html', name='ee')

if __name__ == '__main__':
    app.debug = True
    app.run(None, 4000)
