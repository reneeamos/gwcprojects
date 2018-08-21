var tag = document.createElement('script');

   tag.src = "https://www.youtube.com/iframe_api";
   var firstScriptTag = document.getElementsByTagName('script')[0];
   firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

   // 3. This function creates an <iframe> (and YouTube player)
   //    after the API code downloads.
   var player;
   function onYouTubeIframeAPIReady() {
     player = new YT.Player('player', {
       height: '390',
       width: '640',
       videoId: 'qqBibE1d_y0',
       playerVars:  { 'autoplay': 1 },
       events: {
         'onReady': onPlayerReady,

       }
     });
   }


function onPlayerReady(event) {
  event.target.playVideo();
}


function pause() {
   player.pauseVideo();
}
function play() {
   player.playVideo();
}

function stop() {
  player.stopVideo();

}
 function switchone() {
//qqBibE1d_y0
player.loadVideoById("qqBibE1d_y0", 0, "large");

 }

function switchtwo() {
  player.loadVideoById("oMFxQsaT274", 0, "large");
}


function switchthree(){
function randnum() {
    var randnum = Math.floor((Math.random() * 10));
}
  if (randnum >= 5) {
      player.loadVideoById("kJQP7kiw5Fk", 0, "large");

  }
  else if (randnum <= 4) {
      player.loadVideoById("dQw4w9WgXcQ", 0, "large");

  }
  else {
    console.log("error!!");
  }
}
