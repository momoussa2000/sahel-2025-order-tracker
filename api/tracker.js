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
      total_clients: 51,
      freezer_clients: 36,
      total_freezers: 69,
      trucks: ["NPR 7219 (Tariq)", "TFR 9987 (Mohamed)"],
      sales_reps: ["Eslam", "Akrm", "Mouner", "Hussein Sabra", "Ahmed Hussein"],
      timestamp: new Date().toISOString(),
      message: "نظام متتبع طلبات مكعبات الثلج للساحل الشمالي 2025",
      features: ["Contact Information", "Freezer Monitoring", "Delivery Tracking", "WhatsApp Integration", "Ice Cube Bags (3kg, 4kg, 5kg)", "Ice Cups"]
    };
    
    res.setHeader('Content-Type', 'application/json');
    return res.status(200).json(summary);
  }

  // For POST requests, we could add the Python integration later
  res.status(405).json({ error: 'Method not allowed' });
}; 