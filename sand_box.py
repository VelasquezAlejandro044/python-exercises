fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

def two_or_more_vowels():
    fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
    fruits_with_more_than_two_vowels = []
    vowel_count = 0
   
    for fruit in fruits:
        for letter in list(fruit.lower):
            if letter in ('a', 'e', 'i', 'o', 'u'):
                vowel_count += 1
    return vowel_count
    
print(two_or_more_vowels)
            