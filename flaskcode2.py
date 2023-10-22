from flask import Flask

app2=Flask(__name__)
#decorator to route URL to access webpage directly
@app2.route('/hello')
def hello_world():
    return "Hello World!"

if __name__=='__main__':
    app2.run()