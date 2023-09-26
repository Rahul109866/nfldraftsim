def firstnames():
    with open('firstnames.txt', 'r') as namelist:
        names = namelist.readlines()
        first_names = [name.strip() for name in names]
        first_names.sort()
        return first_names
    
def secondnames():
    with open('secondnames.txt', 'r') as namelist:
        names = namelist.readlines()
        second_names = []
        
        for name in names:
            if not name == "\n":
                a = name.strip().split(" ")
                second_names.append(a[1])
        second_names.sort()
        return second_names
        
    
        
        
