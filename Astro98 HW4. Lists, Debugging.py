#Making a list variable
size = 21                #size = int(input("Enter an integer:"))      to generalize for any size
zero_to_twenty = []

for i in range(size):            
    zero_to_twenty.append(i)

print(zero_to_twenty)
    

#Working with list elements
def square_numbers_in_a_list(numbers_in_a_list):
    squared_numbers_list = []
    for i in numbers_in_a_list:                      #Debugging: At first I was unsure on how to get a list  
        i = i**2                                          #to then append elements to it, then I reviewed my notes and
        squared_numbers_list.append(i)                    #realized i can just do: list = []
    return squared_numbers_list                            #Also forgot to return the list at the end and was getting nothing back
square_numbers_list = square_numbers_in_a_list(zero_to_twenty)

print(square_numbers_list)


#Slicing
def first_fifteen(numbers_in_a_list):
    numbers_in_a_list = numbers_in_a_list[0:15]         
    return numbers_in_a_list
first_fifteen_list = first_fifteen(square_numbers_list)

print(first_fifteen_list)


#Striding
def every_fifth(numbers_in_a_list):                
    numbers_in_a_list = numbers_in_a_list[4::5]    #Debugging: I was unsure whether to include zero or not
    return numbers_in_a_list                       #as it was messing up the calculations, for example the indices [4::5]
every_fifth_list = every_fifth(square_numbers_list)   #so I tried multiples ways to achieve the same results as in the ws

print(every_fifth_list)


#Slicing and striding
def fancy_function(numbers_in_a_list):                #debugging
    every_third = numbers_in_a_list[2::3]            #I couldn't get a new list with the elements in reverse,
    fancy_list = every_third[::-1]                   #I kept trying different ways and then just decided to 
    return fancy_list                                #google it and found out i can use [::-1]
fancy_list = fancy_function(square_numbers_list)

print(fancy_list)


#Creating a 5x5 2D list
def nested_five():
    nested_five = [[],[],[],[],[]]                   
    for i in range(5):                               
        for j in range(5):                           
            nested_five[i].append(j+1+i*5)           
    return nested_five

nested_five_list = nested_five()
print(nested_five_list)


#Replacing 2D list with multiples of 3
def replace_every_third(nested_list):                 #debugging: the [i][j] indices was kind of confusing,
    for i in range(len(nested_list)):                 #I kept getting only the first sublist to have numbers
        for j in range(len(nested_list)):             #or the program would just tell me the list I was trying to access
            if nested_list[i][j] % 3 == 0:            #didnt exist
                nested_list[i][j] = "?"
    return nested_list


every_third_list = replace_every_third(nested_five_list)

print(every_third_list)


def sum(question):
    count = 0
    for i in range(len(question)):
        for j in range (len(question)):
            if question[i][j] != "?":
                count = count + int(question[i][j])
    return count

print(sum(every_third_list))