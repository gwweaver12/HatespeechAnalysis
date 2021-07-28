import pandas as pd
import xlrd
import time

with lzma.open('C:/Users/Weave/Downloads/Gab/Gab/GABPOSTS_CORPUS.xz', mode='rt') as file:

    start = time.time()
    line_cnt = 1
    data = []
    for line in file:
        tweet = {}

        for entry in line.split(","):
            key = ''
            if '"body"' in entry:
                key = entry.lower()
            if '"type"' in entry:
                key = entry.split("{")[2]
            if '"dislike_count"' in entry:
                key = entry
            if '"like_count"' in entry:
                key = entry
            if '"id"' in entry and '{' not in entry:
                key = entry

            if key != '':
                words = key.split(':')
                tweet[words[0][1:-1]] = words[1]

        data.append(tweet)
        #print(tweet)
        # if line_cnt > 250:
        #     break
        # line_cnt = line_cnt + 1

    bad_word = '1488'
    cnt = 0
    dislike_cnt = 0
    like_cnt = 0
    bad_word_list = []
    for tweet in data:
        if bad_word in tweet['body']:
            bad_word_list.append(tweet)
            #print(tweet['body'])
            cnt = cnt + 1
            dislike_cnt = dislike_cnt + int(tweet['dislike_count'])
            like_cnt = like_cnt + int(tweet['like_count'])

    print(bad_word_list)
    print(len(bad_word_list))
    print(dislike_cnt)
    print(like_cnt)

    end = time.time()
    print('time', end-start)