#!/usr/bin/env python3

import unittest

from WordWorm import WordWorm

class TestWordWorm(unittest.TestCase):

  def test_constuctor(self):
    ww = WordWorm()

    self.assertIsNotNone(ww)

  def test_analyze(self):
    words = ['aba', 'cec', 'dii', 'ffo']

    ww = WordWorm()

    ww.analyze(words)

    # did we find all of the vowel tokens?
    self.assertIn( 'a', ww.vowels)
    self.assertIn( 'e', ww.vowels)
    self.assertIn('ii', ww.vowels)
    self.assertIn( 'o', ww.vowels)

    # did we find all of the consonant tokens?
    self.assertIn( 'b', ww.consonants)
    self.assertIn( 'c', ww.consonants)
    self.assertIn( 'd', ww.consonants)
    self.assertIn('ff', ww.consonants)

    # did we count the number of tokens?
    self.assertIn(2, ww.tokenFrequency)
    self.assertIn(3, ww.tokenFrequency)

    # did we calc basic stats correctly?
    self.assertAlmostEqual(0.25, ww.startWithVowel)

  def test_doNotCountDuplicateWords(self):
    words = ['a', 'a', 'b']

    ww = WordWorm()

    ww.analyze(words)

    # 'a' should appear as often as 'b', since we ignore dups

    self.assertEqual(0.5, ww.vowels['a'])
    self.assertEqual(0.5, ww.consonants['b'])

  def test_tokenFrequency(self):
    words = ['a', 'ab', 'ba', 'aba']

    ww = WordWorm()

    ww.analyze(words)

    self.assertAlmostEqual(0.25, ww.tokenFrequency[1])
    self.assertAlmostEqual(0.50, ww.tokenFrequency[2])
    self.assertAlmostEqual(0.25, ww.tokenFrequency[3])

if __name__ == '__main__':
  unittest.main()
