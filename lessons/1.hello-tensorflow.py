#!/usr/bin/env python3

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import tensorflow as tf

h = tf.constant('Hello, TensorFlow!')
s = tf.compat.v1.Session()

print(s.run(h))
