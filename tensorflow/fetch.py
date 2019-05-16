import tensorflow as tf

i1 = tf.constant(3)
i2 = tf.constant(2)
i3 = tf.constant(5)

intermed = tf.add(i1, i2)
mul = tf.multiply(i1, intermed)

with tf.Session() as sess:
    print(sess.run([mul, intermed]))
