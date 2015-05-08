#!/usr/bin/env python
# -*- coding: utf-8 -*-
def checkio(data):
	coun_A=0; coun_a=0; coun_d=0
	for i in data:
		if i.isupper():
			coun_A+=1
		elif i.islower():
			coun_a+=1
		elif i.isdigit():
			coun_d+=1
	if (len(data)> 9) and (coun_a > 1) and (coun_A > 1) and ((coun_d < len(data)) and (coun_d > 0)):
		return True
	else: return False

	#replace this for solution
	

#Some hints
#Just check all conditions

#~ 
if __name__ == '__main__':
	#~ #These "asserts" using only for self-checking and not necessary for auto-testing
	assert checkio(u'A1213pokl') == False, "1st example"
	assert checkio(u'bAse730onE4') == True, "2nd example"
	assert checkio(u'asasasasasasasaas') == False, "3rd example"
	assert checkio(u'QWERTYqwerty') == False, "4th example"
	assert checkio(u'123456123456') == False, "5th example"
	assert checkio(u'QwErTy911poqqqq') == True, "6th example"
	assert checkio(u"Pv4HdnUNb") == False
	assert checkio("Fa11con777") == True
