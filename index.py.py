#Creating a list 
print("list")
my_list=["monisha", "teju","vishnu"]
print(my_list)
#Accessing elements in the list by index
print(my_list[1])
#Append  an element at the end of the list
my_list.append("keerthi")
print(my_list)
#Insert an element at any given position in the list
my_list.insert(0,"srayashya")
print(my_list)
#Remove an element from the list using its index
del my_list[1]
print(my_list)
print("set")
my_set={"monisha", "teju","vishnu","keerthi"}
print(my_set)
#Appending  an element to the set
my_set.add("srayashya")
print(my_set)
#Removing  an element from the set
my_set.remove("monisha")
print(my_set)
#To find the length of the set
print(len(my_set))
print("Dictionaries")
my_dict = {"1": "teju", "2":"vishnu"}
print(my_dict)
#Adding a key-value pair to the dictionary
my_dict[3]="monisha"
print(my_dict)
#Removing  a value with its corresponding key from the dictionary
my_dict.pop("1")
print(my_dict)
#To know the length of the dictionary
print(len(my_dict))
