from flask import Flask, render_template, request, json, redirect, session
from flask import Markup
import requests

app = Flask(__name__)
app.config["DEBUG"] = False

@app.route("/chart")
def chart():
    headers = {
        'Authorization': 'Bearer keyMdNcOcmTFobuDZ',
    }

    params = (
        ('view', 'Grid view'),
    )

    r = requests.get('https://api.airtable.com/v0/appAmdfpYQu9wNQdc/Imported%20table?api_key=keyMdNcOcmTFobuDZ', headers=headers, params=params)
    dict1 = r.json()
    dict2 = {}
    dataset = []
    name_list = []
    score_list = []
    for i in dict1['records']:
         dict2 = i['fields']
         dataset.append(dict2)
    for item in dataset:
        user_name_list.append(item.get('user_name'))
        member_score_list.append(item.get('member_score'))
    return render_template('index2.html', entries = zip(user_name_list, member_score_list))

if __name__ == '__main__':
   app.run(debug = True)
