# name_f_2 = str(input('Enter the name of your file'))
with open('ex_2.txt', 'r', encoding='utf-8') as f_2:
    line_f_2 = f_2.readlines()
    for i, count in enumerate(line_f_2, 1):
        number_words = len(count.split())
        print(f"String {i} contains {number_words} words")
