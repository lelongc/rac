const fs = require('fs');
const test3 = JSON.parse(fs.readFileSync('web/data/test3.json', 'utf8'));

function testLogic(q, isPractice, isExamActive) {
  const isListeningPart12 = q.part === 1 || q.part === 2;
  const hideOptionText = isExamActive && isListeningPart12;

  let optionsList = [];
  ['A', 'B', 'C', 'D'].forEach(optKey => {
    if (!q.options[optKey]) return;
    const displayText = hideOptionText ? `(${optKey})` : q.options[optKey];
    optionsList.push(displayText);
  });

  let stem = '';
  if (hideOptionText) {
    stem = 'Mark your answer on your answer sheet.';
  } else {
    stem = q.questionText;
  }

  return { stem, optionsList, hideOptionText };
}

console.log('=== TEST 1: THI THỬ (EXAM ACTIVE) ===');
const q1_exam = testLogic(test3.questions[0], false, true);
console.log('Q1 Stem:', q1_exam.stem);
console.log('Q1 Options:', q1_exam.optionsList);
console.log('Q1 has statement text?:', q1_exam.optionsList.some(o => o.includes('painting')));

const q7_exam = testLogic(test3.questions[6], false, true);
console.log('Q7 Stem:', q7_exam.stem);
console.log('Q7 has spoken text?:', q7_exam.stem.includes('flour'));
console.log('Q7 Options:', q7_exam.optionsList);
console.log('Q7 has response text?:', q7_exam.optionsList.some(o => o.includes('stock')));

console.log('\n=== TEST 2: REVIEW (AFTER SUBMIT) ===');
const q1_rev = testLogic(test3.questions[0], true, false);
console.log('Q1 Stem:', q1_rev.stem);
console.log('Q1 Options:', q1_rev.optionsList);
console.log('Q1 has statement text?:', q1_rev.optionsList.some(o => o.includes('painting')));

const q7_rev = testLogic(test3.questions[6], true, false);
console.log('Q7 Stem:', q7_rev.stem);
console.log('Q7 has spoken text?:', q7_rev.stem.includes('flour'));
console.log('Q7 Options:', q7_rev.optionsList);
console.log('Q7 has response text?:', q7_rev.optionsList.some(o => o.includes('stock')));
