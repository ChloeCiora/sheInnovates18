
navigator.getUserMedia ||
	(navigator.getUserMedia = navigator.mozGetUserMedia) ||
	navigator.webkitGetUserMedia || navigator.msGetUserMedia);

if(navigator.getUserMedia){
	navigator.getUserMedia({video:true, audio:false}, onSuccess, onError);
}
else{
	alert('Your browser is not supported');
}
function onSuccess(stream){
	alert('Connection Successful!');
}

function onError(){
	alert('Houston, we have a problem');
}

