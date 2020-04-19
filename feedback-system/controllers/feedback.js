const express = require("express");

const router = express.Router();

const { Exercise, Routine } = require("../models/Workout");

const authConfig = require("../config/authentication.config");

router.post("/", authConfig.isAuthenticated, (req, res) => {
  console.log(req.body);

  Exercise.findById(req.body.exercise_id, function(error, response) {
    if (response) {
      const requiredExercise = response;

      requiredExercise.numberOfVotes += 1;
      requiredExercise.likes += req.body.like;

      Exercise.updateOne({ _id: req.body.id }, requiredExercise, function(
        error,
        updateResponse
      ) {
        if (error) {
          res.status(301).json({
            success: false,
            error
          });
        } else {
          Routine.findById(req.body.routine_id).then(foundRoutine => {
            const updatedRoutine = foundRoutine;

            updatedRoutine["workouts"][req.body.week]["days"][req.body.day][
              "exercises"
            ][req.body.index]["hasGivenFeedback"] = true;

            console.log(updatedRoutine["workouts"][req.body.week]["days"][req.body.day][
              "exercises"
            ][req.body.index]);

            Routine.findByIdAndUpdate(req.body.routine_id, updatedRoutine, {
              new: true
            })
              .then(updatedRoutine => {
                res.status(200).json({
                  success: true,
                  updatedRoutine
                });
              })
              .catch(error => {
                res.status(200).json({
                  success: false,
                  error
                });
              });
          });
        }
      });
    } else {
      res.status(301).json({
        success: false,
        error
      });
    }
  });

});

module.exports = router;