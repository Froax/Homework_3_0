#3_2 + 3_3

Leeftijd = int(input('Hoe oud ben je? '))
Paspoort = str(input('Heb je een Nederlands paspoort? ja/nee '))

if ((Leeftijd >= 18) and (Paspoort == 'ja')):
    print('Je kunt stemmen!')
else:
    print('Je mag niet stemmen.')