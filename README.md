# WordWorm

A Python library for processing a list of words, and breaking it up into tokens of continuous vowel / consonant characters. Also includes statistical information about the list of words.

For example, the word 'John' would be broken up into the following tokens: `j`, `o`, `hn`

WordWorm can either be ran from the command line, or used as a library.

## How To Run

`./WordWorm.py <file>`

## Files

`WordWorm.py` - core program

`Tests.py`- unit tests

`names.txt` - list of names taken from https://www.ssa.gov/oact/babynames/

## Output

The tokens are sorted by vowels / consonants. They are also sorted by how often they appear. In the sample output below, the token `a` appears in 66% of all words in the data set.

The token frequency is how many tokens are in a given word. In the sample output, 35% of the words had 5 tokens.

Finally the output lists how many words started with a vowel.

## Sample Output

```
vowels:
  "a": 0.66882,
  "e": 0.44373,
  "i": 0.26643,
  "o": 0.23207,
  "y": 0.11902,
  "ia": 0.08068,
  "ie": 0.05428,
  "u": 0.05129,
  "ay": 0.04034,
  "ai": 0.03685,
  "ey": 0.03486,
  // snip many lines of output
consonants:
  "n": 0.35359,
  "l": 0.29133,
  "r": 0.20867,
  "m": 0.15538,
  "s": 0.12052,
  "d": 0.11006,
  "k": 0.09363,
  "j": 0.08715,
  "c": 0.08068,
  "h": 0.07570,
  "nn": 0.05627,
  "v": 0.05578,
  "ll": 0.04980,
  "t": 0.04582,
  "br": 0.04084,
  "b": 0.03884,
  "g": 0.03635,
  "st": 0.02888,
  "z": 0.02540,
  "th": 0.02092,
  // snip many lines of output
token frequency:
  "5": 0.35209,
  "4": 0.30030,
  "6": 0.14841,
  "3": 0.09562,
  "7": 0.05926,
  "2": 0.02888,
  "8": 0.01345,
  "9": 0.00100,
  "1": 0.00050,
  "10": 0.00050
Radio of words that start with a vowel: 0.22560
```
