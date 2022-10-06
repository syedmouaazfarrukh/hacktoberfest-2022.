num = input('Enter your number ')
digits_set = []

for digit in num:
    digits_set+=digit

if len(digits_set) % 2 != 0:
    mid_num = digits_set[len(digits_set)//2]
else:
    mid_index_a = len(digits_set)//2
    mid_index_b = mid_index_a - 1  
    mid_num = (int(digits_set[mid_index_a]) + int(digits_set[mid_index_b])) / 2
print(mid_num)