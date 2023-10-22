#using variables in flask
from flask import Flask

app3=Flask(__name__)
@app3.route('/hello/<name>')
def hello_v(name):
    return "hi there %s"%name

if __name__=='__main__':
    app3.run(debug=True)



