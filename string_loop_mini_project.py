sentence = input("Enter the sentence: ")
words = sentence.split()
print(f"Total number of words: {len(words)}")
characters = sentence.replace(" ", "")
print(f"Total number of characters: {len(characters)}")
print(f"Python appears {sentence.lower().count('python')} times.")
for word in words:
    print(word[::-1])
vowel_count=0
for char in sentence.lower():
    if char in "aeiou":
        vowel_count += 1
print(f"total vowels: {vowel_count}")

