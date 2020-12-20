import random

context = 10

def generateChainDict(l):
	out = {}
	for message in l:
		for i,char in enumerate(message):
			if i < context:
				if not message[0:i + 1] in out:
					out[message[0:i + 1]] = {}
				if char == ",":
					pass
				else:
					try:
						out[message[0:i + 1]][message[i+1]] += 1
					except:
						out[message[0:i + 1]][message[i+1]] = 1
			else:
				if not message[i-(context - 1):i + 1] in out:
					out[message[i-(context - 1):i + 1]] = {}
				if char == ",":
					pass
				else:
					try:
						out[message[i-(context - 1):i + 1]][message[i+1]] += 1
					except:
						out[message[i-(context - 1):i + 1]][message[i+1]] = 1


	return out

def createMessage():
	messages = []
	with open("messages.txt", "r", encoding="utf-8") as f:
		messages = f.readlines()

	messages = list(set(messages))

	with open("messages.txt", "w", encoding="utf-8") as f:
		for line in messages:
			f.write(line)

	clean = []
	for i in messages:
		if i != "":
			clean.append(i.strip())

	messages = clean[:]

	message_data = generateChainDict(messages)

	cont = True

	out = ":"

	while cont:
		if len(out) < context:
			s = 0
			for i in message_data[out[0:len(out)]].keys():
				s += message_data[out[0:len(out)]][i]

			rand = random.randint(0, s)

			for i in message_data[out[0:len(out)]].keys():
				rand -= message_data[out[0:len(out)]][i]
				if rand <= 0:
					out += i
					if i == ",":
						cont = False
					break
		else:
			s = 0
			for i in message_data[out[len(out)-context:len(out)]].keys():
				s += message_data[out[len(out)-context:len(out)]][i]

			rand = random.randint(0, s)

			for i in message_data[out[len(out)-context:len(out)]].keys():
				rand -= message_data[out[len(out)-context:len(out)]][i]
				if rand <= 0:
					out += i
					if i == ",":
						cont = False
					break



	return decode(out)




def decode(s):
	return s.replace(u"\ufffc", "\n")
