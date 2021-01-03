from random import shuffle
import pickle

alphabets = "abcdefghijklmnopqrstuvwxyz,."

shuffle_alphabets = list(alphabets)+[" "]
shuffle(shuffle_alphabets)
roter1 = ''.join(shuffle_alphabets)

shuffle_alphabets = list(alphabets)+[" "]
shuffle(shuffle_alphabets)
roter2 = ''.join(shuffle_alphabets)


shuffle_alphabets = list(alphabets)+[" "]
shuffle(shuffle_alphabets)
roter3 = "".join(shuffle_alphabets)

shuffle_alphabets = list(alphabets)+[" "]
shuffle(shuffle_alphabets)
roter4 = "".join(shuffle_alphabets)

shuffle_alphabets = list(alphabets)+[" "]
shuffle(shuffle_alphabets)
roter5 = "".join(shuffle_alphabets)

f = open("./todays_roters_space.enigma", 'wb')
# pickle.dump((roter1, roter2, roter3), f)
pickle.dump((roter1, roter2, roter3, roter4, roter5), f)
f.close()


print(roter1)
print(roter2)
print(roter3)
print(roter4)
print(roter5)
