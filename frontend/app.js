const API_BASE = "http://127.0.0.1:5000"; // Flask backend URL

document.getElementById("uploadForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const formData = new FormData();
  formData.append("category", document.getElementById("category").value);
  formData.append("rank", document.getElementById("rank").value);
  formData.append("top_n", document.getElementById("top_n").value);

  try {
    const res = await fetch(`${API_BASE}/process`, {
      method: "POST",
      body: formData
    });

    const data = await res.json();

    if (data.error) {
      document.getElementById("results").innerHTML =
        `<p style="color:red;">❌ ${data.error}</p>`;
      return;
    }

    if (data.results.length === 0) {
      document.getElementById("results").innerHTML =
        `<p style="color:orange;">⚠ ${data.message || "No colleges found."}</p>`;
      return;
    }

    // Build results table
    let table = `
      <table>
        <tr>
          <th>Institution</th>
          <th>Course</th>
          <th>Cutoff (${document.getElementById("category").value})</th>
          <th>Predicted Avg Cutoff</th>
        </tr>
    `;

    data.results.forEach(r => {
      table += `
        <tr>
          <td>${r.Institution}</td>
          <td>${r.CourseName}</td>
          <td>${r[document.getElementById("category").value]}</td>
          <td>${r.Predicted_AvgCutoffRank.toFixed(2)}</td>
        </tr>
      `;
    });

    table += "</table>";

    // Add download link
    if (data.download) {
      table += `<p><a href="${API_BASE}${data.download}" target="_blank">⬇ Download results CSV</a></p>`;
    }

    document.getElementById("results").innerHTML = table;

  } catch (err) {
    console.error(err);
    document.getElementById("results").innerHTML =
      `<p style="color:red;">⚠ Something went wrong. Check backend is running.</p>`;
  }
});
