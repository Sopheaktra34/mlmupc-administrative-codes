const province = document.getElementById("province");
const district = document.getElementById("district");
const commune = document.getElementById("commune");
const village = document.getElementById("village");

const resultBody = document.getElementById("resultBody");
const codeInput = document.getElementById("code");
const nameSearch = document.getElementById("nameSearch");

/* ---------- TABLE RENDER ---------- */
function render(rows) {
  if (!rows || rows.length === 0) {
    resultBody.innerHTML = `
      <tr>
        <td colspan="4" class="p-4 text-center text-red-500">
          No data found
        </td>
      </tr>`;
    return;
  }

  resultBody.innerHTML = "";
  rows.forEach(r => {
    resultBody.innerHTML += `
      <tr class="hover:bg-gray-100">
        <td class="border p-2">${r.level}</td>
        <td class="border p-2">${r.code}</td>
        <td class="border p-2">${r.name_kh}</td>
        <td class="border p-2">${r.name_en || ""}</td>
      </tr>`;
  });
}

/* ---------- LOAD PROVINCES ---------- */
async function loadProvinces() {
  const res = await fetch("/provinces");
  const data = await res.json();

  province.innerHTML = '<option value="">Province</option>';
  district.innerHTML = '<option value="">District</option>';
  commune.innerHTML = '<option value="">Commune</option>';
  village.innerHTML = '<option value="">Village</option>';

  data.forEach(p => {
    province.innerHTML += `
      <option value="${p[0]}" data-code="${p[1]}">
        ${p[1]} - ${p[3]}
      </option>`;
  });
}

/* ---------- CASCADING ---------- */
province.onchange = async () => {
  const res = await fetch(`/districts?province_code=${province.value}`);
  const data = await res.json();

  district.innerHTML = '<option value="">District</option>';
  commune.innerHTML = '<option value="">Commune</option>';
  village.innerHTML = '<option value="">Village</option>';

  data.forEach(d => {
    district.innerHTML += `
      <option value="${d[0]}" data-code="${d[1]}">
        ${d[1]} - ${d[3]}
      </option>`;
  });

  if (province.value) loadContextCounts("province", province.value);
};

district.onchange = async () => {
  const res = await fetch(`/communes?district_code=${district.value}`);
  const data = await res.json();

  commune.innerHTML = '<option value="">Commune</option>';
  village.innerHTML = '<option value="">Village</option>';

  data.forEach(c => {
    commune.innerHTML += `
      <option value="${c[0]}" data-code="${c[1]}">
        ${c[1]} - ${c[3]}
      </option>`;
  });

  if (district.value) loadContextCounts("district", district.value);
};

commune.onchange = async () => {
  const res = await fetch(`/villages?commune_code=${commune.value}`);
  const data = await res.json();

  village.innerHTML = '<option value="">Village</option>';

  data.forEach(v => {
    village.innerHTML += `
      <option value="${v[0]}" data-code="${v[1]}">
        ${v[1]} - ${v[3]}
      </option>`;
  });

  if (commune.value) loadContextCounts("commune", commune.value);
};

/* ---------- LOOKUP ---------- */
async function lookup(code) {
  resultBody.innerHTML = `
    <tr>
      <td colspan="4" class="p-4 text-center text-blue-500">
        Loading...
      </td>
    </tr>`;

  const res = await fetch(`/lookup/code?code=${code}`);
  const data = await res.json();

  if (data.error) {
    render([]);
    return;
  }

  render(data.hierarchy);
}

/* ---------- ACTIONS ---------- */
function showSelected() {
  for (const s of [village, commune, district, province]) {
    if (s.value) {
      lookup(s.options[s.selectedIndex].dataset.code);
      return;
    }
  }
}

function searchByCode() {
  const code = codeInput.value.trim();
  if (code) lookup(code);
}

async function searchByName() {
  const q = nameSearch.value.trim();
  if (!q) return;

  resultBody.innerHTML = `
    <tr>
      <td colspan="4" class="p-4 text-center text-blue-500">
        Searching...
      </td>
    </tr>`;

  const res = await fetch(`/lookup/name?q=${encodeURIComponent(q)}`);
  const data = await res.json();
  render(data);
}

/* ---------- COUNTS ---------- */
async function loadOverallCounts() {
  const res = await fetch("/counts/overall");
  const data = await res.json();

  stat1.textContent = data.provinces;
  stat2.textContent = data.districts;
  stat3.textContent = data.communes;
  stat4.textContent = data.villages;
}

async function loadContextCounts(level, id) {
  const res = await fetch(`/counts/context?level=${level}&id=${id}`);
  const data = await res.json();

  stat1.textContent = "-";
  stat2.textContent = data.districts ?? "-";
  stat3.textContent = data.communes ?? "-";
  stat4.textContent = data.villages ?? "-";
}

/* ---------- INIT ---------- */
loadProvinces();
loadOverallCounts();