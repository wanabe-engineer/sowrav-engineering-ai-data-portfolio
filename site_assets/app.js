const evidenceClusters = [
  ["GED103 - History of Emergence", 70],
  ["Lab Electrical Circuits I", 40],
  ["CSE480", 35],
  ["ENG 103", 30],
  ["CSE 104", 22],
  ["VLSI Lab", 20],
  ["Chemistry Fall 2020", 19],
  ["World Civilization", 18],
  ["Electrical Services Design", 16],
  ["Power Electronics Lab", 14],
];

const chart = document.querySelector("#courseChart");

if (chart) {
  const max = Math.max(...evidenceClusters.map(([, value]) => value));
  chart.innerHTML = evidenceClusters
    .map(([label, value]) => {
      const width = Math.max(4, Math.round((value / max) * 100));
      return `
        <div class="bar-row">
          <span>${label}</span>
          <span class="bar-track"><span class="bar-fill" style="width: ${width}%"></span></span>
          <strong>${value}</strong>
        </div>
      `;
    })
    .join("");
}
