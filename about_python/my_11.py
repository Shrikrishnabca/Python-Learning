import random

wicket_kipper = ["Ryan Rickelton", "Nicholas Pooran", "Rishabh Pant"]
bats_man = ["Mitchell Marsh", " Abdul Samad", "Ayush Badoni", "D Miller",
            "Rohit Sharma", "Suryakumar Yadav", "Tilak Varma", ""]
all_rounder = ["Shardul Thakur", "Aiden Markram",
               "Hardik Pandya", "santnar", ]
bowler = ["Prince Yadav", "Ashwani Kumar", "Trent Boult", "Bumra", "D chahar", ]
for i in range(13):
    team_11 = list()
    team_11.append(random.choices(wicket_kipper,k=1))
    team_11.append(random.choices(bats_man, k=4))
    team_11.append(random.choices(all_rounder, k=3))
    team_11.append(random.choices(bowler, k=3))
    print(team_11)

