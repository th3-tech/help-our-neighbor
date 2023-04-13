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

all_characters = [
  karl_m,
  redd_neck
]

discovered = [redd_neck]
