module.exports = (app) => {
    const readings = require('./reading.controller.js');

    // Create a new Product
    app.post('/readings', readings.create);

    // Retrieve all Products
    app.get('/readings', readings.findAll);

    app.get('/destroy' , readings.deleteAll);

}