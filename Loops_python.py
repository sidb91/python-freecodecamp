#Loops
"""i = 1
while i<=10:
    print(i)
    i+=1"""
#while loop guessing game
"""secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("out of guesses, you lose")
else:
    print("you win!")"""

#for loop
"""for letter in "Giraffe":
    print(letter)"""

"""friends = ["Jim","Karen","Kevin","Tim"]
for name in friends:
    print(name)
    print(len(friends))"""

"""for i in range(3,10):
    print(i)"""

friends = ["Jim","Karen","Kevin","Tim"]
for index in range(len(friends)):
    print(friends[index])

 
