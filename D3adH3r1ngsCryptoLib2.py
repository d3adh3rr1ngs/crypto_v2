def prepChar(keyChar, msgChar):
	keyCharBits =  f'{ord(keyChar):08b}'
	msgCharBits =  f'{ord(msgChar):08b}'

	retByte = ""

	for i in range(0,8):
		tmpRetBt = ""
		if keyCharBits[i] == msgCharBits[i]:
			tmpRetBt= 0
		else :
			tmpRetBt= 1

		retByte+=str(tmpRetBt)

	return chr(int(retByte, base=2))

def encrypt(key, instr):
	secretText = list()
	
	keyIter = 0
	
	for i in range(0, len(instr)):
		if keyIter == len(key):
			keyIter = 0

		secretText.append(prepChar(key[keyIter], instr[i]))

		keyIter+=1
		
	
	return "".join(secretText)
	
		
		


		
