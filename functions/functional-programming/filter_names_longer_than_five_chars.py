name_list = ['nithin','reddy','kommera', 'shubham','gond']

updated_name_list = list(filter(lambda name:len(name)>=5, name_list))

print(updated_name_list)