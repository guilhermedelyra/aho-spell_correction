from math import log
import enchant
import wx
from enchant.checker import SpellChecker
from enchant.checker.wxSpellCheckerDialog import wxSpellCheckerDialog
# file = open("words-by-frequency.txt", "r")
# # Build a cost dictionary, assuming Zipf's law and cost = -math.log(probability).
with open("words-by-frequency.txt") as f:
    words = [line.strip() for line in f.readlines()]
    wordcost = dict((k, log((i+1)*log(len(words)))) for i,k in enumerate(words))
    maxword = max(len(x) for x in words)

def correct_spell(s):
    chkr = enchant.checker.SpellChecker("pt_BR")
    chkr.set_text(s)
    for err in chkr:
        sug = err.suggest()[0]
        err.replace(sug)

    c = chkr.get_text() #returns corrected text
    return c

def infer_spaces(s):
    """Uses dynamic programming to infer the location of spaces in a string
    without spaces."""

    # Find the best match for the i first characters, assuming cost has
    # been built for the i-1 first characters.
    # Returns a pair (match_cost, match_length).
    def best_match(i):
        candidates = enumerate(reversed(cost[max(0, i-maxword):i]))
        return min((c + wordcost.get(s[i-k-1:i], 9e999), k+1) for k,c in candidates)

    # Build the cost array.
    cost = [0]
    for i in range(1,len(s)+1):
        c,k = best_match(i)
        cost.append(c)

    # Backtrack to recover the minimal-cost string.
    out = []
    i = len(s)
    while i>0:
        c,k = best_match(i)
        assert c == cost[i]
        out.append(s[i-k:i])
        i -= k

    return " ".join(reversed(out))

messy_txt = "previdensia sosial é augo difisio e disc utido no bra sil"
messy_corrected = correct_spell(messy_txt)
print(messy_corrected)
print(infer_spaces(messy_txt.lower().replace(' ', '').replace(',', '')).capitalize())
print(infer_spaces(messy_corrected.lower().replace(' ', '').replace(',', '')).capitalize())
print(correct_spell(infer_spaces(messy_txt.lower().replace(' ', '').replace(',', '')).capitalize()))

# import re
# from collections import Counter

# def words(text): return re.findall(r'\w+', text.lower())

# WORDS = Counter(words(open('words-by-frequency.txt').read()))

# def P(word, N=sum(WORDS.values())): 
#     "Probability of `word`."
#     return WORDS[word] / N

# def correction(word): 
#     "Most probable spelling correction for word."
#     return max(candidates(word), key=P)

# def candidates(word): 
#     "Generate possible spelling corrections for word."
#     return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])

# def known(words): 
#     "The subset of `words` that appear in the dictionary of WORDS."
#     return set(w for w in words if w in WORDS)

# def edits1(word):
#     "All edits that are one edit away from `word`."
#     letters    = 'abcdefghijklmnopqrstuvwxyzàáâãçéèêíîìòóôõöùúûü'
#     splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
#     deletes    = [L + R[1:]               for L, R in splits if R]
#     transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
#     replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
#     inserts    = [L + c + R               for L, R in splits for c in letters]
#     return set(deletes + transposes + replaces + inserts)

# def edits2(word): 
#     "All edits that are two edits away from `word`."
#     return (e2 for e1 in edits1(word) for e2 in edits1(e1))

# print (correction("difisio"))
# print (correction("previsensia"))
# file.close()