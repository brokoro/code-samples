sentence = "the quick brown fox jumps over the lazy dog"

# Returns list of strings in sentence separated by spaces
words = sentence.split()
print words

# Comprehends list of lengths of words other than "the"
word_lengths = [len(word) for word in words if word != "the"]
print word_lengths
