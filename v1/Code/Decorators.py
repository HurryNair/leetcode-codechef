def addint(func):
    def inner(*args, **kwargs):
        return int(func(*args, **kwargs))
    return inner()

@addint
def add(n1, n2):
    return n1 + n2

if __name__ == "__main__":
    print(add(2,3.5))