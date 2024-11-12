def is_power_of_two(n):
    if n == 1:
        return True
    if n <1 or n %2 != 0:
        return False
    return is_power_of_two(n //2)

print(is_power_of_two(16))
# print(is_power_of_two(18))