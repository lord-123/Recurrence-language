function = "f = lambda n:"

seed = 0

tokens = {
    "n": "n",
    
    "b": "f(n-1)",
    "c": "f(n-2)",
    "d": "f(n-3)",

    "A": "(n)",
    "B": "(n-1)",
    "C": "(n-2)",
    "D": "(n-3)",

    "+": "1 + 1",

    "1": "1 if n > 1 else 1"
}

for i in input("program: "):
    function += tokens[i] + "*"

    print(f"token: {i}\nfunction: {function}")

function = function[:-1]
print(function)

exec(function)
print(f(int(input())))
