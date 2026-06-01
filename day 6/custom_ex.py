class InvalidAgeError(Exception):
    """checks for age validity"""

    def __init__(self, age, *args):
        super().__init__(*args)
        self.age = age

    def __str__(self):
        return f"Age: {self.age} is not valid for voting"
    

