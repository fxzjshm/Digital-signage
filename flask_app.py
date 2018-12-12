# https://fxzjshm.pythonanywhere.com/Digital-signage
from flask import Flask, request, Response
from flask_script import Manager
import urllib.request

app = Flask(__name__)
manager = Manager(app)

@app.route('/<path:path>')
def test(path):
    response = urllib.request.urlopen('https://fxzjshm.github.io/' + path)
#    print response.read()
    res=Response(response.read())
    res.headers['Content-Type']=response.info()['Content-Type']
    return res, response.status

if __name__ == "__main__":
    manager.run()

