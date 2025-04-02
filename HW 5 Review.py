"""

1. You have been plopped into this directory system. What command will tell you what your working directory is?
Answer: %pwd

2. The command tells you ~/python_decal/judy_decal. What command will list all the files in your current working directory?
Answer: %ls

3. Brianna just sent out an announcement that there was a typo on homework.py.
So you need to pull the updates. What commands will let you move to the correct repository and pull the latest changes?
Answer:
cd ~/python_decal/brianna_repo
git pull

4. How would you move this new homework.py to your personal repository homework directory?
Answer:
mv ~/python_decal/brianna_repo/homework.py ~/python_decal/judy_decal/homework/

5. You want to see the contents of the homework.py in your terminal from your personal repository. 
What command(s) will let you do this?
Answer:
cat ~/python_decal/judy_decal/homework/homework.py

6. You want to edit the contents of the homework.py in your terminal from your personal repository.
What command will let you do this?
Answer:
nano ~/python_decal/judy_decal/homework/homework.py


7. You have finished the homework. What commands will allow you to save
the changes and push from your local repository to your remote repository?
Answer:
git add .
git commit -m "Finished homework"
git push

8. Oh no! Git gave you the following error. What commands should you call to resolve this errorand push your homework properly? What does the error mean?
Answer:
The error means that there are updates on the remote repo that you don't have locally.
To fix it:
git pull --rebase
(Then solve any merge conflicts)
git push

Judy’s mistake was trying to push without first pulling remote changes.

9. What absolute path will allow you to move to Recents/?
Answer:
cd ~/Recents/

"""
import numpy as np

#2.1 Data Types
def data_type(element):
    return type(element)
print(data_type(45))


#2.2 Conditionals
def even_or_odd(number):
    result = ''
    if number % 2 == 0:
        result = 'even'
    else:
        result = 'odd'
    return result

print(even_or_odd(11))


#3 Loops
def sum_with_loops(matrix):
    count = 0
    for element in matrix:
        count += element 
    return count 

numbers = [1,2,3,4,5]
print(sum_with_loops(numbers))


#4.1 Lists
def duplicateList(matrix):
    new_list = []
    for element in matrix:
        new_list += 2*element
    return new_list

a = ['a','b','c']

print(duplicateList(a))



#4.2 Debugging

def square(num):                  #missing : after function in defined
    return num * num



