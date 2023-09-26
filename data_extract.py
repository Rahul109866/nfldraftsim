from collections import namedtuple


def firstnames():  # function to extract all first names
    with open("firstnames.txt", "r") as namelist:
        names = namelist.readlines()
        first_names = [name.strip() for name in names]
        first_names.sort()
        return first_names


def secondnames():
    with open("secondnames.txt", "r") as namelist:
        names = namelist.readlines()
        second_names = []

        for name in names:
            if not name == "\n":  # the file has extra newlines b/w each entry
                # each entry is "<num> <name>" so we seperate name and num
                a = name.strip().split(" ")

                second_names.append(a[1])  # get only name
        second_names.sort()
        return second_names


def positions():
    with open("positions.csv", "r") as position_file:
        pos_csv = position_file.readlines()

        positions_offense = [
            position.strip().split(" ")[1]
            for position in pos_csv
            if "offense" in position
        ]
        positions_defense = [
            position.strip().split(" ")[1]
            for position in pos_csv
            if "defense" in position
        ]
        positions_special = [
            position.strip().split(" ")[1]
            for position in pos_csv
            if "special" in position
        ]
        return positions_offense, positions_defense, positions_special


def college():
    with open("colleges.txt", "r") as college_file:
        colleges = college_file.readlines()
        college = namedtuple("college", ["name", "ranking"])

        univ = ("university", "University", "College", "college", "Institute")
        univs = [
            col.strip() for col in colleges if any(keyword in col for keyword in univ)
        ]
        return univs


if __name__ == "__main__":
    print(college())
