primes=[2,3]

def isPrime1(n):
	for i in range(2, int(n**0.5), 2):
		if n%i==0:
			return False
	return True

def isPRime2(n):
	if prime>int(n**0.5):
		return True
	for prime in primes:
		if n%prime==0:
			return False

print(2)
print(3)
for i in range(100):
	x=6*i+1
	y=6*i-1
	if isPrime1(x):
		print(x)
	if isPrime1(y):
		print(y)

for i in range(100,100000000):
	x=6*i+1
	y=6*i-1
	if isPrime2(x):
		print(x)
	if isPrime2(y):
		print(y)
