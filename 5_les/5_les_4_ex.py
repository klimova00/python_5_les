my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('result_ex_4.txt', 'w', encoding='utf-8') as res_f_4:
    with open('ex_4.txt', 'r', encoding='utf-8') as f_4:
        for string in f_4:
            engl, *num = string.split()
            rus=my_dict[engl]
            res_f_4.write(' '.join([rus]+num) + "\n")
