#Oski stole your power
def power(x,y):
    result = 1
    for _ in range(y):
        result *= x
    return result

print(power(2,3))



#What to wear?
def temperature(data):
    hottest = max(data)
    coldest = min(data)
    
    answer = (coldest, hottest)
    return answer

readings = [15, 14, 17, 20, 23, 28, 20]
print(temperature(readings))



#Check if its the weekend
def weekend(x):
    x = (x-1)%7
    if x<=4:
        return False
    if x>4:
        return True

print(weekend(7))



#Fuel Efficiency Calculator
def fuel_eff(distance,fuel):
    efficiency = distance/fuel
    return efficiency

travel = 70
fuel_used = 21.5

print(fuel_eff(travel,fuel_used))



#Secret Code
def code(x):
    lg = len(str(x)) - 1
    x = x//10 + (x%10)*(10**lg)
    return x

print(code(12345))



#Min and Max with for loops
def find_max_for(numbers):
    max = numbers[0]
    for n in numbers:
        if n>max:
            max = n

    return max

def find_min_for(numbers):
    min = numbers[0]
    for n in numbers:
        if n<min:
            min = n
    return min

nums = [2024, 98, 131, 2, 3, 72]
print(find_max_for(nums))
print(find_min_for(nums))


#Min and Max with while loops
def find_max_while(numbers):
    max = numbers[0]
    i = 1

    while i < len(numbers):
        n = numbers[i]
        if n > max:
            max = n
        i += 1

    return max
 
 def find_min_while(numbers):
    min = numbers[0]
    i = 1

    while i < len(numbers):
        n = numbers[i]
        if n < min:
            min = n
        i += 1
    return min

print(find_max_while(nums))
print(find_min_while(nums))



#Counting Vowels
def vowels_consonants(text):
    vowels = 0
    consonants = 0
    
    for letter in text:
        valid = letter.isalpha()
        if valid == True:
            if letter in ('a','e','i','o','u','A','E','I','O','U'):
                vowels +=1
            else:
                consonants +=1
    return (vowels, consonants)

text1 = "UC Berkeley, founded in 1868!"
print(vowels_consonants(text1))



#Calculate Digital Robot
def digital_root(input_number):
    result = 0
    number = str(input_number)
    n = len(number)

    for digits in number:
        result += int(digits)


    return result

print(digital_root(142))


