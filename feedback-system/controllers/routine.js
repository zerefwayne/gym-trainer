const router = require("express").Router();

const { Routine, IndividualExercise, Exercise } = require("../models/Workout");

const { isAuthenticated } = require("../config/authentication.config");

router.post("/create", isAuthenticated, (req, res) => {
  console.log(req.user);

  const newRoutine = {
    userId: req.user["id"],
    workouts: []
  };

  const workouts = req.body.workouts;

  for (let week = 0; week < 6; week++) {
    const newWeek = {
      days: []
    };

    for (let day = 0; day < 7; day++) {
      const day_object = workouts[week][day];

      let newDay = {
        isRestDay: day_object["rest"] == 1,
        exercises: []
      };

      if (day_object["rest"] == 0) {
        newDay["exercises"] = [];

        for (let ex = 0; ex < 5; ex++) {
          const exercise = day_object["exercises"][ex];

          const newExercise = {
            exercise: exercise.id
          };

          newDay["exercises"].push(newExercise);
        }
      }

      newWeek["days"].push(newDay);
    }

    newRoutine.workouts.push(newWeek);
  }

  Routine.create(newRoutine)
    .then(response => {
      res.send({ success: true, message: response });
    })
    .catch(error => {
      res.send({ success: false, error });
    });
});

router.post("/", isAuthenticated, (req, res) => {
  Routine.findById(req.body.routineId)
    .then(document => {
      res.send({ success: true, message: document });
    })
    .catch(error => {
      res.send({ success: false, message: error });
    });
});

router.post("/exercise/update", isAuthenticated, (req, res) => {
  console.log(req.body);

  Routine.findById(req.body.routine)
    .then(routine => {
      console.log(routine);

      const newRoutine = routine;

      newRoutine["workouts"][req.body.week]["days"][req.body.day]["exercises"][
        req.body.exercise
      ]["isExerciseCompleted"] = true;

      let isDayComplete = true;

      for (let i = 0; i < 5; i++) {
        if (
          newRoutine["workouts"][req.body.week]["days"][req.body.day][
            "exercises"
          ][i]["isExerciseCompleted"] == false
        ) {
          isDayComplete = false;
          break;
        }
      }

      if (isDayComplete) {
        newRoutine["workouts"][req.body.week]["days"][req.body.day][
          "isDayCompleted"
        ] = true;

        if (req.body.day == 6) {
          newRoutine["workouts"][req.body.week]["isWeekCompleted"] = true;

          if (req.body.week == 5) {
            newRoutine["isRoutineCompleted"] = true;
            newRoutine["dateFinished"] = new Date();
          }
        }
      }

      Routine.findByIdAndUpdate(req.body.routine, newRoutine, { new: true })
        .then(updatedDocument => {
          console.log(
            "Updated",
            updatedDocument["workouts"][req.body.week]["days"][req.body.day][
              "exercises"
            ]
          );

          res.send({ success: true, updatedDocument });
        })
        .catch(error => {
          console.log(error);
          res.send({ success: false, error });
        });
    })
    .catch(error => {
      console.log(error);
    });
});

router.get("/current", isAuthenticated, (req, res) => {
  const user = req.user;

  Routine.findOne({ userId: user["_id"], isRoutineCompleted: false })
    .then(response => {
      res.send({ success: true, message: response });
    })
    .catch(error => {
      res.send({ success: false, message: error });
    });
});

router.get("/completed", isAuthenticated, (req, res) => {
  const user = req.user;

  Routine.find({ userId: user["_id"], isRoutineCompleted: true })
    .then(response => {
      res.send({ success: true, message: response });
    })
    .catch(error => {
      res.send({ success: false, message: error });
    });
});

module.exports = router;
