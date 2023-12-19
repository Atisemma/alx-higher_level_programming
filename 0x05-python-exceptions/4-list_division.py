#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            elem_1 = my_list_1[i]
            elem_2 = my_list_2[i]

            if not isinstance(elem_1, (int, float)) or \
               not isinstance(elem_2, (int, float)):
                raise TypeError("wrong type")

            if elem_2 == 0:
                raise ZeroDivisionError("division by 0")

            division_result = elem_1 / elem_2

        except IndexError:
            print("out of range")
            division_result = 0

        except TypeError:
            print("wrong type")
            division_result = 0

        except ZeroDivisionError:
            print("division by 0")
            division_result = 0

        finally:
            result.append(division_result)

    return result
