import os
import numpy as np
import pandas as pd
import tensorflow as tf

(X_train, y_train), (X_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()

os.makedirs("data/raw", exist_ok=True)

X_train_flat = X_train.reshape(X_train.shape[0], -1)
X_test_flat = X_test.reshape(X_test.shape[0], -1)

pd.DataFrame(X_train_flat).to_csv("data/raw/X_train.csv", index=False)
pd.DataFrame(y_train).to_csv("data/raw/y_train.csv", index=False)
pd.DataFrame(X_test_flat).to_csv("data/raw/X_test.csv", index=False)
pd.DataFrame(y_test).to_csv("data/raw/y_test.csv", index=False)
