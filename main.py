alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

def caesar(direction, text, shift):
  word_list = list(text)
  caesar_cipher = []
  text = ''

  if direction == 'decode':
    shift *= -1

  for char in word_list:
    current_position = alphabet.index(char)

    new_position = current_position + shift
    
    if (new_position > len(alphabet)):
      new_position = round(new_position % len(alphabet))
    elif (new_position < 0):
      new_position = len(alphabet) + (new_position)
      
    caesar_cipher.append(alphabet[new_position])

  print(f"The {direction}d text is {text.join(caesar_cipher)}")

if 'encode' in  direction or 'decode' in direction:
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  caesar(direction, text, shift)
else:
  print(f"\nSorry the command {direction} is not valid.\nPlease use 'encode' or 'decode'")
