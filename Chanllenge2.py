data = ["K", "M", "O", "Q", "E", "G"]
expect_string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
simple_string = "g fmnc wms bgblr"

def getOffset(firstString, secondString):
	offset = getNumber(firstString) - getNumber(secondString)
	return offset

def isLetter(string):
	return (getNumber(string) > 65)

def getNumber(string):
	return ord(string)

def getString(number):
	return chr(number)

def turnString(number):
	if(number > 122):
		set = number - 122
		return chr(96+set)
	return chr(number)

def getResult(string, offset):
	result = ""
	for s in string:
		if(isLetter(s)):
			result += turnString(ord(s) + offset)
		else:
			result += s
	return result

offset = (getOffset(data[1],data[0]))
result = getResult("map", offset)
print(result)