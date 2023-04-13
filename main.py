import textwrap, characters
from os import system, name
from time import sleep
from playsound import playsound


def openingText():
  clear()
  print('HELP THY NEIGHBORS')
  sleep(1)
  clear()
  #sleep(0.2)
  print('HELP YOUR NEIGHBORS')
  sleep(1)
  clear()
  #sleep(0.3)
  print('HELP OUR NEIGHBORS')
  sleep(1)
  print('\nMade for the Millburn 2023 STEAMfest \nby alex delorenzo, dialogue trees by ayati jend\n\n\n')


def prompt(question_list):
  try:
    for i, question in enumerate(question_list):
      print('{}) {}'.format(i + 1, question))
    answer = input('\n>>> ')
    for i, question in enumerate(question_list):
      if answer.lower() == question.lower() or answer == str(i + 1):
        return (i + 1)
  except:
    print('please enter a number or string\n')
    prompt(question_list)


def introduction():
  print(textwrap.fill('Welcome to the town of Millburn, New Jersey. The grass is green and the roads are paved with gold. If you work hard, you can help our neighbors — these poor, misguided capitalists — to realize the error of their ways and you can turn this poor town into a prosperous communist dictatorship.\n', 80))
  print('\nStart?')
  if prompt(['Yes', 'No']) == 2:
    print('okay?')
  else:
    clear()
    print(
      textwrap.fill('"It is high time that Communists should openly, in the face of the whole world, publish their views, their aims, their tendencies, and meet this nursery tale of the Spectre of Communism" \n— Preamble of the Communist Manifesto.', 80))
    print('\nThis is HELP OUR NEIGHBORS by Alex DeLorenzo and Ayati Jend\n\nBegin your journey:')
    
    actions()


def actions():
  print()
  action = prompt(['Convince the populace', 'Review Personality Assessments', 'See Progress', 'Help', 'Clear'])
  
  if action == 1:  #Convince the Populace
    output = []
    for i, person in enumerate(characters.discovered):
      output.append(person.name)
    a = prompt(output)
    for i, person in enumerate(characters.discovered):
      if a == i+1:
        person.expose()
        converse(person)
    actions()
  elif action == 2:  #Personality assessments
    while True:
      try:
        page = int(input('\nPage (input 0 for all entries) >>> '))
        break
      except ValueError:
        print('\nPlease enter a number')
    print()
    if page > 0:
      for i in range(10):
        try:
          print(
            characters.discovered[i + (int(page) - 1) * 10].personality_assessment)
        except IndexError:
          print('\n--No More Entries--')
          break
    else:
      for i in characters.discovered:
        print(i.personality_assessment)
    actions()
  elif action == 3:  #progress
    print()  #spacing
    for i in characters.discovered:
      print(f'{i.name} | Level {i.level}')
    actions()
  elif action == 4:  #help
    print(
      "\nAnswer questions with the number beside the option or the name itself (not case sensitive, but I would recommend numbers to avoid errors)"
    )
    actions()
  elif action == 5:
    clear()
    actions()


def converse(person):
  score = 0
  file = person.file
  level = person.level
  with open(f'trees/{file}') as f:
    actions = 5
    line_num = 0
    # Loop through each line in the file
    while actions:
      print()
      f.seek(0)
      lines = f.readlines()
      cur_line_num = 0
      #Go to level
      try:
        for i in lines:
          level_num, text = i.split('~')
          if int(level_num) == level:
            break
          cur_line_num += 1
      #Go to line
        line = lines[cur_line_num + line_num].strip()
      except:
        print('reached maxed level')
        break
      if not line:
        break
      level_num, text = line.split('~')
      #split question and answers
      question, answer_choices = text.split(" \\ ")
      print('{}\n'.format(question))
      choices = answer_choices.split("; ")
      #split answer, score, next question
      for i, answer_choice in enumerate(choices):
        answer, score_value, route = answer_choice.split(":")
        print('{}) {}'.format(i + 1, answer))
      #input
      user_answer = input("> ")
      #check answers
      for i, answer_choice in enumerate(choices):
        answer, score_value, next_question_num = answer_choice.split(":")
        if user_answer.lower() == answer.lower() or user_answer == str(i + 1):
          if next_question_num == 'x':
            return
          score += float(score_value)
          actions -= 1
          line_num = int(next_question_num) - 1
          break
  if score >= 5:
    #level += 1
    pos = characters.discovered.index(person)
    if pos == len(characters.discovered) - 1:
      characters.discovered.append(characters.all_characters[len(characters.discovered)])
  a = input('1) Try Again\n2) Give up (for now)\n>> ')
  if a == '1':
    converse(file, level)


def ending():
  print("\n\n\nYou've reached the end of the game. Continue?")
  actions() if prompt(['yes', 'no']) == 2 else clear()
  print('-----Twelve Years Later----- (press enter to continue)')
  endingText = [
    'Your back aches after hours on your throne.',
    'The steel uniform burns with its heavy fasteners digging into your flesh and the epaulette weighing down upon your shoulder.',
    'Your heavy torso is marred with bullet holes and scars',
    'The wounds in your soul run deeper.', 'You had won',
    'the word holds little meaning',
    'In every sense of the word you were successful:',
    'You had riches and power, control beyond your wildest dreams.', 'and yet',
    'You stare at the skulls out the window, piled nearly to the highest floor of the castle',
    '\nBooted footsteps echo through the empty hall.', '"Guards!"',
    'A miserable silhouette of a man limps into the throne room',
    '"they\'ve left. you know that"',
    '"Yes, yes. We didn\'t need them anymore."',
    '"oh, none would dare, would they?"', '"None would."', '\na pause\n',
    '"Why do you come?"',
    '"to see you. some say you are no man, but a beast."', 'you scowl',
    '"We are a man, as any other."', 'he laughs', '"you lie, my comrade."',
    '"Who are you?"', 'a hollow chuckle', '"ha. you don\'t remember me?"',
    "'Why should we remember the likes of you?'", 'he chuckles',
    '"not a man remains in this town to pay you tribute or frolic in this utopia."',
    '"Do not criticize our regime."', 'your hand lowers to your holster',
    '"you promised us peace. you promised us land and bread."',
    '"PEASANT, WHAT IS YOUR NAME"', '"karl"',
    '"Karl, say another word and you\'ll join that pile." you gesture out the window'
  ]
  for text in endingText:
    input('')
    print(text, end='')
  input()
  print('\nhe pauses\n')
  sleep(1)
  for character in 'slowly:      "long live my vozhd"':
    print(character, end='', flush=True)
    sleep(0.3)
  sleep(3)
  try:
    playsound('theme.wav', block=False)
  except:
    print('    --Audio file doesn\'t want to play nice, just imagine a very dissonant transposition of the Soviet Anthem--')
  print('\n\n\nbang')
  sleep(3)
  credits()
  

def credits():
  print()
  with open('credits.txt') as f:
    for lines in f.readlines():
      for character in lines:
        print(character, end='', flush=True)
        sleep(0.1)
  sleep(5)
  print('\n\nPlay Again?')
  a = prompt(['yes', 'no'])
  if a == 2:
    return()
  else:
    print('Restart Progress? (Cannot be undone)')
    if prompt(['Yes', 'No']) == 1:
      for i in characters.discovered:
        i.level = 1
      characters.discovered = [characters.karl_m]
    clear()
    introduction()

def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
clear()
# ending()
openingText()
introduction()
