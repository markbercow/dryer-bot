document.addEventListener("DOMContentLoaded", () => {
  const socket = io();
  const statusLight = document.getElementById("connection-status");

  socket.on("connect", () => {
    statusLight.classList.remove("disconnected");
    statusLight.classList.add("connected");
  });

  socket.on("disconnect", () => {
    statusLight.classList.remove("connected");
    statusLight.classList.add("disconnected");
  });

  socket.on("status", (data) => {
    document.getElementById("running").textContent = data.running ? "✅ Yes" : "❌ No";
    document.getElementById("elapsed").textContent = data.elapsed_time;
    document.getElementById("last").textContent = data.last_completed || "N/A";
  });
});
