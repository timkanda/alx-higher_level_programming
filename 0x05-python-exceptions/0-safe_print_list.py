def safe_print_list(my_list=[], x=0):
    try:
        for i in (x):
            print(my_list[i])
    except Exception as e:
        print("Error occure", e)
