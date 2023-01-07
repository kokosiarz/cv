# coding=UTF8
import json
from flask import Flask, render_template
from flask_frozen import Freezer

app=Flask(__name__)
@app.route('/')
def home():
    with open('data.json',encoding='utf8') as data_file:
        data = json.load(data_file)
    return render_template('cv.html',data=data, getid = lambda x : "skill_level_"+str(id(x)))

# @app.route('/pdf/')
# def pdf():
#     with open('data.json',encoding='utf8') as data_file:
#         data = json.load(data_file)
#     return data


# freezer = Freezer(app)

if __name__ == "__main__":
    # freezer.freeze()
    app.run(debug=True)
