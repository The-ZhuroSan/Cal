import numpy as np

#1. Prime Clusters
def is_Prime(n):
    if n<2:
        return False
    return all (n%i != 0 for i in range(2,int( (n**0.5) + 1)))


def contains_Prime(array):
    filtered_array = [row for row in array if any(is_Prime(x) for x in row)]
    return np.array(filtered_array)

# For example:
matrix = np.array([
    [4, 6, 8, 10],
    [2, 4, 6, 8],
    [9, 15, 21, 27],
    [7, 11, 13, 17]
])

result = contains_Prime(matrix)
print(result)



#2. Checkers
    #2.1
def checkerboard():
    checkboard = np.zeros((8,8), dtype=int)

    #2.2
    for i in range(4):
        for j in range(4):
            checkboard[(2*i),(2*j)] = 1

    #2.3
    for q in range(4):         # I strugled to do the odd rows
        for k in range(4):      #for quite a bit
            checkboard[(2*q)+1, (2*k)+1] = 1
    
    return checkboard

    #2.4

def reverse_checkboard():  
    checkboard = np.ones((8,8), dtype=int)
    for i in range(4):
        for j in range(4):
            checkboard[(2*i),(2*j)] = 0

    for q in range(4):
        for k in range(4):
            checkboard[(2*q)+1, (2*k)+1] = 0
    
    return checkboard

print(checkerboard())
print(reverse_checkboard())



#3. Expanding Universe                     
def expansion(word, x):
    new_word = ''
    for letter in word:
        new_word += letter + x * ' ' 
    return new_word

print(expansion("universe",5))



#4. Second-Dimmest Star
def second_dimmest(matrix):
    sorted_matrix = np.sort(matrix, axis=0)
    second_smallest = sorted_matrix[1]
    return second_smallest

stars = np.random.randint(500, 2000, (5, 5))
print(stars)
print(second_dimmest(stars))