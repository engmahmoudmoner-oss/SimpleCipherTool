import string
print("""hi welcom to encrypted words program >>>
------------------------------------------
for encrypt type 1
for decrypt type 2
------------------------------------------""")
result=input("type 1 ,or  2 : ")
print("--------------------------------------------")
if result=="1":
     alphabet = string.ascii_lowercase
     word = input("type your word : ")
     key =int(input("type key number : "))
     encrypted_word = "" 
     for letter in word:
        if letter.lower() in alphabet:
            original_position = alphabet.index(letter.lower())
            new_position = (original_position + key) % 26
            new_letter= alphabet[new_position]
            if letter.isupper():
                encrypted_word += new_letter.upper()
            else:
                encrypted_word+= new_letter
        else:
            encrypted_word += letter
     print("encrypted word is : ", encrypted_word)
if result=="2":
     alphabet = string.ascii_lowercase
     word = input("type your word : ")
     key = int(input("type key number : "))

     decrypted_word = "" 
     for letter in word:
         if letter.lower() in alphabet:
            original_position = alphabet.index(letter.lower())
            new_position = (original_position - key) % 26
            new_letter = alphabet[new_position]
            if letter.isupper():
                decrypted_word += new_letter.upper()
            else:
                decrypted_word += new_letter
         else:
            decrypted_word += letter

     print("decrypted word is : ", decrypted_word)
