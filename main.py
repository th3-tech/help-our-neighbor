import os, time, textwrap, characters


def openingText():
  print('HELP THY NEIGHBORS')
  time.sleep(1)
  os.system('clear')
  #time.sleep(0.2)
  print('HELP YOUR NEIGHBORS')
  time.sleep(1)
  os.system('clear')
  #time.sleep(0.3)
  print('HELP OUR NEIGHBORS')
  time.sleep(1)
  print('\nMade for the Millburn 2023 STEAMfest \nby alex delorenzo, dialogue trees by ayati jend\n\n\n')


def prompt(question_list):
  try:
    for i, question in enumerate(question_list):
      print('{}) {}'.format(i + 1, question))
    answer = input('\n>>> ')
    for i, question in enumerate(question_list):
      if answer.lower() == question.lower() or answer == str(i + 1):
        return (i + 1)
  except TypeError:
    print('please enter a number or string\n')
    prompt(question_list)


def introduction():
  print(textwrap.fill('Welcome to the town of Millburn, New Jersey. The grass is green and the roads are paved with gold. If you work hard, you can help our neighbors — these poor, misguided capitalists — to realize the error of their ways and you can turn this poor town into a prosperous communist dictatorship.\n', 80))
  print('\nStart?')
  if prompt(['Yes', 'No']) == 2:
    print('okay?')
  else:
    os.system('clear')
    print(
      textwrap.fill('"It is high time that Communists should openly, in the face of the whole world, publish their views, their aims, their tendencies, and meet this nursery tale of the Spectre of Communism" \n— Preamble of the Communist Manifesto.', 80))
    print('\nThis is HELP OUR NEIGHBORS by Alex DeLorenzo and Ayati Jend\n\nBegin your journey:')
    
    actions()


def actions():
  print()
  action = prompt(['Convince the populace', 'Review Personality Assesments', 'See Progress', 'Help', 'Clear'])
  
  if action == 1:  #Convince the Populace
    output = []
    for i, person in enumerate(characters.discovered):
      output.append(person.name)
    a = prompt(output)
    for i, person in enumerate(characters.discovered):
      if a == i+1:
        converse(person.file, person.level)
    actions()
  elif action == 2:  #Personality Assesments
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
            characters.discovered[i + (int(page) - 1) * 10].personality_assesment)
        except IndexError:
          print('\n--No More Entries--')
          break
    else:
      for i in characters.discovered:
        print(i.personality_assesment)
    actions()
  elif action == 3:  #progress
    print()  #spacing
    for i in characters.discovered:
      print(f'{i.name} | Level {i.level}')
    actions()
  elif action == 4:  #help
    print(
      "\nAnswer questions with the number beside the option or the name itself (not case sensitive, but I would reccomend numbers to avoid errors)"
    )
    actions()
  elif action == 5:
    os.system('clear')
    actions()


def converse(file, level):
  score = 0
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
      #split answer, score, next questino
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
          score += int(score_value)
          actions -= 1
          line_num = int(next_question_num) - 1
          break
  if score >= 10:
    level += 1
  a = input('1) go again\n2) stop\n>> ')
  if a == '1':
    converse(file, level)


def ending():
  print("\n\n\nYou've reached the end of the game. Continue?")
  actions() if prompt(['yes', 'no']) == 2 else os.system('clear')
  print('-----Twelve Years Later----- (press enter to continue)')
  endingText = [
    'Your back aches after hours on your throne.',
    'The steel uniform burns with its heavy fastners digging into your flesh and the epaulette weighing down upon your shoulder.',
    'Your heavy torso is marred with bullet holes and scars',
    'The wounds in your soul run deeper.', 'You had won',
    'the word holds little meaning',
    'In every sense of the word you were succesful:',
    'You had riches and power, control beyond your wildest dreams.', 'and yet',
    'You stare at the skulls out the window, piled nearly to the highest floor of the castle',
    '\nBooted footsteps echo through the empty hall.', '"Guards!"',
    'A miserable shilloute of a man limps into the throne room',
    '"they\'ve left. you know that"',
    '"Yes, yes. We didn\'t need them anymore."',
    '"oh, none would dare, would they?"', '"None would."', '\na pause\n',
    '"Why do you come?"',
    '"to see you. some say you are no man, but a beast."', 'you scowl',
    '"We are a man, as any other."', 'he laughs', '"you lie, my comrade."',
    '"Who are you?"', '"ha. you don\'t remember me, tsar?"',
    "'Why should we remember the likes of you?'", 'he chuckles',
    '"not a man remains in this town to pay you tribute or frolick in this utopia."',
    '"Do not critize our regime."', 'your hand lowers to your holster',
    '"you promissed us peace. you promised us land and bread."',
    '"PEASENT, WHAT IS YOUR NAME"', '"karl"',
    '"Karl, say another word and you\'ll join that pile." you gesture out the window'
  ]
  for text in endingText:
    input('')
    print(text, end='')
  input()
  print('\nhe pauses\n')
  time.sleep(1)
  for character in 'slowly:      "long live the tsar"':
    print(character, end='', flush=True)
    time.sleep(0.3)
  time.sleep(3)
  print('\n\n\nbang')


openingText()
introduction()
