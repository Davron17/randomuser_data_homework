import json

def get_gender_users(data:dict) -> list:
    """
    Take the gender of the users and return the list.
    
    The list items are as follows:
        If the user is male: {"Male":1}
        If the user is female: {"Female":0}
    
    Args:
        data(dict): data
    Returns:
        list: users get gender list
    """
    f=open(data).read()
    d=json.loads(f)["results"]
    l={}
    m={}
    c=0
    g=0
    o=[]
    p=[]
    for i in d:
        if i["gender"]=="male":            
            o.append("male")
            a=len(o)
            
            m["male"]=a

            c+=1
        else:      
            p.append("female")
            b=len(p)
            g+=1
            l["female"]=b
        
            
    return l,m
data = 'randomuser_data.json'
print(get_gender_users(data))