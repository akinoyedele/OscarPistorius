import json
from re import sub, match, findall
from collections import Counter
from csv import reader
from urllib import urlopen

data = []
with open('OscarTrial327.json') as f:
    for line in f:
        data.append(json.loads(line))

tweets = []
for t in data:
    tweets.append(t['created_at']+ " " + t["user"]["screen_name"] + " " + t['text'])


#A series of regular expressions to divide the tweets into time periods. Note: Twitter timestamps the data in GMT.

six = []
sixfif = []
sixthirty = []
sixforty = []
seven = []
sevenfif = []
seventhirty = []
sevenforty = []
eight = []


for t in tweets:

    if match("^Fri Mar 28 06:(0[0-9]|1[0-4])",t):
        six.append(t)

    if match("^Fri Mar 28 06:(1[5-9]|2[0-9])",t):
        sixfif.append(t)

    if match("^Fri Mar 28 06:(3[0-9]|4[0-4])",t):
        sixthirty.append(t)

    if match("^Fri Mar 28 06:(4[5-9]|5[0-9])",t):
        sixforty.append(t)

    if match("^Fri Mar 28 07:(0[0-9]|1[0-4])",t):
        seven.append(t)

    if match("^Fri Mar 28 07:(1[5-9]|2[0-9])",t):
        sevenfif.append(t)

    if match("^Fri Mar 28 07:(3[0-9]|4[0-4])",t):
        seventhirty.append(t)

    if match("^Fri Mar 28 07:(4[5-9]|5[0-9])",t):
        sevenforty.append(t)

    if match("^Fri Mar 28 08:(0[0-9]|1[0-4])",t):
        eight.append(t)




print len(six), len(sixfif), len(sixthirty), len(sixforty), len(seven), len(sevenfif), len(seventhirty), len(sevenforty), len(eight), len(data)


    

    


