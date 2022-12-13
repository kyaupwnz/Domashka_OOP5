class TeamIterator:
  def __init__(self, team):
      self.team = team
      self.counter_jun = 0
      self.counter_sen = 0
      self.name = ''

  def __next__(self):
      if self.counter_jun < len(self.team._juniorMembers):
          x = self.team._juniorMembers[self.counter_jun]
          self.counter_jun += 1
          self.name = 'junior'
          return x, self.name
      elif self.counter_sen < len(self.team._seniorMembers):
          x = self.team._seniorMembers[self.counter_sen]
          self.name = 'senior'
          self.counter_sen += 1
          return x, self.name 
      else:
          self.counter_sen = 0
          raise StopIteration


class Team:
  def __init__(self):
    self._juniorMembers = list()
    self._seniorMembers = list()
  def add_junior_members(self, members):
    self._juniorMembers += members
  def add_senior_members(self, members):
    self._seniorMembers += members
  def __iter__(self):
    return TeamIterator(self)

def main():
  team = Team()
  team.add_junior_members(['Ivan', 'Mary', 'Nikita'])
  team.add_senior_members(['Rita', 'Roma', 'Ramil'])
  print('*** Итерируемся по команде в цикле for ***')
  for member in team:
    print(member)
  print('*** Итерируемся по команде в цикле while ***')
  iterator = iter(team)
  while True:
    try:
      elem = next(iterator)
      print(elem)
    except StopIteration:
      break
if __name__ == '__main__':
    main()
