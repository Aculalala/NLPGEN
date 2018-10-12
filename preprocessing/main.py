import re,collections
import pickle
import numpy as np
import jieba
#删除短行
Finput= open('./input.txt', 'r', encoding='UTF-8', errors='ignore')
Foutput= open('./temp/no_short_line.txt', 'w', encoding='UTF-8')
lines=Finput.readlines()
for line in lines:
    if(len(line)>20):
        Foutput.write(line)
Finput.close()
Foutput.close()

#分词
Finput= open('./temp/no_short_line.txt', 'r', encoding='UTF-8', errors='ignore')
Foutput= open('./temp/div.txt', 'w', encoding='UTF-8')
lines=Finput.read()
Foutput.write("|".join(jieba.cut(lines)))
Finput.close()
Foutput.close()
#
Finput= open('./temp/div.txt', 'r', encoding='UTF-8', errors='ignore')
Foutput= open('./dic.dat', 'wb')
lines=Finput.readlines()
word_list=[]
for line in lines:
    word_list.extend(line.strip().split("|"))
    
collection=collections.Counter(word_list)
ignore={'','”','“'}
for i in ignore:
    collection[i]=0
#0 is for unknown words
i=1
dic={}
reverse_dic={}
for word in collection.most_common(len(collection)):
    dic[word[0]]=i
    reverse_dic[i]=word[0]
    i=i+1
dics=[dic,reverse_dic]
pickle.dump(dics,Foutput)
Finput.close()
Foutput.close()
print("词统计完成")
#
Finput= open('./temp/div.txt', 'r', encoding='UTF-8', errors='ignore')
Foutput= open('./temp/token.txt', 'w')
def tokenize(words):
    def singlemap(word):
        if word in dic:
            return str(dic[word])
        else:
            return str(0)
    return list(map(singlemap,words))
Foutput.write(",".join(tokenize(Finput.read().strip().split("|"))))
Finput.close()
Foutput.close()
print("数字化完成")
#
Finput= open('./temp/token.txt', 'r')
Foutput= open('./train.dat', 'wb')
#Foutput= open('./output.txt', 'w')
data=Finput.read().split(",")
#词频截断
data=list(filter(lambda x: int(x)<4096 , data))
npdata=np.asarray(data,dtype=np.int)
total=npdata.shape[0]
window_size=24+1
finaldata=np.zeros((total-window_size,window_size),dtype=np.int)
for i in range(total-window_size):
    finaldata[i]=npdata[i:i+window_size]
pickle.dump(finaldata,Foutput)
Finput.close()
Foutput.close()
print("搞定")

