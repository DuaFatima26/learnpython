# FUNCTION
def greet():
    name = input("Enter your name: ")
    print("Salam", name)
greet()                                       

#  list
myList1 = []
myList2 = ["Dua" , "Fatima" , "Jane" , "Sahil" , "Satesh"]
myList3 = [1 , 2 , 3 , 4 , 5 , 6 , 7, 8 , 9 , 10]
mynestedlist = [["Dua" , "Jnae"],["Sahil", "Satesh"],["Atif" , "Shahmeer" , "Shahveer"]]

# Using different function of list

print("Empty list" , myList1)
print("String list" , myList2)
print("Integer List" , myList3)
print("Nested list" , mynestedlist )
print("The value at index 2 in single list is: " , myList2[2])
print("The value in nested list is:" , mynestedlist[2][0])
print("slicing" , myList2[1:4])
print("Negative indexing" , myList2[-3])
print("Print complete list" , myList2[:])
print("Afterward value" , myList3[4:])
 
myintlist01 = [5 , 4 , 3 , 2 ,1]
myintlist02 = [1,2,3,4,5,6,7,8,9,10]

myintlist02[2] = 1
print(myintlist02)
# Append method
myintlist02.append(11)
print(myintlist02)
#Remove Method
myintlist02.remove(4)
print(myintlist02)

# Printing odd numbers in the list
print("Print list backward" , myintlist02[::-1])
for num in myintlist02:
    if num % 2 != 0:
        print("The odd number in list 02 are:" , num)

# Printing backward number using negative index
mynestedlist2 = [["a", "b" , "c"] , ['d' , 'e'] , ['f' ,'g']]        
print("printing value using negative index in nestedlist" , mynestedlist2[-2][-2])

