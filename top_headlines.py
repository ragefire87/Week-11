from flask import Flask, render_template
import requests
from datetime import datetime
from secrets_example import api_key
import json
import sys
import codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)


app = Flask(__name__)

@app.route('/')
def about():
    html = '''
      <b><h1> Welcome! </h1></b>
      '''
    return html

section_list = ['home', 'world', 'politics', 'nyregion', 'business', 'opinion', 'technology', 'science', 'health', 'sports', 'arts', 'books', 'food', 'travel', 'magazine', 'realestate', 'upshot']

@app.route('/user/<nm>/<section>')
@app.route('/user/<nm>')
def hello_name(nm, section=""):
    if section in section_list:
        baseurl = 'https://api.nytimes.com/svc/topstories/v2/'
        extendedurl = baseurl + section + '.json'
        params={'api-key': api_key}
        resp = requests.get(extendedurl, params)
        results = json.loads(resp.text)
        mylist = []
        section_list1 = []
        time = datetime.now().time()
        y = str(time).split(":")
        if y[0]<"12" and y[0]>="00":
            time1 = "Good morning"
        elif y[0]=="12" and y[1]=="00":
            time1 = "Good morning"
        elif y[0]>="12" and y[0]<"16" and y[1]>"00":
            time1 = "Good afternoon"
        elif y[0]>"12" and y[0]<"16" and y[1]=="00":
            time1 = "Good afternoon"
        elif y[0]=="16" and y[1]=="00":
            time1 = "Good afternoon"
        elif y[0]>="16" and y[0]<"20" and y[1]>"00":
            time1 = "Good evening"
        elif y[0]>"16" and y[0]<"20" and y[1]=="00":
            time1 = "Good evening"
        elif y[0]=="20" and y[1]=="00":
            time1 = "Good evening"
        elif y[0]>="20" and y[0]<"24" and y[1]>"00":
            time1 = "Good night"
        elif y[0]>"16" and y[0]<"20" and y[1]=="00":
            time1 = "Good night"
        elif y[0]=="24" and y[1]=="00":
            time1 = "Good night"
        elif y[0]=="00" and y[1]=="00":
            time1 = "Good morning"
        else:
            time1 = "Hello"

        j=1
        for i in results['results']:
            y = str(j)+"."+i['title']+" ("+i['url']+")"
            mylist.append(y)
            j+=1

        for j in section_list:
            if j!= section:
                z = '/user/'+nm+'/'+j
                section_list1.append((j,z))

        return render_template('user.html', section = section, section_list = section_list1, name=nm, time = time1, mylist = mylist[:5])

    else:
        section = 'technology'
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
        return render_template('user.html', section = section, name=nm, url = None, time = "Hello", mylist = mylist[:5])




#get_stories(section)

if __name__ == '__main__':
    app.run(debug=True)
