data = {'name' : "ineuron",
"course": ['data science', 'blockchain', 'drone' , 'robotics' , 'cloud' ],
'greeting': 'greeting from ineuron' }

def get_course():
	return data['course']

def greetings():
	return data['greeting']

def key_find():
	return data.keys()

def value_find():
	return data.values()


def Item_find():
	return data.items()