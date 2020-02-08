def f (n):
	if n < 2 :
		return (n)
	return f(n-1) + f(n-2)
x = int(input('ingrse un numero'))
for i in range(x):
	print(f(i))
