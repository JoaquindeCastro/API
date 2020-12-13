import requests
import json
'''
response = requests.get('https://joaquindecastro-api.herokuapp.com/quotes/')

print(response.json())
'''

url = 'https://joaquindecastro-api.herokuapp.com/quotes/post'

for n in range(1, 100):
	params = {
	'method':'getQuote',
	'lang':'en',
	'format':'json'
	}
	response = requests.get('http://api.forismatic.com/api/1.0/',params)
	jsonText = None
	while jsonText is None:
	    try:
	    	jsonText = json.loads(response.text)
	    except:
	         pass

	data = {'quoteText': jsonText['quoteText'],'quoteAuthor':jsonText['quoteAuthor']}

	x = requests.post(url, data = data)

	print(x)