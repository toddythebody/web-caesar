from flask import Flask, request
from caesar import encrypt

app = Flask(__name__)
app.config['DEBUG'] = True

form = '''
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <form method="POST">
        <label for="rotate">Rotate by: </label>
        <input id="rotate" type="text" name="rot" value="0">
        <textarea type="text" name="text">{0}</textarea>
        <input type="submit">
    </form>
    </body>
</html>
'''

@app.route('/', methods=['POST'])
def Encrypt():
    newMessage = encrypt(request.form['text'], int(request.form['rot']))
    return form.format(newMessage)

@app.route('/')
def index():
    return form.format('')

app.run()
