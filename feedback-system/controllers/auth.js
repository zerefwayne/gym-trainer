const router = require("express").Router();
const passport = require("passport");

const authConfig = require("../config/authentication.config");

router.get(
  "/google",
  passport.authenticate("google", { scope: ["profile", "email"] })
);

router.get("/google/redirect", passport.authenticate("google"), function(
  req,
  res
) {

  res.redirect("http://localhost:8080/");
});

router.get("/logout", function(req, res) {
  req.logout();
  res.send({ success: true, message: "Successfully logged out!" });
});

router.get("/user", authConfig.isAuthenticated, function(req, res) {
  res.send(req.user);
});

module.exports = router;
