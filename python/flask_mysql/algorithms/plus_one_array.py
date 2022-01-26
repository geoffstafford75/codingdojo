def up_array(arr):
# If any number is more than 1 digit or is negative
    
    if len(arr) == 0:
        return None
    original_num_str = ""
    for x in arr:
        if x < 0 or x >=10:
            print("bad input")
            return None
        else:
            original_num_str +=  str(x)
    
    print(original_num_str)

    new_num_str = str(int(original_num_str) + 1)
    
    new_num_list = []
    for y in new_num_str:
        new_num_list.append(int(y))
    
    print(new_num_list)

up_array([1,2,3])
        