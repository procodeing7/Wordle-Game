import random,os
guess = ""
feedback = ""
guess_list = []
try:
    with open('wordlist.txt') as f:
        for line in f:
            guess_list.append(line.strip())
except FileNotFoundError:
    print("file not found")
showall = input("Show All Remaining Words? y/n")
if showall.lower() not in ['y','n']:
  showall = "n"
os.system("clear")
for guesses in range(6):
    if showall=="n":
      os.system('clear')
    if guesses == 0:
      print("Good starter words are: slice, tried, crane")
    double = []
    print("You could try",random.choice(guess_list))
    guess = input("\n Enter The Word >>> ").lower()
    print("g - green, y - yellow, w - wrong / grey")
    feedback = input("Enter Feedback >>> ").lower()
    if feedback == "ggggg":
        print("Well Done! Guess",guesses+1)
        break
            
    temp_tuple = tuple(guess_list)
    for word in temp_tuple: # You can't iterate over a list you want to change, so using a tuple.
        for i in range(5):
            if feedback[i] == "w" and guess[i] in word:
              									
                  guess_list.remove(word)
                  break
            elif feedback[i] == "g" and guess[i] != word[i]:
              									
                  guess_list.remove(word)
                  break
            elif feedback[i] == "y" and guess[i] not in word:
                  guess_list.remove(word)
                  break
            elif feedback[i] == "y" and guess[i] == word[i]:
                  guess_list.remove(word)
                  break
    counter = 0
    print("Pick A Word: ")
    for word in guess_list:
        print(word,end=", ")
        counter+=1
        if counter == 8:
            print("")
            counter = 0
