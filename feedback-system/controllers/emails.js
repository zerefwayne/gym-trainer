const sendgrid = require("@sendgrid/mail");

const KEYS = require("../config/keys");

sendgrid.setApiKey(KEYS.sendgrid.api_key);
sendgrid.setSubstitutionWrappers('{{','}}');

/*
{ _id: 5dcc4004bfcb075376752b02,
    google_id: '118184136259259068801',
    name: 'Aayush Joglekar',
    displayPhotoUrl:
     'https://lh3.googleusercontent.com/a-/AAuE7mCpmEzUI8uhe-PI17p5FyJxZea97vwoyQbLwyda',
    email: 'aayushjog@gmail.com',
    __v: 0 } */

function newUserEmail(user) {
  console.log(user);

  const msg = {
    to: user.email,
    from: "welcome@fitapp.com",
    subject: "Welcome to FitApp!",
    text: "and easy to do anywhere, even with Node.js",
    substitutions: {name: user.name},
    html: '<div style="height: 400px; display: flex; flex-direction: column; align-items: center; justify-content: center;"><h2 style="font-size: 40px; color: #333333;">Welcome to FitApp, {{name}} </h2><p style="font-size: 16px; color: #222222;">Create your first plan today using our expert systems.</p></div>'
  };

  sendgrid
    .send(msg)
    .then(res => {
      console.log("SUCCESS!");
    })
    .catch(error => {
      console.log(error);
    });
}

module.exports = {
  newUserEmail
};
