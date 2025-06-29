const { PythonShell } = require('python-shell');

module.exports = (req, res) => {
  // Add CORS headers
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  
  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  // Simple response for now to test deployment
  if (req.method === 'GET') {
    const summary = {
      status: "SAHEL 2025 Order Tracker - Active",
      zones: 16,
      total_clients: 47,
      freezer_clients: 32,
      trucks: ["NPR 7219 (Tariq)", "TFR 9987 (Mohamed)"],
      timestamp: new Date().toISOString(),
      message: "نظام متتبع طلبات الآيس كريم للساحل الشمالي 2025"
    };
    
    res.setHeader('Content-Type', 'application/json');
    return res.status(200).json(summary);
  }

  // For POST requests, we could add the Python integration later
  res.status(405).json({ error: 'Method not allowed' });
}; 