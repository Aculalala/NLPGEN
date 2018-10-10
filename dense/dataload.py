import pickle
import numpy as np
dics=pickle.load(open('./dic.dat', 'rb'))
dic=dics[0]
reverse_dic=dics[1]
dataset=pickle.load(open('./train.dat', 'rb'))
def shuffle_data():
    global dataset
    np.random.shuffle(dataset)
