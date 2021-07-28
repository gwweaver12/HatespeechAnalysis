import os
from bs4 import BeautifulSoup
import pickle

# name = "c6cdd5281ff44612a993d59002529ae0"
# name = "00000fc2fb034a6f8e2d2d7f947201f5"

def process_file(soup):
    # initialize the dictionary
    dictionary = dict()

    # get text
    text = []
    content = soup.body.find_all("div", attrs={'class', "card--body"})
    for c in content:
        text.append(c.p.text)
    dictionary["text"] = text

    # get actions
    actions = soup.body.find_all('div', attrs={'class', "pa--item--wrapper"})
    for action in actions:
        cnt_type = action.img['alt'].lower()
        cnt = action.span.text
        if "comment" in cnt_type:
            dictionary["comments"] = cnt
        elif "echoes" in cnt_type:
            dictionary["echoes"] = cnt
        elif "upvotes" in cnt_type:
            dictionary["upvotes"] = cnt
        else:
            raise Exception("Unknown count type: " + cnt_type)

    # get the date
    time_stamp = soup.body.find('span', attrs={"class", "post--timestamp" }).text
    dictionary["time"] = time_stamp
    dictionary["filename"] = name

    return dictionary

pref = 'C:/Users/Weave/Downloads/parler_2020-01-06_posts-partial/'
outfile_name = pref + "output.pickle"

filelist = open(pref + 'parler_2020-01-06_posts-partial.zip.filelist.txt', 'r')
outfile = open(outfile_name, 'wb')

output = []

for filename in filelist:
    name = filename.split('\n')[0]
    file = open(pref + name)
    soup = BeautifulSoup(file)
    file.close()

    try:
        proc_dict = process_file(soup)
        output.append(proc_dict)
        print(proc_dict)
    except:
        pass

print(len(output))
pickle.dump(output, outfile)
outfile.close()
