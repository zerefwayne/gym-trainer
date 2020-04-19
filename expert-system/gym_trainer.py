from experta import *


class Num_hours_per_day(Fact):
    pass


def print_detail(sets, exc):
    if exc == "":
        return ""
    temparray = exc.split('%')
    num = round(int(temparray[1]) * sets)
    if num == 0:
        return ""
    temparray[1] = str(num)
    return temparray


current_fitness = -1
bmi = -1
goal_fitness = -1
rep_multiplier = -1
hr = -1
beginner_data = {}
intermediate_data = {}
pro_data = {}

response = dict({
    'data': {},
    'workouts': []
})

workouts = []


class gym_train(KnowledgeEngine):
    # all the rules and facts are here
    @DefFacts()
    def symptoms(self):
        yield Fact(action="det_current")
        yield Fact(action="det_goal")
        yield Fact(action="det_reps")

    @Rule(Fact(action='det_current'),
          AS.bmi << Fact(symptom=L("BMI24") | L("BMI23") |
                                 L("BMI22") | L("BMI21") | L("BMI20")))
    def det_bmi1(self):
        global current_fitness
        #         print("MY bmi is :" + str(bmi))
        current_fitness = 15

    @Rule(Fact(action='det_current'),
          AS.bmi << Fact(symptom=L("BMI19") | L("BMI18") |
                                 L("BMI17") | L("BMI16") | L("BMI15")))
    def det_bmi2(self):
        global current_fitness
        #         print("MY bmi is :" + str(bmi))
        current_fitness = 15 - (20 - bmi) * 0.7

    @Rule(Fact(action='det_current'),
          AS.bmi << Fact(symptom=L("BMI25") | L("BMI26") |
                                 L("BMI27") | L("BMI28") | L("BMI29")))
    def det_bmi3(self):
        global current_fitness
        #         print("MY bmi is :" + str(bmi))
        current_fitness = 15 - (bmi - 24) * 0.7

    @Rule(Fact(action='det_current'),
          AS.bmi << Fact(symptom=L("BMI30") | L("BMI31") |
                                 L("BMI32") | L("BMI33") | L("BMI34")))
    def det_bmi4(self):
        global current_fitness
        #         print("MY bmi is :" + str(bmi))
        current_fitness = 15 - (bmi - 24)

    @Rule(Fact(action='det_goal'),
          Fact(symptom="slim"))
    def goal1(self):
        global goal_fitness
        goal_fitness = 18

    @Rule(Fact(action='det_goal'),
          Fact(symptom="ripped"))
    def goal2(self):
        global goal_fitness
        goal_fitness = 20

    @Rule(Fact(action='det_goal'),
          Fact(symptom="fit"))
    def goal3(self):
        global goal_fitness
        goal_fitness = 15

    @Rule(Fact(action='det_reps'),
          AS.hr << Num_hours_per_day(hours=P(lambda x: x > 50) & P(lambda x: x <= 65)))
    def rep1(self):
        global rep_multiplier
        rep_multiplier = 0.75 + (hr - 50) / 60

    @Rule(Fact(action='det_reps'),
          AS.hr << Num_hours_per_day(hours=P(lambda x: x > 35) & P(lambda x: x <= 50)))
    def rep2(self):
        global rep_multiplier
        rep_multiplier = 0.5 + (hr - 35) / 60

    @Rule(Fact(action='det_reps'),
          AS.hr << Num_hours_per_day(hours=P(lambda x: x > 20) & P(lambda x: x <= 35)))
    def rep3(self):
        global rep_multiplier
        rep_multiplier = 0.25 + (hr - 20) / 60

    @Rule(Fact(action='det_reps'),
          AS.hr << Num_hours_per_day(hours=P(lambda x: x > 65) & P(lambda x: x <= 80)))
    def rep4(self):
        global rep_multiplier
        rep_multiplier = 1 + (hr - 65) / 60

    @Rule(Fact(action='det_reps'),
          AS.hr << Num_hours_per_day(hours=P(lambda x: x > 80) & P(lambda x: x <= 95)))
    def rep5(self):
        global rep_multiplier
        rep_multiplier = 1.25 + (hr - 80) / 60

    @Rule(Fact(action='det_reps'),
          AS.hr << Num_hours_per_day(hours=P(lambda x: x > 95) & P(lambda x: x <= 110)))
    def rep6(self):
        global rep_multiplier
        rep_multiplier = 1.5 + (hr - 95) / 60

    @Rule(Fact(action='det_reps'),
          AS.hr << Num_hours_per_day(hours=P(lambda x: x > 110) & P(lambda x: x <= 130)))
    def rep7(self):
        global rep_multiplier
        rep_multiplier = 1.75 + (hr - 110) / 60

    @Rule(Fact(action='det_reps'),
          AS.hr << Num_hours_per_day(hours=P(lambda x: x > 0) & P(lambda x: x <= 20)))
    def rep8(self):
        global rep_multiplier
        rep_multiplier = 0 + (hr - 0) / 80

    @Rule(Fact(level='beginner'))
    def beginner(self):

        global beginner_data
        global workouts

        workouts = []

        count = 0

        for i in range(7):
            if i % 2 == 0:
                workouts.append(dict({"rest": 1}))
            else:
                for u in beginner_data:
                    if count == len(beginner_data[u]):
                        count = 0
                    workouts.append(
                        dict({"rest": 0, "workouts": print_detail(rep_multiplier, beginner_data[u][count])}))
                count += 1

    @Rule(Fact(level='intermediate'))
    def intermediate(self):
        global intermediate_data
        global workouts

        workouts = []

        count = 0

        for i in range(6):
            if i % 4 == 0:
                workouts.append(dict({"rest": 1}))
            else:
                for u in intermediate_data:
                    if count == len(intermediate_data[u]):
                        count = 0
                    workouts.append(
                        dict({"rest": 0, "workouts": print_detail(rep_multiplier, beginner_data[u][count])}))
                count += 1

        workouts.append(dict({"rest": 1}))

    @Rule(Fact(level='pro'))
    def pro(self):
        global pro_data
        global workouts

        workouts = []

        count = 0

        for i in range(6):
            for u in pro_data:
                if count == len(pro_data[u]):
                    count = 0
                workouts.append(dict({"rest": 0, "workouts": print_detail(rep_multiplier, beginner_data[u][count])}))
                count += 1

        workouts.append(dict({"rest": 1}))


