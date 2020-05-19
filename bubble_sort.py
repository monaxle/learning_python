my_list = [566554,866554,1332,333,23]
still_swapping = True
while still_swapping:
    still_swapping = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i+1]:
            my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
            still_swapping = True
print(my_list)