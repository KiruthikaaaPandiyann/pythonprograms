def is_number(s):
    try:
        float(s)
        return("yes")
    except ValueError:
        return("no")
s=input()
print(is_number(s))
