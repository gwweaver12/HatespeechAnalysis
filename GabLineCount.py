import lzma

with lzma.open('C:/Users/Weave/Downloads/Gab/Gab/GABPOSTS_CORPUS.xz', mode='rt') as file:
    num_lines  = sum(1 for line in file)
    print(num_lines)
