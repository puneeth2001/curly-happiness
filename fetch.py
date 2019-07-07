import requests
import os
query =  """
	{
			allDiseases{
		name
		symptom {
		  name
		}
		}
	}"""

request = requests.get('http://127.0.0.1:8090/graphql/', json={'query': query})
a = request.json()

def no_of_diseases_registered():
	b = a['data']['allDiseases']
	total = len(b)
	return(total)

length = no_of_diseases_registered()

def get_diseases():
	for i in range (length):
		symptom = a['data']['allDiseases'][i]['name']
		print(symptom)

def no_of_symptoms():
	for i in range(length):
		total = len(a['data']['allDiseases'][i]['symptom'])
		return(total)

nos= no_of_symptoms()

def get_symptoms():
	for i in range (length):
		for j in range(nos):
			disease = a['data']['allDiseases'][i]['symptom'][j]['name']
			print(disease)


get_diseases()
get_symptoms()


