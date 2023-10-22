from flask import Flask

app2=Flask(__name__)
#decorator to route URL to access webpage directly
@app2.route('/hello')
def hello_world():
    return "Hello World!"
#alternatively use add_url_rule to bind URL to function
def hi_devi(self):
    return "Hi Devi how are you?"
app2.add_url_rule('/','hidevi',hi_devi)

if __name__=='__main__':
    app2.run()

    
