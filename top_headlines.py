from flask import Flask, render_template
import requests
from secrets_example import api_key
import json
import sys
import codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)


app = Flask(__name__)


@app.route('/user/<nm>')
def hello_name(nm):
    baseurl = 'https://api.nytimes.com/svc/topstories/v2/'
    extendedurl = baseurl + section + '.json'
    params={'api-key': api_key}
    resp = requests.get(extendedurl, params)
    results = json.loads(resp.text)
    mylist = []
    j=1
    for i in results['results']:
        y = str(j)+"."+i['title']+" ("+i['url']+")"
        mylist.append(y)
        j+=1
    return render_template('user.html', name=nm, mylist = mylist[:5])

@app.route('/')
def about():
    html = '''
      <b><h1> Welcome! </h1></b>
      '''
    return html


section = 'technology'
#get_stories(section)

if __name__ == '__main__':
    app.run(debug=True)
