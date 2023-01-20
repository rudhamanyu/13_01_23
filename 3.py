# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc

def get_data(f):
    with open(f, 'r') as d:
        data = d.read()
        return data


def convert(my_str: str):
    num = ''
    res_str = ''
    count = 1
    new_str = '1'
    for i in range(len(my_str)):
        if my_str[0].isdigit():
            if my_str[i].isdigit():
                num += my_str[i]
            else:
                new_str = ''
                for _ in range(int(num)):
                    new_str += my_str[i]
                res_str += new_str
                num = ''
        else:
            if i != len(my_str)-1:
                if my_str[i] == my_str[i+1]:
                    count += 1
                    new_str = str(count)
                else:
                    res_str += new_str + my_str[i]
                    count = 1
                    new_str = '1'
            else:
                res_str += new_str + my_str[i]
    return res_str


def print_res(f):
    s = get_data(f)
    res = convert(s)
    print(res)


print_res('file1.txt')
print_res('file2.txt')
