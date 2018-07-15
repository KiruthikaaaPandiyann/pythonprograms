def is_number(s):
    try:
        float(s)
        return("Yes")
    except ValueError:
        return("No")
s=input()
print(is_number(s))
