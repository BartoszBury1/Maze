
import queue
import time



def createLab():
    Lab = []
    Lab.append(["#","#", "#", "#", "#", "S", "#", "#", "#"])
    Lab.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    Lab.append(["#"," ", "#", " ", " ", " ", "#", " ", "#"])
    Lab.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    Lab.append(["#"," ", "#", " ", "#", "#", "#", " ", "#"])
    Lab.append(["#"," ", " ", " ", " ", "#", " ", " ", "#"])
    Lab.append(["#"," ", "#", "#", " ", " ", " ", " ", "#"])
    Lab.append(["#"," ", " ", "#", " ", "#", "#", " ", "#"])
    Lab.append(["#","#", "#", "#", "#", "#", "#", "F", "#"])

    return Lab


def printLab(Lab, path=""):
    for x, pos in enumerate(Lab[0]):
        if pos == "S":
            start = x

    i = start
    j = 0
    pos = set()
    for move in path:
        if move == "L":
            i -= 1

        elif move == "P":
            i += 1

        elif move == "G":
            j -= 1

        elif move == "D":
            j += 1
        pos.add((j, i))
    
    for j, row in enumerate(Lab):
        for i, col in enumerate(row):
            if (j, i) in pos:
                print("^ ", end="")
            else:
                print(col + " ", end="")
        print()
        


def valid(Lab, moves):
    for x, pos in enumerate(Lab[0]):
        if pos == "S":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "P":
            i += 1

        elif move == "G":
            j -= 1

        elif move == "D":
            j += 1

        if not(0 <= i < len(Lab[0]) and 0 <= j < len(Lab)):
            return False
        elif (Lab[j][i] == "#"):
            return False

    return True


def findEnd(Lab, moves):
    for x, pos in enumerate(Lab[0]):
        if pos == "S":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "P":
            i += 1

        elif move == "G":
            j -= 1

        elif move == "D":
            j += 1

    if Lab[j][i] == "F":
        printLab(Lab, moves)
        print("Wykonane Ruchy: " +moves)
        return True

    return False


num = queue.Queue()
num.put("")
add = ""
Lab  = createLab()

while not findEnd(Lab, add): 
    add = num.get()
    #print(add)
    for j in ["L", "P", "G", "D"]:
        put = add + j
        if valid(Lab, put):
            num.put(put)



            