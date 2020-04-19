import pymongo

client = pymongo.MongoClient('localhost', 27017)
db = client['gym-trainer']
exercise_collection = db['exercises']

data = {
    'beginner': {'chest': ["Barbell Bench Press%4%8",
                           "Machine Chest Press%4%10",
                           "Cable Fly%4%10"],
                 'back': ["Lat-pulldowns%4%10",
                          "T-Bar Row%4%10",
                          "Close-Grip Pulldowns%4%12"],
                 'shoulders': ["Seated Dumbbell Press%4%10",
                               "Lateral Raises%3%20",
                               "EZ Bar Upright Rows%3%15"],
                 'legs': ["Leg Extensions%4%10",
                          "Leg Press Machine%4%8",
                          "Lunges%3%10"],
                 'biceps': ["Barbell Bbicep Curls%3%10",
                            "EZ Bar Curls%4%10",
                            "Hammer Curls%3%12"],
                 'tricep': ["Barbell Bench Press%4%8",
                            "Machine Chest Press%4%10",
                            "Cable Fly%4%10"],
                 'abdomen': ["Lat-pulldowns%4%10",
                             "T-Bar Row%4%10",
                             "Close-Grip Pulldowns%4%12"],
                 'forearms': ["Seated Dumbbell Press%4%10",
                              "Lateral Raises%3%20",
                              "EZ Bar Upright Rows%3%15"]},
    'intermediate': {'chest': ["Barbell Bench Press%4%8",
                               "Machine Chest Press%4%10",
                               "Cable Fly%4%10"],
                     'back': ["Lat-pulldowns%4%10",
                              "T-Bar Row%4%10",
                              "Close-Grip Pulldowns%4%12"],
                     'shoulders': ["Seated Dumbbell Press%4%10",
                                   "Lateral Raises%3%20",
                                   "EZ Bar Upright Rows%3%15"],
                     'legs': ["Leg Extensions%4%10",
                              "Leg Press Machine%4%8",
                              "Lunges%3%10"],
                     'biceps': ["Barbell Bbicep Curls%3%10",
                                "EZ Bar Curls%4%10",
                                "Hammer Curls%3%12"],
                     'tricep': ["Barbell Bench Press%4%8",
                                "Machine Chest Press%4%10",
                                "Cable Fly%4%10"],
                     'abdomen': ["Lat-pulldowns%4%10",
                                 "T-Bar Row%4%10",
                                 "Close-Grip Pulldowns%4%12"],
                     'forearms': ["Seated Dumbbell Press%4%10",
                                  "Lateral Raises%3%20",
                                  "EZ Bar Upright Rows%3%15"]},
    'pro': {'chest': ["Barbell Bench Press%4%8",
                      "Machine Chest Press%4%10",
                      "Cable Fly%4%10"],
            'back': ["Lat-pulldowns%4%10",
                     "T-Bar Row%4%10",
                     "Close-Grip Pulldowns%4%12"],
            'shoulders': ["Seated Dumbbell Press%4%10",
                          "Lateral Raises%3%20",
                          "EZ Bar Upright Rows%3%15"],
            'legs': ["Leg Extensions%4%10",
                     "Leg Press Machine%4%8",
                     "Lunges%3%10"],
            'biceps': ["Barbell Bbicep Curls%3%10",
                       "EZ Bar Curls%4%10",
                       "Hammer Curls%3%12"],
            'tricep': ["Barbell Bench Press%4%8",
                       "Machine Chest Press%4%10",
                       "Cable Fly%4%10"],
            'abdomen': ["Lat-pulldowns%4%10",
                        "T-Bar Row%4%10",
                        "Close-Grip Pulldowns%4%12"],
            'forearms': ["Seated Dumbbell Press%4%10",
                         "Lateral Raises%3%20",
                         "EZ Bar Upright Rows%3%15"]}
}

for difficulty in data:
    for body_part in data[difficulty]:
        for exercise in data[difficulty][body_part]:
            details = exercise.split("%")

            name = details[0]
            sets = details[1]
            reps = details[2]

            data_push = dict({
                "difficulty": difficulty,
                "bodyPart": body_part,
                "exercise": name,
                "sets": sets,
                "reps": reps,
                "numberOfVotes": 0,
                "likes": 0
            })

            exercise_collection.insert_one(data_push)
