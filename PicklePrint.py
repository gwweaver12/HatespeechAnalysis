import pickle
file = open("C:/Users/Weave/Downloads/parler_2020-01-06_posts-partial/output.pickle", "rb")
all_list = pickle.load(file)
print(len(all_list))