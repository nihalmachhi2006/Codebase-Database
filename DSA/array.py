# Given a number check whether the number is Prime or not


def Cheack_Prime(n):
    is_prime = True
    if n > 1:
        for i in range(2,n):
            if(n%2) == 0:
                is_prime = False
                break
    return is_prime


print(Cheack_Prime(40))