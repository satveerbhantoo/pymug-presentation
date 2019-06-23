const mongoose = require('mongoose');

const ReadingSchema = mongoose.Schema({
    temp: Number,
    humidity: Number, 
    time: String
}, {
    timestamps: true
});

module.exports = mongoose.model('Readings', ReadingSchema);