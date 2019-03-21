from flask import Flask, request
from caesar import encrypt

app = Flask(__name__)
app.config['DEBUG'] = True

form = '''
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
      <form method="post">
        <label for="rotate">Rotate by: </label>
        <input id="rotate" type="text" name="rot" value="0">
        <textarea type="text" name="text"></textarea>
        <input type="submit">
    </body>
</html>
'''

@app.route('/', methods=['POST'])
def Encrypt(rot, text):
    newMessage = encrypt(text, rot)
    return "<h1>" + newMessage + "</h1>"

@app.route('/')
def index():
    return form

app.run()
