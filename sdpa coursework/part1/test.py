import pickle
import os

data = {"1": "123"}
filepath = os.path.join(os.getcwd(), "allusers.txt")
f = open(filepath, "wb")
pickle.dump(data, f)
f.close()