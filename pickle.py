import pickle

dict1 = {"a": 1, "b": 2, "c": 3, "d": 4}

pickle_file = open("pickle.txt", "wb")

pickle.dump(dict1, pickle_file)

pickle_file = open("pickle.txt", "r")
new_dict = pickle.load(pickle_file)

print(new_dict)
