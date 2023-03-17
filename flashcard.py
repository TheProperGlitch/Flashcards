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
  ["What was the first ever video game called? \n(1: Pong, 2: Space Invaders, 3: BitCrunch, 4: Tennis for Two)", 4],
  ["The number one most sold game is Minecraft. What is number 2? \n(1: Tetris, 2:GTA5, 3:Red Dead Redemption 4:Legend of Zelda; Breath of the Wild)", 2],
  ["Which of the following is the highest grossing game of all time? \n(1: Pac-Man, 2: League of Legends, 3: Dungeon Fighter Online, 4: Minecraft)", 3],
  ["What was the first video game console played in space? \n(1:Nentendo Gameboy, 2: Sega Saturn, 3: Sony PlayStation, 4: Atari 2600)", 1]
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
