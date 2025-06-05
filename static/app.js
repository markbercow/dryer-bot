async function updateStatus() {
  try {
    const res = await fetch("/status");
    const data = await res.json();
    document.getElementById("running").textContent = data.running ? "✅ Yes" : "❌ No";
    document.getElementById("elapsed").textContent = data.elapsed_time + " seconds";
    document.getElementById("last").textContent = data.last_completed || "N/A";
  } catch (err) {
    console.error("Status update failed:", err);
  }
}

document.addEventListener("DOMContentLoaded", () => {
  updateStatus();
  setInterval(updateStatus, 5000);
});
