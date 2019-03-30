""" Module Title.

here is the description of the module.
This is shown with the help function
"""

class TestClass:
    """ The TestClass is to show docstring for Classes.

    Some detailed description of the class goes here, right after
    the class statement. Again, first line is for the title
    """

    def __init__(self):
        """ The Constructor

        This is the parameterless constructor of the class
        """

    def theAnswer(self):
        """ The Answer function

        It returns the answer to anything, you do not even need
        to pass a question
        """
        return("41")

    @staticmethod
    def theStaticAnswer():
        """ The static Answer function

        It returns the answer to anything, you do not even need
        to pass a question.
        It is a static function, hence it needs no self parameter
        """
        return("41")


if __name__ == "__main__":
    tc = TestClass()
    
    print(tc.theAnswer())
    print(TestClass.theStaticAnswer())

    # Print the docstring for the theAnswer function
    print(TestClass.theAnswer.__doc__)

    # print the docstring for the TestClass class
    print(TestClass.__doc__)

    # The docstring for the module could be displayed by
    #   import docstring
    #   help(docstring)
