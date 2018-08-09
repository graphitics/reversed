import glob

def reverse(directory):
    list = glob.glob(directory, recursive=True)
    for file in list:
        text = open(file, "r")
        print("Loading file " + file)
        temp = text.read()
        text.close()
        text = open("r" + file, "w+")
        text.write(temp[::-1])
        text.close()

dir = "rdata/*.txt"
reverse(dir)
