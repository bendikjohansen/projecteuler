words_file = open('42-input.txt', 'r')
words = eval(words_file.read())

word_values = [sum([ord(character) - ord('A') + 1 for character in word]) for word in words]
triangle_numbers = [int(0.5 * n * (n + 1)) for n in range(1, 24)]
triangle_word_counter = 0
for word_value in word_values:
  if word_value in triangle_numbers:
    triangle_word_counter += 1
print(triangle_word_counter)
