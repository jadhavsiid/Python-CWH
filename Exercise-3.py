"""Exercise-3: Guess the number"""
""" Consider a number n=18 and give option for user to guess. Now take input from a user and keep helping
him to guess that number by telling whether the number a small or large than the already considerd number.
Keep Number of guesses =10
Also print no.of guesses left:
if guesses are over write 'Game Over !
if the user win print 'Congrats! you won with the number of guesses he left.'"""

print("WELCOME TO THE GUESSING GAME !!")
n = 18
number_of_guesses= 1
print("Can you guess a hidden number by us in 10 Guesses ?? ")
while(number_of_guesses<=10):
    inp=int(input("Guess the number: "))
    if inp<18:
        print("You Entered a smaller number than our hidden number !"
              "Guess Agaian !!")
    elif inp>18:
        print("You Entered a larger number than our hidden number !"
              "Guess Again !!")
    else:
        print("YOU WON!!!"
              "You Predicted number in",number_of_guesses,"Guesses.*")
        break
    print("no of guesses left:",10-number_of_guesses)
    number_of_guesses = number_of_guesses + 1
    if (number_of_guesses >10):
        print("Sorry, You Lost !!!")

