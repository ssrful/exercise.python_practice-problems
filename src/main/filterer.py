# Created by Leon Hunter at 12:10 PM 12/08/2020
class Filterer(object):
    def remove_characters(self, string_to_remove_from, characters_to_remove):
        characterToRemove = ""
        for character in string_to_remove_from:
            if character not in characters_to_remove:
                characterToRemove += character
        return characterToRemove

    def remove_vowels(self, string_to_remove_from):
        vowels = ['a', 'e', 'i', 'o', 'u']
        removeVowels = ""
        for characters in string_to_remove_from:
            if characters not in vowels:
                removeVowels += characters
        return removeVowels

    def remove_consonants(self, string_to_remove_from):
        consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        removeConsonants = ""
        for characters in string_to_remove_from:
            if characters not in consonants:
                removeConsonants += characters
        return removeConsonants

