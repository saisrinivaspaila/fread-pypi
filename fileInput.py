import os


def getInputsAsFile(mainFilePath, inputFilePath):
    with open('input.txt', 'a') as f:
        f.write('\n')
    with open(mainFilePath) as f:
        script = "fileOpenAsInput = open('"+inputFilePath+"')\n"
        c = f.readline()
        while c != '':
            if "getInputsAsFile" in c:
                c = f.readline()
                continue
            if "input()" in c:
                c = c.replace("input()", "fileOpenAsInput.readline()[:-1]")
            elif "sys.stdin.readline()" in c:
                c = c.replace("sys.stdin.readline()",
                              "fileOpenAsInput.readline()[:-1]")
            script += c
            c = f.readline()
        exec(script)
    exit()
