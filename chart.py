from flask import Flask, render_template
import requests
import json
app = Flask(__name__)



@app.route('/')
def details():
	url="http://api.openweathermap.org/data/2.5/forecast/?q=singapore&cnt=5&mode=json&units=metric&APPID=ad4a9fa289b339beaebe078f6f28a831"
	d=requests.get(url).text
	afterjason=json.loads(d)
	mn=afterjason.get('list')[0].get('main').get('temp_min')
	mx=afterjason.get('list')[0].get('main').get('temp_max')
	des=afterjason.get('list')[0].get('weather')[0].get('description',"Not Available")
	return render_template("table.html",maximum=mx,minimum=mn,description=des,name="marcus")


@app.route('/full')
@app.route('/full/<placename>')
def fulldetails(placename="singapore"):
	url="http://api.openweathermap.org/data/2.5/forecast/?q=%s&cnt=5&mode=json&units=metric&APPID=ad4a9fa289b339beaebe078f6f28a831"%(placename)
	d=requests.get(url).text
	afterjason=json.loads(d)
	mini=""
	maxi=""
	for eachday in afterjason.get('list'):
		mini=mini+""" %s,"""%(eachday.get('main').get('temp_min'))
		maxi=maxi+""" %s,"""%(eachday.get('main').get('temp_max'))
	return render_template("chart.html",min=mini,max=maxi,placename=placename)





if __name__ == '__main__':
   app.run(debug=True)