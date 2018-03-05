var counter = 0;
var pairsLeft;
var attempts = 0;
var pick_1 = 0;
var pick_2 = 0;
var stopWatchRunning = false;
var startTime;
var currentdate;
var time;


function getPairs() {
  var pairs = location.pathname.substring(1);
  if (pairs == "two") {
    pairsLeft = 4;
  }else if (pairs == "three") {
    pairsLeft = 6;
  }else {
    pairsLeft = 8;
  }
}

getPairs();

$(function() {
  registerClock();
  setTime();
});

function setTime() {
  currentdate = new Date();
  var datetime = + currentdate.getDate() + "."
                + (currentdate.getMonth()+1)  + "."
                + currentdate.getFullYear() + " "
                + currentdate.getHours() + ":"
                + currentdate.getMinutes() + ":"
                + currentdate.getSeconds();
}

function updateClock() {
  setTime();
  setStopWatch();
}

function registerClock() {
  setInterval(updateClock, 250);
}

function updateClock() {
  setTime();
  setStopWatch();
}

function setStopWatch() {
  if (stopWatchRunning == false) {
    return;
  }
  var duration = new Date(currentdate - startTime);
  var showDuration = "Time: " + duration.getMinutes() + ":"
                + duration.getSeconds();
  $("#timer").text(showDuration);
}



function swapImage(id,front) {
    if (stopWatchRunning == false) {
      startTime = new Date();
      stopWatchRunning = true;
    }

    filepath=document.getElementById(id).src;
    if (filepath.match('static/images/grumpy.jpg') && counter < 2) {
      document.getElementById(id).src=front;
      counter = counter + 1;
      if (pick_1 == 0){
          pick_1 = id;
      }
      else if (pick_2 == 0){
          pick_2 = id;
      }
    }
    else{
      return;
    }

    if(counter == 2) {
      attempts = attempts + 1;

      document.getElementById("attempts").innerHTML = "Attempts: " + attempts;
      setTimeout(function() {
        if(checkMatch(pick_1, pick_2, id) == true) {
            pairsLeft = pairsLeft - 1;
            if(pairsLeft == 0){
              stopWatchRunning = false;
              tempTime = $("#timer").text();
              time = tempTime.replace("Time: ", "");
              submitWin(time, attempts);
            }

            counter = 0;
            pick_1 = 0;
            pick_2 = 0;

        } else {
            document.getElementById(pick_1).src='static/images/grumpy.jpg';
            document.getElementById(pick_2).src='static/images/grumpy.jpg';
            pick_1 = 0;
            pick_2 = 0;
            counter = 0;
        }
      }, 2000);

    }
}

function checkMatch(pick_1, pick_2, id) {
  if (pick_1.replace("-", "") == pick_2.replace("-", "")){
    return true;
  }else {
    return false;
  }

}

function submitWin(time, attempts) {
  $('input[name="attempts"]').val(attempts);
  $('input[name="time"]').val(time);
  // $('input[name="grid"]').val("two");
  document.getElementById('winForm').submit();
}