Finput= open('./input.txt', 'r', encoding='UTF-8', errors='ignore')
Foutput= open('./output.txt', 'w', encoding='UTF-8')
lines=Finput.readlines()
t=0
for line in lines:
    if(len(line)>30):
        Foutput.write(line)
print(t)

Finput.close()
Foutput.close()
