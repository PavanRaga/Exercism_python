from math import sqrt

def prime(number):
    if number <= 0:
        raise ValueError("error")
    prime_list = [2]
    num = 3
    while len(prime_list) < number:
        if is_prime(num):
            prime_list.append(num)
        else:
            pass
        num += 2
    return prime_list[-1]

def is_prime(num):
    factor = 2
    while factor <= sqrt(num):
        if num%factor == 0:
            return False
        factor += 1
    else:
        return True

if __name__ == "__main__":
    print(prime(500000))