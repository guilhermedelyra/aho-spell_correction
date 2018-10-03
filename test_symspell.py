import os
import aho
from symspellpy.symspellpy import SymSpell, Verbosity  # import the module

def main():
    initial_capacity = 83000
    max_edit_distance_dictionary = 3
    prefix_length = 7
    sym_spell = SymSpell(initial_capacity, max_edit_distance_dictionary, prefix_length)
    dictionary_path = "alfabeto.txt"
    term_index = 0  # column of the term in the dictionary text file
    count_index = 1  # column of the term frequency in the dictionary text file

    if not sym_spell.load_dictionary(dictionary_path, term_index, count_index):
        print("Dictionary file not found")
        return

    input_term = ("previdensia sosial é augo difisio e discitido no bra sil")
    max_edit_distance_lookup = 3
    suggestions = sym_spell.lookup_compound(input_term, max_edit_distance_lookup)

    for suggestion in suggestions:
        print("{}, {}, {}".format(suggestion.term, suggestion.count,
                                  suggestion.distance))

if __name__ == "__main__":
    main()