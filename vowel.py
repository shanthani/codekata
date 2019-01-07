n=input("")
if n.isalpha():
	s=['a','e','i','o','u','A','E','I','O','U']
	if n in s:
		print("Vowel")
	else:
		print("Consonant")
else:
	print("invalid")
