import os, random
files = os.listdir('.')
files.remove("flashcard.py")
files.remove(".git")
files.remove("README.md")
print(f"Hello, and welcome to AV flashcards! Current players are {files}")
name = input("What is your chosen name/username: ")
if not name in files:
     with open(name+".py","w") as file:
        file.write("points = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10] \ntotal = 200")
     with open(name+".py","r") as file:
         old_score = file.read()
else:
    with open(name+".py","r") as file:
         old_score = file.read()
flashcards = [
  ["What is the starting area called in Hollow Knight? \n(1: King's Pass, 2: Dirtmouth, 3: Forgotten Crossroads, 4: Kingdom's Edge)", 1],
  ["Which of the three dreamers does Quirrel work for? \n(1: Monomon the Teacher 2: Lurien the Watcher, 3: Herrah the Beast 4: Dreaming Jerry)", 1],
  ["Which of the following is not a boss found in the forgotten crossroads? \n(1: Vengefly King, 2: Brooding Mawlek, 3: False Knight, 4: Gruz Mother)", 1],
  ["How much geo drops from the False Knight chest? \n(1: 200, 2: 300, 3: 150, 4: 250)", 1],
  ["What song plays when sitting on the Pale King's throne? \n(1: Hollow Knight Theme, 2: Pale King's Theme, 3: Flight of the Bumblebee, 4: White Palace Theme)", 1],
  ["What was the Mothwing Cloak's original name? \n(1: Dashmaster's Cloak, 2: Mothdust Cloak, 3: Stinging Cloak, 4: Mothfloat Cloak)", 2],
  ["What is the correct name of this item in Hollow Knight? \n(1: Super Dash, 2: Crystal Heart, 3: Crystal Dash, 4: Super Heart)", 2],
  ["What is the main character's offical name? \n(1: The Hollow Knight, 2: No cannon name, 3: The Knight, 4: The Wanderer)", 2],
  ["Is this a placeholder? \n(1: No, 2: Yes, 3: Why no good sir, 4: 14)", 2],
  ["Is this a placeholder? \n(1: No, 2: Yes, 3: Why no good sir, 4: 14)", 2],
  ["Why are there so many flashcards? \n(1: I don't know, 2: Torture, 3: So we have to automate it, 4: Just cuz)", 3],
  ["Why are there so many flashcards? \n(1: I don't know, 2: Torture, 3: So we have to automate it, 4: Just cuz)", 3],
  ["Why are there so many flashcards? \n(1: I don't know, 2: Torture, 3: So we have to automate it, 4: Just cuz)", 3],
  ["Why are there so many flashcards? \n(1: I don't know, 2: Torture, 3: So we have to automate it, 4: Just cuz)", 3],
  ["Why are there so many flashcards? \n(1: I don't know, 2: Torture, 3: So we have to automate it, 4: Just cuz)", 3],
  ["How much sleep did I get before this? \n(1: A good amount, 2: Meh 50/50, 3: So much sleep, 4: An \"I don't get paid enough\" amount)", 4],
  ["How much sleep did I get before this? \n(1: A good amount, 2: Meh 50/50, 3: So much sleep, 4: An \"I don't get paid enough\" amount)", 4],
  ["How much sleep did I get before this? \n(1: A good amount, 2: Meh 50/50, 3: So much sleep, 4: An \"I don't get paid enough\" amount)", 4],
  ["How much sleep did I get before this? \n(1: A good amount, 2: Meh 50/50, 3: So much sleep, 4: An \"I don't get paid enough\" amount)", 4],
  ["How much sleep did I get before this? \n(1: A good amount, 2: Meh 50/50, 3: So much sleep, 4: An \"I don't get paid enough\" amount)", 4]
]
question_numbers = [
0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19
]
playing = True
while playing:
    exec(old_score)
    if total == 0:
        playing = False
        print("You win! You have learned the necessary material.")
    else:
      question_num = random.choices(question_numbers, weights = points, k = 1)[0]
      print(question_num)
      print(flashcards[question_num][0])
      question = flashcards[question_num][0]
      correct_answer = flashcards[question_num][1]
      answer = int(input(""))
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
