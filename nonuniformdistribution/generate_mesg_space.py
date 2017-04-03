#totally 1000000 password

f2 = open("password.txt", 'w')

for num in range(0,1000000):
	pwd = str(num).zfill(6)
	f2.write(pwd + "\n")
			
f2.close()
