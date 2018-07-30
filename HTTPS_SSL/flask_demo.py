from flask import Flask    
app = Flask(__name__) 
@app.route('/')
def hello_word():
    return 'Hello World!'   
app.run('0.0.0.0', debug=True, port=433, ssl_context=('/root/ssl/aiwechat.top.crt', '/root/ssl/aiwechat.top.key'))  
