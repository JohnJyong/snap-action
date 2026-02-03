document.getElementById("snapBtn").addEventListener("click", () => {
  // Capture the visible tab
  chrome.tabs.captureVisibleTab(null, { format: "png" }, (dataUrl) => {
    
    // Send the image (DataURL) to the content script to display the capsule
    // Note: In a real app, you would send this to your Python backend API first
    
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
      chrome.tabs.sendMessage(tabs[0].id, {
        action: "SHOW_CAPSULE",
        imageData: dataUrl,
        pageUrl: tabs[0].url // Sending URL helps context!
      });
    });
    
    window.close(); // Close popup
  });
});
