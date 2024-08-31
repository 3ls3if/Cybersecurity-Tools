alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

str_in = input("Enter message: ")
shift = int(input("Enter shift value: "))

n = len(str_in)
str_out = ""

for i in range(n):
	c = str_in[i].upper()
	loc = alpha.find(c)
	newloc = (loc+shift)%26
	
	#if newloc >= 26:
		#newloc -= 26

	str_out += alpha[newloc]
	#print(newloc, str_out)

print(f"Obfuscated Version: {str_out}")
