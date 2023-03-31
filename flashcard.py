import os, random
files = os.listdir('.')
files.remove("flashcard.py")
files.remove(".git")
files.remove("README.md")
print(f"Hello, and welcome to AV flashcards! Current players are {files}")
name = input("What is your chosen name/username: ")
if not name in files:
     with open(name+".py","w") as file:
        file.write("points = [10,10,10,10] \ntotal = 40")
     with open(name+".py","r") as file:
         old_score = file.read()
else:
    with open(name+".py","r") as file:
         old_score = file.read()
flashcards = [
  ["What is the starting are called in Hollow Knight? \n(1: King's Pass, 2: Dirtmouth, 3: Forgotten Crossroads, 4: Kingdom's Edge)", 1],
  ["Which of the three dreamers does Quirrel work for? \n(1: Monomon the Teacher 2: Lurien the Watcher, 3: Herrah the Beast 4: Dreaming Jerry)", 1],
  ["Which of the following is not a boss found in the forgotten crossroads? \n(1: Vengefly King, 2: Brooding Mawlek, 3: False Knight, 4: Gruz Mother)", 1],
  ["How much geo drops from the False Knight chest? \n(1: 200, 2: 300, 3: 150, 4: 250)", 1],
  [""]
]
question_numbers = [
0,
1,
2,
3
]
playing = True
while playing:
    exec(old_score)
    if total == 0:
        playing = False
        print("You win! You have learned the necessary material.")
    else:
      question_num = random.choices(question_numbers, weights = points, k = 1)[0]
      print(flashcards[question_num][0])
      question = flashcards[question_num][0]
      correct_answer = flashcards[question_num][1]
      answer = int(input(" "))
      if answer == correct_answer:
        print("Correct!")
        points[question_num] = points[question_num]-1
        total -= 1
        with open(name+".py","w") as file:
            file.write(f"points = {points} \ntotal = {total}")
        with open(name+".py","r") as file:
            old_score = file.read()
      else:
          print(f"Ha! You actually thought that! The correct answer is obviously number {correct_answer}.")
          points[question_num] = points[question_num]+1
          total += 1
          with open(name+".py","w") as file:
            file.write(f"points = {points} \ntotal = {total}")
          with open(name+".py","r") as file:
            old_score = file.read()
