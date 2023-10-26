#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    lis = []
    for i in range(list_length):
        try:
            c = my_list_1[i] / my_list_2[i]
        except Exception:
            if my_list_2[i] == 0:
                c = 0
                print("division by 0")
            elif type(my_list_1[i]) is not int or type(my_list_2[i]) is not int:
                c = 0
                print("wrong type")
            elif len(my_list_1) != len(my_list_2):
                print("out of range")
                c = 0
        finally:
            lis.append(c)
    return (lis)
