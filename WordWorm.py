#!/usr/bin/env python3

import io
import operator
import os
import re
import sys

class WordWorm(object):
  """
  Split a list of words into tokens, grouped by continuous vowels/consonants.
  """

  def __init__(self):

    self.vowels = {}
    """dictionary of vowel tokens; key is token, value is frequency"""

    self.consonants = {}
    """dictionary of consonant tokens; key is token, value is frequency"""

    self.tokenFrequency = {}
    """dictionary of token count frequency; key is the token count, value is the frequency"""

    self.startWithVowel = -1.0
    """ratio of words that start with a vowel"""

    self.vowelTokens = 'aeiouy'
    """characters that match any of these tokens will be considered a vowel"""

  def analyze(self, words):

    # generate the re
    vowel_re = re.compile('([{}]+)'.format(self.vowelTokens))
    consonant_re = re.compile('([^{}]+)'.format(self.vowelTokens))

    # containers
    vowels = {}
    consonants = {}
    tokenCount = {}
    startWithVowel = 0

    # remove duplicates
    words = list(set(words))
    wordCount = len(words)

    # analyze
    for word in words:
      tokens = 0 # count tokens in word
      word = word.lower()

      if vowel_re.match(word[0]):
        startWithVowel += 1

      for match in vowel_re.findall(word):
        self._count(vowels, match)
        tokens += 1

      for match in consonant_re.findall(word):
        self._count(consonants, match)
        tokens += 1

      self._count(tokenCount, tokens)

    # normalize
    for word, count in vowels.items():
      vowels[word] = count / float(wordCount)
    for word, count in consonants.items():
      consonants[word] = count / float(wordCount)
    for token, count in tokenCount.items():
      tokenCount[token] = count / float(wordCount)
    startWithVowel = startWithVowel / float(len(words))

    # set members with updated info
    self.vowels = vowels
    self.consonants = consonants
    self.tokenFrequency = tokenCount
    self.startWithVowel = startWithVowel

  def toString(self):

    s = []
    s.append('vowels:')
    s.append(self._formatTable(self.vowels))
    s.append('consonants:')
    s.append(self._formatTable(self.consonants))
    s.append('token frequency:')
    s.append(self._formatTable(self.tokenFrequency))

    return "\n".join(s)

  def __repr__(self):
    return self.toString()

  @staticmethod
  def _formatTable(table):
    sortedTable = sorted(table.items(), key=operator.itemgetter(1), reverse=True)
    items = []

    for item in sortedTable:
      items.append('  "{}": {:.5f}'.format(item[0], item[1]))

    return ",\n".join(items)

  @staticmethod
  def _count(d, k):
    if k not in d: d[k] = 0
    d[k] += 1

if __name__ == '__main__':

  if not len(sys.argv) == 2:
    print("Useage: python {} <file>".format(os.path.basename(__file__)))
    sys.exit(2)

  words = []
  filename = sys.argv[1]

  try:
    with open(filename, 'r') as file:
      words = file.read().split()
  except IOError as e:
    print(str(e))
    sys.exit(1)

  wordWorm = WordWorm()
  wordWorm.analyze(words)

  print(wordWorm)
  print('Radio of words that start with a vowel: {:.5f}'.format(wordWorm.startWithVowel))

  sys.exit(0)
