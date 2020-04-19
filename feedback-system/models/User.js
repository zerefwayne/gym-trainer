const mongoose = require('mongoose');

const UserSchema = mongoose.Schema({
    google_id: String,
    name: String,
    displayPhotoUrl: String,
    email: String
});

const User = mongoose.model('user', UserSchema);

module.exports = User;

