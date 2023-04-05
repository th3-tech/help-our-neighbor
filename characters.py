class person():

  def __init__(self, name, file, level, personality_assesment, exposition):
    self.name = name
    self.file = file
    self.level = level
    self.personality_assesment = personality_assesment
    self.exposition = exposition

  def expose(self):
    for i in self.exposition:
      print(i, end=' ')
      input()


karl_m = person(
  'Karl M', 'karl m.txt', 1,
  'Karl M: Already leaning towards communism. Seeks power. Wants a wife and at least 7 kids.',
  ['wow', 'nice'])

discovered = [karl_m]
