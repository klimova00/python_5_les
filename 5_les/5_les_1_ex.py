print('Enter your text. Enter an empty line to end. ')
with open("ex_1.txt", 'w', encoding='utf-8') as f_1:
    while (my_str := input('Enter your string: ')) != '':
        f_1.write(f'{my_str}\n')
