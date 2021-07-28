# import os
# file = open('C:/Users/Weave/Downloads/parler_2020-01-06_posts-partial/$ffff27981a9d4502a8d9b6df04a9f864.txt')
# filename = file.readline()
# while file:
#     count = 0
#     for line in file:
#         count += 1
#         print( line)


import pickle
file = open("C:/Users/Weave/Downloads/parler_2020-01-06_posts-partial/output.pickle", "rb")
all_list = pickle.load(file)
file.close()
print(all_list[0].keys())
key_word = "antifa"
count = 0
upvotes = 0
comments = 0
echoes = 0
bad = 0
for file_dict in all_list:
    for text in file_dict["text"]:
        if key_word in text.lower():
            try:
                upvotes = upvotes+int(file_dict["upvotes"])
                comments = comments+int(file_dict["comments"])
                echoes = echoes + int(file_dict["echoes"])
                count = count + 1
            except:
                bad = bad + 1
                break
print("Word count:", count)
print("Upvote total:", upvotes)
print("Upvotes Avg:", (upvotes/count))
print("Comments total:", comments)
print("Comments Average:", (comments/count))
print("Echoes total:", echoes)
print("Echoes Average:", (echoes/count))
print("Excluded posts", bad)
