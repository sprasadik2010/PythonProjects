test_list = [
    ("Gayathri",12,"7A"),
    ("Srikeshav",14,"7A"),
    ("Shyam",10,"6A"),
    ("Uchith",8,"3A"),
    ("Udhav",6,"17A")
    ]
# initializing list of tuples
#test_list = [(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]
 
# printing original list
print ("The original list is : " + str(test_list))
 
# using list comprehension to get names
res = [lis[0] for lis in test_list]
     
# printing result
print ("List with only nth tuple element (i.e names) : " + str(res))