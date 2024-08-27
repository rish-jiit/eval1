def reverse_words_and_capitalize(sentence):
   
    words = sentence.split()
    
   
    reversed_words = words[::-1]
    
    capitalized_words = [word.capitalize() for word in reversed_words]
   

    reversed_sentence =' '.join(capitalized_words)
    
    return reversed_sentence


input_sentence = "hello world this is a test"
result = reverse_words_and_capitalize(input_sentence)
print(result)  
