import re,collections
import pickle
import numpy as np
import tensorflow as tf
from const import *
ss=tf.placeholder(tf.float32)
Input=tf.placeholder(tf.int32, [None,C_window_size+1])
X = Input[::,:C_window_size]
Y = Input[::,-1]
Y_hot=tf.one_hot(
    Y,
    depth=C_cut_off,
    axis=1,
)
#词嵌入
WE_matrix=tf.get_variable(name='WEM',shape=(C_cut_off,C_WE_dim),dtype=tf.float32,trainable=True)
WE=tf.gather(WE_matrix,X)
#简单全连接处理
FC=tf.reshape(WE,(-1,C_window_size*C_WE_dim))
for i in range(3):
    FC=tf.layers.dense(FC,2048,activation=tf.nn.relu)
output=tf.layers.dense(FC,C_cut_off)
prediction=tf.argmax(output, 1)
loss=tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(
    labels=Y_hot,
    logits=output,
))

train=tf.train.AdamOptimizer(learning_rate=ss).minimize(loss)
