from model import *
from dataload import *
from const import *
import numpy as np
dics=pickle.load(open('./dic.dat', 'rb'))
dic=dics[0]
reverse_dic=dics[1]
def sample(sess,out_len,warm_len=C_window_size*2,startwith=None):
    Memory=np.zeros((1,C_window_size+warm_len+out_len+1),dtype=np.int)
    #随机初始化
    Memory[0,:C_window_size]=np.random.randint(0, high=C_cut_off, size=C_window_size, dtype=np.int)
    #RNN-Style-gen
    for i in range(C_window_size,C_window_size+warm_len+out_len):
        next_char=sess.run(soft_prediction,feed_dict={Input:Memory[::,i-C_window_size:i+1]})
        Memory[::,i]=next_char	
    return(Memory[0,C_window_size+warm_len:C_window_size+warm_len+out_len])

def singleimap(w_id):
    if w_id in reverse_dic:
        return str(reverse_dic[w_id])
    else:
        return ""

def write(sess,out_len,warm_len=C_window_size*2):
    ids=sample(sess,out_len,warm_len)
    return "".join(list(map(singleimap,ids)))
    
