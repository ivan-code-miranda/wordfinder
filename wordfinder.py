"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
  ""Program to find random words in a dictionary""


  def __init__(self, path):
    ""Reads dictionary and returns how many words has read""

    dict_file = open(path)

    self.words = self.parse(dict_file)

    print(f"{len(self.words)} words read")

  def parse(self, dict_file):
    ""Parse dict_file to a list of words""

    return [w.strip() for w in dict_file]

  def random(self):
    ""Returns a random word""

    return random.choice(self.words)

class SpecialWordFinder(WordFinder):
  """Exculdes blank lines/comments."""
  def parse(self, dict_file):
    ""Parse dict_file to a list of words, skippping blanks and comments.""

    return [w.strip() for w in dict_file
              if w.strip() and not w.startswith("#")]
    

