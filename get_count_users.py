import json

def get_count_users(data:dict) -> int:
    """
    You are given dictionary. Find the number of users.

    Args:
        data(dict): data
    Returns:
        int: number of users
    """
    f=open(data).read()
    d=json.loads(f)["results"]
    c=0
    for i in d: 
        k=(i["name"]["last"])
        c+=1
    return c

data = "randomuser_data.json"
total = get_count_users(data)
print(total)

    
