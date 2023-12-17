import random


if __name__ == "__main__":
    print("Type in the name of the Persons")
    persons = input().split()
    personNumber = len(persons)
    print("select number of Teammembers")
    pairs = int(input())
    residue = personNumber % pairs;
    numberOfTeams = int(personNumber / pairs)
    teamnumber = 0;
    for x in range(personNumber-1, -1, -1):
        if(x == personNumber-1 and personNumber % pairs != 0):
            print("Residue: ")
        if ((x+1) % pairs == 0):
            teamnumber = teamnumber + 1;
            print(f"Team Nummer: {teamnumber}")
        print(persons.pop(random.randint(0,x)))