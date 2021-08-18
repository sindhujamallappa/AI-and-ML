# import string
# clist=["Tesla Model S", "Toyots", "Ford Fiesta ST", "BMW", "Alfa Romeo Giulia QV", "Honda Civic Type R", "Ferrari 458 Speciale", "McLarena P1", "Ferrari Laferrari", "Porsche 918"]

def count(li):
        num_vowel = 0
        for char in li:
            if char in "aeiouAEIOU":
               num_vowel = num_vowel + 1
        return num_vowel

list=["Tesla Model S", "Toyots", "Ford Fiesta ST", "BMW", "Alfa Romeo Giulia QV", "Honda Civic Type R", "Ferrari 458 Speciale", "McLarena P1", "Ferrari Laferrari", "Porsche 918"]
list.sort(key=count)
print(list)

