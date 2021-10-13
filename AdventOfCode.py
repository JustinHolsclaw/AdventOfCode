def get_one(adapterList):
    total_difference_of1  = 0
    total_difference_of3 = 0
    for adapter in range(len(adapterList)-1):
        if((adapterList[adapter+1]- adapterList[adapter]) == 1):
            total_difference_of1 = total_difference_of1 +1
            print("added one for one")
        elif((adapterList[adapter+1]- adapterList[adapter])== 3):
            total_difference_of3 = total_difference_of3+1
            print("added one for three")
    print(total_difference_of1, total_difference_of3)
    return (total_difference_of3 * total_difference_of1)

inputList = open("Nodes.txt", "r")
array = [0]
for num in inputList.readlines():
    array.append(int(num))
array.sort()
array.append(array[len(array)-1]+3)
#print(array)
#print("The difference multiplied is ", get_one(array))

def get_possible_paths(recurse_array):
    def recurse_dat_bottom(array, stop):
            for item in range(len(array)-1):
                if( array[item] == ):
                    print ("to the end.")
                    return
                else:
                    if((array[item + 1] - array[item]) == 3):
                        recurse_dat_bottom(array[item+1:], stop)
                    else:
                        if(array[item + 2]- array[item] == 3):
                            recurse_dat_bottom(array[item+1:], stop)
                            recurse_dat_bottom(array[item+2:], stop)
                        else:
                            if(array[item + 3]- array[item] ==3):
                                recurse_dat_bottom(array[item+1:], stop)
                                recurse_dat_bottom(array[item+2:], stop)
                                recurse_dat_bottom(array[item+3:], stop)
    
    recurse_stop = len(recurse_array) 
    recurse_dat_bottom(recurse_array, recurse_stop)

print(get_possible_paths(array))