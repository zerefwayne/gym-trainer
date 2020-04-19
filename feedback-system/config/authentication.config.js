const isAuthenticated = (req, res, done) => {

  if (!req.user) {
    res.send({ success: false, errors: { authentication: true } });
  } else {
    done();
  }

};

module.exports = {
  isAuthenticated
};