def create_fitness_plan(input_data):
    global current_fitness
    global bmi
    global goal_fitness
    global rep_multiplier
    global hr
    global beginner_data
    global intermediate_data
    global pro_data
    global response
    global workouts

    print(input_data)


    engine = gym_train()

    age = int(input_data['age'])

    goal = input_data['goal']

    engine.reset()
    engine.declare(Fact(symptom=goal))
    engine.run()

    bmi = round((int(input_data['weight']) * 100 * 100) / (int(input_data['height']) ** 2))

    engine.reset()
    check = "BMI" + str(bmi)

    response['data']['bmi'] = bmi

    engine.declare(Fact(symptom=check))
    engine.run()

    engine.reset()
    hr = int(input_data['time'])
    engine.declare(Num_hours_per_day(hours=hr))
    engine.run()

    response['data']['current_fitness'] = current_fitness
    response['data']['goal_fitness'] = goal_fitness
    response['data']['rep_multiplier'] = rep_multiplier

    data = {
        'beginner': {'chest': ["beginner Barbell Bench Press – %4% sets of 8 reps",
                               "Machine Chest Press – %4% sets of 10 reps",
                               "Cable Fly – %4% sets of 10 reps"],
                     'back': ["Lat-pulldowns – %4% sets of 10 reps",
                              "T-Bar Row – %4% sets of 10 reps",
                              "Close-Grip Pulldowns – %4% sets of 12 reps"],
                     'shoulders': ["Seated Dumbbell Press – %4% sets of 10 reps",
                                   "Lateral Raises – %3% sets of 20 reps",
                                   "EZ Bar Upright Rows – %3% sets of 15 reps"],
                     'legs': ["Leg Extensions – %4% sets of 10 reps",
                              "Leg Press Machine – %4% sets of 8 reps",
                              "Lunges – %3% sets of 10 reps per leg"],
                     'biceps': ["Barbell Bbicep Curls – %3% sets of 10 reps",
                                "EZ Bar Curls – %4% sets of 10 reps",
                                "Hammer Curls – %3% sets of 12 reps"],
                     'tricep': ["Barbell Bench Press – %4% sets of 8 reps",
                                "Machine Chest Press – %4% sets of 10 reps",
                                "Cable Fly – %4% sets of 10 reps"],
                     'abdomen': ["Lat-pulldowns – %4% sets of 10 reps",
                                 "T-Bar Row – %4% sets of 10 reps",
                                 "Close-Grip Pulldowns – %4% sets of 12 reps"],
                     'forearms': ["Seated Dumbbell Press – %4% sets of 10 reps",
                                  "Lateral Raises – %3% sets of 20 reps",
                                  "EZ Bar Upright Rows – %3% sets of 15 reps"]},
        'intermediate': {'chest': ["intermediate Barbell Bench Press – %4% sets of 8 reps",
                                   "Machine Chest Press – %4% sets of 10 reps",
                                   "Cable Fly – %4% sets of 10 reps"],
                         'back': ["Lat-pulldowns – %4% sets of 10 reps",
                                  "T-Bar Row – %4% sets of 10 reps",
                                  "Close-Grip Pulldowns – %4% sets of 12 reps"],
                         'shoulders': ["Seated Dumbbell Press – %4% sets of 10 reps",
                                       "Lateral Raises – %3% sets of 20 reps",
                                       "EZ Bar Upright Rows – %3% sets of 15 reps"],
                         'legs': ["Leg Extensions – %4% sets of 10 reps",
                                  "Leg Press Machine – %4% sets of 8 reps",
                                  "Lunges – %3% sets of 10 reps per leg"],
                         'biceps': ["Barbell Bbicep Curls – %3% sets of 10 reps",
                                    "EZ Bar Curls – %4% sets of 10 reps",
                                    "Hammer Curls – %3% sets of 12 reps"],
                         'tricep': ["Barbell Bench Press – %4% sets of 8 reps",
                                    "Machine Chest Press – %4% sets of 10 reps",
                                    "Cable Fly – %4% sets of 10 reps"],
                         'abdomen': ["Lat-pulldowns – %4% sets of 10 reps",
                                     "T-Bar Row – %4% sets of 10 reps",
                                     "Close-Grip Pulldowns – %4% sets of 12 reps"],
                         'forearms': ["Seated Dumbbell Press – %4% sets of 10 reps",
                                      "Lateral Raises – %3% sets of 20 reps",
                                      "EZ Bar Upright Rows – %3% sets of 15 reps"]},
        'pro': {'chest': ["advanced Barbell Bench Press – %4% sets of 8 reps",
                          "Machine Chest Press – %4% sets of 10 reps",
                          "Cable Fly – %4% sets of 10 reps"],
                'back': ["Lat-pulldowns – %4% sets of 10 reps",
                         "T-Bar Row – %4% sets of 10 reps",
                         "Close-Grip Pulldowns – %4% sets of 12 reps"],
                'shoulders': ["Seated Dumbbell Press – %4% sets of 10 reps",
                              "Lateral Raises – %3% sets of 20 reps",
                              "EZ Bar Upright Rows – %3% sets of 15 reps"],
                'legs': ["Leg Extensions – %4% sets of 10 reps",
                         "Leg Press Machine – %4% sets of 8 reps",
                         "Lunges – %3% sets of 10 reps per leg"],
                'biceps': ["Barbell Bbicep Curls – %3% sets of 10 reps",
                           "EZ Bar Curls – %4% sets of 10 reps",
                           "Hammer Curls – %3% sets of 12 reps"],
                'tricep': ["Barbell Bench Press – %4% sets of 8 reps",
                           "Machine Chest Press – %4% sets of 10 reps",
                           "Cable Fly – %4% sets of 10 reps"],
                'abdomen': ["Lat-pulldowns – %4% sets of 10 reps",
                            "T-Bar Row – %4% sets of 10 reps",
                            "Close-Grip Pulldowns – %4% sets of 12 reps"],
                'forearms': ["Seated Dumbbell Press – %4% sets of 10 reps",
                             "Lateral Raises – %3% sets of 20 reps",
                             "EZ Bar Upright Rows – %3% sets of 15 reps"]}
    }

    beginner_data = {}
    intermediate_data = {}
    pro_data = {}

    response['workout'] = []

    for choice in input_data['choices']:
        beginner_data[choice] = data['beginner'][choice]
        intermediate_data[choice] = data['intermediate'][choice]
        pro_data[choice] = data['pro'][choice]

    if age >= 50 or goal_fitness - current_fitness >= 10:

        for i in range(6):
            engine.reset()
            engine.declare(Fact(level='beginner'))
            response['workout'].append(workouts)
            engine.run()

    else:

        if goal_fitness == 20 and current_fitness >= 15 and age < 35:

            for i in range(2):
                engine.reset()
                engine.declare(Fact(level='intermediate'))
                response['workout'].append(workouts)
                engine.run()

            for i in range(4):
                engine.reset()
                engine.declare(Fact(level='pro'))
                response['workout'].append(workouts)
                engine.run()

        elif goal_fitness == 20 and current_fitness >= 15 and 35 <= age < 50:

            engine.reset()
            engine.declare(Fact(level='beginner'))
            response['workout'].append(workouts)
            engine.run()

            for i in range(3):
                engine.reset()
                engine.declare(Fact(level='intermediate'))
                response['workout'].append(workouts)
                engine.run()

            for i in range(2):
                engine.reset()
                engine.declare(Fact(level='pro'))
                response['workout'].append(workouts)
                engine.run()

        elif goal_fitness - current_fitness <= 5 and 35 <= age < 50:

            for i in range(0):
                engine.reset()
                engine.declare(Fact(level='beginner'))
                response['workout'].append(workouts)
                engine.run()

            for i in range(3):
                engine.reset()
                engine.declare(Fact(level='intermediate'))
                response['workout'].append(workouts)
                engine.run()

            for i in range(3):
                engine.reset()
                engine.declare(Fact(level='pro'))
                response['workout'].append(workouts)
                engine.run()

        elif goal_fitness - current_fitness > 5 and 35 <= age < 50:

            for i in range(4):
                engine.reset()
                engine.declare(Fact(level='beginner'))
                response['workout'].append(workouts)
                engine.run()

            for i in range(2):
                engine.reset()
                engine.declare(Fact(level='intermediate'))
                response['workout'].append(workouts)
                engine.run()

            for i in range(0):
                engine.reset()
                engine.declare(Fact(level='pro'))
                response['workout'].append(workouts)
                engine.run()


        elif goal_fitness - current_fitness <= 5 and age < 35:

            for i in range(0):
                engine.reset()
                engine.declare(Fact(level='beginner'))
                response['workout'].append(workouts)
                engine.run()

            for i in range(3):
                engine.reset()
                engine.declare(Fact(level='intermediate'))
                response['workout'].append(workouts)
                engine.run()

            for i in range(3):
                engine.reset()
                engine.declare(Fact(level='pro'))
                response['workout'].append(workouts)
                engine.run()

        elif goal_fitness - current_fitness > 5 and age < 35:

            for i in range(2):
                engine.reset()
                engine.declare(Fact(level='beginner'))
                response['workout'].append(workouts)
                engine.run()

            for i in range(2):
                engine.reset()
                engine.declare(Fact(level='intermediate'))
                response['workout'].append(workouts)
                engine.run()

            for i in range(2):
                engine.reset()
                engine.declare(Fact(level='pro'))
                response['workout'].append(workouts)
                engine.run()

    return response

input_options = dict({
    "height": 155,
    "weight": 65,
    "age": 20,
    "goal": "ripped",
    "time": 120,
    "choices": ['chest', 'back', 'shoulders', 'legs', 'biceps']
})

print(create_fitness_plan(input_options))
