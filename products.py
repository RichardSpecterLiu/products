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

with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('product, price\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')

with open('products.txt', 'w') as f:
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')