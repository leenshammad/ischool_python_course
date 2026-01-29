# task:  out of the word
# inputs: n/a
# outputs: count number

def count_vowles (string):
    vowles=['a','e','i', 'o','u']
    count=0

    lower_string=string.lower()
    for vowle in vowles:
        count+=lower_string.count(vowle)

    return(count)
    
excampel ='hi leen'



print(count_vowles(excampel))



