#!/usr/bin/env python3

import os
import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL'] = "2"

hello = tf.constant('TensorFlow')

print("Hello {} {}!".format(hello.numpy().decode('utf-8'), tf.version.VERSION))
