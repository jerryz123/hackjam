fullmessages = open('messages.htm', 'r').read()
#finds indices of where people begin
start = fullmessages.find('<div class="thread">')
listthreads = []
while start != -1:
	listthreads.append(start)
	start = fullmessages.find('<div class="thread">', start+1)
listthreads.append(len(fullmessages))
print(len(listthreads))
#group people into list
people = []
for i in range(len(listthreads) - 1):
	people.append(fullmessages[listthreads[i]:listthreads[i+1]])
print(len(people))
actualpeople = [[] for i in people]
class message:
	def __init__(self, s, d, t):
		self.sender = s
		self.date = d
		self.text = t
for i in range(len(actualpeople)):
	actualpeople[i].append(people[i][20:people[i].find('<div class="message">')])
	people[i] = people[i][people[i].find('<div class="message">'):]
	'''actualpeople[i].append([])
	while people[i].find('<div class="message"><div class="message_header"><span class="user">')!= -1:
		s = people[i][68:people[i].find('</span>')]
		people[i] = people[i][people[i].find('meta">') + 6:]
		d = people[i][:people[i].find('</span>')]
		people[i] = people[i][people[i].find('<p') + 3:]
		t = people[i][:people[i].find('</p')]
		actualpeople[i][1].append(message(s,d,t))
		people[i] = people[i][people[i].find('</p>') + 4:]'''
def indexperson(name):
	for x in range(len(actualpeople)):
		if name in actualpeople[x][0]:
			return x

def listperson(name):
	i = indexperson(name)
	sigh = []
	thing = people[i]
	while thing.find('<div class="message"><div class="message_header"><span class="user">')!= -1:
		s = thing[68:thing.find('</span>')]
		thing = thing[thing.find('meta">') + 6:]
		d = thing[:thing.find('</span>')]
		thing = thing[thing.find('<p') + 3:]
		t = thing[:thing.find('</p')]
		sigh.append(message(s,d,t))
		thing = thing[thing.find('</p>') + 4:]
	return sigh

def howmuchdotheylikeme(name):
	messages = listperson(name)
	liking = 0
	for message in messages:
		if message.sender == name:
			liking += 1
	return liking / len(messages)


