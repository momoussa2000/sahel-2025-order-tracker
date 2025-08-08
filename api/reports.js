// Serverless API to persist multi-day data
// GET: returns reports JSON from GitHub (raw) or local fallback
// POST: merges and commits to GitHub via REST if GITHUB_TOKEN/REPO are configured

// Use global fetch provided by Vercel (Node 18+)

const OWNER_REPO = process.env.REPO || 'momoussa2000/sahel-2025-order-tracker';
const FILE_PATH = 'data/reports.json';
const BRANCH = process.env.REPO_BRANCH || 'main';

async function readFromGitHub() {
  const url = `https://raw.githubusercontent.com/${OWNER_REPO}/${BRANCH}/${FILE_PATH}`;
  try {
    const res = await fetch(url, { headers: { 'Accept': 'application/json' } });
    if (!res.ok) return {};
    const text = await res.text();
    if (!text) return {};
    return JSON.parse(text);
  } catch (e) {
    return {};
  }
}

async function getGitFileSha(token) {
  const apiUrl = `https://api.github.com/repos/${OWNER_REPO}/contents/${FILE_PATH}?ref=${BRANCH}`;
  const res = await fetch(apiUrl, { headers: { Authorization: `token ${token}`, 'Accept': 'application/vnd.github+json' } });
  if (!res.ok) return null;
  const json = await res.json();
  return json.sha || null;
}

async function writeToGitHub(token, data) {
  const apiUrl = `https://api.github.com/repos/${OWNER_REPO}/contents/${FILE_PATH}`;
  const sha = await getGitFileSha(token);
  const body = {
    message: 'Update reports.json via API',
    content: Buffer.from(JSON.stringify(data, null, 2)).toString('base64'),
    branch: BRANCH,
    sha: sha || undefined,
  };
  const res = await fetch(apiUrl, {
    method: 'PUT',
    headers: { Authorization: `token ${token}`, 'Accept': 'application/vnd.github+json' },
    body: JSON.stringify(body),
  });
  if (!res.ok) {
    const t = await res.text();
    throw new Error(`GitHub write failed: ${res.status} ${t}`);
  }
  return true;
}

function mergeDedup(base, incoming) {
  const out = { ...(base || {}) };
  for (const [day, payload] of Object.entries(incoming || {})) {
    const cur = out[day] || {};
    // shallow merge top-level
    const merged = { ...cur, ...payload };
    // dedup orders
    const orders = [];
    const seenOrder = new Set();
    const routes = (payload.orders_made && payload.orders_made.routes) || [];
    routes.forEach(r => {
      const ro = { ...r, orders: [] };
      (r.orders || []).forEach(o => {
        const key = `${r.route_name || r.route_number || ''}|${o.client}|${o['3kg']||0}|${o['4kg']||0}|${o['5kg']||0}|${o.cups||0}`;
        if (seenOrder.has(key)) return;
        seenOrder.add(key);
        ro.orders.push(o);
      });
      orders.push(ro);
    });
    if (!merged.orders_made) merged.orders_made = { date: payload?.orders_made?.date || day, routes: [] };
    merged.orders_made.routes = orders.concat((cur.orders_made?.routes || [])).slice(0);

    // dedup deliveries
    const reports = [];
    const seenDel = new Set();
    ((payload.sales_fulfillment && payload.sales_fulfillment.reports) || []).forEach(rep => {
      const nr = { ...rep, deliveries: [] };
      (rep.deliveries || []).forEach(d => {
        const key = `${rep.route||''}|${rep.vehicle_number||''}|${d.client}|${d['3kg']||0}|${d['4kg']||0}|${d['5kg']||0}|${d.cups||0}`;
        if (seenDel.has(key)) return;
        seenDel.add(key);
        nr.deliveries.push(d);
      });
      reports.push(nr);
    });
    if (!merged.sales_fulfillment) merged.sales_fulfillment = { date: payload?.sales_fulfillment?.date || day, reports: [] };
    merged.sales_fulfillment.reports = reports.concat((cur.sales_fulfillment?.reports || [])).slice(0);

    out[day] = merged;
  }
  return out;
}

module.exports = async (req, res) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET,POST,OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization');
  if (req.method === 'OPTIONS') return res.status(200).end();

  if (req.method === 'GET') {
    const data = await readFromGitHub();
    return res.status(200).json({ ok: true, data });
  }

  if (req.method === 'POST') {
    const token = process.env.GITHUB_TOKEN;
    if (!token) return res.status(501).json({ ok: false, error: 'Server not configured for writes. Set GITHUB_TOKEN and REPO.' });
    try {
      const incoming = typeof req.body === 'string' ? JSON.parse(req.body) : req.body;
      const current = await readFromGitHub();
      const merged = mergeDedup(current, incoming);
      await writeToGitHub(token, merged);
      return res.status(200).json({ ok: true });
    } catch (e) {
      return res.status(500).json({ ok: false, error: e.message });
    }
  }

  return res.status(405).json({ ok: false, error: 'Method not allowed' });
};


