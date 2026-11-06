import pandas as pd

num = [1, 2, 3, 4]

# Cách 1
squared_nums = []
for i in num:
    squared_nums.append(i**2)
print("Cách 1:", squared_nums)

# Cách 2
squared_nums_2 = [i**2 for i in num]
print("Cách 2:", squared_nums_2)

# Cách 3
squared_nums_3 = list(map(lambda x: x**2, num))
print("Cách 3:", squared_nums_3)

# Hàm filter: Tạo danh sách các số nguyên tố < 100
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = 100
prime_nums = list(filter(is_prime, range(2, n)))

print("\nCác số nguyên tố < 100:")
for p in prime_nums:
    print(p, end=" ")

#Read health dataset
health_df = pd.read_excel("")

health_df

def ghi_chu(r):
    if r['BMI']<18:
        