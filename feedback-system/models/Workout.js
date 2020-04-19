const mongoose = require("mongoose");

const ExerciseSchema = new mongoose.Schema({
  bodyPart: String,
  difficulty: String,
  exercise: String,
  sets: Number,
  reps: Number,
  numberOfVotes: Number,
  likes: Number,
  time: {
    type: Number,
    default: 0
  }
});

const IndividualExerciseSchema = new mongoose.Schema({
  exercise: {
    type: mongoose.Schema.Types.ObjectId,
    ref: "exercise",
    autopopulate: true
  },
  isExerciseCompleted: {
    type: Boolean,
    default: false
  },
  hasGivenFeedback: {
    type: Boolean,
    default: false
  }
});

IndividualExerciseSchema.plugin(require('mongoose-autopopulate'));

const DaySchema = new mongoose.Schema(
  {
    exercises: [IndividualExerciseSchema],
    isRestDay: {
      type: Boolean,
      default: false
    },
    isDayCompleted: {
      type: Boolean,
      default: false
    }
  },
  { _id: false }
);

const WeekSchema = new mongoose.Schema(
  {
    days: [DaySchema],
    isWeekCompleted: {
      type: Boolean,
      default: false
    }
  },
  { _id: false }
);

const RoutineSchema = new mongoose.Schema({
  userId: {
    type: mongoose.Schema.Types.ObjectId,
    ref: "user",
    autopopulate: true
  },
  dateCreated: {
    type: String,
    default: new Date()
  },
  workouts: [WeekSchema],
  dateFinished: String,
  isRoutineCompleted: {
    type: Boolean,
    default: false
  },
  current: {
    day: {
      type: Number,
      default: 0
    },
    exercise: {
      type: Number,
      default: 0
    },
    week: {
      type: Number,
      default: 0
    }
  }
});

RoutineSchema.plugin(require('mongoose-autopopulate'));

const Routine = new mongoose.model("routine", RoutineSchema);

const IndividualExercise = new mongoose.model(
  "individual_exercise",
  IndividualExerciseSchema
);

const Exercise = new mongoose.model("exercise", ExerciseSchema);

module.exports = { Routine, IndividualExercise, Exercise };
