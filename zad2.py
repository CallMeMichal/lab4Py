# Napisz funkcję sprawdzającą czy podane liczby są liczbami pierwszymi w szybszy sposób niż w przykładzie.
# Do funkcji można przekazać dowolną liczbę argumentów (liczby). Liczby 0 i 1 nie są liczbami pierwszymi. (10%)

def prime(*numbers):
    for numb in numbers:
        is_prime = True
        for i in range(2, numb):
            if numb % i == 0:
                is_prime = False
            break
        if is_prime:
            print(f"{numb} is prime")
        else:
            print(f"{numb} is not prime")


prime(1, 2, 3, 4, 5, 6, 11)
