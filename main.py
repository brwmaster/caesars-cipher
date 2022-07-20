alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
  word_list = list(text)
  encypted_list = []
  encrypted_word = ''

  for char in word_list:
    current_posistion = alphabet.index(char)
    new_position = current_posistion + shift
    
    if (new_position > len(alphabet)):
      new_position = round(new_position % len(alphabet))


    encypted_list.append(alphabet[new_position])

  print(f"The encoded text is {encrypted_word.join(encypted_list)}")

encrypt(text, shift)