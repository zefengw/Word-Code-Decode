def code(word):
  coded_word = ""
  counter = 1
  for i in word:
    res = ord(i)
    res += counter
    coded_word += chr(res)
    counter += 1
  return coded_word

def decode(word):
  decoded_word = ""
  counter = 1
  for i in word:
    res = ord(i)
    res -= counter
    decoded_word += chr(res)
    counter += 1
  return decoded_word

word = input("Enter a word: ")
choice = input("Would you like to \"code\" or \"decode\" your word(code/decode): ")
if choice == "code": 
  print(f"Your input was {word} and your coded word is {code(word)}.")
elif choice == "decode":
  print(f"Your input was {word} and your decoded word is {decode(word)}.")
else:
  print("Please enter a valid word.")
