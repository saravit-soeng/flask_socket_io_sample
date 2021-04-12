$(document).ready(() => {
    var socket = io.connect('http://'+document.domain + ":" + location.port);
    socket.on('connect', () => {
        socket.emit('connected', {data:'Connected'});
    });
    socket.on('value update', (msg)=>{
        $("#rand-value").text(msg);
    })
});