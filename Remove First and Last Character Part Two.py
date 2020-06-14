# You are given a list of character sequences as a comma separated string. 
# Write a function which returns another string containing all the character sequences 
# except the first and the last ones, separated by spaces. If the input string is empty, or the removal of the first and last items would cause the string to be empty, return a null value.

def array(string):
    return string[string.find(',')+1:string.rfind(',')].replace(",", " ") if string.count(',')>=2 else None
