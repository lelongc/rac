// flashcard.js: Interactive Flashcard Engine for ETS TOEIC 2024
class FlashcardApp {
  constructor(vocabBank) {
    this.vocabBank = vocabBank || [];
    this.currentList = [...this.vocabBank];
    this.currentIndex = 0;
    this.isFlipped = false;
    this.selectedPart = 'all';

    this.initElements();
    this.bindEvents();
  }

  initElements() {
    this.cardContainer = document.getElementById('flashcard3D');
    this.wordEl = document.getElementById('fcWord');
    this.ipaEl = document.getElementById('fcIpa');
    this.posEl = document.getElementById('fcPos');
    this.partBadgeEl = document.getElementById('fcPartBadge');
    this.meaningEl = document.getElementById('fcMeaning');
    this.exampleEl = document.getElementById('fcExample');
    this.counterEl = document.getElementById('fcCounter');
    this.prevBtn = document.getElementById('fcPrev');
    this.nextBtn = document.getElementById('fcNext');
    this.flipBtn = document.getElementById('fcFlipBtn');
    this.speakBtn = document.getElementById('fcSpeak');
    this.starBtn = document.getElementById('fcStar');
    this.partFilter = document.getElementById('fcPartFilter');
    this.shuffleBtn = document.getElementById('fcShuffle');
  }

  bindEvents() {
    if (!this.cardContainer) return;

    this.cardContainer.addEventListener('click', (e) => {
      // Avoid flipping when clicking star or speak
      if (e.target.closest('.icon-btn') || e.target.closest('button')) return;
      this.flip();
    });

    if (this.flipBtn) {
      this.flipBtn.addEventListener('click', () => this.flip());
    }

    this.prevBtn.addEventListener('click', () => this.prev());
    this.nextBtn.addEventListener('click', () => this.next());

    this.speakBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      this.speakCurrent();
    });

    this.starBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      this.toggleStarCurrent();
    });

    if (this.shuffleBtn) {
      this.shuffleBtn.addEventListener('click', () => this.shuffle());
    }

    if (this.partFilter) {
      this.partFilter.addEventListener('change', (e) => {
        this.filterByPart(e.target.value);
      });
    }

    // Keyboard navigation
    document.addEventListener('keydown', (e) => {
      const flashcardView = document.getElementById('flashcardView');
      if (flashcardView && flashcardView.style.display !== 'none') {
        if (e.key === ' ' || e.key === 'ArrowUp' || e.key === 'ArrowDown') {
          e.preventDefault();
          this.flip();
        } else if (e.key === 'ArrowLeft') {
          this.prev();
        } else if (e.key === 'ArrowRight') {
          this.next();
        }
      }
    });
  }

  filterByPart(part) {
    this.selectedPart = part;
    if (part === 'all') {
      this.currentList = [...this.vocabBank];
    } else if (part === 'starred') {
      const starred = window.StorageManager.getStarredVocab();
      this.currentList = this.vocabBank.filter(v => starred.includes(v.word));
    } else {
      const pNum = parseInt(part);
      this.currentList = this.vocabBank.filter(v => v.part === pNum);
    }

    this.currentIndex = 0;
    this.isFlipped = false;
    this.render();
  }

  shuffle() {
    for (let i = this.currentList.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [this.currentList[i], this.currentList[j]] = [this.currentList[j], this.currentList[i]];
    }
    this.currentIndex = 0;
    this.isFlipped = false;
    this.render();
  }

  flip() {
    this.isFlipped = !this.isFlipped;
    if (this.isFlipped) {
      this.cardContainer.classList.add('flipped');
    } else {
      this.cardContainer.classList.remove('flipped');
    }
  }

  prev() {
    if (this.currentList.length === 0) return;
    this.currentIndex = (this.currentIndex - 1 + this.currentList.length) % this.currentList.length;
    this.resetAndRender();
  }

  next() {
    if (this.currentList.length === 0) return;
    this.currentIndex = (this.currentIndex + 1) % this.currentList.length;
    this.resetAndRender();
  }

  resetAndRender() {
    this.isFlipped = false;
    this.cardContainer.classList.remove('flipped');
    setTimeout(() => this.render(), 120);
  }

  render() {
    if (this.currentList.length === 0) {
      this.wordEl.textContent = "Không có từ vựng";
      this.ipaEl.textContent = "";
      this.posEl.textContent = "";
      this.meaningEl.textContent = "Chưa có từ nào trong danh mục này!";
      this.exampleEl.textContent = "";
      this.counterEl.textContent = "0 / 0";
      return;
    }

    const item = this.currentList[this.currentIndex];
    this.wordEl.textContent = item.word;
    this.ipaEl.textContent = item.ipa || "";
    this.posEl.textContent = item.pos ? `[${item.pos}]` : "";
    this.partBadgeEl.textContent = `Part ${item.part} • Q${item.questionId}`;
    this.meaningEl.textContent = item.meaning;
    this.exampleEl.textContent = item.example ? `“${item.example}”` : "";
    this.counterEl.textContent = `${this.currentIndex + 1} / ${this.currentList.length}`;

    // Update star button
    const starred = window.StorageManager.getStarredVocab();
    if (starred.includes(item.word)) {
      this.starBtn.style.color = "var(--warning)";
      this.starBtn.querySelector('i').className = "ph-fill ph-star";
    } else {
      this.starBtn.style.color = "var(--text-muted)";
      this.starBtn.querySelector('i').className = "ph-bold ph-star";
    }
  }

  speakCurrent() {
    if (this.currentList.length === 0) return;
    const word = this.currentList[this.currentIndex].word;
    if ('speechSynthesis' in window) {
      window.speechSynthesis.cancel();
      const utterance = new SpeechSynthesisUtterance(word);
      utterance.lang = 'en-US';
      utterance.rate = 0.9;
      window.speechSynthesis.speak(utterance);
    }
  }

  toggleStarCurrent() {
    if (this.currentList.length === 0) return;
    const word = this.currentList[this.currentIndex].word;
    const isStarred = window.StorageManager.toggleStarredVocab(word);
    this.render();
  }
}

window.FlashcardApp = FlashcardApp;
