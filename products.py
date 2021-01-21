products = [] 
while True:
	name = input('products\' names:')
	if name == 'q':
		break
	preis = input('wie kostet das:')
	products.append([name, preis])
print(products)

for p in products:
	print('Products:', p[0], 'Preis:', p[1])
