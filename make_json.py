import numpy as np
import glob

files = glob.glob("*.png")

with open("desnames.json", "w") as f:
    f.write("[\n")
    for i,fl in enumerate(files):
        if i == len(files)-1:
            f.write('  "%s"\n'%fl.split(".")[0])
        else:
            f.write('  "%s", \n'%fl.split(".")[0])

    f.write("]")
