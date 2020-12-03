import os

path = "./HPWREN-FIgLib-Data"
# NOTE: this counts folders themselves as files, which isn't great, so count will be inflated by the number of subfolders
num_files = sum([len(files) for r, d, files in os.walk(path)])
print("{} files in {}".format(num_files, path))
