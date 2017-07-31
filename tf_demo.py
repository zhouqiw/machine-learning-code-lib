#!/usr/bin/python2
# -*-coding:utf-8-*-



def main():

 import  tf_demo_1








import tensorflow as tf

with tf.Session() as sess:

    matrix1 =  tf.constant([[3,3]])
    matrix2 =  tf.constant([[2],
                            [2]])
    product = tf.matmul(matrix1,matrix2)

    #mothod 1


    result = sess.run(product)
    print (result)




    print ('nihao python3')





    # variable()
    # placeholder()
    # demo()
    # tf_demo_1.show_data()

if __name__ == '__main__':
    main()