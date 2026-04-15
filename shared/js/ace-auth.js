// ace-auth.js — PUBLIC BUILD (no login required)
// Original file redirected non-authenticated users to enrollment.html.
// This stub exposes the same globals so pages that reference them don't throw.
// No gating is performed.
(function () {
  'use strict';
  window.AceAuth = window.AceAuth || {
    getSession: async function () { return null; },
    isLoggedIn: function () { return false; },
    getProfile: function () { return null; }
  };
  window.aceLogout = function () {};
  window.aceGetProfile = function () { return null; };
})();
