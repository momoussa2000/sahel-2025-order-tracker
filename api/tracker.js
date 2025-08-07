const { PythonShell } = require('python-shell');

module.exports = (req, res) => {
  // Add CORS headers
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  
  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  // Enhanced response with production and storage data
  if (req.method === 'GET') {
    const summary = {
      status: "SAHEL 2025 Order Tracker - Enhanced Active",
      zones: 16,
      total_clients: 51,
      freezer_clients: 36,
      total_freezers: 69,
      trucks: ["NPR 7219 (Tariq)", "TFR 9987 (Mohamed)"],
      sales_reps: ["Eslam", "Akrm", "Mouner", "Hussein Sabra", "Ahmed Hussein"],
      timestamp: new Date().toISOString(),
      message: "نظام متتبع طلبات مكعبات الثلج للساحل الشمالي 2025 - محسن",
      
      // Enhanced production data
      production: {
        date: "3/8/2025", // Date from production sheet
        daily: {
          "3kg": 2638,
          "4kg": 0,
          "5kg": 725,
          "cups": 0,
          "total_kg": 11539,
          "total_tons": 11.5
        },
        by_machine: {
          "old_machine": {
            "3kg": 0,
            "4kg": 0,
            "5kg": 725,
            "total_kg": 3625,
            "total_tons": 3.6
          },
          "new_machine": {
            "3kg": 2638,
            "4kg": 0,
            "5kg": 0,
            "total_kg": 7914,
            "total_tons": 7.9
          }
        },
        by_shift: {
          "first_shift": {
            "3kg": 1180,
            "4kg": 0,
            "5kg": 370,
            "total_kg": 5390,
            "total_tons": 5.4
          },
          "second_shift": {
            "3kg": 1458,
            "4kg": 0,
            "5kg": 355,
            "total_kg": 6149,
            "total_tons": 6.1
          }
        }
      },
      
      // Enhanced storage data
      storage: {
        rooms: {
          "main": {
            "name": "Main Storage Room",
            "3kg": 6231,
            "4kg": 0,
            "5kg": 1666,
            "cups": 200,
            "total_kg": 27023,
            "total_tons": 27.0
          },
          "mahdi": {
            "name": "External Storage 1 (Mahdi)",
            "3kg": 0,
            "4kg": 0,
            "5kg": 0,
            "cups": 0,
            "total_kg": 0,
            "total_tons": 0.0
          },
          "apex": {
            "name": "External Storage 2 (Apex for Food Industries)",
            "3kg": 0,
            "4kg": 0,
            "5kg": 37778,
            "cups": 0,
            "total_kg": 188890,
            "total_tons": 188.9
          },
          "brothers": {
            "name": "External Storage 3 (Brothers)",
            "3kg": 0,
            "4kg": 0,
            "5kg": 0,
            "cups": 0,
            "total_kg": 0,
            "total_tons": 0.0
          }
        },
        total: {
          "3kg": 6231,
          "4kg": 0,
          "5kg": 39444,
          "cups": 200,
          "total_kg": 215913,
          "total_tons": 215.9
        }
      },
      
      // Distribution and tracking
      distribution: {
        "3kg": 225,
        "4kg": 0,
        "5kg": 300,
        "total_kg": 2175,
        "total_tons": 2.2
      },
      
      refunds: {
        "3kg": 58,
        "4kg": 0,
        "5kg": 53,
        "total_kg": 439,
        "total_tons": 0.44
      },
      
      damages: {
        "3kg": 10,
        "4kg": 0,
        "5kg": 6,
        "total_kg": 60,
        "total_tons": 0.06
      },
      
      // Orders Made Report
      orders_made: {
        date: "3/8/2025",
        routes: [
          {
            route_number: 1,
            destination: "Cairo",
            route_name: "Maadi & Tagamoa",
            vehicle_type: "Rental Car",
            vehicle_owner: "Mohamed Moussa",
            vehicle_number: "3729",
            shift: "Morning",
            orders: [
              { client: "Circle K El Nakhil", "3kg": 30, "4kg": 0, "5kg": 0, "cups": 0 },
              { client: "W Mart El Shouifat", "3kg": 15, "4kg": 0, "5kg": 0, "cups": 10 },
              { client: "Gourmet Cove", "3kg": 30, "4kg": 0, "5kg": 0, "cups": 0 },
              { client: "Voo El Lotus", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 20 },
              { client: "W Mart El Banafsag", "3kg": 30, "4kg": 0, "5kg": 0, "cups": 20 },
              { client: "Bing", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 70 },
              { client: "Saudi El Maadi 2", "3kg": 55, "4kg": 0, "5kg": 0, "cups": 0 },
              { client: "Voo El Maadi", "3kg": 25, "4kg": 0, "5kg": 0, "cups": 0 }
            ]
          },
          {
            route_number: 2,
            destination: "Cairo",
            route_name: "Tagamoa & Masr El Gedida",
            vehicle_type: "Factory Owned",
            vehicle_owner: "Factory",
            vehicle_number: "9987",
            vehicle_model: "Tank",
            shift: "Evening",
            orders: [
              { client: "Seven Fortunes Drive", "3kg": 0, "4kg": 0, "5kg": 25, "cups": 0 },
              { client: "Seven Fortunes Waterway", "3kg": 0, "4kg": 0, "5kg": 15, "cups": 0 },
              { client: "Seven Fortunes Mafida", "3kg": 12, "4kg": 0, "5kg": 0, "cups": 0 },
              { client: "Rabbit El Rehab", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 12 },
              { client: "Brown Nose Mall OR 1", "3kg": 0, "4kg": 0, "5kg": 20, "cups": 0 },
              { client: "W Mart El Rehab", "3kg": 15, "4kg": 0, "5kg": 0, "cups": 20 },
              { client: "Edge El Rehab", "3kg": 55, "4kg": 0, "5kg": 0, "cups": 0 },
              { client: "Tabs El Rehab", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 20 },
              { client: "Seven Fortunes Masr El Gedida", "3kg": 15, "4kg": 0, "5kg": 0, "cups": 0 },
              { client: "Eatgram Company", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 10 }
            ]
          }
        ]
      },
      
      // Sales Rep Fulfillment Report (what was actually delivered)
      sales_fulfillment: {
        date: "3/8/2025",
        reports: [
          {
            route: "Sokhna - El Gouna - Hurghada",
            vehicle_type: "Rental Car",
            vehicle_number: "8659",
            driver: "Basil Gamal (Rental)",
            sales_rep: "Hussein Sabra",
            deliveries: [
              { client: "KIG Sokhna", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 50 },
              { client: "Dreams Talaat", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 100 },
              { client: "Dreams La Vista", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 100 },
              { client: "Gourmet El Gouna", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 300 },
              { client: "Best Way Mangrove", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 40 },
              { client: "Best Way Marina", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 90 },
              { client: "Best Way Town", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 80 },
              { client: "Best Way Store", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 171 },
              { client: "Senior Sassi", "3kg": 0, "4kg": 0, "5kg": 30, "cups": 0 },
              { client: "Smokery El Gouna", "3kg": 0, "4kg": 0, "5kg": 70, "cups": 0 },
              { client: "Steigenberger Hotel", "3kg": 0, "4kg": 0, "5kg": 40, "cups": 0 },
              { client: "Jazz Somabay Hotel", "3kg": 0, "4kg": 0, "5kg": 105, "cups": 20, "bonus": 5 }
            ]
          },
          {
            route: "Sharm El Sheikh & Dahab",
            vehicle_type: "Rental Car",
            vehicle_number: "2344",
            driver: "Monir",
            sales_rep: "Monir",
            deliveries: [
              { client: "Marabella Hotel", "3kg": 0, "4kg": 0, "5kg": 600, "cups": 0 },
              { client: "Jazz El Fanar Hotel", "3kg": 0, "4kg": 0, "5kg": 200, "cups": 0 },
              { client: "El Kazar Hotel", "3kg": 0, "4kg": 0, "5kg": 300, "cups": 0 },
              { client: "Jazz Dahabiya Hotel", "3kg": 0, "4kg": 0, "5kg": 150, "cups": 0 }
            ]
          },
          {
            route: "Heliopolis",
            vehicle_type: "Factory Owned Tank",
            vehicle_number: "9987",
            driver: "Shenouda Labib",
            sales_rep: "Shenouda Labib",
            deliveries: [
              { client: "Almaza TBS", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 65 },
              { client: "Garden TBS", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 40 },
              { client: "El Korba TBS", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 40 },
              { client: "Voo Heliopolis", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 20 },
              { client: "Drinks Faisal", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 20 }
            ]
          },
          {
            route: "Maadi & Tagamoa",
            vehicle_type: "Rental Car",
            vehicle_number: "3729",
            driver: "Mohamed Mahi",
            sales_rep: "Mohamed Mahi (Mohamed Moussa)",
            deliveries: [
              { client: "Voo El Maadi", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 44 },
              { client: "Mariam Market", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 35, "bonus": 20 },
              { client: "Bing", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 70 },
              { client: "W Mart El Banafsag", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 60 },
              { client: "Gourmet Cove", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 35, "bonus": 20 },
              { client: "Saudi El Maadi", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 50, "bonus": 5 }
            ]
          },
          {
            route: "Sahel Coast",
            vehicle_type: "Factory Owned",
            vehicle_number: "N/A",
            driver: "Islam Ahmed",
            sales_rep: "Islam Ahmed",
            deliveries: [
              { client: "Drinks Stella Abdelrahman", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 5 },
              { client: "Marasi TBS", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 30 },
              { client: "Coffee Culture", "3kg": 0, "4kg": 0, "5kg": 250, "cups": 0 },
              { client: "Smokery Bianki", "3kg": 0, "4kg": 0, "5kg": 40, "cups": 0 },
              { client: "H.H.", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 120 },
              { client: "Dreams El W", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 20 },
              { client: "Dreams Stella", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 50 },
              { client: "Dreams Cascada", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 50 },
              { client: "Dreams Swan Lake", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 100 }
            ]
          },
          {
            route: "October & Zamalek",
            vehicle_type: "Rental Car",
            vehicle_number: "N/A",
            driver: "Abdelrahman Tarek",
            sales_rep: "Abdelrahman Tarek",
            deliveries: [
              { client: "Noy Metropole", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 13 },
              { client: "Gourmet SODIC", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 20 },
              { client: "SODIC TBS", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 10 },
              { client: "Pier88 Zamalek", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 20 },
              { client: "Sass Zamalek", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 20 },
              { client: "Seeb Zamalek", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 15 },
              { client: "Miami", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 9 },
              { client: "Zamalek TBS", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 15 },
              { client: "Dara Zamalek", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 10 },
              { client: "Drinks Zamalek", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 20 },
              { client: "Seeb Tahrir", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 12 },
              { client: "Azakaba", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 18 },
              { client: "Seven Fortunes Arkan", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 3 },
              { client: "Gourmet Arkan", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 60, "bonus": 125 },
              { client: "Circle K Zayed", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 25 },
              { client: "Dreams Palm", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 55 },
              { client: "Bizex City View", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 50 }
            ]
          },
          {
            route: "Tagamoa & Masr El Gedida",
            vehicle_type: "Factory Owned",
            vehicle_number: "9987",
            driver: "Abdeljawad",
            sales_rep: "Abdeljawad",
            shift: "Evening",
            deliveries: [
              { client: "Seven Fortunes Heliopolis", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 8 },
              { client: "Heliopolis Club Party", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 10 },
              { client: "Edge", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 26 },
              { client: "Rabbit Tagamoa", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 10 },
              { client: "W Mart El Shouifat", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 15 },
              { client: "O1 Brown Nose", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 25 },
              { client: "W Mart El Rehab", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 20 },
              { client: "Seven Fortunes Drive", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 20 },
              { client: "Seven Fortunes Waterway", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 15 },
              { client: "Seven Fortunes Mafida", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 16 }
            ]
          }
        ]
      },
      
      features: [
        "Contact Information", 
        "Freezer Monitoring", 
        "Delivery Tracking", 
        "WhatsApp Integration", 
        "Ice Cube Bags (3kg, 4kg, 5kg)", 
        "Ice Cups",
        "Production Tracking by Machine",
        "Storage Room Management",
        "Shift-based Production",
        "Refund & Damage Tracking",
        "Distribution Monitoring"
      ]
    };
    
    res.setHeader('Content-Type', 'application/json');
    return res.status(200).json(summary);
  }

  // For POST requests, we could add the Python integration later
  res.status(405).json({ error: 'Method not allowed' });
}; 