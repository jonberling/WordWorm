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

    self.startWithVowel = 0
    """ratio of words that start with a vowel"""

    self.vowelTokens = 'aeiouy'
    """characters that match any of these tokens will be considered a vowel"""

  def analyze(self, words):
    # remove duplicates
    words = list(set(words))

    # compile the regex's
    vowel_re = re.compile('([{}]+)'.format(self.vowelTokens))
    consonant_re = re.compile('([^{}]+)'.format(self.vowelTokens))

    # stats
    vowels = {}            # key: vowel token;      value: number of times seen
    consonants = {}        # key: constonant token; value: number of times seen
    tokenFrequency = {}    # key: number of tokens in a single word
                           # value: count of words with same number of tokens
    startWithVowel = 0     # count of words that start with a vowel
    wordCount = len(words) # total number of words

    # analyze
    for word in words:
      tokensInWord = 0
      word = word.lower()

      if vowel_re.match(word[0]):
        startWithVowel += 1

      tokensInWord += self._processMatches(word, vowel_re, vowels)
      tokensInWord += self._processMatches(word, consonant_re, consonants)
      self._count(tokenFrequency, tokensInWord)

    # normalize counts
    self._normalize(vowels, wordCount)
    self._normalize(consonants, wordCount)
    self._normalize(tokenFrequency, wordCount)
    startWithVowel = startWithVowel / float(wordCount)

    # set members with updated info
    self.vowels = vowels
    self.consonants = consonants
    self.tokenFrequency = tokenFrequency
    self.startWithVowel = startWithVowel

  def toString(self):

    s = []
    s.append('vowels:')
    s.append(self._formatTable(self.vowels))
    s.append('consonants:')
    s.append(self._formatTable(self.consonants))
    s.append('token frequency:')
    s.append(self._formatTable(self.tokenFrequency))
    s.append('Radio of words that start with a vowel: {:.5f}'.format(wordWorm.startWithVowel))

    return "\n".join(s)

  def __repr__(self):
    return self.toString()

  @staticmethod
  def _processMatches(word, re, container):
    tokens = 0
    for match in re.findall(word):
      WordWorm._count(container, match)
      tokens += 1

    return tokens

  @staticmethod
  def _normalize(container, wordCount):
    for word, count in container.items():
      container[word] = count / float(wordCount)

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

  sys.exit(0)
