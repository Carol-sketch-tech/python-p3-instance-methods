# Behaviour of Objects.
# there are a number of ways for us to interact with objects for us to elicit a response.

# 1.Dot Notation.
class Dog:
    pass

fido = Dog()
fido.__dir__()

# when we interact with an object through dot notation, we are calling the variable or funtion that is defined inside of the function.
# we call these attributes and these instance fucntions methods. Unless otherwise specified, all of an objects methods are considered instance methods.
# instance methods can access attributes and modify the attributes of an instance.

# we acces the instance's __dir__ () method by seperating the object fido by the method __dir__ by a dot.


# Building your own instance methods.