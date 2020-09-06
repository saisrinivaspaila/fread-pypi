# fread

Python package to convert the interactive based console to file input based with single statement

---

    Version - 1.0
    Pypi -
    Github - https://github.com/saisrinivaspaila/fread-pypi

### Why to use?

There are people like me, who uses python for competitive programming or for building console bases applications. When I use my local editors I need to enter the code from console everytime. There are ways I can change it to file input based, but for that I need to refactor a lot of code while submissions.
So this package helps you to take inputs directly from files with the same code that we write for interactive console even. With one line we can change the code from interactive console to file based input.

I hope you people find it is usefull.

### How to use?

##### installing

    pip install fread

##### how to use in code

    from fread import get_input
    get_input.fileInput(mainPythonFile, yourInputTextFile)

##### Example

main.py:

    from fread import get_input
    get_input.fileInput("main.py","input.txt")
    n1 = int(input())
    n2 = int(input())
    print("sum:",n1+n2)
    str1 = input()
    print("string:",str1)
    list1 = map(int,input().split())
    print("list:",list1)

input.txt:

    1
    2
    python is love, Happy Coding
    1 2 3 4

output:

    sum: 3
    string: python is love, Happy coding
    list: [1,2,3,4]
