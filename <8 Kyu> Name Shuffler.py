'''

Write a function that returns a string in which firstname is swapped with last name.

name_shuffler('john McClane'); => "McClane john"

'''


def name_shuffler(str_):
    return str_[str_.find(" ")+1:] + " " + str_[0:str_.find(" ")]#your code here
