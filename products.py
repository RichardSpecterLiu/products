products = [] 
while True:
	name = input('products\' names:')
	if name == 'q':
		break
	preis = input('wie kostet das:')
	products.append([name, preis])
print(products)
