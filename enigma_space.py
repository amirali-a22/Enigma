import pickle

alphabets = "abcdefghijklmnopqrstuvwxy z,."

f = open('todays_roters_space.enigma', 'rb')
roter1, roter2, roter3, roter4, roter5 = pickle.load(f)


# print(roter1)
# print(roter2)
# print(roter3)
# print(roter4)
# print(roter5)


def reflector(char):
    """" This function reflect the entry character"""
    return alphabets[len(alphabets) - alphabets.find(char) - 1]


def enigma(char, roter_1, roter_2, roter_3):
    """" This function do the job of Enigma device """
    char1 = roter_1[alphabets.find(char)]
    # print(f"char1-{char1}-")
    char2 = roter_2[alphabets.find(char1)]
    # print(f"char2-{char2}-")
    char3 = roter_3[alphabets.find(char2)]
    # print(f"char3-{char3}-")
    reflected = reflector(char3)
    # print(f"reflected-{reflected}-")
    char3 = alphabets[roter_3.find(reflected)]
    # print(f"char3-{char3}-")
    char2 = alphabets[roter_2.find(char3)]
    # print(f"char2-{char2}-")
    char1 = alphabets[roter_1.find(char2)]
    print(f"char1-{char1}-")
    return char1


def rotate_roters():
    """ This function rotate the rotors """
    global roter1, roter2, roter3
    roter1 = roter1[1:] + roter1[0]
    if rotates % 29:
        roter2 = roter2[1:] + roter2[0]
    if rotates % 29 * 29:
        roter3 = roter3[1:] + roter3[0]


# plain = "hi my name is amirali, and i wanna learn django."
plain = "ywranbvrx uqxkpeu pqzglpcvydivfbjobwss..nuipcfdk"
# print(len(plain))
cipher = ''

# plain = plain.lower()
# plain.replace(" ", "S")
rotates = 0
for i in plain:
    cipher += enigma(i, roter1, roter4, roter5)
    rotates += 1
    rotate_roters()
print(cipher)

print(len(alphabets))
# enigma("n", roter1, roter2, roter3)
# print(alphabets.find("n"))
# print(reflector(" "))
