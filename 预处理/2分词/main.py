import jieba
Finput= open('./input.txt', 'r', encoding='UTF-8', errors='ignore')
Foutput= open('./output.txt', 'w', encoding='UTF-8')
lines=Finput.read()
Foutput.write("|".join(jieba.cut(lines)))

Finput.close()
Foutput.close()
