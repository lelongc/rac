// storage.js: LocalStorage Manager for ETS TOEIC 2024 (Tests 1 - 10)
class StorageManager {
  static currentTest = 1;

  static _sanitizeTestId(testId = null) {
    if (testId !== null && testId !== undefined) {
      const parsed = parseInt(testId, 10);
      if (!isNaN(parsed) && parsed >= 1 && parsed <= 10) return parsed;
    }
    const cur = parseInt(this.currentTest, 10);
    if (!isNaN(cur) && cur >= 1 && cur <= 10) return cur;
    return this.getCurrentTest();
  }

  static getCurrentTest() {
    try {
      const t = localStorage.getItem('toeic2024_active_test');
      const val = parseInt(t, 10);
      if (!isNaN(val) && val >= 1 && val <= 10) {
        return val;
      }
      localStorage.setItem('toeic2024_active_test', '1');
      return 1;
    } catch (e) {
      return 1;
    }
  }

  static setCurrentTest(testId) {
    const val = parseInt(testId, 10);
    this.currentTest = (!isNaN(val) && val >= 1 && val <= 10) ? val : 1;
    try {
      localStorage.setItem('toeic2024_active_test', this.currentTest.toString());
    } catch (e) {}
  }

  // ==========================================
  // PRACTICE MODE ANSWERS (PERSISTENT SELECTIONS)
  // ==========================================
  static getPracticeAnswers(testId = null) {
    const t = this._sanitizeTestId(testId);
    try {
      const data = localStorage.getItem(`toeic2024_t${t}_practice_answers`);
      if (data) return JSON.parse(data);

      // Graceful migration from legacy single answer key if exists
      const legacy = localStorage.getItem(`toeic2024_t${t}_answers`);
      if (legacy) {
        const parsed = JSON.parse(legacy);
        localStorage.setItem(`toeic2024_t${t}_practice_answers`, legacy);
        return parsed;
      }
      return {};
    } catch (e) {
      return {};
    }
  }

  static savePracticeAnswer(questionId, selectedOption, testId = null) {
    const t = this._sanitizeTestId(testId);
    const answers = this.getPracticeAnswers(t);
    answers[questionId] = selectedOption;
    try {
      localStorage.setItem(`toeic2024_t${t}_practice_answers`, JSON.stringify(answers));
      // Also sync to legacy key for backwards compatibility
      localStorage.setItem(`toeic2024_t${t}_answers`, JSON.stringify(answers));
    } catch (e) {}
  }

  static clearPracticeAnswers(testId = null) {
    const t = this._sanitizeTestId(testId);
    try {
      localStorage.removeItem(`toeic2024_t${t}_practice_answers`);
      localStorage.removeItem(`toeic2024_t${t}_answers`);
    } catch (e) {}
  }

  static clearAllPracticeAnswers() {
    try {
      for (let t = 1; t <= 10; t++) {
        localStorage.removeItem(`toeic2024_t${t}_practice_answers`);
        localStorage.removeItem(`toeic2024_t${t}_answers`);
      }
    } catch (e) {}
  }

  // ==========================================
  // EXAM MODE ANSWERS (IN-PROGRESS ATTEMPT)
  // ==========================================
  static getExamAnswers(testId = null) {
    const t = this._sanitizeTestId(testId);
    try {
      const data = localStorage.getItem(`toeic2024_t${t}_exam_answers`);
      return data ? JSON.parse(data) : {};
    } catch (e) {
      return {};
    }
  }

  static saveExamAnswer(questionId, selectedOption, testId = null) {
    const t = this._sanitizeTestId(testId);
    const answers = this.getExamAnswers(t);
    answers[questionId] = selectedOption;
    try {
      localStorage.setItem(`toeic2024_t${t}_exam_answers`, JSON.stringify(answers));
    } catch (e) {}
  }

  static clearExamAnswers(testId = null) {
    const t = this._sanitizeTestId(testId);
    try {
      localStorage.removeItem(`toeic2024_t${t}_exam_answers`);
      localStorage.removeItem(`toeic2024_t${t}_exam_time`);
    } catch (e) {}
  }

  // Backwards compatibility wrappers
  static getAnswers(testId = null) {
    return this.getPracticeAnswers(testId);
  }

  static saveAnswer(questionId, selectedOption, testId = null) {
    return this.savePracticeAnswer(questionId, selectedOption, testId);
  }

  static clearAnswers(testId = null) {
    return this.clearPracticeAnswers(testId);
  }

