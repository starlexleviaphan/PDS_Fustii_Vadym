import os
def explorer():
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    dirs = [f for f in os.listdir('.') if os.path.isdir(f)]

    for f in files:
        print(f)
    for i in dirs:
        print("|", i, sep="")
    nfiles = len(files)
    ndirs = len(dirs)
    print("files in directory = ", nfiles, "\n", "directories in: ", ndirs)

explorer()