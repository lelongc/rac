// app.js: Main Application Controller for ETS TOEIC 2024 Test 1 Pro Master
class TOEICApp {
  constructor() {
    this.questions = [];
    this.vocabBank = [];
    this.grammarBank = [];
    this.currentMode = 'practice'; // 'practice' | 'exam' | 'flashcard' | 'grammar'
    this.selectedPart = 'all';
    this.selectedFilter = 'all';
    this.examTimeLeft = 120 * 60; // 120 minutes in seconds
    this.timerInterval = null;
    this.isExamSubmitted = false;
    this.audioPlayer = null;
    this.flashcardApp = null;
    this.currentQAudio = new Audio();
    this.activeQId = null;
    this.loopMap = {};

    // Lightbox Pan & Zoom State
    this.zoomScale = 1;
    this.zoomX = 0;
    this.zoomY = 0;
    this.isDragging = false;
    this.dragStartX = 0;
    this.dragStartY = 0;
    this.hasDragged = false;
    this.currentZoomSrc = '';
    this.currentReviewAnswers = null;
    this.currentReviewResultId = null;

    this.currentTestId = window.StorageManager.getCurrentTest();
    this.init();
  }

  async init() {
    try { this.initTheme(); } catch (e) { console.error("initTheme error:", e); }

    // Ensure questions view is visible on startup
    const questionsView = document.getElementById('questionsView');
    if (questionsView) questionsView.style.display = 'flex';

    // 1. Load questions data first
    await this.loadData();

    // 2. Render questions immediately as top priority so user sees them on screen
    try {
      this.renderQuestions();
      this.updatePalette();
      this.updateProgressIndicator();
    } catch (e) {
      console.error("renderQuestions error:", e);
    }

    // 3. Initialize auxiliary modules safely
    try {
      this.audioPlayer = new window.AudioPlayer();
      this.audioPlayer.setTest(this.currentTestId);
    } catch (e) { console.error("AudioPlayer init error:", e); }

    try {
      this.flashcardApp = new window.FlashcardApp(this.vocabBank);
    } catch (e) { console.error("FlashcardApp init error:", e); }

    try { this.initQuestionAudioListeners(); } catch (e) { console.error("initQuestionAudioListeners error:", e); }
    try { this.initTestSelector(); } catch (e) { console.error("initTestSelector error:", e); }
    try { this.initNavbar(); } catch (e) { console.error("initNavbar error:", e); }
    try { this.initPartTabs(); } catch (e) { console.error("initPartTabs error:", e); }
    try { this.initFilter(); } catch (e) { console.error("initFilter error:", e); }
    try { this.initModals(); } catch (e) { console.error("initModals error:", e); }
    try { this.initHistoryModal(); } catch (e) { console.error("initHistoryModal error:", e); }
    try { this.initImageZoom(); } catch (e) { console.error("initImageZoom error:", e); }
    try { this.initSidebar(); } catch (e) { console.error("initSidebar error:", e); }
    try { this.renderGrammarList(); } catch (e) { console.error("renderGrammarList error:", e); }
  }

  initTheme() {
    const savedTheme = window.StorageManager.getTheme();
    document.documentElement.setAttribute('data-theme', savedTheme);
    const themeBtn = document.getElementById('themeToggle');
    if (themeBtn) {
      themeBtn.innerHTML = savedTheme === 'dark' ? '<i class="ph-bold ph-sun"></i>' : '<i class="ph-bold ph-moon"></i>';
      themeBtn.addEventListener('click', () => {
        const current = document.documentElement.getAttribute('data-theme');
        const next = current === 'dark' ? 'light' : 'dark';
        document.documentElement.setAttribute('data-theme', next);
        window.StorageManager.setTheme(next);
        themeBtn.innerHTML = next === 'dark' ? '<i class="ph-bold ph-sun"></i>' : '<i class="ph-bold ph-moon"></i>';
      });
    }
  }

  async loadData() {
    let tid = parseInt(this.currentTestId, 10);
    if (isNaN(tid) || tid < 1 || tid > 10) {
      tid = 1;
    }
    this.currentTestId = tid;
    if (window.StorageManager) {
      window.StorageManager.setCurrentTest(tid);
    }

    // 1. Load questions (Priority 1)
    try {
      const testRes = await fetch(`data/test${tid}.json`);
      if (!testRes.ok) throw new Error(`HTTP ${testRes.status}`);
      const testData = await testRes.json();
      this.questions = testData.questions || [];
      console.log(`Loaded Test ${tid}: ${this.questions.length} questions.`);
    } catch (e) {
      console.error(`Failed to load test${tid}.json:`, e);
      try {
        const fallbackRes = await fetch('data/test1.json');
        if (fallbackRes.ok) {
          const fallbackData = await fallbackRes.json();
          this.questions = fallbackData.questions || [];
          this.currentTestId = 1;
          if (window.StorageManager) window.StorageManager.setCurrentTest(1);
          console.log(`Fallback to Test 1: ${this.questions.length} questions.`);
        }
      } catch (err2) {
        console.error("Fallback load failed:", err2);
      }
    }

    // 2. Load auxiliary banks in background without blocking questions
    fetch('data/vocab_bank.json')
      .then(r => r.json())
      .then(v => {
        this.vocabBank = v;
        if (this.flashcardApp) this.flashcardApp.vocabBank = v;
      })
      .catch(e => console.warn("Vocab bank load error:", e));

    fetch('data/grammar_bank.json')
      .then(r => r.json())
      .then(g => {
        this.grammarBank = g;
        this.renderGrammarList();
      })
      .catch(e => console.warn("Grammar bank load error:", e));
  }

  initTestSelector() {
    const testSelect = document.getElementById('testSelect');
    if (testSelect) {
      testSelect.value = this.currentTestId.toString();
      testSelect.addEventListener('change', (e) => {
        const newTest = parseInt(e.target.value, 10);
        this.switchTest(newTest);
      });
    }
  }

