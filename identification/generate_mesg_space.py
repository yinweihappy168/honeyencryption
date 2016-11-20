#with open('locationfield2.txt','r') as bin:
#    prefixes = bin.read()

# locationfield2.txt has 3519 lines. so idsorted has 3519*365 * 49 =314686575 ids
f = open("locationfield2.txt", 'r')
prefixes = f.readlines()

f2 = open("idsorted.txt", 'w')

for prefix in prefixes:
	for year in range(2012,2017):
		for month in range(1, 13):
			if month in (1,3,5,7,8,10,12):
				for day in range(1, 32):
					for num in range(1,50):
						id = prefix.strip() + str(year) + str(month).zfill(2) + str(day).zfill(2) + str(num).zfill(3);
						f2.write(id+"\n")
				f2.flush()
			elif month==2:
				for day in range(1, 29):
					for num in range(1,50):
						id = prefix.strip() + str(year) + str(month).zfill(2) + str(day).zfill(2) + str(num).zfill(3);
						f2.write(id+"\n")
				f2.flush()
			elif month in (4,6,9,11):
				for day in range(1, 31):
					for num in range(1,50):
						id = prefix.strip() + str(year) + str(month).zfill(2) + str(day).zfill(2) + str(num).zfill(3);
						f2.write(id+"\n")
				f2.flush()
f.close()
f2.close()
