# with open chiude automanticamente il file
try:
    with open('test.txt') as file:  # se non fosse nella cartella del progetto avrei bisogno dell'intero path
        print(file.read())
except FileNotFoundError:
    print("That file was not found")

# print(file.closed)

text = "Yooooooo\nThis is some text\nHave a good one!"
text2 = "\nHave a nice day! See ya!"
with open('test2.txt', 'w') as file:
    file.write(text)

with open('test2.txt', 'a') as file:
    file.write(text2)
