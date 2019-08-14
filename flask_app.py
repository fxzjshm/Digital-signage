# https://fxzjshm.pythonanywhere.com/Digital-signage

from flask import Flask, Response
from flask_script import Manager
import urllib.request
from urllib.parse import quote
import string

app = Flask(__name__)
manager = Manager(app)

@app.route('/<path:path>')
def test(path):

    # https://blog.csdn.net/qq_25406563/article/details/81253347
    url = quote('https://fxzjshm.github.io/' + path, safe=string.printable)

    response = urllib.request.urlopen(url)
#   print response.read()
    res=Response(response.read())
    res.headers['Content-Type']=response.info()['Content-Type']
    return res, response.status

if __name__ == "__main__":
    manager.run()

