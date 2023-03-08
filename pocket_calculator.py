current = 0  # current value in calc as int
restr = ""  # most recent operation performed as str
reint = 0  # most recent argument as int
series = "(0)"  # series of operations performed as str


def get_value():
    global current
    return current


def clear(a=0):
    global restr
    restr = "0"
    global reint
    reint = 0
    global current
    current = a
    global series
    series = str(a)
    return current


def step(astr, bint):
    global restr
    global reint
    global current
    global series
    if astr == "+":
        current = current + bint
        series = "(" + series + ")" + astr + str(bint)
        restr = astr
        reint = bint
        return current
    elif astr == "-":
        current = current - bint
        series = "(" + series + ")" + astr + str(bint)
        restr = astr
        reint = bint
        return current
    elif astr == "*":
        current = current * bint
        series = "(" + series + ")" + astr + str(bint)
        restr = astr
        reint = bint
        return current
    elif astr == "//":
        if bint == 0:
            return "Error"
        current = current // bint
        series = "(" + series + ")" + astr + str(bint)
        restr = astr
        reint = bint
        return current


def repeat():
    global restr
    global reint
    if restr == "":
        return current
    else:
        step(restr, reint)
        return current


def get_expr():
    global series
    return series
