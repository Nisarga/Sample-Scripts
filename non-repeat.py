import os
strx = raw_input("Please enter the string")
print "\n" +strx
lenStr=len(strx)
dict_words = dict()
i=0
while i<lenStr:
	ch = strx[i]
	if ch not in dict_words.keys():
		dict_words[ch]=1
	else:
		dict_words[ch]=dict_words[ch]+1
	i = i + 1

print dict_words

minIndex=1000000
for key in dict_words:
	if (dict_words[key]==1):
		if strx.index(key)<minIndex:
			minIndex = strx.index(key)
			char = key

print char