  // ==========================================
  // EXAM HISTORY (MOCK TEST ATTEMPTS & RESULTS)
  // ==========================================
  static getExamHistory(testId = null) {
    try {
      const consolidated = localStorage.getItem('toeic2024_exam_history_v2');
      let history = [];

      if (consolidated !== null) {
        history = JSON.parse(consolidated);
      } else {
        // One-time migration only if key never existed before
        for (let i = 1; i <= 10; i++) {
          const oldScores = localStorage.getItem(`toeic2024_t${i}_scores`);
          if (oldScores) {
            try {
              const parsed = JSON.parse(oldScores);
              parsed.forEach((item, idx) => {
                history.push({
                  id: `legacy_${i}_${idx}_${Date.now()}`,
                  testId: i,
                  testTitle: `ETS 2024 • Test ${i}`,
                  timestamp: item.date ? new Date(item.date).getTime() : Date.now() - (idx * 3600000),
                  dateStr: item.date ? new Date(item.date).toLocaleString('vi-VN') : 'Trước đây',
                  totalScore: item.totalScore || 0,
                  lcScore: item.lcScore || 0,
                  rcScore: item.rcScore || 0,
                  lcCorrect: item.lcCorrect || 0,
                  rcCorrect: item.rcCorrect || 0,
                  totalCorrect: (item.lcCorrect || 0) + (item.rcCorrect || 0),
                  partStats: item.partStats || null,
                  answers: item.answers || {}
                });
              });
              // Clean up legacy key so it never interferes
              localStorage.removeItem(`toeic2024_t${i}_scores`);
            } catch (e) {}
          }
        }
        localStorage.setItem('toeic2024_exam_history_v2', JSON.stringify(history));
      }

      if (testId && testId !== 'all') {
        const tid = parseInt(testId, 10);
        history = history.filter(item => item.testId === tid);
      }
      return history.sort((a, b) => (b.timestamp || 0) - (a.timestamp || 0));
    } catch (e) {
      console.error(e);
      return [];
    }
  }

  static saveExamResult(resultData) {
    try {
      const history = this.getExamHistory('all');
      history.unshift(resultData);
      localStorage.setItem('toeic2024_exam_history_v2', JSON.stringify(history));
      return true;
    } catch (e) {
      console.error('Failed to save exam result:', e);
      return false;
    }
  }

  static deleteExamResult(resultId) {
    try {
      let history = this.getExamHistory('all');
      const target = history.find(r => r.id === resultId);
      history = history.filter(r => r.id !== resultId);
      localStorage.setItem('toeic2024_exam_history_v2', JSON.stringify(history));

      // Also clean from legacy per-test key if still present
      if (target && target.testId) {
        localStorage.removeItem(`toeic2024_t${target.testId}_scores`);
      }
      return true;
    } catch (e) {
      console.error(e);
      return false;
    }
  }

  static clearExamHistory(testId = null) {
    try {
      if (testId && testId !== 'all') {
        const tid = parseInt(testId, 10);
        let history = this.getExamHistory('all');
        history = history.filter(r => r.testId !== tid);
        localStorage.setItem('toeic2024_exam_history_v2', JSON.stringify(history));
        localStorage.removeItem(`toeic2024_t${tid}_scores`);
      } else {
        localStorage.setItem('toeic2024_exam_history_v2', JSON.stringify([]));
        for (let i = 1; i <= 10; i++) {
          localStorage.removeItem(`toeic2024_t${i}_scores`);
        }
      }
      return true;
    } catch (e) {
      console.error(e);
      return false;
    }
  }

  static saveScores(scoreData, testId = null) {
    const t = testId || this.currentTest || this.getCurrentTest();
    return this.saveExamResult({
      id: 'score_' + Date.now(),
      testId: t,
      testTitle: `ETS 2024 • Test ${t}`,
      timestamp: Date.now(),
      dateStr: new Date().toLocaleString('vi-VN'),
      ...scoreData
    });
  }

  static getScoreHistory(testId = null) {
    const t = this._sanitizeTestId(testId);
    try {
      const data = localStorage.getItem(`toeic2024_t${t}_scores`);
      return data ? JSON.parse(data) : [];
    } catch (e) {
      return [];
    }
  }

  // ==========================================
  // FLAGS & VOCABULARY & THEME
  // ==========================================
  static getFlagged(testId = null) {
    const t = this._sanitizeTestId(testId);
    try {
      const data = localStorage.getItem(`toeic2024_t${t}_flagged`);
      return data ? JSON.parse(data) : [];
    } catch (e) {
      return [];
    }
  }

  static toggleFlag(questionId, testId = null) {
    const t = this._sanitizeTestId(testId);
    const flagged = this.getFlagged(t);
    const index = flagged.indexOf(questionId);
    if (index > -1) {
      flagged.splice(index, 1);
    } else {
      flagged.push(questionId);
    }
    try {
      localStorage.setItem(`toeic2024_t${t}_flagged`, JSON.stringify(flagged));
    } catch (e) {}
    return index === -1;
  }

  static clearFlagged(testId = null) {
    const t = this._sanitizeTestId(testId);
    try {
      localStorage.removeItem(`toeic2024_t${t}_flagged`);
    } catch (e) {}
  }

  static getStarredVocab() {
    try {
      const data = localStorage.getItem('toeic2024_starred_vocab');
      return data ? JSON.parse(data) : [];
    } catch (e) {
      return [];
    }
  }

  static toggleStarredVocab(word) {
    const starred = this.getStarredVocab();
    const index = starred.indexOf(word);
    if (index > -1) {
      starred.splice(index, 1);
    } else {
      starred.push(word);
    }
    try {
      localStorage.setItem('toeic2024_starred_vocab', JSON.stringify(starred));
    } catch (e) {}
    return index === -1;
  }

  static getTheme() {
    return localStorage.getItem('toeic2024_theme') || 'dark';
  }

  static setTheme(theme) {
    localStorage.setItem('toeic2024_theme', theme);
  }
}

window.StorageManager = StorageManager;
