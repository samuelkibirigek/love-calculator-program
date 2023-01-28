
name1 = input("Enter name of first love bird: ")
name2 = input("Enter name of second love bird: ")

true = "true"
love = "love"

true_count = 0
love_count = 0

names = name1 + name2
lover_names = names.lower().strip().replace(" ", "")

for letter in true:
    true_count += lover_names.count(letter)

for letter in love:
    love_count += lover_names.count(letter)

result = str(true_count) + str(love_count)
final = int(result)

if final < 10 or final > 90:
    print(f"Your score is {final}, you go together like coke and mentos.")
elif 40 <= final <= 50:
    print(f"Your score is {final}, you are alright together.")
else:
    print(f"Your score is {final}")


window.mainloop()

