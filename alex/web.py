import duckduckgo
import unirest
from stanford_corenlp_pywrapper import sockwrap

def weather(query):
	print 'Identifying the location . . .'
	try:
		response = unirest.post("https://textanalysis.p.mashape.com/nltk-stanford-ner",
	  		headers={
	    	"X-Mashape-Key": "E7WffsNDbNmshj4aVC4NUwj9dT9ep1S2cc3jsnFp5wSCzNBiaP",
	    	"Content-Type": "application/x-www-form-urlencoded"
	  			},
	  		params={
	    	"text": query
	  		}
		)
	except:
		print 'Unable to connect to internet'
		return
	location = ''
	for entity in response.body['result'].split():
		word,tag = entity.split('/')
		if(tag == 'LOCATION'):
			location += ' '+word
	if(location != ''):
		print 'Gathering weather information for'+location
		import urllib2, urllib, json
		baseurl = "https://query.yahooapis.com/v1/public/yql?"
		yql_query = "select * from weather.forecast where woeid in (select woeid from geo.places(1) where text=\""+location+"\")"
		yql_url = baseurl + urllib.urlencode({'q':yql_query}) + "&format=json"
		try:
			result = urllib2.urlopen(yql_url).read()
			data = json.loads(result)
			result = data['query']['results']['channel']
			print result['location']['city']+' '+result['location']['country']+' '+result['location']['region']
			print result['item']['condition']['date']
			print result['item']['condition']['text']
			print result['item']['condition']['temp']+' '+result['units']['temperature'] 
		except:
			print 'Unable to connect to internet'
	else:
		print 'Unable to get the location.'
	

def generic(query):
	pass