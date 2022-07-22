from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(direction, text, shift):
  word_list = list(text)
  caesar_cipher = []
  text = ''

  if direction == 'decode':
    shift *= -1

  for char in word_list:
    if char in alphabet:
      current_position = alphabet.index(char)
      new_position = current_position + shift
      
      if (new_position > len(alphabet)):
        new_position = round(new_position % len(alphabet))
      elif (new_position < 0):
        new_position = len(alphabet) + (new_position)
        
      caesar_cipher.append(alphabet[new_position])
    else:
      caesar_cipher.append(char)

  print(f"The {direction}d text is: {text.join(caesar_cipher)}")

print(logo)
quit_program = False
while not quit_program:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

  if 'encode' in  direction or 'decode' in direction:
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(direction, text, shift)
    user_input = input("\nType 'yes if you want to go agian. Otherwise type 'no' ").lower()

    if(user_input == 'no'):
      quit_program = True
  else:
    print(f"\nSorry the command {direction} is not valid.\nPlease use 'encode' or 'decode'")
  
 
