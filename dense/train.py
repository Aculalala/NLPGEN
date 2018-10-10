from model import *
from dataload import *
from const import *
from exetime import *
import sample
config = tf.ConfigProto(allow_soft_placement=True)
config.gpu_options.allow_growth=True
with tf.Session(config=config) as sess:
    sess.run([tf.global_variables_initializer(),tf.local_variables_initializer()])
    total_batch=int(dataset.shape[0]/C_batch_size)
    stat=np.zeros(total_batch)
    while(True):
        shuffle_data()
        for epoch in range(100000):
            for i in range(total_batch):
                def iteration():
                    batch=dataset[i*C_batch_size:(i+1)*C_batch_size]
                    LOSS,_=sess.run([loss,train],feed_dict={Input:batch,ss:0.001})
                    stat[i]=LOSS
                iteration()
            print("Epoch:%d Loss:%f"%(epoch,np.mean(stat)))
            print(sample.write(sess,32))
            if(epoch%5==0):
                open('./results/'+str(epoch)+'.txt', 'w').write(sample.write(sess,1000))
