from flask import Flask

app=Flask(__name__)

@app.route('/hey/<username>/<int:password>')
def hey_there(username,password):
    return f"<h1>hey there</h1> {username}!<h2>is your password</h2>{password}?"

if __name__=='__main__':
    app.run(debug=True)
