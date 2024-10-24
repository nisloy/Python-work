def word_frequencies(sentence):
    words = sentence.lower().split()
    frequency_dict = {}

    for word in words:
        if word in frequency_dict:
            frequency_dict[word] += 1  
        else:
            frequency_dict[word] = 1  

    return frequency_dict

input_sentence = "Amuza MUGISHA loves drinking water in a container."
result = word_frequencies(input_sentence)

print(result)  