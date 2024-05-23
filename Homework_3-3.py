def test_(*args, **kwargs):
        print(*args, kwargs)

test_(77, 99, {88, 66}, [33, 44], 'Text', name1 = 'Oleg', name2 = 'Ivan')

def factor_(n: int):
    if n == 1:
        return n
    else:
        return n * factor_(n-1)

print (factor_(5))