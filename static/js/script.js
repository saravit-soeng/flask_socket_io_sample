$(document).ready(() => {
    var socket = io.connect('http://'+document.domain + ":" + location.port);
    socket.on('connect', () => {
        socket.emit('connected', {data:'Connected'});
    });
    socket.on('value update', (data)=>{
        
        // Destroy carousel object before reinitialize it
        $('#display-slide').trigger('destroy.owl.carousel');
        
        data = data['message'];
        console.log(data);
        var e = '';
        data.forEach(element => {
            e += '<div class="item"><h3>' + element + '</h3></div>';
        });
        $('#display-slide').html(e);
        $('#display-slide').addClass('owl-carousel');
        $('#display-slide').owlCarousel({
            items:1,
            loop:true,
            margin:10,
            autoplay:true,
            autoplayTimeout:2000,
            animateOut: 'fadeOut',
            animateIn: 'fadeIn',
        });
    })
});