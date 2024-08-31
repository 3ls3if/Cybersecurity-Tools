text = input("Enter text: ")
key = input("Enter key: ")

n = len(text)

cipher = ""

for i in range(n):
	t = text[i]
	k = key[i%len(key)]
	x = ord(k) ^ ord(t)
	cipher += chr(x)

print(text, key, cipher.encode().hex()) 
