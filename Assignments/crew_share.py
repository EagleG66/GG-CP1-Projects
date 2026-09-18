#GLENN GUDMUNSON crew share

import random

unit_total = random.randint(500,5000)

while True:
    try:
        pirates = int(input("How many pirates are on the ship: "))
    except:
        print("THAT'S NOT AN INTEGER YOU IDIOT!!!")
    else:
        if pirates >= 2:
            break
        else:
            print("THERE MUST BE AT LEAST TWO, YONDU AND QUILL!!! YOU DUMB DUMB!!!")
    

unit_total_aft = unit_total - (pirates - 2) * 3

yondu_share = round(unit_total_aft * 0.13, 2)
quill_share = round((unit_total_aft - yondu_share) * 0.11, 2)
crew_share = round(((unit_total_aft - quill_share) - yondu_share) / pirates, 2)

yondu_share = round(yondu_share + crew_share, 2)
quill_share = round(quill_share + crew_share, 2)

print(f"Total units: {unit_total} \nYondu's share: {yondu_share} \nQuill's share: {quill_share} \nCrew's share: {crew_share}")