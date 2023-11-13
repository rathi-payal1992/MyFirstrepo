import sys
environments= sys.argv[1]
list_of_environments=environments.split(",")
def modify_array():
   for position, name in enumerate(list_of_environments):
       print(f"{name}: {position}")
       match name:
         case 'S1':
            print('this is S1')
            list_of_environments[position]='S1+whteverstrng'
         case 'S2':
            print('this is S2')
            list_of_environments[position]='S2+whteverstrng'
 
        # case 418:
            # return "I'm a teapot"

        # If an exact match is not confirmed, this last case will be used if provided
         case _:
            print("Wrong env name")
   print(list_of_environments)
   return list_of_environments

# def main():
#    modify_array()
# 
# if __name__ == "__main__":
    # main()
modify_array()
