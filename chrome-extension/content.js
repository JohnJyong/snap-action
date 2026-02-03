// Listen for messages from popup
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "SHOW_CAPSULE") {
    console.log("📸 SnapAction received image from: " + request.pageUrl);
    
    // Simulate Analysis (Mock)
    // In real version: fetch('http://localhost:5000/analyze', { method: 'POST', body: ... })
    
    let intent = analyzeMock(request.pageUrl);
    showCapsule(intent);
  }
});

function analyzeMock(url) {
  if (url.includes("taobao") || url.includes("amazon")) {
    return { icon: "🛒", text: "Find Lower Price" };
  } else if (url.includes("maps") || url.includes("dianping")) {
    return { icon: "📍", text: "Navigate Here" };
  } else if (url.includes("ticket") || url.includes("event")) {
    return { icon: "📅", text: "Add to Calendar" };
  } else {
    return { icon: "✨", text: "Summarize Page" };
  }
}

function showCapsule(intent) {
  // Remove existing
  const existing = document.getElementById("snap-action-capsule-root");
  if (existing) existing.remove();

  // Create Container
  const container = document.createElement("div");
  container.id = "snap-action-capsule-root";
  
  // Create HTML
  container.innerHTML = `
    <div class="sa-capsule">
      <span class="sa-icon">${intent.icon}</span>
      <span class="sa-text">${intent.text}</span>
      <span class="sa-arrow">↗</span>
    </div>
  `;
  
  // Interaction
  container.addEventListener("click", () => {
    alert(`🚀 Action Triggered: ${intent.text}`);
    container.remove();
  });
  
  document.body.appendChild(container);
  
  // Auto hide after 5s
  setTimeout(() => {
    if(container) {
      container.style.opacity = "0";
      setTimeout(() => container.remove(), 500);
    }
  }, 5000);
}
