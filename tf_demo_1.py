#!/usr/bin/python2
# -*-coding:utf-8-*-



import tensorflow as tf
def variable():
    state = tf.Variable(0,name = 'connter')

    one  = tf.constant(1)


    new_value = tf.add(state, one)
    update = tf.assign(state,new_value)

    init = tf.initialize_all_variables() #must have if dedine variable

    with tf.Session() as sess:
        sess.run(init)
        for _ in range(3):
            sess.run(update)
            print(sess.run(state))





def placeholder():


    input1 = tf.placeholder(tf.float32)
    input2 = tf.placeholder(tf.float32)


    output = tf.multiply(input1,input2)

    with tf.Session() as seas:
        #placeholder
        print(seas.run(output,feed_dict={input1:[7.],input2:[3.]}))




# activation function(deep learning)
# 激励函数是可以微分
# 某一部分的神经元会被激活，

# def actevationfun():




def demo():

    import tkinter as tk

    window = tk.Tk()
    window.title('my window')
    window.geometry('200x100')

    var = tk.StringVar()
    l = tk.Label(window, textvariable=var, bg='green', font=('Arial', 12), width=15,
                 height=2)
    #l = tk.Label(window, text='OMG! this is TK!', bg='green', font=('Arial', 12), width=15, height=2)
    l.pack()

    on_hit = False
    def hit_me():
        global on_hit
        if on_hit == False:
            on_hit = True
            var.set('you hit me')
        else:
            on_hit = False
            var.set('')

    b = tk.Button(window, text='hit me', width=15,
                  height=2, command=hit_me)
    b.pack()


    window.mainloop()


def show_data():
    import matplotlib.pyplot as plt
    import numpy as np


    np.random.seed(0)

    x, y = np.random.randn(2, 100)
    fig = plt.figure()
    ax1 = fig.add_subplot(211)
    ax1.xcorr(x, y, usevlines=True, maxlags=50, normed=True, lw=2)
    ax1.grid(True)
    ax1.axhline(0, color='red', lw=2)

    ax2 = fig.add_subplot(212, sharex=ax1)
    ax2.acorr(x, usevlines=True, normed=True, maxlags=50, lw=2)
    ax2.grid(True)
    ax2.axhline(0, color='green', lw=2)

    plt.show()


show_data()