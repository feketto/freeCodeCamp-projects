const display = document.getElementById('display');
const pads = document.querySelectorAll('.drum-pad');

function playSound(key) {
    const upperKey = key.toUpperCase();
    
    const audio = document.getElementById(upperKey);
    
    if (audio) {
        const pad = audio.parentElement;
        
        audio.currentTime = 0;
        
        const playPromise = audio.play();
        if (playPromise !== undefined) {
            playPromise.catch(error => {
                console.log("Audio playback failed: " + error);
            });
        }
        
        display.innerText = pad.id.replace(/-/g, ' ');
        
        pad.classList.add('active');
        
        setTimeout(() => {
            pad.classList.remove('active');
        }, 100);
    }
}

pads.forEach(pad => {
    pad.addEventListener('click', () => {
        const key = pad.innerText;
        playSound(key);
    });
});

document.addEventListener('keydown', (event) => {
    playSound(event.key);
});
