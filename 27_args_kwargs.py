'''
*args vs **kwargs

Syntax                               Stores data as                                      Example

*args                                  Tuple                                     ("Python", "Java")

**kwargs                               Dictionary                              {"name": "Vipul", "age": 22}
'''
def details(*args, **kwargs):
    print(args)
    print(kwargs)

details("Python", "DSA", name="Vipul", age=22)

def test(*args, **kwargs):
    print(args[1])
    print(kwargs["course"])

test("Python", "Java", "C++", course="DSA", level="Beginner")