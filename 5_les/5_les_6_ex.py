with open('ex_6.txt', 'r', encoding='utf-8') as f_6:
    my_dict = dict()
    for line in f_6:
        lesson, res = line.split(':')
        res = res.split()
        number = 0
        for part in res:
            if '-' in part:
                continue
            nums, type = part.split('(')
            number += int(nums)
        my_dict[lesson] = number
print(my_dict)
