//Initialization
//#region 
// HTML Object initialization
const title = document.getElementById('title');
const monthDD = document.getElementById('monthDropDown');
const dayDD = document.getElementById('dayDropDown');
const hourDD = document.getElementById('hourDropDown');
const minuteDD = document.getElementById('minuteDropDown');
const secondDD = document.getElementById('secondsDropDown');
const timer = document.getElementById('timer');
const startStopButton = document.getElementById('start/stop');
const resetButton = document.getElementById('reset');
const alarmAudio = new Audio('alarm_chime.wav');

// Calculation variables
let months = 0;
let days = 0;
let hours = 0;
let minutes = 0;
let seconds = 0;
let timeInSeconds = 0;
let timeUnits = [months, days, hours, minutes, seconds];

// Conversion factors (in seconds)
const hoursToSeconds = 3600;
const daysToSeconds = 86400;
const monthsToSeconds = 2592000;

// Whether the timer is currently running
let timerRunning = false;
let timerHasBegun = false;
//#endregion

// Detects user interaction
//#region 
// Detects changes in the dropdown menus
monthDD.onchange = function () {
    months = Number(monthDD.value);
    setTime();
    setButtonText();
}

dayDD.onchange = function () {
    days = Number(dayDD.value);
    setTime();
    setButtonText();
}

hourDD.onchange = function () {
    hours = Number(hourDD.value);
    setTime();
    setButtonText();
}

minuteDD.onchange = function () {
    minutes = Number(minuteDD.value);
    setTime();
    setButtonText();
}

secondDD.onchange = function () {
    seconds = Number(secondDD.value);
    setTime();
    setButtonText();
}

// Detects button presses
startStopButton.onclick = function () {
    if (!timerHasBegun && timeInSeconds > 0) {
        timerHasBegun = true
    }
    timerRunning = !timerRunning
    setButtonText();
}

resetButton.onclick = function () {
    location.reload();
}
//#endregion


function setButtonText() {
    /** Sets the text of the Start/Stop button based on whether the timer is running  */
    if (timerRunning) {
        startStopButton.innerText = 'Pause Timer';
    }
    else {
        startStopButton.innerText = 'Start Timer'
    }
}

function setTime(){
    /** Calculates the time in seconds represented by the selected dropdown menus */
    timeInSeconds = seconds + (minutes*60) + (hours*hoursToSeconds) 
        + (days*daysToSeconds) + (months*monthsToSeconds);
    
    timerHasBegun = false;
    timerRunning = false;
}

function calculateTimeUnits(time){
    /** Calculates the number of months,days,hours,minutes,seconds left in the timer */
    let mon = Math.floor(time/monthsToSeconds);
    time -= mon * monthsToSeconds;

    let day = Math.floor(time/daysToSeconds);
    time -= day * daysToSeconds;

    let hour = Math.floor(time/hoursToSeconds);
    time -= hour * hoursToSeconds;

    let min = Math.floor(time/60);
    time -= min * 60;

    return [mon, day, hour, min, time];
}

function updateTimer(timeUnits){
    /** Updates the timer display with each unit of time */
    let display = ''

    if (timeUnits[0] < 10) {
        display = display + '0' + String(timeUnits[0]) + ':'
    } 
    else {display = display + timeUnits[0] + ':'}

    if (timeUnits[1] < 10) {
        display = display + '0' + String(timeUnits[1]) + ':'
    } 
    else {display = display + timeUnits[1] + ':'}

    if (timeUnits[2] < 10) {
        display = display + '0' + String(timeUnits[2]) + ':'
    } 
    else {display = display + timeUnits[2] + ':'}

    if (timeUnits[3] < 10) {
        display = display + '0' + String(timeUnits[3]) + ':'
    } 
    else {display = display + timeUnits[3] + ':'}

    if (timeUnits[4] < 10) {
        display = display + '0' + String(timeUnits[4])
    } 
    else {display = display + timeUnits[4]}

    timer.innerHTML = display;
}

function updateTitle(timeUnits) {
    /** Updates the tab title based on the time left on the timer */
    if (timeUnits[0] != 0){
        title.innerHTML = timeUnits[0] + ' Month Timer';
    }
    else if (timeUnits[1] != 0){
        title.innerHTML = timeUnits[1] + ' Day Timer';
    }
    else if (timeUnits[2] != 0){
        title.innerHTML = timeUnits[2] + ' Hour Timer';
    }
    else if (timeUnits[3] != 0){
        title.innerHTML = timeUnits[3] + ' Minute Timer';
    }
    else if (timeUnits[4] != 0){
        title.innerHTML = timeUnits[4] + ' Second Timer';
    }
    else {
        title.innerHTML = 'Unset Timer'
    }

}

// Runs when page is loaded
updateTimer(timeUnits);
title.innerHTML = 'Unset Timer'
startStopButton.innerText = 'Start Timer';
resetButton.innerText = 'Reset'

const updateDisplay = setInterval(function() {
    /** Updates the timer and tab title display (set to 250ms for responsiveness) */
    timeUnits = calculateTimeUnits(timeInSeconds);
    updateTimer(timeUnits);
    updateTitle(timeUnits);

}, 250);

const countdown = setInterval(function() {
    /** Counds down the timer */
    if (timerRunning && timeInSeconds > 0) {
        timeInSeconds -= 1
    }
}, 1000);

const alarmCheck = setInterval(function() {
    /** Plays a chime if the alarm counted down to 0 */
    if (timerHasBegun && timeInSeconds == 0) {
        alarmAudio.play()
    }
}, 3000);


