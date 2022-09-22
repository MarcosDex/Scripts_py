#write a program that asks for 3 words, then prints the longest word and the number of characters in it
word1 = input('Entre com a primeira palavra: ')
length1 = len(word1)
word2 = input('Entre com a segunda palavra: ')
length2 = len(word2)
word3 = input('Entre com a terceira palavra: ')
length3 = len(word3)
if length1 > length2 and length3:
    print('%s é a maior palavra, com %d caracters' % (word1, length1))
elif length2 > length1 and length3:
    print('%s é a maior palavra, com %d caracters' % (word2, length2))
elif length3 > length1 and length2:
    print('%s é a maior palavra, com %d caracters' % (word3, length3))
else:
    print('Algumas palavras tem o mesmo tamanho.')