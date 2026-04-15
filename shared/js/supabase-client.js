// supabase-client.js — PUBLIC BUILD (localStorage-only tracking)
// Original: transparent proxy to /api/student/... backend endpoints.
// Public build: records events in localStorage so each student sees their OWN
// progress in their OWN browser. Nothing leaves the device.
//
// API preserved (called by drill.html, flashcards.html, jeopardy.html):
//   window.AceSupabase.trackQuestionEvent({questionId, correct, category, ...})
//   window.AceSupabase.trackSessionSummary({sessionType, score, total, ...})
(function () {
  'use strict';

  var STORAGE_KEY = 'caet_practice_progress_v1';

  function loadProgress() {
    try {
      var raw = localStorage.getItem(STORAGE_KEY);
      if (!raw) return { questions: {}, sessions: [], totals: { attempted: 0, correct: 0 } };
      return JSON.parse(raw);
    } catch (e) {
      return { questions: {}, sessions: [], totals: { attempted: 0, correct: 0 } };
    }
  }

  function saveProgress(p) {
    try { localStorage.setItem(STORAGE_KEY, JSON.stringify(p)); }
    catch (e) { /* quota exceeded — silently ignore */ }
  }

  window.AceSupabase = {
    trackQuestionEvent: function (evt) {
      try {
        var p = loadProgress();
        var qid = evt && (evt.questionId || evt.question_id || evt.id);
        if (!qid) return;
        var rec = p.questions[qid] || { attempts: 0, correct: 0, lastSeen: null, category: evt.category || null };
        rec.attempts += 1;
        if (evt.correct || evt.isCorrect) rec.correct += 1;
        rec.lastSeen = new Date().toISOString();
        if (evt.category) rec.category = evt.category;
        p.questions[qid] = rec;
        p.totals.attempted += 1;
        if (evt.correct || evt.isCorrect) p.totals.correct += 1;
        saveProgress(p);
      } catch (e) { /* no-op */ }
    },

    trackSessionSummary: function (evt) {
      try {
        var p = loadProgress();
        p.sessions.push({
          at: new Date().toISOString(),
          type: evt && (evt.sessionType || evt.session_type || 'unknown'),
          score: evt && (evt.score != null ? evt.score : null),
          total: evt && (evt.total != null ? evt.total : null),
          category: evt && (evt.category || null)
        });
        // keep only last 100 sessions to avoid unbounded growth
        if (p.sessions.length > 100) p.sessions = p.sessions.slice(-100);
        saveProgress(p);
      } catch (e) { /* no-op */ }
    },

    // Public helpers that pages / a future stats view can use:
    getProgress: loadProgress,
    resetProgress: function () { localStorage.removeItem(STORAGE_KEY); }
  };
})();