  async switchTest(newTestId) {
    const tid = parseInt(newTestId, 10);
    const validTestId = (!isNaN(tid) && tid >= 1 && tid <= 10) ? tid : 1;

    if (this.currentTestId === validTestId && this.questions && this.questions.length > 0) return;

    if (this.timerInterval) {
      this.stopExamTimer();
    }

    this.currentTestId = validTestId;
    window.StorageManager.setCurrentTest(validTestId);

    const testSelect = document.getElementById('testSelect');
    if (testSelect) testSelect.value = validTestId.toString();

    if (this.audioPlayer) {
      this.audioPlayer.setTest(validTestId);
    }

    try {
      const res = await fetch(`data/test${validTestId}.json`);
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const data = await res.json();
      this.questions = data.questions || [];
    } catch (e) {
      console.error(`Failed to load test ${validTestId}:`, e);
      if (validTestId !== 1) {
        return this.switchTest(1);
      }
      return;
    }

    this.isExamSubmitted = false;
    this.currentReviewAnswers = null;
    this.selectedPart = 'all';
    this.selectedFilter = 'all';
    document.title = `ETS TOEIC 2024 - Test ${validTestId} Pro Master`;

    const subtext = document.getElementById('brandSubtext');
    if (subtext) {
      subtext.textContent = `FULL 200 CÂU • TEST ${validTestId} • GIẢI CHI TIẾT 100% ETS`;
    }

    this.renderQuestions();
    this.updatePalette();
    this.updateProgressIndicator();

    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  initNavbar() {
    const modeBtns = document.querySelectorAll('.mode-btn');
    modeBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        modeBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        const mode = btn.dataset.mode;
        this.switchMode(mode);
      });
    });
  }

  switchMode(mode) {
    this.currentMode = mode;
    const questionsView = document.getElementById('questionsView');
    const flashcardView = document.getElementById('flashcardView');
    const grammarView = document.getElementById('grammarView');
    const sidebar = document.getElementById('sidebarColumn');
    const examTimerBox = document.getElementById('examTimerBox');
    const partNavBar = document.getElementById('partNavBar');
    const clearBtnText = document.getElementById('clearBtnText');
    const btnSubmitText = document.getElementById('btnSubmitText');

    // Synchronize active indicator on navbar buttons
    document.querySelectorAll('.mode-btn').forEach(b => {
      b.classList.toggle('active', b.dataset.mode === mode);
    });

    if (mode === 'practice') {
      questionsView.style.display = 'flex';
      flashcardView.style.display = 'none';
      grammarView.style.display = 'none';
      sidebar.style.display = 'block';
      examTimerBox.style.display = 'none';
      partNavBar.style.display = 'flex';
      if (clearBtnText) clearBtnText.textContent = 'Xóa kết quả luyện tập';
      if (btnSubmitText) btnSubmitText.textContent = 'Chấm điểm luyện tập';
      this.currentReviewAnswers = null;
      this.currentReviewResultId = null;
      this.renderReviewBanner();
      this.stopExamTimer();
      this.renderQuestions();
      this.updatePalette();
      this.updateProgressIndicator();
    } else if (mode === 'exam') {
      questionsView.style.display = 'flex';
      flashcardView.style.display = 'none';
      grammarView.style.display = 'none';
      sidebar.style.display = 'block';
      examTimerBox.style.display = 'block';
      partNavBar.style.display = 'flex';
      if (clearBtnText) clearBtnText.textContent = 'Hủy & Làm lại bài thi';
      if (btnSubmitText) btnSubmitText.textContent = 'Nộp bài & Chấm điểm ETS';
      if (!this.currentReviewResultId) {
        this.renderReviewBanner();
      }
      this.startExam();
    } else if (mode === 'flashcard') {
      questionsView.style.display = 'none';
      flashcardView.style.display = 'flex';
      grammarView.style.display = 'none';
      sidebar.style.display = 'none';
      partNavBar.style.display = 'none';
      this.currentReviewResultId = null;
      this.renderReviewBanner();
      this.stopExamTimer();
      this.flashcardApp.render();
    } else if (mode === 'grammar') {
      questionsView.style.display = 'none';
      flashcardView.style.display = 'none';
      grammarView.style.display = 'block';
      sidebar.style.display = 'none';
      partNavBar.style.display = 'none';
      this.currentReviewResultId = null;
      this.renderReviewBanner();
      this.stopExamTimer();
    }
  }

  getCurrentAnswers() {
    if (this.currentMode === 'practice') {
      return window.StorageManager.getPracticeAnswers(this.currentTestId);
    } else if (this.currentMode === 'exam') {
      if (this.isExamSubmitted && this.currentReviewAnswers) {
        return this.currentReviewAnswers;
      }
      return window.StorageManager.getExamAnswers(this.currentTestId);
    }
    return {};
  }

  startExam() {
    this.isExamSubmitted = false;
    this.currentReviewAnswers = null;
    this.examTimeLeft = 120 * 60;
    this.renderQuestions();
    this.updatePalette();
    this.updateProgressIndicator();
    this.startExamTimer();
  }

  startExamTimer() {
    clearInterval(this.timerInterval);
    const timerDisplay = document.getElementById('timerDisplay');

    this.timerInterval = setInterval(() => {
      if (this.examTimeLeft <= 0) {
        clearInterval(this.timerInterval);
        this.submitExam(true);
        return;
      }
      this.examTimeLeft--;
      const hours = Math.floor(this.examTimeLeft / 3600);
      const minutes = Math.floor((this.examTimeLeft % 3600) / 60);
      const seconds = this.examTimeLeft % 60;

      timerDisplay.textContent = `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
      if (this.examTimeLeft < 300) {
        timerDisplay.classList.add('low-time');
      } else {
        timerDisplay.classList.remove('low-time');
      }
    }, 1000);
  }

  stopExamTimer() {
    clearInterval(this.timerInterval);
  }

  initPartTabs() {
    const tabs = document.querySelectorAll('.part-tab');
    tabs.forEach(tab => {
      tab.addEventListener('click', () => {
        tabs.forEach(t => t.classList.remove('active'));
        tab.classList.add('active');
        this.selectedPart = tab.dataset.part;
        this.renderQuestions();

        // If selecting LC part, switch audio track
        if (['1', '2', '3', '4'].includes(this.selectedPart)) {
          this.audioPlayer.loadPart(parseInt(this.selectedPart), false);
          this.audioPlayer.showPlayer(true);
        }
      });
    });
  }

  initFilter() {
    const filterSelect = document.getElementById('questionFilter');
    if (filterSelect) {
      filterSelect.addEventListener('change', (e) => {
        this.selectedFilter = e.target.value;
        this.renderQuestions();
      });
    }
  }

  initSidebar() {
    const submitBtn = document.getElementById('btnSubmitTest');
    if (submitBtn) {
      submitBtn.addEventListener('click', () => this.confirmSubmitExam());
    }

    const clearAnswersBtn = document.getElementById('btnClearAnswers');
    if (clearAnswersBtn) {
      clearAnswersBtn.addEventListener('click', () => this.handleClearAnswers());
    }

    const clearQuickBtn = document.getElementById('btnClearAnswersQuick');
    if (clearQuickBtn) {
      clearQuickBtn.addEventListener('click', () => this.handleClearAnswers());
    }

    const resetBarBtn = document.getElementById('btnResetPracticeBar');
    if (resetBarBtn) {
      resetBarBtn.addEventListener('click', () => this.handleClearAnswers());
    }

    const sidebarHistoryBtn = document.getElementById('btnSidebarHistory');
    if (sidebarHistoryBtn) {
      sidebarHistoryBtn.addEventListener('click', () => this.showExamHistoryModal());
    }
  }

  handleClearAnswers() {
    if (this.currentMode === 'practice') {
      const answers = window.StorageManager.getPracticeAnswers(this.currentTestId);
      const count = Object.keys(answers).length;
      if (count === 0) {
        this.showToast(`Bạn chưa chọn câu trả lời nào ở bài thi Test ${this.currentTestId}.`, 'info');
        return;
      }
      if (confirm(`Bạn có chắc chắn muốn xóa toàn bộ ${count} câu trả lời luyện tập của Test ${this.currentTestId} để làm lại từ đầu không?\n\n(Lựa chọn của bạn ở các câu hỏi Test ${this.currentTestId} sẽ được đặt lại về trạng thái ban đầu)`)) {
        window.StorageManager.clearPracticeAnswers(this.currentTestId);
        // Reset filter to 'all' so questions don't disappear if user was filtering by answered/wrong
        if (this.selectedFilter === 'answered' || this.selectedFilter === 'wrong') {
          this.selectedFilter = 'all';
          const filterSelect = document.getElementById('questionFilter');
          if (filterSelect) filterSelect.value = 'all';
        }
        this.renderQuestions();
        this.updatePalette();
        this.updateProgressIndicator();
        this.showToast(`Đã xóa toàn bộ câu trả lời luyện tập Test ${this.currentTestId}!`, 'info');
      }
    } else if (this.currentMode === 'exam') {
      if (this.isExamSubmitted) {
        if (confirm(`Bạn muốn làm lại đề thi Test ${this.currentTestId} (120 phút) từ đầu không?`)) {
          this.startExam();
          this.showToast(`Bắt đầu làm lại bài thi Test ${this.currentTestId}!`, 'info');
        }
      } else {
        const answers = window.StorageManager.getExamAnswers(this.currentTestId);
        const count = Object.keys(answers).length;
        if (confirm(`Bạn có chắc chắn muốn hủy bài thi đang làm dở (${count} câu đã làm) để bắt đầu lại từ đầu không?`)) {
          window.StorageManager.clearExamAnswers(this.currentTestId);
          this.startExam();
          this.showToast(`Đã đặt lại bài thi thử Test ${this.currentTestId}!`, 'info');
        }
      }
    }
  }

  confirmSubmitExam() {
    const answers = this.getCurrentAnswers();
    const answeredCount = Object.keys(answers).length;
    const unanswered = 200 - answeredCount;

    let msg = `Bạn đã hoàn thành ${answeredCount}/200 câu.`;
    if (unanswered > 0) {
      msg += ` Còn ${unanswered} câu chưa làm. Bạn có chắc chắn muốn nộp bài để chấm điểm ngay không?`;
    } else {
      msg += ` Bạn đã hoàn thành đủ tất cả câu hỏi. Nộp bài ngay để xem điểm thi?`;
    }

    if (confirm(msg)) {
      this.submitExam();
    }
  }

  submitExam(isTimeOut = false) {
    this.stopExamTimer();
    this.isExamSubmitted = true;

    const answers = { ...this.getCurrentAnswers() };
    this.currentReviewAnswers = answers;

    let lcCorrect = 0;
    let rcCorrect = 0;
    const partStats = {
      1: { c: 0, t: 6 },
      2: { c: 0, t: 25 },
      3: { c: 0, t: 39 },
      4: { c: 0, t: 30 },
      5: { c: 0, t: 30 },
      6: { c: 0, t: 16 },
      7: { c: 0, t: 54 }
    };

    this.questions.forEach(q => {
      const userChoice = answers[q.id];
      const isCorrect = userChoice === q.correctAnswer;
      const part = q.part;

      if (isCorrect) {
        partStats[part].c++;
        if (part <= 4) lcCorrect++;
        else rcCorrect++;
      }
    });

    const scaledLC = this.calculateScaledScore(lcCorrect, 'LC');
    const scaledRC = this.calculateScaledScore(rcCorrect, 'RC');
    const totalScore = scaledLC + scaledRC;
    const totalCorrect = lcCorrect + rcCorrect;

    const timeSpentSec = (120 * 60) - Math.max(0, this.examTimeLeft);
    const minutesSpent = Math.max(1, Math.round(timeSpentSec / 60));

    // Save exam result into permanent history
    const examResult = {
      id: 'exam_' + Date.now(),
      testId: this.currentTestId,
      testTitle: `ETS 2024 • Test ${this.currentTestId}`,
      timestamp: Date.now(),
      dateStr: new Date().toLocaleString('vi-VN', {
        year: 'numeric', month: '2-digit', day: '2-digit',
        hour: '2-digit', minute: '2-digit'
      }),
      totalScore: totalScore,
      lcScore: scaledLC,
      rcScore: scaledRC,
      lcCorrect: lcCorrect,
      rcCorrect: rcCorrect,
      totalCorrect: totalCorrect,
      partStats: partStats,
      timeSpentMinutes: minutesSpent,
      answers: answers
    };
    window.StorageManager.saveExamResult(examResult);

    // Clear in-progress exam answers if in exam mode
    if (this.currentMode === 'exam') {
      window.StorageManager.clearExamAnswers(this.currentTestId);
    }

    this.showScoreModal(scaledLC, scaledRC, totalScore, lcCorrect, rcCorrect, partStats);
    this.renderQuestions();
    this.updatePalette();
    this.updateProgressIndicator();
    this.showToast(`Đã nộp bài & lưu kết quả thi Test ${this.currentTestId}: ${totalScore} điểm!`, 'success');
  }

  calculateScaledScore(rawScore, section) {
    // Official ETS 2024 Scaled Score Conversion formula estimation
    if (rawScore <= 0) return 5;
    if (rawScore >= 96) return 495;

    let scaled = 5;
    if (section === 'LC') {
      if (rawScore <= 15) scaled = 5 + rawScore * 5;
      else if (rawScore <= 30) scaled = 80 + (rawScore - 15) * 5;
      else if (rawScore <= 60) scaled = 155 + (rawScore - 30) * 5;
      else if (rawScore <= 85) scaled = 305 + (rawScore - 60) * 5.5;
      else scaled = 445 + (rawScore - 85) * 5;
    } else {
      if (rawScore <= 15) scaled = 5 + rawScore * 4;
      else if (rawScore <= 30) scaled = 65 + (rawScore - 15) * 5;
      else if (rawScore <= 60) scaled = 140 + (rawScore - 30) * 5;
      else if (rawScore <= 85) scaled = 290 + (rawScore - 60) * 5.8;
      else scaled = 435 + (rawScore - 85) * 5.5;
    }

    // Round to nearest 5
    return Math.min(495, Math.max(5, Math.round(scaled / 5) * 5));
  }

  showScoreModal(lcScore, rcScore, totalScore, lcCorrect, rcCorrect, partStats) {
    const modal = document.getElementById('scoreModal');
    document.getElementById('modalTotalScore').textContent = totalScore;
    document.getElementById('modalLCScore').textContent = `${lcScore} / 495 (${lcCorrect}/100)`;
    document.getElementById('modalRCScore').textContent = `${rcScore} / 495 (${rcCorrect}/100)`;

    const breakdownContainer = document.getElementById('partBreakdownGrid');
    breakdownContainer.innerHTML = '';

    for (let p = 1; p <= 7; p++) {
      const stat = partStats[p];
      const pct = Math.round((stat.c / stat.t) * 100);
      const div = document.createElement('div');
      div.className = 'score-box';
      div.innerHTML = `
        <h4>Part ${p}</h4>
        <div class="score-val" style="font-size: 1.2rem;">${stat.c} / ${stat.t}</div>
        <div style="font-size: 0.75rem; color: ${pct >= 70 ? 'var(--success)' : 'var(--warning)'}; font-weight: 700;">${pct}% Đúng</div>
      `;
      breakdownContainer.appendChild(div);
    }

    modal.classList.add('active');
  }

  initModals() {
    const scoreModal = document.getElementById('scoreModal');
    const btnReview = document.getElementById('btnReviewAfterScore');
    const closeScoreModal = document.getElementById('closeScoreModal');
    const btnScoreHistory = document.getElementById('btnOpenHistoryFromScore');

    if (closeScoreModal && scoreModal) {
      closeScoreModal.addEventListener('click', () => scoreModal.classList.remove('active'));
    }
    if (scoreModal) {
      scoreModal.addEventListener('click', (e) => {
        if (e.target === scoreModal) scoreModal.classList.remove('active');
      });
    }
    if (btnReview) {
      btnReview.addEventListener('click', () => {
        if (scoreModal) scoreModal.classList.remove('active');
        this.switchMode('practice');
      });
    }
    if (btnScoreHistory) {
      btnScoreHistory.addEventListener('click', () => {
        if (scoreModal) scoreModal.classList.remove('active');
        this.showExamHistoryModal();
      });
    }
  }

  initHistoryModal() {
    const historyModal = document.getElementById('examHistoryModal');
    const closeBtn = document.getElementById('closeExamHistoryModal');
    const openBtnNav = document.getElementById('btnOpenHistory');
    const filterSelect = document.getElementById('historyFilterSelect');
    const clearAllBtn = document.getElementById('btnClearAllHistoryBtn');

    if (openBtnNav) {
      openBtnNav.addEventListener('click', () => this.showExamHistoryModal());
    }
    if (closeBtn && historyModal) {
      closeBtn.addEventListener('click', () => historyModal.classList.remove('active'));
    }
    if (historyModal) {
      historyModal.addEventListener('click', (e) => {
        if (e.target === historyModal) historyModal.classList.remove('active');
      });
    }
    if (filterSelect) {
      filterSelect.addEventListener('change', (e) => {
        this.renderHistoryList(e.target.value);
      });
    }
    if (clearAllBtn) {
      clearAllBtn.addEventListener('click', () => {
        const filterVal = filterSelect ? filterSelect.value : 'all';
        const msg = filterVal === 'all'
          ? "Bạn có chắc chắn muốn XÓA TOÀN BỘ lịch sử kết quả thi thử của tất cả các đề không?\n\n(Dữ liệu điểm số các lần thi trước sẽ bị xóa vĩnh viễn)"
          : `Bạn có chắc chắn muốn xóa toàn bộ lịch sử thi thử của Test ${filterVal} không?`;

        if (confirm(msg)) {
          window.StorageManager.clearExamHistory(filterVal);
          this.renderHistoryList(filterVal);
          this.showToast(filterVal === 'all' ? "Đã xóa toàn bộ lịch sử thi thử!" : `Đã xóa lịch sử thi thử của Test ${filterVal}!`, "info");
        }
      });
    }
  }

  showExamHistoryModal(filterTestId = 'all') {
    const historyModal = document.getElementById('examHistoryModal');
    if (!historyModal) return;

    const filterSelect = document.getElementById('historyFilterSelect');
    if (filterSelect) {
      filterSelect.value = filterTestId.toString();
    }

    this.renderHistoryList(filterTestId);
    historyModal.classList.add('active');
  }

  renderHistoryList(filterTestId = 'all') {
    const listContainer = document.getElementById('historyList');
    const statsBar = document.getElementById('historyStatsBar');
    if (!listContainer || !statsBar) return;

    const history = window.StorageManager.getExamHistory(filterTestId);

    // Render KPI Stats
    if (history.length === 0) {
      statsBar.innerHTML = `
        <div class="history-stat-card">
          <div class="history-stat-num">0</div>
          <div class="history-stat-label">Số lần thi</div>
        </div>
        <div class="history-stat-card">
          <div class="history-stat-num">--</div>
          <div class="history-stat-label">Điểm cao nhất</div>
        </div>
        <div class="history-stat-card">
          <div class="history-stat-num">--</div>
          <div class="history-stat-label">Điểm trung bình</div>
        </div>
        <div class="history-stat-card">
          <div class="history-stat-num">--</div>
          <div class="history-stat-label">Lần thi gần nhất</div>
        </div>
      `;

      listContainer.innerHTML = `
        <div class="history-empty-state">
          <div class="history-empty-icon"><i class="ph-bold ph-notebook"></i></div>
          <h3 style="color: #fff; margin-bottom: 0.5rem; font-size: 1.2rem;">Chưa có lịch sử thi thử</h3>
          <p style="font-size: 0.9rem; line-height: 1.6; max-width: 450px; margin: 0 auto 1.25rem;">
            Bạn chưa có kết quả bài thi thử nào${filterTestId !== 'all' ? ' cho Test ' + filterTestId : ''}. Bạn có thể quay lại làm bài luyện tập hoặc bắt đầu thi thử tính giờ ngay bây giờ!
          </p>
          <div style="display: flex; gap: 0.75rem; justify-content: center; flex-wrap: wrap;">
            <button class="btn-action-sm" onclick="document.getElementById('examHistoryModal').classList.remove('active'); window.app.switchMode('practice');" style="background: var(--bg-secondary); border: 1px solid var(--border-color); color: #fff; padding: 0.65rem 1.25rem;">
              <i class="ph-bold ph-arrow-left"></i> Quay lại luyện tập (Hiện câu hỏi)
            </button>
            <button class="btn-action-sm" onclick="document.getElementById('examHistoryModal').classList.remove('active'); window.app.switchMode('exam');" style="background: var(--accent-gradient); color: #fff; border: none; padding: 0.65rem 1.25rem;">
              <i class="ph-bold ph-play"></i> Bắt đầu thi thử ngay
            </button>
          </div>
        </div>
      `;
      return;
    }

    const totalAttempts = history.length;
    const scores = history.map(h => h.totalScore || 0);
    const maxScore = Math.max(...scores);
    const avgScore = Math.round(scores.reduce((a, b) => a + b, 0) / scores.length);
    const latestScore = history[0].totalScore || 0;

    statsBar.innerHTML = `
      <div class="history-stat-card">
        <div class="history-stat-num">${totalAttempts}</div>
        <div class="history-stat-label">Số lần thi</div>
      </div>
      <div class="history-stat-card">
        <div class="history-stat-num" style="color: var(--success);">${maxScore}</div>
        <div class="history-stat-label">Điểm cao nhất</div>
      </div>
      <div class="history-stat-card">
        <div class="history-stat-num" style="color: var(--info);">${avgScore}</div>
        <div class="history-stat-label">Điểm trung bình</div>
      </div>
      <div class="history-stat-card">
        <div class="history-stat-num" style="color: var(--warning);">${latestScore}</div>
        <div class="history-stat-label">Lần thi gần nhất</div>
      </div>
    `;

    listContainer.innerHTML = '';
    history.forEach(item => {
      const card = document.createElement('div');
      card.className = 'history-card';

      // Part accuracy chips
      let partChipsHtml = '';
      if (item.partStats) {
        for (let p = 1; p <= 7; p++) {
          const st = item.partStats[p];
          if (st) {
            const pct = Math.round((st.c / st.t) * 100);
            const chipClass = pct >= 80 ? 'high' : (pct >= 60 ? 'mid' : '');
            partChipsHtml += `<span class="history-chip ${chipClass}">P${p}: ${st.c}/${st.t} (${pct}%)</span>`;
          }
        }
      }

      const timeText = item.timeSpentMinutes ? `${item.timeSpentMinutes} phút` : '';

      card.innerHTML = `
        <div class="history-card-top">
          <div class="history-card-title">
            <span class="q-part-badge" style="background: var(--accent-gradient); color: #fff; font-weight: 800;">TEST ${item.testId}</span>
            <strong>${item.testTitle || `ETS 2024 • Test ${item.testId}`}</strong>
          </div>
          <div style="display: flex; align-items: center; gap: 0.6rem;">
            <span class="history-date-badge"><i class="ph-bold ph-calendar-blank"></i> ${item.dateStr || 'Vừa xong'}</span>
            ${timeText ? `<span class="history-date-badge"><i class="ph-bold ph-timer"></i> ${timeText}</span>` : ''}
          </div>
        </div>

        <div class="history-card-scores">
          <div class="history-total-badge">
            <span class="history-total-num">${item.totalScore}</span>
            <span class="history-total-sub">/ 990</span>
          </div>

          <div class="history-section-scores">
            <div class="history-section-item">
              <span class="sec-label">Listening</span>
              <span class="sec-val" style="color: #818cf8;">${item.lcScore} / 495 (${item.lcCorrect !== undefined ? item.lcCorrect + '/100' : ''})</span>
            </div>
            <div class="history-section-item">
              <span class="sec-label">Reading</span>
              <span class="sec-val" style="color: #f472b6;">${item.rcScore} / 495 (${item.rcCorrect !== undefined ? item.rcCorrect + '/100' : ''})</span>
            </div>
            <div class="history-section-item">
              <span class="sec-label">Tổng số câu đúng</span>
              <span class="sec-val" style="color: var(--success);">${item.totalCorrect !== undefined ? item.totalCorrect : (item.lcCorrect + item.rcCorrect)} / 200</span>
            </div>
          </div>
        </div>

        ${partChipsHtml ? `<div class="history-part-chips">${partChipsHtml}</div>` : ''}

        <div class="history-card-footer">
          <div style="font-size: 0.8rem; color: var(--text-muted);">
            ID: <code style="font-family: var(--font-mono);">${item.id}</code>
          </div>
          <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
            <button class="btn-action-sm" onclick="window.app.reviewPastExam('${item.id}')" title="Xem lại chi tiết từng câu trong bài thi này">
              <i class="ph-bold ph-eye"></i> Xem lại bài làm
            </button>
            <button class="btn-action-sm btn-danger-sm" onclick="window.app.deleteHistoryItem('${item.id}')" title="Xóa toàn bộ câu trả lời và kết quả lần thi này">
              <i class="ph-bold ph-trash"></i> Xóa lần thi này
            </button>
          </div>
        </div>
      `;

      listContainer.appendChild(card);
    });
  }

  async reviewPastExam(resultId) {
    const history = window.StorageManager.getExamHistory();
    const item = history.find(h => h.id === resultId);
    if (!item) return;

    // Close history modal
    const historyModal = document.getElementById('examHistoryModal');
    if (historyModal) historyModal.classList.remove('active');

    // Switch test if needed
    if (this.currentTestId !== item.testId) {
      await this.switchTest(item.testId);
    }

    // Switch to exam review mode
    this.currentMode = 'exam';
    this.isExamSubmitted = true;
    this.currentReviewResultId = resultId;
    this.currentReviewAnswers = item.answers || {};

    const questionsView = document.getElementById('questionsView');
    const flashcardView = document.getElementById('flashcardView');
    const grammarView = document.getElementById('grammarView');
    const sidebar = document.getElementById('sidebarColumn');
    const examTimerBox = document.getElementById('examTimerBox');
    const partNavBar = document.getElementById('partNavBar');

    questionsView.style.display = 'flex';
    flashcardView.style.display = 'none';
    grammarView.style.display = 'none';
    sidebar.style.display = 'block';
    examTimerBox.style.display = 'none';
    partNavBar.style.display = 'flex';

    document.querySelectorAll('.mode-btn').forEach(b => {
      b.classList.toggle('active', b.dataset.mode === 'exam');
    });

    this.renderReviewBanner(item);
    this.renderQuestions();
    this.updatePalette();
    this.updateProgressIndicator();

    this.showToast(`Đang xem lại bài thi Test ${item.testId} (${item.totalScore} Điểm • ${item.dateStr})`, 'success');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  renderReviewBanner(item = null) {
    const bannerContainer = document.getElementById('reviewBannerContainer');
    if (!bannerContainer) return;

    if (!item || !this.currentReviewResultId) {
      bannerContainer.innerHTML = '';
      return;
    }

    bannerContainer.innerHTML = `
      <div class="review-mode-banner">
        <div class="review-banner-left">
          <i class="ph-fill ph-clock-counter-clockwise"></i>
          <div>
            <strong>ĐANG XEM LẠI BÀI THI: ${item.testTitle || `Test ${item.testId}`} • Ngày nộp: ${item.dateStr || 'Gần đây'}</strong>
            <span>Điểm số: <b style="color: var(--accent-primary); font-size: 1.1rem;">${item.totalScore}/990</b> (LC: ${item.lcScore} | RC: ${item.rcScore}) • Tổng câu đúng: <b style="color: var(--success);">${item.totalCorrect !== undefined ? item.totalCorrect : (item.lcCorrect + item.rcCorrect)}/200</b></span>
          </div>
        </div>
        <div class="review-banner-actions">
          <button class="btn-action-sm btn-danger-sm" onclick="window.app.deleteCurrentReviewedHistory()" title="Xóa toàn bộ câu trả lời và kết quả lần thi này khỏi hệ thống">
            <i class="ph-bold ph-trash"></i> Xóa bài thi này
          </button>
          <button class="btn-action-sm" onclick="window.app.exitReviewMode()" title="Quay lại chế độ luyện tập bình thường">
            <i class="ph-bold ph-sign-out"></i> Thoát xem lại
          </button>
        </div>
      </div>
    `;
  }

  deleteCurrentReviewedHistory() {
    if (!this.currentReviewResultId) return;
    const history = window.StorageManager.getExamHistory();
    const item = history.find(h => h.id === this.currentReviewResultId);
    const label = item ? `${item.testTitle || 'Test ' + item.testId} (${item.dateStr || ''})` : 'bài thi này';

    if (confirm(`Bạn có chắc chắn muốn xóa ${label} và toàn bộ câu trả lời đã lưu của lần thi này không?\n\n(Dữ liệu bài thi này sẽ bị xóa vĩnh viễn khỏi lịch sử)`)) {
      window.StorageManager.deleteExamResult(this.currentReviewResultId);
      this.showToast(`Đã xóa vĩnh viễn ${label} khỏi lịch sử!`, 'success');
      this.exitReviewMode();
    }
  }

  exitReviewMode() {
    this.currentReviewResultId = null;
    this.currentReviewAnswers = null;
    this.isExamSubmitted = false;
    this.selectedPart = 'all';
    this.selectedFilter = 'all';
    const filterSelect = document.getElementById('questionFilter');
    if (filterSelect) filterSelect.value = 'all';
    document.querySelectorAll('.part-tab').forEach(t => {
      t.classList.toggle('active', t.dataset.part === 'all');
    });
    this.renderReviewBanner();
    this.switchMode('practice');
  }

  deleteHistoryItem(resultId) {
    const history = window.StorageManager.getExamHistory();
    const item = history.find(h => h.id === resultId);
    const itemLabel = item ? `${item.testTitle || 'Test ' + item.testId} (${item.dateStr || ''})` : 'lần thi này';

    if (confirm(`Bạn có chắc chắn muốn xóa toàn bộ kết quả và câu trả lời đã lưu của ${itemLabel} không?\n\n(Hành động này sẽ xóa vĩnh viễn dữ liệu lần thi này)`)) {
      window.StorageManager.deleteExamResult(resultId);

      // If currently reviewing this deleted exam, exit review mode
      if (this.currentReviewResultId === resultId) {
        this.exitReviewMode();
      }

      const filterSelect = document.getElementById('historyFilterSelect');
      const curFilter = filterSelect ? filterSelect.value : 'all';
      this.renderHistoryList(curFilter);
      this.showToast(`Đã xóa vĩnh viễn bài thi ${itemLabel}!`, "success");
    }
  }

  showToast(message, type = 'info') {
    const container = document.getElementById('toastContainer');
    if (!container) return;
    const toast = document.createElement('div');
    toast.className = `toast-message ${type}`;
    const icon = type === 'success' ? 'ph-check-circle' : (type === 'danger' ? 'ph-warning-circle' : 'ph-info');
    toast.innerHTML = `<i class="ph-fill ${icon}"></i><span>${message}</span>`;
    container.appendChild(toast);
    setTimeout(() => {
      toast.style.opacity = '0';
      toast.style.transform = 'translateY(10px) scale(0.95)';
      setTimeout(() => toast.remove(), 300);
    }, 3200);
  }

  initImageZoom() {
    const zoomModal = document.getElementById('imageZoomModal');
    const canvas = document.getElementById('lightboxCanvas');
    const closeZoomModal = document.getElementById('closeZoomModal');
    const btnZoomIn = document.getElementById('btnZoomIn');
    const btnZoomOut = document.getElementById('btnZoomOut');
    const btnZoomReset = document.getElementById('btnZoomReset');
    const btnZoomFit = document.getElementById('btnZoomFit');
    const btnZoomOpenNew = document.getElementById('btnZoomOpenNew');

    if (!zoomModal || !canvas) return;

    if (closeZoomModal) {
      closeZoomModal.addEventListener('click', () => this.closeImageZoom());
    }

    if (btnZoomIn) {
      btnZoomIn.addEventListener('click', (e) => {
        e.stopPropagation();
        this.setZoom(Math.min(5.0, this.zoomScale + 0.3));
      });
    }

    if (btnZoomOut) {
      btnZoomOut.addEventListener('click', (e) => {
        e.stopPropagation();
        this.setZoom(Math.max(0.4, this.zoomScale - 0.3));
      });
    }

    if (btnZoomReset) {
      btnZoomReset.addEventListener('click', (e) => {
        e.stopPropagation();
        this.resetZoom();
      });
    }

    if (btnZoomFit) {
      btnZoomFit.addEventListener('click', (e) => {
        e.stopPropagation();
        this.resetZoom();
      });
    }

    if (btnZoomOpenNew) {
      btnZoomOpenNew.addEventListener('click', (e) => {
        e.stopPropagation();
        if (this.currentZoomSrc) {
          window.open(this.currentZoomSrc, '_blank');
        }
      });
    }

    // Mouse Wheel to Zoom
    canvas.addEventListener('wheel', (e) => {
      e.preventDefault();
      const delta = e.deltaY < 0 ? 0.2 : -0.2;
      const newScale = Math.min(5.0, Math.max(0.4, this.zoomScale + delta));
      this.setZoom(newScale);
    }, { passive: false });

    // Drag to Pan
    canvas.addEventListener('mousedown', (e) => {
      if (e.button !== 0) return;
      this.isDragging = true;
      this.hasDragged = false;
      this.dragStartX = e.clientX - this.zoomX;
      this.dragStartY = e.clientY - this.zoomY;
      canvas.classList.add('dragging');
    });

    window.addEventListener('mousemove', (e) => {
      if (!this.isDragging) return;
      this.hasDragged = true;
      this.zoomX = e.clientX - this.dragStartX;
      this.zoomY = e.clientY - this.dragStartY;
      this.updateZoomTransform();
    });

    window.addEventListener('mouseup', () => {
      if (this.isDragging) {
        this.isDragging = false;
        canvas.classList.remove('dragging');
      }
    });

    // Touch support for drag
    canvas.addEventListener('touchstart', (e) => {
      if (e.touches.length === 1) {
        this.isDragging = true;
        this.dragStartX = e.touches[0].clientX - this.zoomX;
        this.dragStartY = e.touches[0].clientY - this.zoomY;
      }
    }, { passive: true });

    window.addEventListener('touchmove', (e) => {
      if (!this.isDragging || e.touches.length !== 1) return;
      this.zoomX = e.touches[0].clientX - this.dragStartX;
      this.zoomY = e.touches[0].clientY - this.dragStartY;
      this.updateZoomTransform();
    }, { passive: true });

    window.addEventListener('touchend', () => {
      this.isDragging = false;
    });

    // Double-click to toggle zoom
    canvas.addEventListener('dblclick', (e) => {
      e.preventDefault();
      if (this.zoomScale > 1.1) {
        this.resetZoom();
      } else {
        this.setZoom(2.2);
      }
    });

    // Close on clicking canvas background (if not dragged)
    canvas.addEventListener('click', (e) => {
      if (e.target === canvas && !this.hasDragged) {
        this.closeImageZoom();
      }
    });

    // Keyboard Shortcuts
    window.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        const historyModal = document.getElementById('examHistoryModal');
        if (historyModal && historyModal.classList.contains('active')) {
          historyModal.classList.remove('active');
        }
        const scoreModal = document.getElementById('scoreModal');
        if (scoreModal && scoreModal.classList.contains('active')) {
          scoreModal.classList.remove('active');
        }
        if (zoomModal.classList.contains('active')) {
          this.closeImageZoom();
        }
        return;
      }

      if (!zoomModal.classList.contains('active')) return;

      if (e.key === '+' || e.key === '=') {
        this.setZoom(Math.min(5.0, this.zoomScale + 0.3));
      } else if (e.key === '-' || e.key === '_') {
        this.setZoom(Math.max(0.4, this.zoomScale - 0.3));
      } else if (e.key === '0') {
        this.resetZoom();
      }
    });
  }

  setZoom(scale) {
    this.zoomScale = Math.round(scale * 100) / 100;
    this.updateZoomTransform();
  }

  resetZoom() {
    this.zoomScale = 1;
    this.zoomX = 0;
    this.zoomY = 0;
    this.updateZoomTransform();
  }

  updateZoomTransform() {
    const zoomedImg = document.getElementById('zoomedImage');
    const scaleEl = document.getElementById('lightboxScale');
    if (zoomedImg) {
      zoomedImg.style.transform = `translate(${this.zoomX}px, ${this.zoomY}px) scale(${this.zoomScale})`;
    }
    if (scaleEl) {
      scaleEl.textContent = `${Math.round(this.zoomScale * 100)}%`;
    }
  }

  openImageZoom(imageSrc, title = 'Hình ảnh chi tiết') {
    const zoomModal = document.getElementById('imageZoomModal');
    const zoomedImg = document.getElementById('zoomedImage');
    const titleEl = document.getElementById('lightboxTitle');
    if (!zoomModal || !zoomedImg) return;

    this.currentZoomSrc = imageSrc;
    zoomedImg.src = imageSrc;
    if (titleEl) titleEl.textContent = title;

    this.resetZoom();
    zoomModal.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  closeImageZoom() {
    const zoomModal = document.getElementById('imageZoomModal');
    if (zoomModal) {
      zoomModal.classList.remove('active');
      document.body.style.overflow = '';
    }
  }

  resetFilter() {
    this.selectedPart = 'all';
    this.selectedFilter = 'all';
    document.querySelectorAll('.part-tab').forEach(t => {
      t.classList.toggle('active', t.dataset.part === 'all');
    });
    const filterSelect = document.getElementById('questionFilter');
    if (filterSelect) filterSelect.value = 'all';
    this.renderQuestions();
    this.showToast('Đã xóa bộ lọc, hiển thị toàn bộ 200 câu hỏi!', 'info');
  }

  renderQuestions() {
    const container = document.getElementById('questionsList');
    if (!container) return;
    container.innerHTML = '';

    // Safety recovery: if questions array is empty (e.g., failed load)
    if (!this.questions || this.questions.length === 0) {
      container.innerHTML = `
        <div style="text-align: center; padding: 4rem 1rem; color: var(--text-muted); background: var(--bg-card); border-radius: var(--radius-lg); border: 1px dashed var(--border-color);">
          <i class="ph-bold ph-warning-circle" style="font-size: 3rem; color: var(--accent-primary); margin-bottom: 1rem; display: block;"></i>
          <h3 style="color: #fff; margin-bottom: 0.5rem;">Đang tải danh sách câu hỏi đề ETS Test ${this.currentTestId}...</h3>
          <p style="font-size: 0.95rem; margin-bottom: 1.5rem; color: var(--text-secondary);">Nếu chưa thấy câu hỏi xuất hiện, vui lòng bấm nút dưới đây để tải lại:</p>
          <button class="btn-action-sm" onclick="window.app.switchTest(1)" style="margin: 0 auto; background: var(--accent-gradient); color: #fff; border: none; padding: 0.75rem 1.5rem; font-size: 0.95rem; cursor: pointer; border-radius: var(--radius-sm);">
            <i class="ph-bold ph-arrows-clockwise"></i> Tải lại Test 1 (200 câu hỏi)
          </button>
        </div>
      `;
      return;
    }

    const answers = this.getCurrentAnswers();
    const flagged = window.StorageManager.getFlagged(this.currentTestId);
    const isPractice = this.currentMode === 'practice' || this.isExamSubmitted;

    // Filter questions
    let filtered = this.questions.filter(q => {
      if (this.selectedPart !== 'all' && q.part.toString() !== this.selectedPart) {
        return false;
      }
      const hasAnswer = answers[q.id] !== undefined;
      const isFlag = flagged.includes(q.id);
      const isWrong = hasAnswer && answers[q.id] !== q.correctAnswer;

      if (this.selectedFilter === 'unanswered' && hasAnswer) return false;
      if (this.selectedFilter === 'answered' && !hasAnswer) return false;
      if (this.selectedFilter === 'flagged' && !isFlag) return false;
      if (this.selectedFilter === 'wrong' && !isWrong) return false;

      return true;
    });

    if (filtered.length === 0) {
      const filterLabels = {
        'all': 'Tất cả',
        'unanswered': 'Câu chưa làm',
        'answered': 'Câu đã làm',
        'flagged': 'Đã gắn cờ 🚩',
        'wrong': 'Câu làm sai ❌'
      };
      container.innerHTML = `
        <div style="text-align: center; padding: 3.5rem 1rem; color: var(--text-muted); background: var(--bg-card); border-radius: var(--radius-lg); border: 1px dashed var(--border-color);">
          <i class="ph-bold ph-funnel" style="font-size: 2.5rem; margin-bottom: 1rem; display: block; color: var(--accent-primary);"></i>
          <h3 style="color: #fff; margin-bottom: 0.5rem;">Không tìm thấy câu hỏi phù hợp với bộ lọc</h3>
          <p style="font-size: 0.95rem; margin-bottom: 1.25rem; color: var(--text-secondary);">
            Bộ lọc hiện tại: <strong>${filterLabels[this.selectedFilter] || this.selectedFilter}</strong> 
            • Part: <strong>${this.selectedPart === 'all' ? 'Tất cả Part' : 'Part ' + this.selectedPart}</strong>
          </p>
          <button class="btn-action-sm" onclick="window.app.resetFilter()" style="margin: 0 auto; background: var(--accent-gradient); color: #fff; border: none; padding: 0.7rem 1.5rem; font-size: 0.95rem; cursor: pointer; border-radius: var(--radius-sm);">
            <i class="ph-bold ph-arrows-clockwise"></i> Hiển thị lại toàn bộ 200 câu hỏi (Xóa bộ lọc)
          </button>
        </div>
      `;
      return;
    }

    // Grouping for Passages (Part 6 and 7)
    let lastPassageId = null;

    filtered.forEach(q => {
      // Render Passage Container if new passage
      if (q.passageId && q.passageId !== lastPassageId) {
        lastPassageId = q.passageId;
        const passageBox = document.createElement('div');
        passageBox.className = 'passage-container';
        passageBox.id = `passage_${q.passageId}`;

        const pageImagesHtml = (q.pageImages || (q.pageImage ? [q.pageImage] : [])).map((img, idx) => `
          <button class="btn-action-sm" onclick="window.app.openImageZoom('${img}', 'Part ${q.part}: Đoạn đọc ${q.passageId} - Bản scan sách đề gốc HD ${idx > 0 ? '(' + (idx + 1) + ')' : ''}')">
            <i class="ph-bold ph-file-magnifying-glass"></i> Xem trang gốc scan HD
          </button>
        `).join('');

        passageBox.innerHTML = `
          <div class="passage-header">
            <div class="passage-title">
              <i class="ph-fill ph-book-open-text"></i>
              <span>${q.passageTitle || 'Reading Passage'}</span>
            </div>
            <div class="passage-actions">
              ${pageImagesHtml}
              ${isPractice ? `
                <button class="btn-action-sm" onclick="window.app.togglePassageVi('${q.passageId}')">
                  <i class="ph-bold ph-translate"></i> Dịch Tiếng Việt
                </button>
              ` : ''}
            </div>
          </div>
          <div class="passage-body">${q.passageText}</div>
          <div class="passage-body-vi" id="pvi_${q.passageId}" style="display: none;">
            <strong>Dịch nghĩa tiếng Việt:</strong><br/>
            ${q.passageTextVi || ''}
          </div>
        `;
        container.appendChild(passageBox);
      }

      // Render Question Card
      const card = this.createQuestionCard(q, answers, flagged);
      container.appendChild(card);
    });

    this.updateProgressIndicator();
  }

  createQuestionCard(q, answers, flagged) {
    const card = document.createElement('div');
    card.className = 'question-card';
    card.id = `q_${q.id}`;
    if (flagged.includes(q.id)) card.classList.add('flagged');

    const userAnswer = answers[q.id];
    const isAnswered = userAnswer !== undefined;
    const isPractice = this.currentMode === 'practice' || this.isExamSubmitted;
    const isExamActive = this.currentMode === 'exam' && !this.isExamSubmitted;
    const isListeningPart12 = q.part === 1 || q.part === 2;
    const hideOptionText = isExamActive && isListeningPart12;

    // Image for Part 1 or graphic questions
    let imageHtml = '';
    if (q.image) {
      const imgTitle = q.part === 1 ? `Part 1: Câu ${q.id} - Tranh mô tả` : `Part ${q.part}: Câu ${q.id} - Hình ảnh minh họa & Biểu đồ`;
      imageHtml = `
        <div class="question-image-box">
          <div class="question-img-wrapper" onclick="window.app.openImageZoom('${q.image}', '${imgTitle}')">
            <img src="${q.image}" alt="Question Graphic" class="question-img" />
            <span class="img-zoom-tag"><i class="ph-bold ph-magnifying-glass-plus"></i> Bấm để phóng to</span>
          </div>
        </div>
      `;
    }

    // Audio Cue button for LC
    let audioBtnHtml = '';
    if (q.part <= 4) {
      audioBtnHtml = `
        <button class="btn-action-sm" onclick="window.app.audioPlayer.loadPart(${q.part}, true); window.app.audioPlayer.showPlayer(true);" title="Nghe Audio Part ${q.part}">
          <i class="ph-fill ph-speaker-high"></i> Audio Part ${q.part}
        </button>
      `;
    }

    // Options HTML
    let optionsHtml = '';
    ['A', 'B', 'C', 'D'].forEach(optKey => {
      if (!q.options[optKey]) return;

      let optClass = 'option-item';
      if (userAnswer === optKey) {
        optClass += ' selected';
        if (isPractice) {
          optClass += (optKey === q.correctAnswer) ? ' correct' : ' wrong';
        }
      } else if (isPractice && isAnswered && optKey === q.correctAnswer) {
        optClass += ' correct';
      }

      // Hide option statement/response text for Part 1 & 2 in Exam Mode (TOEIC Standard)
      const displayText = hideOptionText ? `(${optKey})` : q.options[optKey];
      const viTextHtml = (isPractice && q.optionsVi && q.optionsVi[optKey])
        ? `<div class="option-text-vi q-trans-${q.id}">${q.optionsVi[optKey]}</div>`
        : '';

      optionsHtml += `
        <div class="${optClass}" onclick="window.app.selectOption(${q.id}, '${optKey}')">
          <div class="option-letter">${optKey}</div>
          <div class="option-text-wrap">
            <div class="option-text">${displayText}</div>
            ${viTextHtml}
          </div>
        </div>
      `;
    });

    const optionsListClass = hideOptionText
      ? `options-list options-audio-exam ${q.part === 2 ? 'part-2-options' : ''}`
      : 'options-list';

    // Accordion for Practice mode / Exam review mode
    let accordionHtml = '';
    if (isPractice) {
      accordionHtml = this.createAccordionHtml(q, userAnswer);
    }

    // Individual Question Audio Banner
    let qAudioBannerHtml = '';
    if (q.audioClip) {
      const isThisPlaying = this.activeQId === q.id && !this.currentQAudio.paused;
      const isLoop = !!this.loopMap[q.id];
      qAudioBannerHtml = `
        <div class="q-audio-banner" id="banner_q_${q.id}">
          <div class="q-audio-left">
            <button class="btn-q-play ${isThisPlaying ? 'playing' : ''}" id="btn_play_q_${q.id}" onclick="window.app.togglePlayQuestion(${q.id}, '${q.audioClip}')">
              <i class="ph-fill ${isThisPlaying ? 'ph-pause' : 'ph-play'}" id="icon_play_q_${q.id}"></i>
              <span id="label_play_q_${q.id}">${isThisPlaying ? 'Tạm dừng' : (q.audioLabel || 'Nghe câu ' + q.id)}</span>
            </button>
          </div>
          <div class="q-audio-timeline">
            <span class="q-audio-time" id="time_q_${q.id}">00:00</span>
            <input type="range" class="q-audio-slider" id="slider_q_${q.id}" min="0" max="100" value="0" oninput="window.app.seekQuestionSlider(${q.id}, this.value)" />
          </div>
          <div class="q-audio-actions">
            <button class="btn-q-icon" onclick="window.app.seekQuestionAudio(${q.id}, -5)" title="Tua lùi 5s">
              <i class="ph-bold ph-rewind-5"></i>
            </button>
            <button class="btn-q-icon" onclick="window.app.seekQuestionAudio(${q.id}, 5)" title="Tua tới 5s">
              <i class="ph-bold ph-fast-forward-5"></i>
            </button>
            <button class="btn-q-icon ${isLoop ? 'active' : ''}" id="btn_loop_q_${q.id}" onclick="window.app.toggleLoopQuestion(${q.id})" title="Lặp lại câu này">
              <i class="ph-bold ph-repeat"></i>
            </button>
          </div>
        </div>
      `;
    }

    // Translation button only available in practice mode or after exam submission
    const translationBtnHtml = isPractice ? `
      <button class="btn-action-sm" onclick="window.app.toggleTranslation(${q.id})">
        <i class="ph-bold ph-translate"></i> Dịch câu
      </button>
    ` : '';

    // Question stem: Part 1 & 2 in active exam mode display standard TOEIC test book prompt
    let stemHtml = '';
    if (hideOptionText) {
      if (q.part === 1) {
        stemHtml = `
          <div class="question-stem"><i class="ph-fill ph-headphones"></i> Mark your answer on your answer sheet.</div>
          <div class="audio-exam-subtext"><i class="ph-bold ph-speaker-simple-high"></i> Hãy nghe 4 phương án (A, B, C, D) trong đoạn băng để chọn câu trả lời đúng.</div>
        `;
      } else if (q.part === 2) {
        stemHtml = `
          <div class="question-stem"><i class="ph-fill ph-headphones"></i> Mark your answer on your answer sheet.</div>
          <div class="audio-exam-subtext"><i class="ph-bold ph-speaker-simple-high"></i> Hãy nghe câu hỏi và 3 câu phản hồi (A, B, C) trong đoạn băng để chọn câu trả lời đúng.</div>
        `;
      }
    } else {
      stemHtml = `
        <div class="question-stem">${q.questionText}</div>
        ${isPractice && q.questionTextVi ? `<div class="question-stem-vi q-trans-${q.id}">${q.questionTextVi}</div>` : ''}
      `;
    }

    card.innerHTML = `
      <div class="question-top-meta">
        <div class="q-badge-wrap">
          <span class="q-number-badge">Câu ${q.id}</span>
          <span class="q-part-badge">${q.partName || `Part ${q.part}`}</span>
        </div>
        <div class="q-actions">
          ${audioBtnHtml}
          ${translationBtnHtml}
          <button class="btn-flag ${flagged.includes(q.id) ? 'active' : ''}" onclick="window.app.toggleFlag(${q.id})" title="Đánh dấu câu hỏi này">
            <i class="ph-fill ph-flag"></i>
          </button>
        </div>
      </div>

      ${qAudioBannerHtml}

      ${imageHtml}

      ${stemHtml}

      <div class="${optionsListClass}">${optionsHtml}</div>

      ${accordionHtml}
    `;

    return card;
  }

  createAccordionHtml(q, userAnswer = undefined) {
    const vocabList = q.vocabulary || q.vocab || [];
    const vocabItemsHtml = vocabList.map(v => `
      <div class="vocab-card-sm">
        <div class="vocab-head">
          <span class="vocab-word">${v.word}</span>
          <span class="vocab-pos">${v.pos || ''}</span>
        </div>
        <div class="vocab-ipa">${v.ipa || ''}</div>
        <div class="vocab-meaning">${v.meaning}</div>
        ${v.example ? `<div class="vocab-example">“${v.example}”</div>` : ''}
        <div style="display: flex; justify-content: flex-end; gap: 0.4rem; margin-top: 0.35rem;">
          <button class="btn-speak" onclick="window.app.flashcardApp.speakCurrentWord('${v.word}')" title="Phát âm">
            <i class="ph-bold ph-speaker-high"></i>
          </button>
          <button class="btn-speak" onclick="window.app.toggleSaveWord('${v.word}', this)" title="Lưu vào sổ từ">
            <i class="${window.StorageManager.getStarredVocab().includes(v.word) ? 'ph-fill ph-star' : 'ph-bold ph-star'}"></i>
          </button>
        </div>
      </div>
    `).join('');

    const collocationsHtml = (q.collocations || []).map(c => `
      <div class="collocation-pill">
        <strong>${c.phrase}:</strong> <span>${c.meaning}</span>
      </div>
    `).join('');

    const grammarList = q.grammarPoints || q.grammar || [];
    const grammarHtml = grammarList.map(g => `
      <div class="grammar-note-box">
        <h4>${g.title}</h4>
        ${g.rule ? `<div class="grammar-rule" style="font-family: monospace; color: var(--accent-primary); margin-bottom: 0.35rem; font-weight: 600;">${g.rule}</div>` : ''}
        <p style="margin-top: 0.25rem; line-height: 1.6;">${g.content || g.analysis || ''}</p>
      </div>
    `).join('');

    const transcriptHtml = q.transcript ? `
      <div style="margin-bottom: 1rem;">
        <strong style="color: var(--accent-primary);">Transcript Nghe:</strong>
        <p style="white-space: pre-line; margin-top: 0.35rem;">${q.transcript}</p>
        <div style="margin-top: 0.75rem; padding-top: 0.75rem; border-top: 1px dashed var(--border-color); font-style: italic; color: var(--text-secondary);">
          <strong>Dịch nghĩa Transcript:</strong><br/>
          <p style="white-space: pre-line;">${q.transcriptVi || ''}</p>
        </div>
      </div>
    ` : '';

    let answerStatusBadge = '';
    let explanationPrefix = '';
    if (userAnswer !== undefined) {
      const isCorrect = userAnswer === q.correctAnswer;
      if (isCorrect) {
        answerStatusBadge = `<span class="answer-status-pill correct"><i class="ph-bold ph-check"></i> Đã chọn (${userAnswer}) - Đúng</span>`;
        explanationPrefix = `<div style="padding: 0.5rem 0.75rem; background: var(--success-bg); border: 1px solid var(--success-border); border-radius: var(--radius-sm); margin-bottom: 0.75rem; color: var(--success); font-weight: 700; font-size: 0.85rem;"><i class="ph-bold ph-check-circle"></i> Chính xác! Bạn đã chọn phương án (${userAnswer}).</div>`;
      } else {
        answerStatusBadge = `<span class="answer-status-pill wrong"><i class="ph-bold ph-x"></i> Đã chọn (${userAnswer}) - Sai • Đúng là (${q.correctAnswer})</span>`;
        explanationPrefix = `<div style="padding: 0.5rem 0.75rem; background: var(--danger-bg); border: 1px solid var(--danger-border); border-radius: var(--radius-sm); margin-bottom: 0.75rem; color: var(--danger); font-weight: 700; font-size: 0.85rem;"><i class="ph-bold ph-x-circle"></i> Chưa chính xác. Bạn đã chọn (${userAnswer}), đáp án đúng của đề là (${q.correctAnswer}).</div>`;
      }
    }

    return `
      <div class="accordion-section">
        <button class="accordion-toggle" onclick="window.app.toggleAccordion(${q.id})">
          <span style="display: flex; align-items: center; flex-wrap: wrap; gap: 0.5rem;">
            <span><i class="ph-bold ph-lightbulb"></i> Xem Đáp án, Giải thích, Từ vựng & Ngữ pháp</span>
            ${answerStatusBadge}
          </span>
          <i class="ph-bold ph-caret-down" id="caret_${q.id}"></i>
        </button>
        <div class="accordion-content" id="acc_${q.id}">
          <div class="deep-tabs">
            <button class="deep-tab-btn active" onclick="window.app.switchDeepTab(${q.id}, 'explain')">📝 Giải thích & Bẫy</button>
            ${q.transcript ? `<button class="deep-tab-btn" onclick="window.app.switchDeepTab(${q.id}, 'transcript')">🗣️ Transcript</button>` : ''}
            <button class="deep-tab-btn" onclick="window.app.switchDeepTab(${q.id}, 'vocab')">📚 Từ vựng (${vocabList.length})</button>
            <button class="deep-tab-btn" onclick="window.app.switchDeepTab(${q.id}, 'collocation')">🔗 Cụm từ (${(q.collocations || []).length})</button>
            <button class="deep-tab-btn" onclick="window.app.switchDeepTab(${q.id}, 'grammar')">📐 Ngữ pháp (${grammarList.length})</button>
          </div>

          <div class="deep-pane active" id="pane_${q.id}_explain">
            <div class="explanation-box">
              ${explanationPrefix}
              <strong>Đáp án đúng: <span style="color: var(--success); font-size: 1.1rem; font-weight: 800;">(${q.correctAnswer})</span></strong>
              <p style="margin-top: 0.5rem; line-height: 1.7;">${q.explanation}</p>
            </div>
          </div>

          ${q.transcript ? `
            <div class="deep-pane" id="pane_${q.id}_transcript">
              ${transcriptHtml}
            </div>
          ` : ''}

          <div class="deep-pane" id="pane_${q.id}_vocab">
            <div class="vocab-cards-grid">
              ${vocabItemsHtml || '<p style="color: var(--text-muted);">Không có từ vựng riêng cho câu này.</p>'}
            </div>
          </div>

          <div class="deep-pane" id="pane_${q.id}_collocation">
            ${collocationsHtml || '<p style="color: var(--text-muted);">Không có cụm từ riêng cho câu này.</p>'}
          </div>

          <div class="deep-pane" id="pane_${q.id}_grammar">
            ${grammarHtml || '<p style="color: var(--text-muted);">Không có điểm ngữ pháp đặc thù cho câu này.</p>'}
          </div>
        </div>
      </div>
    `;
  }

  toggleAccordion(qId) {
    const acc = document.getElementById(`acc_${qId}`);
    const caret = document.getElementById(`caret_${qId}`);
    if (acc) {
      const isOpen = acc.classList.toggle('open');
      caret.className = isOpen ? 'ph-bold ph-caret-up' : 'ph-bold ph-caret-down';
    }
  }

  switchDeepTab(qId, tabName) {
    const card = document.getElementById(`q_${qId}`);
    if (!card) return;

    const tabs = card.querySelectorAll('.deep-tab-btn');
    const panes = card.querySelectorAll('.deep-pane');

    tabs.forEach(t => t.classList.remove('active'));
    panes.forEach(p => p.classList.remove('active'));

    const targetPane = document.getElementById(`pane_${qId}_${tabName}`);
    if (targetPane) targetPane.classList.add('active');

    // Find clicked tab button
    tabs.forEach(t => {
      if (t.getAttribute('onclick').includes(`'${tabName}'`)) {
        t.classList.add('active');
      }
    });
  }

  selectOption(qId, optionKey) {
    if (this.currentMode === 'practice') {
      window.StorageManager.savePracticeAnswer(qId, optionKey, this.currentTestId);
    } else if (this.currentMode === 'exam') {
      if (this.isExamSubmitted) {
        return;
      }
      window.StorageManager.saveExamAnswer(qId, optionKey, this.currentTestId);
    }

    // Re-render single question card
    const card = document.getElementById(`q_${qId}`);
    const qData = this.questions.find(q => q.id === qId);
    if (card && qData) {
      const answers = this.getCurrentAnswers();
      const flagged = window.StorageManager.getFlagged(this.currentTestId);
      const newCard = this.createQuestionCard(qData, answers, flagged);
      card.replaceWith(newCard);

      // In practice mode, automatically open accordion
      if (this.currentMode === 'practice') {
        const acc = document.getElementById(`acc_${qId}`);
        const caret = document.getElementById(`caret_${qId}`);
        if (acc) {
          acc.classList.add('open');
          if (caret) caret.className = 'ph-bold ph-caret-up';
        }
      }
    }

    this.updatePalette();
    this.updateProgressIndicator();
  }

  toggleTranslation(qId) {
    const elements = document.querySelectorAll(`.q-trans-${qId}`);
    elements.forEach(el => el.classList.toggle('show'));
  }

  togglePassageVi(passageId) {
    const el = document.getElementById(`pvi_${passageId}`);
    if (el) {
      el.style.display = el.style.display === 'none' ? 'block' : 'none';
    }
  }

  toggleFlag(qId) {
    const isNowFlagged = window.StorageManager.toggleFlag(qId, this.currentTestId);
    const card = document.getElementById(`q_${qId}`);
    if (card) {
      card.classList.toggle('flagged', isNowFlagged);
      const flagBtn = card.querySelector('.btn-flag');
      if (flagBtn) flagBtn.classList.toggle('active', isNowFlagged);
    }
    this.updatePalette();
  }

  toggleSaveWord(word, btn) {
    const isStarred = window.StorageManager.toggleStarredVocab(word);
    const icon = btn.querySelector('i');
    if (icon) {
      icon.className = isStarred ? 'ph-fill ph-star' : 'ph-bold ph-star';
      btn.style.color = isStarred ? 'var(--warning)' : 'var(--text-muted)';
    }
  }

  updatePalette() {
    const paletteGrid = document.getElementById('paletteGrid');
    if (!paletteGrid) return;

    paletteGrid.innerHTML = '';
    const answers = this.getCurrentAnswers();
    const flagged = window.StorageManager.getFlagged(this.currentTestId);

    for (let i = 1; i <= 200; i++) {
      const btn = document.createElement('button');
      btn.className = 'palette-btn';
      btn.textContent = i;
      btn.id = `palette_btn_${i}`;

      const userChoice = answers[i];
      const isFlag = flagged.includes(i);
      const q = this.questions.find(item => item.id === i);

      if (isFlag) btn.classList.add('flagged');

      if (userChoice !== undefined) {
        if (this.currentMode === 'practice' || this.isExamSubmitted) {
          if (q && userChoice === q.correctAnswer) {
            btn.classList.add('correct');
          } else {
            btn.classList.add('wrong');
          }
        } else {
          btn.classList.add('answered');
        }
      }

      btn.addEventListener('click', () => {
        this.scrollToQuestion(i);
      });

      paletteGrid.appendChild(btn);
    }

    const answeredCount = Object.keys(answers).length;
    const statsEl = document.getElementById('paletteStats');
    if (statsEl) statsEl.textContent = `${answeredCount} / 200`;
  }

  scrollToQuestion(qId) {
    const target = document.getElementById(`q_${qId}`);
    if (target) {
      target.scrollIntoView({ behavior: 'smooth', block: 'center' });
      target.style.transition = 'box-shadow 0.3s';
      target.style.boxShadow = '0 0 20px rgba(99, 102, 241, 0.6)';
      setTimeout(() => {
        target.style.boxShadow = '';
      }, 1500);
    } else {
      // If filtered out, switch to all and scroll
      this.selectedPart = 'all';
      this.selectedFilter = 'all';
      document.querySelectorAll('.part-tab').forEach(t => t.classList.remove('active'));
      document.querySelector('.part-tab[data-part="all"]').classList.add('active');
      document.getElementById('questionFilter').value = 'all';
      this.renderQuestions();
      setTimeout(() => this.scrollToQuestion(qId), 100);
    }
  }

  updateProgressIndicator() {
    const answers = this.getCurrentAnswers();
    const count = Object.keys(answers).length;
    const pct = Math.round((count / 200) * 100);

    const textEl = document.getElementById('progressText');
    const fillEl = document.getElementById('progressFill');

    if (textEl) textEl.textContent = `${count} / 200 (${pct}%)`;
    if (fillEl) fillEl.style.width = `${pct}%`;
  }

  initQuestionAudioListeners() {
    this.currentQAudio.addEventListener('timeupdate', () => {
      if (!this.activeQId) return;
      const cur = this.currentQAudio.currentTime;
      const dur = this.currentQAudio.duration;
      const timeEl = document.getElementById(`time_q_${this.activeQId}`);
      const slider = document.getElementById(`slider_q_${this.activeQId}`);
      if (timeEl && dur) {
        timeEl.textContent = `${this.formatAudioTime(cur)} / ${this.formatAudioTime(dur)}`;
      }
      if (slider && dur) {
        slider.value = (cur / dur) * 100;
      }
    });

    this.currentQAudio.addEventListener('ended', () => {
      if (!this.activeQId) return;
      if (this.loopMap[this.activeQId]) {
        this.currentQAudio.currentTime = 0;
        this.currentQAudio.play();
      } else {
        this.resetQuestionAudioUI(this.activeQId);
        this.activeQId = null;
      }
    });

    this.currentQAudio.addEventListener('pause', () => {
      if (this.activeQId) {
        const btn = document.getElementById(`btn_play_q_${this.activeQId}`);
        const icon = document.getElementById(`icon_play_q_${this.activeQId}`);
        const label = document.getElementById(`label_play_q_${this.activeQId}`);
        if (btn) btn.classList.remove('playing');
        if (icon) icon.className = 'ph-fill ph-play';
        if (label) {
          const q = this.questions.find(item => item.id === this.activeQId);
          label.textContent = q ? (q.audioLabel || 'Nghe câu ' + q.id) : 'Nghe câu này';
        }
      }
    });

    this.currentQAudio.addEventListener('play', () => {
      if (this.activeQId) {
        const btn = document.getElementById(`btn_play_q_${this.activeQId}`);
        const icon = document.getElementById(`icon_play_q_${this.activeQId}`);
        const label = document.getElementById(`label_play_q_${this.activeQId}`);
        if (btn) btn.classList.add('playing');
        if (icon) icon.className = 'ph-fill ph-pause';
        if (label) label.textContent = 'Đang phát (Tạm dừng)';
      }
    });
  }

  togglePlayQuestion(qId, clipSrc) {
    // Pause main sticky audio player if playing
    if (this.audioPlayer && this.audioPlayer.isPlaying) {
      this.audioPlayer.togglePlay();
    }

    if (this.activeQId === qId) {
      if (this.currentQAudio.paused) {
        this.currentQAudio.play();
      } else {
        this.currentQAudio.pause();
      }
    } else {
      if (this.activeQId) {
        this.resetQuestionAudioUI(this.activeQId);
      }
      this.activeQId = qId;
      this.currentQAudio.src = clipSrc;
      this.currentQAudio.currentTime = 0;
      this.currentQAudio.play().catch(e => console.log('Audio error:', e));
    }
  }

  seekQuestionAudio(qId, seconds) {
    if (this.activeQId !== qId) {
      const q = this.questions.find(item => item.id === qId);
      if (q && q.audioClip) {
        this.togglePlayQuestion(qId, q.audioClip);
      }
    }
    if (this.currentQAudio.duration) {
      this.currentQAudio.currentTime = Math.max(0, Math.min(this.currentQAudio.duration, this.currentQAudio.currentTime + seconds));
    }
  }

  seekQuestionSlider(qId, value) {
    if (this.activeQId === qId && this.currentQAudio.duration) {
      this.currentQAudio.currentTime = (value / 100) * this.currentQAudio.duration;
    }
  }

  toggleLoopQuestion(qId) {
    this.loopMap[qId] = !this.loopMap[qId];
    const loopBtn = document.getElementById(`btn_loop_q_${qId}`);
    if (loopBtn) {
      loopBtn.classList.toggle('active', this.loopMap[qId]);
    }
  }

  resetQuestionAudioUI(qId) {
    const btn = document.getElementById(`btn_play_q_${qId}`);
    const icon = document.getElementById(`icon_play_q_${qId}`);
    const label = document.getElementById(`label_play_q_${qId}`);
    const slider = document.getElementById(`slider_q_${qId}`);
    const timeEl = document.getElementById(`time_q_${qId}`);
    if (btn) btn.classList.remove('playing');
    if (icon) icon.className = 'ph-fill ph-play';
    if (label) {
      const q = this.questions.find(item => item.id === qId);
      label.textContent = q ? (q.audioLabel || 'Nghe câu ' + q.id) : 'Nghe câu này';
    }
    if (slider) slider.value = 0;
    if (timeEl) timeEl.textContent = '00:00';
  }

  formatAudioTime(secs) {
    if (isNaN(secs)) return '00:00';
    const m = Math.floor(secs / 60);
    const s = Math.floor(secs % 60);
    return `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
  }

  renderGrammarList() {
    const container = document.getElementById('grammarContainer');
    if (!container) return;

    container.innerHTML = '';
    this.grammarBank.forEach(g => {
      const card = document.createElement('div');
      card.className = 'grammar-note-box';
      card.style.background = 'var(--bg-card)';
      card.innerHTML = `
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.5rem;">
          <h3 style="color: var(--accent-primary); font-size: 1.05rem;">${g.title}</h3>
          <span class="q-part-badge">Part ${g.part} • Q${g.questionId}</span>
        </div>
        <p style="line-height: 1.7; font-size: 0.95rem;">${g.content}</p>
        <div style="margin-top: 0.75rem; text-align: right;">
          <button class="btn-action-sm" onclick="window.app.switchMode('practice'); window.app.scrollToQuestion(${g.questionId})">
            <i class="ph-bold ph-arrow-square-out"></i> Xem câu hỏi liên quan (Q${g.questionId})
          </button>
        </div>
      `;
      container.appendChild(card);
    });
  }
}

function startTOEICApp() {
  if (!window.app) {
    try {
      window.app = new TOEICApp();
    } catch (e) {
      console.error("Fatal error starting TOEICApp:", e);
    }
  }
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', startTOEICApp);
} else {
  startTOEICApp();
}
