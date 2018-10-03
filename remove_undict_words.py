from math import log
import enchant
import wx
from enchant.checker import SpellChecker
from enchant.checker.wxSpellCheckerDialog import wxSpellCheckerDialog
# file = open("words-by-frequency.txt", "r")
# # Build a cost dictionary, assuming Zipf's law and cost = -math.log(probability).
out = open("alfabeto.txt", "w")

with open("pt_br_full.txt") as f:
    chkr = enchant.checker.SpellChecker("pt_BR")
    for line in f.readlines():
        x = line.split(' ')[0]
        y = line.split(' ')[1]
        if (chkr.check(x)):
            out.write(x + ' ' + y)

