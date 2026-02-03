// background.js - Service Worker
// Can handle context menus or keyboard shortcuts here

chrome.runtime.onInstalled.addListener(() => {
  console.log("SnapAction Extension Installed");
});
