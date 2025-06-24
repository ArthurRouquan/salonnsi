class TimerApp {
    constructor() {
        this.timers = [];
        this.timerId = 0;
        this.timerCounter = 0;
        this.audio = document.getElementById('timerSound');
        this.globalInterval = null;
        this.init();
    }

    init() {
        this.updateGlobalClock();
        this.setupEventListeners();
        this.loadTimers();
        this.loadDefaultSettings();
        this.startGlobalTick();
    }

    startGlobalTick() {
        // Align the first tick to the next second
        const now = new Date();
        const msToNextSecond = 1000 - now.getMilliseconds();
        setTimeout(() => {
            this.globalInterval = setInterval(() => this.globalTick(), 1000);
            this.globalTick();
        }, msToNextSecond);
    }

    globalTick() {
        this.updateGlobalClock();
        // Update all running timers
        const now = Date.now();
        this.timers.forEach(timer => {
            if (timer.isRunning && !timer.isCompleted) {
                const elapsed = Math.floor((now - timer.startTime.getTime()) / 1000);
                timer.remaining = Math.max(0, timer.duration - elapsed);
                if (timer.remaining <= 0) {
                    this.completeTimer(timer);
                } else {
                    this.updateTimerDisplay(timer);
                }
            }
        });
    }

    updateGlobalClock() {
        const now = new Date();
        const timeString = now.toLocaleTimeString('en-US', { 
            hour12: false,
            hour: '2-digit',
            minute: '2-digit',
            second: '2-digit'
        });
        
        document.getElementById('currentTime').textContent = timeString;
    }

    setupEventListeners() {
        // Default minutes change
        document.getElementById('defaultMinutes').addEventListener('change', (e) => {
            localStorage.setItem('defaultMinutes', e.target.value);
        });
    }

    getNextTimerName() {
        this.timerCounter++;
        return `Table ${this.timerCounter}`;
    }

    addTimer() {
        const minutes = parseInt(document.getElementById('defaultMinutes').value) || 5;

        if (!minutes || minutes <= 0) {
            alert('Please set a duration greater than 0');
            return;
        }

        const timerName = this.getNextTimerName();
        const totalSeconds = minutes * 60;

        const timer = {
            id: ++this.timerId,
            name: timerName,
            duration: totalSeconds,
            originalDuration: totalSeconds,
            remaining: totalSeconds,
            startTime: null,
            endTime: null,
            isRunning: false,
            isCompleted: false
        };

        this.timers.push(timer);
        this.renderTimer(timer);
        this.saveTimers();
    }

    renderTimer(timer) {
        const timerElement = document.createElement('div');
        timerElement.className = 'timer-card';
        timerElement.dataset.timerId = timer.id;
        
        if (timer.isCompleted) timerElement.classList.add('completed');
        else if (timer.isRunning) timerElement.classList.add('running');

        const progress = timer.isCompleted ? 100 : ((timer.duration - timer.remaining) / timer.duration) * 100;
        
        // Only render +/- buttons if timer is ready (not running, not completed)
        let timerTimeHTML = '';
        if (!timer.isRunning && !timer.isCompleted) {
            timerTimeHTML = `
                <button class="timer-adjust" onclick="app.adjustTimerDuration(${timer.id}, -1)"><span class="material-icons">remove</span></button>
                <span class="timer-time">${this.formatTime(timer.remaining)}</span>
                <button class="timer-adjust" onclick="app.adjustTimerDuration(${timer.id}, 1)"><span class="material-icons">add</span></button>
            `;
        } else {
            timerTimeHTML = `
                <span class="timer-time">${this.formatTime(timer.remaining)}</span>
            `;
        }

        timerElement.innerHTML = `
            <div class="timer-header">
                <input class="timer-name-input" type="text" value="${timer.name.replace(/"/g, '&quot;')}" data-timer-id="${timer.id}" maxlength="30" />
                <button class="timer-delete" onclick="app.deleteTimer(${timer.id})"><span class="material-icons">close</span></button>
            </div>
            <div class="timer-time-row">${timerTimeHTML}</div>
            <div class="timer-progress">
                <div class="timer-progress-bar" style="width: ${progress}%"></div>
            </div>
            <div class="timer-times">
                <div>${timer.startTime ? this.formatDateTime(timer.startTime) : '&nbsp;'}</div>
                <div>${timer.endTime ? this.formatDateTime(timer.endTime) : '&nbsp;'}</div>
            </div>
            <div class="timer-controls">
                ${this.getControlButtons(timer)}
            </div>
        `;

        // Add event listener for name input
        const nameInput = timerElement.querySelector('.timer-name-input');
        nameInput.addEventListener('blur', (e) => {
            this.updateTimerNameFromInput(timer.id, e.target.value);
        });
        nameInput.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') {
                e.preventDefault();
                nameInput.blur();
            }
        });

        const container = document.getElementById('timersContainer');
        container.appendChild(timerElement);
    }

    getControlButtons(timer) {
        if (timer.isCompleted) {
            return `
                <button class="btn btn-secondary" onclick="app.resetTimer(${timer.id})">Redémarrer</button>
            `;
        } else if (timer.isRunning) {
            return `
                <button class="btn btn-secondary" onclick="app.resetTimer(${timer.id})">Redémarrer</button>
            `;
        } else {
            return `
                <button class="btn btn-primary" onclick="app.startTimer(${timer.id})">Démarrer</button>
            `;
        }
    }

    startTimer(id) {
        const timer = this.timers.find(t => t.id === id);
        if (!timer || timer.isRunning) return;

        // Set progress bar transition to 1s linear on play
        const element = document.querySelector(`[data-timer-id="${timer.id}"]`);
        if (element) {
            const progressBar = element.querySelector('.timer-progress-bar');
            if (progressBar) {
                progressBar.style.transition = 'width 1s linear, background-color 0.2s';
            }
        }

        timer.isRunning = true;
        timer.startTime = new Date();
        timer.endTime = new Date(timer.startTime.getTime() + timer.remaining * 1000);

        this.updateTimerDisplay(timer);
    }

    resetTimer(id) {
        const timer = this.timers.find(t => t.id === id);
        if (!timer) return;

        // Fast progress bar transition for reset with ease-in-out
        const element = document.querySelector(`[data-timer-id="${timer.id}"]`);
        if (element) {
            const progressBar = element.querySelector('.timer-progress-bar');
            if (progressBar) {
                progressBar.style.transition = 'width 0.3s ease-in, background-color 0.2s';
                progressBar.style.width = '0%';
                // Restore normal transition after reset
                setTimeout(() => {
                    progressBar.style.transition = 'width 1s linear, background-color 0.2s';
                }, 200);
            }
        }

        timer.duration = timer.originalDuration;
        timer.remaining = timer.originalDuration;
        timer.isRunning = false;
        timer.isCompleted = false;
        timer.startTime = null;
        timer.endTime = null;

        this.updateTimerDisplay(timer);
        this.saveTimers();
    }

    deleteTimer(id) {
        const timer = this.timers.find(t => t.id === id);
        if (!timer) return;

        // Remove confirm dialog, delete immediately
        this.timers = this.timers.filter(t => t.id !== id);
        this.removeTimerElement(id);

        // No updates to other timers!
        this.saveTimers();
    }

    completeTimer(timer) {
        timer.isRunning = false;
        timer.isCompleted = true;
        timer.remaining = 0;

        this.updateTimerDisplay(timer);
        this.playNotificationSound();
        this.saveTimers();
    }

    updateTimerDisplay(timer) {
        const element = document.querySelector(`[data-timer-id="${timer.id}"]`);
        if (!element) return;

        // Update time display and +/- buttons
        const timeRow = element.querySelector('.timer-time-row');
        if (timeRow) {
            let timerTimeHTML = '';
            if (!timer.isRunning && !timer.isCompleted) {
                timerTimeHTML = `
                    <button class="timer-adjust" onclick="app.adjustTimerDuration(${timer.id}, -1)"><span class="material-icons">remove</span></button>
                    <span class="timer-time">${this.formatTime(timer.remaining)}</span>
                    <button class="timer-adjust" onclick="app.adjustTimerDuration(${timer.id}, 1)"><span class="material-icons">add</span></button>
                `;
            } else {
                timerTimeHTML = `
                    <span class="timer-time">${this.formatTime(timer.remaining)}</span>
                `;
            }
            timeRow.innerHTML = timerTimeHTML;
        }

        // Update progress bar
        const progress = timer.isCompleted ? 100 : ((timer.duration - timer.remaining) / timer.duration) * 100;
        const progressBar = element.querySelector('.timer-progress-bar');
        if (progressBar) progressBar.style.width = `${progress}%`;

        // Update times
        const timesElement = element.querySelector('.timer-times');
        if (timesElement) {
            timesElement.innerHTML = `
                <div>${timer.startTime ? this.formatDateTime(timer.startTime) : '&nbsp;'}</div>
                <div>${timer.endTime ? this.formatDateTime(timer.endTime) : '&nbsp;'}</div>
            `;
        }

        // Update controls button in place for smooth transition
        const controlsElement = element.querySelector('.timer-controls');
        let state = timer.isCompleted ? 'completed' : timer.isRunning ? 'running' : 'stopped';
        let btn = controlsElement.querySelector('button');
        if (!btn) {
            btn = document.createElement('button');
            controlsElement.appendChild(btn);
        }
        // Remove all btn-* classes
        btn.className = 'btn';
        btn.onclick = null;
        if (timer.isCompleted) {
            btn.classList.add('btn-secondary');
            btn.textContent = 'Redémarrer';
            btn.onclick = () => this.resetTimer(timer.id);
        } else if (timer.isRunning) {
            btn.classList.add('btn-secondary');
            btn.textContent = 'Redémarrer';
            btn.onclick = () => this.resetTimer(timer.id);
        } else {
            btn.classList.add('btn-primary');
            btn.textContent = 'Démarrer';
            btn.onclick = () => this.startTimer(timer.id);
        }
        controlsElement.dataset.state = state;

        // Update card state
        element.className = 'timer-card';
        if (timer.isCompleted) element.classList.add('completed');
        else if (timer.isRunning) element.classList.add('running');
    }

    removeTimerElement(id) {
        const element = document.querySelector(`[data-timer-id="${id}"]`);
        if (element) {
            element.remove();
        }
    }

    formatTime(seconds) {
        const minutes = Math.floor(seconds / 60);
        const secs = seconds % 60;
        return `${minutes.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
    }

    formatDateTime(date) {
        return date.toLocaleTimeString('en-US', { 
            hour12: false,
            hour: '2-digit',
            minute: '2-digit'
        });
    }

    playNotificationSound() {
        const timerSound = document.getElementById('timerSound');
        const notificationSound = document.getElementById('notificationSound');
        const isMuted = localStorage.getItem('timerMuted') === '1';
        if (timerSound && !isMuted) {
            try {
                timerSound.pause();
                timerSound.currentTime = 0;
                timerSound.load();
                timerSound.play().catch(e => console.log('Audio play failed:', e));
            } catch (e) { console.log('Audio play error:', e); }
        }
        if (notificationSound && !isMuted) {
            try {
                notificationSound.pause();
                notificationSound.currentTime = 0;
                notificationSound.load();
                notificationSound.play().catch(e => console.log('Notification MP3 play failed:', e));
            } catch (e) { console.log('Notification play error:', e); }
        }
    }

    loadDefaultSettings() {
        const savedDefaultMinutes = localStorage.getItem('defaultMinutes');
        if (savedDefaultMinutes) {
            document.getElementById('defaultMinutes').value = savedDefaultMinutes;
        }
    }

    saveTimers() {
        const timersData = this.timers.map(timer => ({
            ...timer,
            startTime: timer.startTime ? timer.startTime.toISOString() : null,
            endTime: timer.endTime ? timer.endTime.toISOString() : null
        }));
        localStorage.setItem('timers', JSON.stringify(timersData));
    }

    loadTimers() {
        const saved = localStorage.getItem('timers');
        if (saved) {
            try {
                const timersData = JSON.parse(saved);
                this.timers = timersData.map(timer => ({
                    ...timer,
                    startTime: timer.startTime ? new Date(timer.startTime) : null,
                    endTime: timer.endTime ? new Date(timer.endTime) : null,
                    originalDuration: timer.originalDuration || timer.duration
                }));

                // Find the highest ID and timer counter
                if (this.timers.length > 0) {
                    this.timerId = Math.max(...this.timers.map(t => t.id));
                    // Extract timer numbers for counter
                    const timerNumbers = this.timers
                        .map(t => t.name.match(/Timer(\d+)/))
                        .filter(match => match)
                        .map(match => parseInt(match[1]));
                    this.timerCounter = timerNumbers.length > 0 ? Math.max(...timerNumbers) : 0;
                }

                // Restore all timers accurately
                this.timers.forEach(timer => {
                    if (timer.isRunning && !timer.isCompleted && timer.startTime) {
                        // Calculate elapsed time since startTime (more accurate)
                        const now = Date.now();
                        const elapsed = (now - timer.startTime.getTime()) / 1000;
                        timer.remaining = Math.max(0, Math.round(timer.duration - elapsed));
                        if (timer.remaining <= 0) {
                            timer.isRunning = false;
                            timer.isCompleted = true;
                            timer.remaining = 0;
                        }
                    } else if (!timer.isRunning && !timer.isCompleted) {
                        // Stopped timer: remaining = duration
                        timer.remaining = timer.duration;
                    }
                    this.renderTimer(timer);
                });
            } catch (e) {
                console.error('Error loading timers:', e);
                localStorage.removeItem('timers');
            }
        }
    }

    adjustTimerDuration(id, delta) {
        const timer = this.timers.find(t => t.id === id);
        if (!timer || timer.isRunning || timer.isCompleted) return;
        const newMinutes = Math.max(1, Math.round(timer.duration / 60) + delta);
        timer.duration = newMinutes * 60;
        timer.remaining = timer.duration;
        timer.originalDuration = timer.duration;
        this.updateTimerDisplay(timer);
        this.saveTimers();
    }

    updateTimerNameFromInput(id, newName) {
        const timer = this.timers.find(t => t.id === id);
        if (!timer) return;
        const trimmed = newName.trim();
        if (trimmed && trimmed !== timer.name) {
            timer.name = trimmed;
            this.saveTimers();
        }
    }

    renderAllTimers() {
        const container = document.getElementById('timersContainer');
        // Remove all timer cards except the add button
        Array.from(container.querySelectorAll('.timer-card')).forEach(card => card.remove());
        // Render all timers in order
        this.timers.forEach(timer => this.renderTimer(timer));
    }
}

// Place this after the class definition, before DOMContentLoaded
// --- Audio unlock for browsers ---
let audioUnlocked = false;
function unlockAudio() {
    if (audioUnlocked) return;
    const timerSound = document.getElementById('timerSound');
    const notificationSound = document.getElementById('notificationSound');
    if (timerSound) {
        timerSound.muted = true;
        timerSound.play().catch(() => {});
        timerSound.pause();
        timerSound.currentTime = 0;
        timerSound.muted = localStorage.getItem('timerMuted') === '1';
    }
    if (notificationSound) {
        notificationSound.muted = true;
        notificationSound.play().catch(() => {});
        notificationSound.pause();
        notificationSound.currentTime = 0;
        notificationSound.muted = localStorage.getItem('timerMuted') === '1';
    }
    audioUnlocked = true;
}
document.addEventListener('pointerdown', unlockAudio, { once: true });
// --- End audio unlock ---

// Request notification permission
if ('Notification' in window) {
    Notification.requestPermission();
}

// Initialize the app
window.app = new TimerApp();

// Add event listener for new add button after DOM and app are ready
window.addEventListener('DOMContentLoaded', () => {
    if (window.app) {
        const addBtn = document.getElementById('addTimerBtn');
        if (addBtn) {
            addBtn.addEventListener('click', () => window.app.addTimer());
        }
        const defaultInput = document.getElementById('defaultMinutes');
        const minusBtn = document.getElementById('defaultMinus');
        const plusBtn = document.getElementById('defaultPlus');
        if (minusBtn && defaultInput) {
            minusBtn.addEventListener('click', () => {
                let val = parseInt(defaultInput.value, 10) || 1;
                val = Math.max(1, val - 1);
                defaultInput.value = val;
                defaultInput.dispatchEvent(new Event('change'));
            });
        }
        if (plusBtn && defaultInput) {
            plusBtn.addEventListener('click', () => {
                let val = parseInt(defaultInput.value, 10) || 1;
                val = Math.min(999, val + 1);
                defaultInput.value = val;
                defaultInput.dispatchEvent(new Event('change'));
            });
        }

        // Fullscreen button logic
        const fullscreenBtn = document.getElementById('fullscreenBtn');
        if (fullscreenBtn) {
            const icon = fullscreenBtn.querySelector('.material-icons');
            function updateIcon() {
                if (document.fullscreenElement) {
                    icon.textContent = 'fullscreen_exit';
                } else {
                    icon.textContent = 'fullscreen';
                }
            }
            fullscreenBtn.addEventListener('click', () => {
                if (!document.fullscreenElement) {
                    document.documentElement.requestFullscreen();
                } else {
                    document.exitFullscreen();
                }
            });
            document.addEventListener('fullscreenchange', updateIcon);
            updateIcon();
        }

        // Mute button logic
        const muteBtn = document.getElementById('muteBtn');
        const timerSound = document.getElementById('timerSound');
        const notificationSound = document.getElementById('notificationSound');
        function setMuted(muted) {
            if (muteBtn) {
                const icon = muteBtn.querySelector('.material-icons');
                icon.textContent = muted ? 'volume_off' : 'volume_up';
            }
            if (timerSound) timerSound.muted = muted;
            if (notificationSound) notificationSound.muted = muted;
            localStorage.setItem('timerMuted', muted ? '1' : '0');
        }
        if (muteBtn) {
            muteBtn.addEventListener('click', () => {
                const isMuted = localStorage.getItem('timerMuted') === '1';
                setMuted(!isMuted);
            });
            // Initialize state from localStorage
            const isMuted = localStorage.getItem('timerMuted') === '1';
            setMuted(isMuted);
        }
    }
}); 