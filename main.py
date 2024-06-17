from flask import Flask, jsonify, render_template, request
import telnetlib
host = "177.73.245.76"
port= "3023"
user = "suporte"
senha= "suporte"
cmd1="ip route print"

app = Flask(__name__)

@app.route('/lista')
def listando():

    tn = telnetlib.Telnet(host,port)
    #tn.read_until(b"login: ")
    tn.write(user.encode('ascii') + b"\r")
    #tn.read_until(b">").decode("utf-8")
    
    tn.read_until(b"Password: ").decode("utf-8")
    tn.write(senha.encode('ascii') + b"\r")
    tn.read_until(b">").decode("utf-8")
    tn.read_until(b">").decode("utf-8")
    tn.write(cmd1.encode('ascii') + b"\r")
    tn.read_until(b"#").decode("utf-8")
    aux = tn.read_until(b">").decode("utf-8")
    print(jsonify(aux))
    return jsonify(aux)

@app.route('/')
def index():
    return render_template('index.html')
if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0"
        
        )
