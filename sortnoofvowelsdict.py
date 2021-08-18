# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 13:10:35 2021

@author: Sindhuja Mallappa
"""

def countvowel(str):
        num_vowel = 0
        for char in str:
            if char in "aeiouAEIOU":
               num_vowel = num_vowel + 1
        return num_vowel

list=["Tesla Model S", "Toyots", "Ford Fiesta ST", "BMW", "Alfa Romeo Giulia QV", "Honda Civic Type R", "Ferrari 458 Speciale", "McLarena P1", "Ferrari Laferrari", "Porsche 918"]
vowel_count = {}
for str in list:
    vowel_count[str] = countvowel(str)

print(vowel_count)