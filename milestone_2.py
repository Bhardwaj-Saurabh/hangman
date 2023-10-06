
# import libraries
import random

# create a list of five fav fruits
word_lis = ['apple', 'orange', 'mango', 'banana', 'kiwi']
 
 # output the world list
print(word_lis)

# select a random fruit from word_lis
word = random.choice(word_lis)
print(word)

# ask for a single letter from user
guess = input('Enter a single letter: ')

if len(guess) == 1 and guess.isalpha():
    print('Good guess!')
else:
    print('Oops! That is not a valid input.')
