# fread

Python package to convert the interactive based console to file input based, with a single statement.

---

    Version - 1.0
    Pypi - https://pypi.org/project/fread/1.0/
    Github - https://github.com/saisrinivaspaila/fread-pypi

### Why to use?

There are people like me, who use python for competitive programming or for building console based applications. When I use my local editors, I need to enter the code from the console everytime. There are ways I can change it to file input based, for which I need to refactor a lot of code during submissions.
So this package helps us to take inputs directly from files with the same code that we write for interactive console. With one line command, we can change the code from interactive console to file based input.

I hope you people will find it is useful.

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
