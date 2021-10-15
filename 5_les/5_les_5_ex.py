with open('ex_5.txt', 'w', encoding='utf-8') as f_5:
    my_numbers = [11, 32, 12, 43, 65, 23, 66]
    f_5.write(" ".join(map(str, my_numbers)))
with open('ex_5.txt', 'r', encoding='utf-8') as f_5:
    numbers = [int(i) for i in f_5.read().split()]
    print(f"The sum of the numbers in the file f_5.txt = {sum(numbers)}")