
users = ('bob', 'ann', 'mike', 'liz')
passwords = ('123', 'pass123', 'password123', 'pass123' )
user_inp = input('username: ')
if user_inp in users:
    print('ok')
elif user_inp not in users:
    print('wrong username') , quit()

pass_inp = input('password: ')
if pass_inp in passwords:
    print('ok')
elif pass_inp not in users:
    print('wrong password') , quit()

print("-" * 55)

print('Welcome to the app' ' ' + user_inp + ' ' +  '\nWe have 3 texts to be analyzed.')


texts ={
'1':
'Situated about 10 miles west of Kemmerer, Fossil Butte is a ruggedly impressive topographic feature that rises sharply some 1000 feet above Twin Creek Valley to an elevation of more than 7500 feet above sea level. The butte is located just north of US 30N and the Union Pacific Railroad, which traverse the valley. ',

'2':'At the base of Fossil Butte are the bright red, purple, yellow and gray beds of the Wasatch Formation. Eroded portions of these horizontal beds slope gradually upward from the valley floor and steepen abruptly. Overlying them and extending to the top of the butte are the much steeper buff-to-white beds of the Green River Formation, which are about 300 feet thick.',

'3':'The monument contains 8198 acres and protects a portion of the largest deposit of freshwater fish fossils in the world. The richest fossil fish deposits are found in multiple limestone layers, which lie some 100 feet below the top of the butte. The fossils represent several varieties of perch, as well as other freshwater genera and herring similar to those in modern oceans. Other fish such as paddlefish, garpike and stingray are also present.'
}

print("-" * 55)

one_two_three = str((1, 2, 3,))
number_input = input("Enter a number between 1 and 3 : ")

print("-" * 55)

if number_input not in one_two_three :
    print('ERROR! select a number between 1 and 3 !')


#number of words
sum_chara = texts[number_input]
sum_chara1 = print("There are"+ " " + str(len(sum_chara.split())) + " " + "words in the selected text.")

#number of words starting with a Maj 

my_string = texts[number_input]
words = my_string.strip().split()
num_title = 0
for word in words:
    if word.istitle():
        num_title += 1

word_start_maj = print('There are', str(num_title) ,'titlecase words.')
#počet slov psaných velkými písmeny,

my_string = texts[number_input]
words = my_string.strip().split()
num_title = 0
for word in words:
    if word.isupper():
        num_title += 1

word_all_capital = print('There are', str(num_title) ,'uppercase words.')
#počet slov psaných malými písmeny,
my_string = texts[number_input]
words = my_string.strip().split()
num_title = 0
for word in words:
    if word.islower():
        num_title += 1

word_all_lower = print('There are', str(num_title) ,'lowercase words.')
#počet čísel (ne cifer),
my_string = texts[number_input]
words = my_string.strip().split()
num_title = 0
for word in words:
    if word.isdigit():
        num_title += 1

word_all_capital = print('There are', str(num_title) ,'numeric words.')
#sumu všech čísel (ne cifer) v textu
my_string = texts[number_input]

sum_digit = 0

for words in my_string:
        if words.isdigit() == True:
            z = int(words)
            sum_digit = sum_digit + z

word_all_capital = print('The sum of all numbers', str(sum_digit))

print("-" * 55)

print('LEN|', '  ', 'OCCURENCES', '  ', '|NR.', )


print("-" * 55)

ODDELOVAC = "+--+------------+--+"
vycistena_slova = []
vyskyt_slov = dict()
pet_nejcastejsich = []

for slovo in texts[number_input].split():
    ciste_slovo = slovo.strip(",.:;")
    vycistena_slova.append(ciste_slovo.lower())

for slovo in vycistena_slova:
    if slovo not in vyskyt_slov:
        vyskyt_slov[slovo] = 1
    else:
        vyskyt_slov[slovo] = vyskyt_slov[slovo] + 1

serazeny_vyskyt = sorted(vyskyt_slov.values(), reverse=True)[:15]

for slovo in vyskyt_slov:
    if vyskyt_slov[slovo] in serazeny_vyskyt:
        serazeny_vyskyt.remove(vyskyt_slov[slovo])
        pet_nejcastejsich.append((vyskyt_slov[slovo], slovo))

for index, vysledek in enumerate(sorted(pet_nejcastejsich, reverse=True), 1):
    print( f"{index}.| {vysledek[1]: ^10} |{vysledek[0]}x",  sep="\n")