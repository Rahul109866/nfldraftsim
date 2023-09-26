def firstnames():  # function to extract all first names
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
            if not name == "\n":  # the file has extra newlines b/w each entry
                # each entry is "<num> <name>" so we seperate name and num
                a = name.strip().split(" ")

                second_names.append(a[1])  # get only name
        second_names.sort()
        return second_names
