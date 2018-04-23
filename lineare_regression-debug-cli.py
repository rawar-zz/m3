
# coding: utf-8

# In[1]:


import tensorflow as tf
from tensorflow.python import debug as tf_debug
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[2]:


FILENAME = "./data/fire_theft.csv"


# In[3]:


N_EPOCHS = 500


# In[4]:


LEARNING_RATE=0.001


# In[5]:


df=pd.read_csv(FILENAME)


# In[6]:


data = df.as_matrix()


# In[7]:


x = tf.placeholder(tf.float32, name="X")
y = tf.placeholder(tf.float32, name="Y")


# In[8]:


w = tf.Variable(0.0, name="weights") 
b = tf.Variable(0.0, name="bias")


# In[9]:


w_h = tf.summary.histogram("weights", w)
b_h = tf.summary.histogram("biases", b)


# In[10]:


with tf.name_scope("Wx_b") as scope:
    # y_predicted = tf.mul(w, tf.add(x, b))
    y_predicted = w * x + b


# In[11]:


with tf.name_scope("cost_function") as scope:
    cost = tf.reduce_mean(tf.square(y - y_predicted), name="cost")
    tf.summary.scalar("cost", cost)
    #loss = tf.square(y - y_predicted, name="loss")


# In[12]:


with tf.name_scope("train") as scope:
    optimizer = tf.train.GradientDescentOptimizer(learning_rate=LEARNING_RATE)
    train_op = optimizer.minimize(cost, name="train_op")


# In[13]:


init_op = tf.global_variables_initializer()


# In[14]:


training_costs = []


# In[15]:


model_saver = tf.train.Saver() 


# In[16]:


merged_summary_op = tf.summary.merge_all()


# In[ ]:


with tf.Session() as s:
    s.run(init_op)
    #s = tf_debug.TensorBoardDebugWrapperSession(s, 'localhost:6064')
    s = tf_debug.LocalCLIDebugWrapperSession(s)
    summary_writer = tf.summary.FileWriter('./regressions-modell-log', s.graph)
    for e in range(N_EPOCHS):
        for x_data,y_data in data:
            #print('x=%4f,y=%4f' % (x_data,y_data))
            c, _ = s.run([cost, train_op], feed_dict={x: x_data, y:y_data})
            summary_str = s.run(merged_summary_op, feed_dict={x: x_data, y: y_data})
            summary_writer.add_summary(summary_str, e)
            #training_costs.append(c)
        if not e % 100:
            print('epoche: %4d, cost: %4f' % (e,c))
    w_value, b_value = s.run([w, b])
    print('w_value = %4f, b_value = %4f' % (w_value, b_value))
    save_path = model_saver.save(s, "./regressions-modell.ckpt")
    print("Das Modell ist in : %s gespeichert" % save_path)

