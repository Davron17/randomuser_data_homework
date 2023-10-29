import json

def get_email(data:dict) -> list:
    """
    Take the email of the users and return the list.

    Args:
        data(dict): data
    Returns:
        list: users email
    """
    f=open(data).read()
    d=json.loads(f)["results"]
    l=[]
    for i in d:
        l.append(i["email"])
    return l
data = 'randomuser_data.json'
print(get_email(data))