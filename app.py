import os
from flask import Flask, render_template, jsonify

app = Flask(__name__)


file_list = []

def get_img_url():
    for  files in os.walk('./static'):
        for file in files:
            file_name = "./static/".join(file)
            file_list.append(file_name)
    return file_list

@app.route('/')
def home():
    file = get_img_url()
    print (file)
    return render_template('index.html', file=file)





if __name__ == '__main__':
    app.run(debug=True)
