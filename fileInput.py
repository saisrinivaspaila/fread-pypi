import os


def getInputsAsFile(main, inputFile):
    with open('input.txt', 'a') as f:
        f.write('\n')
    with open(main) as f:
        script = "fileOpenAsInput = open('"+inputFile+"')\n"
        c = f.readline()
        while c != '':
            if "getInputsAsFile" in c:
                c = f.readline()
                continue
            if "time" in c:
                c = f.readline()
                continue
            if "input()" in c:
                c = c.replace("input()", "fileOpenAsInput.readline()[:-1]")
            script += c
            c = f.readline()
        exec(script)
    exit()
