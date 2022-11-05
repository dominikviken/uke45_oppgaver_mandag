import random

'''
Oppgave 1

VELG RIKTIG OUTPUT

alternative 1 = 'none'
alternative 2 = 'invalid syntax'
alternative 3 = 'the cat on the roof'

'''
word = 'the cat on the roof'
print(word)

'''
Oppgave 2

VELG RIKTIG OUTPUT
alternative 1 = 'Eureka'
alternative 2 = 'IM- Åssiden vgs'
alterbative 3 = 'none'
'''
a =1
b =1
c =7
d =5

result = a + b + d
if result < c:
    print('Eureka')
else:
    print('IM- Åssiden vgs')


'''
Oppgave 3 

Hvor mange ganger skal følgende loop kjøres?

VELG RIKTIG SVAR
 alternative 1 = 150
 alternative 2 = 50
 alternative 3 = 10
 alterbative 4 = uendelig mange ganger.


'''

index = 150
while index <= 200:
    print(index)
    index+=5


'''
oppgave 4

Bruk variablene num1 og num2 for implementere en funksjon som 
returnere KUN oddetall. bruk gjerne funskjon print()
'''

def oddeTall():
     num1 = random.randint(1,10) #tilfeldig tall mellom 1 og 10
     num2 = random.randint(2,9) #tilfeldig tall mellom 2 og 9
