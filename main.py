from pythonds.basic import Stack


def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
            print(f"the symbol {symbol}\nat index {index} \nhas been added to the stack\n {s.__str__} \n")
        else:
            if s.isEmpty():
                balanced = False
                print("line 16 stack is empty")
            else:
                top = s.pop()
                print(f"the symbol {top} \nhas been removed from the stack")
                #print(s)
                print("\n")
                if not matches(top, symbol):
                    balanced = False
                    print("line 22 stack is not balanced")
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open, close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)


print(parChecker('{({([][])}())}'))
print(parChecker('[{()]'))
