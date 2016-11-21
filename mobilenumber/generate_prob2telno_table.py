f2 = open("cumprob2telno_table.txt", 'w')
#telno.txt has 28717128 lines using wc -l, meaning there are 28717128 telephone numbers.
sum = 28717128
prob = float(1)/sum
with open("telno.txt") as f:
	i = 0;
    	for line in f:
		i = i + 1
		lineinf2 = str(i*prob) + ',' + line.strip() + '\n'
		f2.write(lineinf2)
f2.close()


