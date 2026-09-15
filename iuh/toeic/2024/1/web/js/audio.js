// audio.js: Sticky Audio Player controller for ETS TOEIC 2024 (Tests 1 - 10)
class AudioPlayer {
  constructor() {
    this.audioElement = new Audio();
    this.isPlaying = false;
    this.currentPart = 1;
    this.currentTest = 1;
    this.playbackRate = 1.0;

    this.initElements();
    this.bindEvents();
    this.loadPart(1, false);
  }

  initElements() {
    this.playBtn = document.getElementById('audioPlayPause');
    this.playIcon = document.getElementById('playPauseIcon');
    this.rewindBtn = document.getElementById('audioRewind');
    this.forwardBtn = document.getElementById('audioForward');
    this.timeline = document.getElementById('audioTimeline');
    this.currentTimeEl = document.getElementById('audioCurrentTime');
    this.totalTimeEl = document.getElementById('audioTotalTime');
    this.speedSelect = document.getElementById('audioSpeed');
    this.trackNameEl = document.getElementById('audioTrackName');
    this.playerBar = document.getElementById('audioPlayerBar');
  }

  bindEvents() {
    if (!this.playBtn) return;

    this.playBtn.addEventListener('click', () => this.togglePlay());
    this.rewindBtn.addEventListener('click', () => this.seekBy(-5));
    this.forwardBtn.addEventListener('click', () => this.seekBy(5));

    if (this.speedSelect) {
      this.speedSelect.addEventListener('change', (e) => {
        this.playbackRate = parseFloat(e.target.value);
        this.audioElement.playbackRate = this.playbackRate;
      });
    }

    if (this.timeline) {
      this.timeline.addEventListener('input', (e) => {
        if (this.audioElement.duration) {
          this.audioElement.currentTime = (e.target.value / 100) * this.audioElement.duration;
        }
      });
    }

    this.audioElement.addEventListener('timeupdate', () => this.updateProgress());
    this.audioElement.addEventListener('loadedmetadata', () => {
      if (this.totalTimeEl) {
        this.totalTimeEl.textContent = this.formatTime(this.audioElement.duration);
      }
    });
    this.audioElement.addEventListener('ended', () => {
      this.isPlaying = false;
      this.updatePlayState();
    });
  }

  getTrackSrc(partNum) {
    return `assets/audio/test${this.currentTest}/part${partNum}.mp3`;
  }

  getTrackName(partNum) {
    const names = {
      1: `Test ${this.currentTest} • Part 1: Photographs`,
      2: `Test ${this.currentTest} • Part 2: Question-Response`,
      3: `Test ${this.currentTest} • Part 3: Conversations`,
      4: `Test ${this.currentTest} • Part 4: Short Talks`
    };
    return names[partNum] || `Part ${partNum}`;
  }

  setTest(testId) {
    this.currentTest = parseInt(testId, 10);
    this.loadPart(this.currentPart, false);
  }

  loadPart(partNum, autoPlay = true) {
    if (partNum < 1 || partNum > 4) {
      return;
    }

    this.currentPart = partNum;
    this.audioElement.src = this.getTrackSrc(partNum);
    this.audioElement.playbackRate = this.playbackRate;
    if (this.trackNameEl) {
      this.trackNameEl.textContent = this.getTrackName(partNum);
    }

    if (autoPlay) {
      this.play();
    } else {
      this.pause();
    }
  }

  togglePlay() {
    if (this.isPlaying) {
      this.pause();
    } else {
      this.play();
    }
  }

  play() {
    this.audioElement.play().then(() => {
      this.isPlaying = true;
      this.updatePlayState();
    }).catch(e => {
      console.warn("Autoplay blocked or audio load error:", e);
      this.isPlaying = false;
      this.updatePlayState();
    });
  }

  pause() {
    this.audioElement.pause();
    this.isPlaying = false;
    this.updatePlayState();
  }

  seekBy(seconds) {
    if (this.audioElement.duration) {
      this.audioElement.currentTime = Math.max(0, Math.min(this.audioElement.duration, this.audioElement.currentTime + seconds));
    }
  }

  updateProgress() {
    if (!this.timeline || !this.audioElement.duration) return;
    const progress = (this.audioElement.currentTime / this.audioElement.duration) * 100;
    this.timeline.value = progress;
    if (this.currentTimeEl) {
      this.currentTimeEl.textContent = this.formatTime(this.audioElement.currentTime);
    }
  }

  updatePlayState() {
    if (!this.playIcon) return;
    if (this.isPlaying) {
      this.playIcon.className = "ph-bold ph-pause";
      this.playBtn.classList.add("playing");
    } else {
      this.playIcon.className = "ph-bold ph-play";
      this.playBtn.classList.remove("playing");
    }
  }

  formatTime(seconds) {
    if (isNaN(seconds)) return "00:00";
    const mins = Math.floor(seconds / 60);
    const secs = Math.floor(seconds % 60);
    return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
  }

  showPlayer(show = true) {
    if (this.playerBar) {
      this.playerBar.style.display = show ? "flex" : "none";
    }
  }
}

window.AudioPlayer = AudioPlayer;
