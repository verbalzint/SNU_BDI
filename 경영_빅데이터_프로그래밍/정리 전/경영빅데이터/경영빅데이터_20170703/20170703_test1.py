fout2 = open('beatles3.txt','w')
fout2.write("'Let it be' by beatles\n\n")
fout2.write('When I find myself in times of trouble\n')
fout2.write('Mother Mary comes to me\n')
fout2.write('Speaking word of wisdom\n')
fout2.write('Let it be-- -\n')
fout2.write('And in my hours darkness She is standing bright in front of me\n')
fout2.write('Speaking words of wisdom\nLet it be-- -\n')
fout2.write('Let it be - Let it be Let it be - Let it be - \n')
fout2.close()
fin = open('beatles3.txt')
print(fin.read())