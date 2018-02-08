# -*- coding: utf-8 -*-


import tensorflow as tf
import os
import numpy as np
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

n_features = 10
n_dense_neurons = 3

x = tf.placeholder(tf.float32,(None,n_features))
W = tf.Variable(tf.random_normal([n_features,n_dense_neurons]))
b = tf.Variable(tf.ones([n_dense_neurons]))

xW = tf.matmul(x,W)
z = tf.add(xW,b)

a= tf.sigmoid(z);

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
layer_out = sess.run(a,feed_dict={x:np.random.random([1,n_features])})
tf.summary.FileWriter('./logs',sess.graph)
print(layer_out)
