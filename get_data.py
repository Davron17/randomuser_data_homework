import json

def get_data(filename:str) -> dict:
    """
    You are given a filename. Read the JSON data from the file and return the dictionary.

    Args:
        filename(str): file name
    Returns:
        dict: JSON data
    """
    f=open(data).read()
    d=json.loads(f)
    
    return d

data = "randomuser_data.json"
total = get_data(data)
print(total)
