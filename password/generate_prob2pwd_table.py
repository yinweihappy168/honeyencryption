f2 = open("cumprob2pwd_table.txt", 'w')
#password.txt has 1000000 lines using wc -l, meaning there are 1000000 telephone numbers.
sum = 1000000
prob = float(1)/sum
with open("password.txt") as f:
	i = 0;
    	for line in f:
		i = i + 1
		lineinf2 = str(i*prob) + ',' + line.strip() + '\n'
		f2.write(lineinf2)
f2.close()


