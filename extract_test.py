from collections import namedtuple


def college():
    with open("colleges.txt", "r") as college_file:
        lines = college_file.readlines()

        # Define the namedtuple for colleges
        College = namedtuple("College", ["name", "ranking"])

        univ = ("university", "University", "College", "college", "Institute")

        i = 0
        while i < len(lines):








if __name__ == "__main__":
    print(college())
