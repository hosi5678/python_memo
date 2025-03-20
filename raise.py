# raiseによる例外の発生

# def f():
#     raise Exception("error message")
  
# try:
#     f()
# except Exception as e:
#     print(e)
#     print(type(e))
#     print(e.args)
#     print(e.with_traceback)

def func(sw:int)-> None:
    if sw==1:
        raise ValueError("invalid value")
    elif sw==0:
        raise ZeroDivisionError("zero division")
    else:
        raise Exception("unknown error")

try:
    func(0)
except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print("no exception")
finally:
  pass
