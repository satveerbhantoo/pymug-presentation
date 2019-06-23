const express = require('express');

setInterval(function(){
   // get dependencies

    console.log('Running logger');
    var dt = new Date(); 

    var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;

    var xhr = new XMLHttpRequest();
    xhr.open("POST", 'http://localhost:3000/readings', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify(
        {temp:getRandomInt(50), humidity: getRandomInt(100), time: dt.toISOString().substring(0, 19)}
    ));
}, 5000);


function getRandomInt(max) {
    return Math.floor(Math.random() * Math.floor(max));
}