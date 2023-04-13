class person():

  def __init__(self, name, file, level, personality_assessment, exposition):
    self.name = name
    self.file = file
    self.level = level
    self.personality_assessment = personality_assessment
    self.exposition = exposition

  def expose(self):
    for i in self.exposition:
      print(i, end=' ')
      input()

karl_m = person(
  'Karl M', 
  'karl m.txt', 
  1, 
  'Karl M: Already leaning towards communism. Seeks power. Wants a wife and at least 7 kids.', 
  ['You begin your journey to enlighten the world (\033[3mpress enter to continue\033[0m)', 'or at least the town of Millburn.', 'First on your list: Karl M.', 'You have some information about him recorded -- check "personality assessments" for more information', 'You knock on the door']
)

redd_neck = person(
  'Redd Neck',
  'redd neck.txt',
  1,
  'Redd Neck: Distrusts government. Strong defender of the second amendment.',
  ['You look down at your clipboard to the next person on your list: Redd Neck', 'You ignore the multiple "No Trespassing" signs and ring the doorbell.', 'A small peephole on the door opens and you see a single green eye peering through.']
)

gertrude_ascotson = person(
  'Gertrude Ascotson',
  'gertrude ascotson.txt',
  1,
  'Gertrude Ascotson: Fierce Capitalist. Do not trust the grandmotherly vibes. She will do what she has to to win.',
  ['Next on your clipboard is a woman, Gertrude Ascotson', 'You walk up to the large house with large windows overlooking her tree-laden yard.', 'You can see inside the windows is pink, frilly decor, stuffed to the brim with doilies, fur, and cozy pillows everywhere.', 'You ring the doorbell, letting off a soft, delicate sound.', 'A little old lady swings the door open. She reminds you vaguely of your grandmother, and she seems to emit an aura of kindness about her.']
)

myrrh_dirher = person(
  'Myrrh DiRher',
  'myrrh dirher.txt',
  1,
  'Myrrh DiRher: Social Recluse. You\'ve heard something about an ongoing investigation, but you\'re sure it\'s nothing',
  ['You walk into a tree-laden property, much farther away than the others.', 'You look down at your list for his name: Myrrh DiRher?', 'You feel confused, yet you continue.', 'You walk through a winding path to a rough-hewn log cabin.', 'The door has deep scars through it, almost as if an axe had been repeatedly swung into it.', 'You steady your breath and rap the door.', 'A man opens the door, his face cast in shadow, and suspicious red splatter marks all over his clothes.', 'He steps forward holding an axe, dripping wet as if just washed.', 'He immediately makes you feel uneasy, your hair standing on end.']
)

all_characters = [
  karl_m,
  redd_neck,
  gertrude_ascotson,
  myrrh_dirher
]

discovered = [karl_m]
