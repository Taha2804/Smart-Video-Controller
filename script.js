// script.js

const video = document.getElementById('video');
const playPauseButton = document.getElementById('play-pause');
const muteButton = document.getElementById('mute');
const progressBar = document.getElementById('progress');
const currentTimeElement = document.getElementById('current-time');
const durationElement = document.getElementById('duration');
const videoTitleElement = document.getElementById('video-title');
const videoDescriptionElement = document.getElementById('video-description');
const viewsElement = document.getElementById('views');
const likesElement = document.getElementById('likes');
const uploadVideoButton = document.getElementById('upload-video-button');
const videoFileInput = document.getElementById('video-file');

let isPlaying = false;
let isMuted = false;

playPauseButton.addEventListener('click', () => {
    if (isPlaying) {
        video.pause();
        playPauseButton.ariaLabel = 'Play';
    } else {
        video.play();
        playPauseButton.ariaLabel = 'Pause';
    }
    isPlaying = !isPlaying;
});

muteButton.addEventListener('click', () => {
    if (isMuted) {
        video.muted = false;
        muteButton.ariaLabel = 'Mute';
    } else {
        video.muted = true;
        muteButton.ariaLabel = 'Unmute';
    }
    isMuted = !isMuted;
});

uploadVideoButton.addEventListener('click', () => {
    const videoFile = videoFileInput.files[0];
    const videoUrl = URL.createObjectURL(videoFile);
    video.src = videoUrl;
    video.play();
});

video.addEventListener('loadedmetadata', () => {
    const duration = video.duration;
    durationElement.textContent = formatTime(duration);
});

video.addEventListener('timeupdate', () => {
    const currentTime = video.currentTime;
    currentTimeElement.textContent = formatTime(currentTime);
    const progress = (currentTime / video.duration) * 100;
    progressBar.style.width = `${progress}%`;
});

function formatTime(time) {
    const hours = Math.floor(time / 3600);
    const minutes = Math.floor((time % 3600) / 60);
    const seconds = Math.floor(time % 60);
    return `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
}