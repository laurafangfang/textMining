# import tensorflow as tf
# state = tf.Variable(0.0,dtype=tf.float32)
# one = tf.constant(1.0,dtype=tf.float32)
# new_val = tf.add(state, one)
# update = tf.assign(state, new_val) #返回tensor， 值为new_val
# update2 = tf.assign(state, 10000)  #没有fetch，便没有执行
# init = tf.initialize_all_variables()
# with tf.Session() as sess:
#     print("sess is ", sess)
#     sess.run(init)
#     for _ in range(3):
#         print (sess.run(update))
# print("state is %s" %state, "one is %s" %one, "new_val is %s" %new_val, "update is %s" %update, "update2 is %s" %update2)


# import tensorflow as tf
# y = tf.Variable(1)
# b = tf.identity(y)
# print("y is %s" %y, "b is : %s" %b)
# with tf.Session() as sess:
#     tf.global_variables_initializer().run()
#     print(sess.run(b,feed_dict={y:3})) #使用3 替换掉
#     #tf.Variable(1)的输出结果，所以打印出来3 
#     #feed_dict{y.name:3} 和上面写法等价

#     print(sess.run(b))  #由于feed只在调用他的方法范围内有效，所以这个打印的结果是 1

import numpy as np

vector1 = np.array([1,2,3])
vector2 = np.array([4,7,5])
op7=np.dot(vector1,vector2)/(np.linalg.norm(vector1)*(np.linalg.norm(vector2)))
print(op7)