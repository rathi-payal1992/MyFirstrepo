import sys
environments= sys.argv[1]
list_of_environments=environments.split(",")
for position, name in enumerate(list_of_environments):
    print(f"{name}: {position}")
    match name:
        case S1:
            print('this is S1')
            list_of_environments[position]='S1+whteverstrng'
        case S2:
            print('this is S2')
            list_of_environments[position]='S2+whteverstrng'
 
        # case 418:
            # return "I'm a teapot"

        # If an exact match is not confirmed, this last case will be
        case _:
            print("Wrong env name")
#return list_of_environments