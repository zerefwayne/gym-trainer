const passport = require("passport");
const GoogleStrategy = require("passport-google-oauth20").Strategy;
const Keys = require("./keys");

const { newUserEmail } = require('../controllers/emails');

const User = require("../models/User");

passport.serializeUser((user, done) => {
  done(null, user["_id"]);
});

passport.deserializeUser((id, done) => {

  User.findById(id)
    .then(user => {
      done(null, user);
    })
    .catch(err => {
      console.log(err);
      done(err);
    });
});

passport.use(
  new GoogleStrategy(
    {
      clientID: Keys.google.client_id,
      clientSecret: Keys.google.client_secret,
      callbackURL: "/auth/google/redirect"
    },
    (accessToken, refreshToken, profile, done) => {
      User.findOne({ google_id: profile["_json"]["sub"] }, function(
        error,
        response
      ) {
        if (error) {
          console.log(error);
          done(error);
        }

        if (!response) {
          const newUser = new User({
            google_id: profile["_json"]["sub"],
            name: profile["_json"]["name"],
            displayPhotoUrl: profile["_json"]["picture"],
            email: profile["_json"]["email"]
          });

          newUser
            .save()
            .then(new_user => {

              newUserEmail(new_user);

              console.log("Created a new user successfully!", new_user);
              done(null, new_user);
            })
            .catch(err => {
              console.log(err);
            });
        } else {
          done(null, response);
          console.log("Already signed up!", response);
        }
      });
    }
  )
);

/*

 _json:
   { sub: '118184136259259068801',
     name: 'Aayush Joglekar',
     given_name: 'Aayush',
     family_name: 'Joglekar',
     picture:
      'https://lh3.googleusercontent.com/a-/AAuE7mCpmEzUI8uhe-PI17p5FyJxZea97vwoyQbLwyda',
     email: 'aayushjog@gmail.com',
     email_verified: true,
     locale: 'en' } }



*/
