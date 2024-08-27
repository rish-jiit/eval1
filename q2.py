from collections import Counter
import string

def count_occurrences(sentence):
 
    sentence_cleaned = sentence.lower().translate(str.maketrans('', '', string.punctuation))
     

    letter_counter = Counter(c for c in sentence_cleaned if c.isalpha())
    
   
    word_counter = Counter(sentence_cleaned.split())
    
    return letter_counter, word_counter


input_sentence = "Hello world! This is a test. Test the counting of letters and words."
letter_counts, word_counts = count_occurrences(input_sentence)

print("Letter counts:")
for letter, count in letter_counts.items():
    print(f"{letter}: {count}")

print("\nWord counts:")
for word, count in word_counts.items():
    print(f"{word}: {count}")
