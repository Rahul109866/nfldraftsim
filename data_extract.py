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
        lines = college_file.readlines()
        university = namedtuple("university", ["name", "ranking"])

        UNIV_KEYWORDS = ("university", "college", "institute", "academy", "school", "schools")
        universities_list = []

        i = 0
        while i < len(lines):
            player_univ = university(name="", ranking="")
            if any(keyword in lines[i].lower() for keyword in UNIV_KEYWORDS):
                player_univ = university(name=lines[i].strip(), ranking="")

                while i < len(lines):
                    if "NCAA" in lines[i]:
                        player_univ = player_univ._replace(ranking=lines[i].strip())
                        break

                    i += 1
            universities_list.append(player_univ)

            i += 1

        return universities_list


if __name__ == "__main__":
    print(college())
