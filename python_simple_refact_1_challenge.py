# This will be code that reads a file and appends the number of
# charactes it contains in each line. 


with open('README.md') as f:
    t = open('some.txt', 'w')
    for x in f:
        n = x.replace("\n", " ") + " ; " + str(len(x)) + "\n"
        t.write(n)
