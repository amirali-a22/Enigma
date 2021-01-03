import pickle

alphabets = "abcdefghijklmnopqrstuvwxyz"

f = open('todays_roters.enigma', 'rb')
roter1, roter2, roter3, roter4, roter5 = pickle.load(f)


# print(roter1)
# print(roter2)
# print(roter3)
# print(roter4)
# print(roter5)


def reflector(char):
    return alphabets[len(alphabets) - alphabets.find(char) - 1]


def enigma(char, roter_1, roter_2, roter_3):
    char1 = roter_1[alphabets.find(char)]
    char2 = roter_2[alphabets.find(char1)]
    char3 = roter_3[alphabets.find(char2)]
    reflected = reflector(char3)
    char3 = alphabets[roter_3.find(reflected)]
    char2 = alphabets[roter_2.find(char3)]
    char1 = alphabets[roter_1.find(char2)]
    return char1


def rotate_roters():
    global roter1, roter2, roter3
    roter1 = roter1[1:] + roter1[0]
    if rotates % 27:
        roter2 = roter2[1:] + roter2[0]
    if rotates % 27 * 27:
        roter3 = roter3[1:] + roter3[0]


# def rotate_roters(roter_1, roter_2, roter_3):
#     global roter1, roter2, roter3, roter4, roter5
#     roter_1 = roter_1[1:] + roter_1[0]
#     if rotates % 26:
#         roter_2 = roter_2[1:] + roter_2[0]
#     if rotates % 26 * 26:
#         roter_3 = roter_3[1:] + roter_3[0]


# plain = "hihihi"
plain = "ealmos"

cipher = ''

# plain = plain.lower()
# plain.replace(" ", "S")
rotates = 0
for i in plain:
    cipher += enigma(i, roter1, roter3, roter5)
    rotates += 1
    rotate_roters()
print(cipher)
