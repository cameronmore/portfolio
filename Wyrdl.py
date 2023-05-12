#Code.py
username=input('What is your name? ' )
print(f"Hello, {username}, time for some Wrdyl!")
secret_word = ['r', 'e', 'n', 't', 's']
Guess_1=list(input('What is your first guess? '))
for i in Guess_1:
    if i in secret_word:
        print(i)

if Guess_1 == secret_word:
    print('Congrats! The word is \'rents\'!')

Guess_2=list(input('What is your second guess? '))
for e in Guess_2:
    if e in secret_word:
        print(e)

if Guess_2 == secret_word:
    print('Congrats! The word is \'rents\'!')

Guess_3=list(input('What is your third guess? '))
for e in Guess_3:
    if e in secret_word:
        print(e)

if Guess_3 == secret_word:
    print('Congrats! The word is \'rents\'!')

Guess_4=list(input('What is your fourth guess? '))
for e in Guess_4:
    if e in secret_word:
        print(e)

if Guess_4 == secret_word:
    print('Congrats! The word is \'rents\'!')

print('WARNING: you have guess remaining!')

Guess_5=list(input('What is your fifth guess? '))
for e in Guess_5:
    if e in secret_word:
        print(e)

if Guess_5 == secret_word:
    print('Congrats! The word is \'rents\'!')
else:
    print('You have lost! try again another time!!')

