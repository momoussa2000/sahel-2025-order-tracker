# 🧊 SAHEL 2025 Order Tracker

**نظام متتبع طلبات مكعبات الثلج للساحل الشمالي 2025**

A comprehensive order tracking system for ice cube deliveries across the North Coast of Egypt, managing 47 clients across 16 zones with freezer monitoring and delivery optimization.

## 🌟 Features

- **📊 Client Management**: 47 North Coast clients organized by 16 zones
- **❄️ Freezer Monitoring**: Track 32 clients with 38 total freezers
- **🚛 Delivery Optimization**: Route planning with 2 delivery trucks
- **👥 Sales Team Tracking**: 5 sales representatives with client assignments
- **📱 WhatsApp Integration**: Ready-to-share summaries
- **🌐 Web API**: RESTful endpoints for integration

## 📋 Project Statistics

| Metric | Count |
|--------|-------|
| **Total Clients** | 47 |
| **Zones** | 16 |
| **Freezer Clients** | 32 |
| **Total Freezers** | 38 |
| **Delivery Trucks** | 2 |
| **Sales Representatives** | 5 |

## 🏗️ Architecture

### Frontend
- **HTML5/CSS3**: Modern responsive landing page
- **Arabic RTL Support**: Full right-to-left text direction
- **Progressive Web App**: Ready for mobile deployment

### Backend
- **Node.js**: Serverless API endpoints
- **Python**: Core tracking logic with async support
- **Vercel**: Serverless deployment platform

### Database Structure
```javascript
clients = {
  "Almaza": [
    {"name": "بير الماظة", "freezer": true, "orders": 0, "freezer_count": 5},
    // ... 7 more clients
  ],
  "Marassi": [
    {"name": "ساشي مراسي", "freezer": true, "orders": 0, "freezer_count": 2},
    // ... 8 more clients
  ],
  // ... 14 more zones
}
```

## 🚀 Quick Start

### Prerequisites
- Node.js (v14 or higher)
- Python 3.7+
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/sahel-2025-order-tracker.git
   cd sahel-2025-order-tracker
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Run locally**
   ```bash
   npm start
   ```

4. **Deploy to Vercel**
   ```bash
   vercel --prod
   ```

## 📁 Project Structure

```
SAHEL 2025 Order Tracker/
├── api/
│   ├── tracker.js          # Vercel serverless API
│   └── sahel_tracker.py    # Core Python tracking logic
├── index.html              # Landing page
├── package.json            # Node.js dependencies
├── vercel.json             # Vercel configuration
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

## 🗺️ Client Zones

### Major Zones
- **Almaza** (8 clients) - Highest concentration
- **Marassi** (9 clients) - Largest zone
- **Hacienda White** (4 clients) - Premium locations
- **Diplomasseen** (4 clients) - All freezer clients
- **Marina** (3 clients) - Coastal locations

### Complete Zone List
1. Almaza
2. Sidi Heneish
3. Mountain View
4. Ghazala Bay
5. Telal
6. Hacienda Red
7. Hacienda White
8. Seashell
9. Bianchi
10. La Vista Cascada
11. Marassi
12. Sidi Abdel Rahman
13. Stella Di Mare
14. Diplomasseen
15. Alamein
16. Marina

## 🚛 Delivery Fleet

| Truck | Capacity | Driver | License |
|-------|----------|--------|---------|
| NPR 7219 | 4.5 tons | Tariq | Grade 2 |
| TFR 9987 | 1.5 tons | Mohamed | Grade 3 |

## 👥 Sales Team

- Eslam
- Akrm
- Mouner
- Hussein Sabra
- Ahmed Hussein

## 🔧 API Endpoints

### GET `/api/track`
Returns system status and statistics.

**Response:**
```json
{
  "status": "SAHEL 2025 Order Tracker - Active",
  "zones": 16,
  "total_clients": 47,
  "freezer_clients": 32,
  "trucks": ["NPR 7219 (Tariq)", "TFR 9987 (Mohamed)"],
  "timestamp": "2025-06-29T17:30:00.000Z",
  "message": "نظام متتبع طلبات الآيس كريم للساحل الشمالي 2025"
}
```

## 🧊 Product Types

- **3kg Bags**: Standard ice cube bags
- **4kg Bags**: Medium ice cube bags
- **5kg Bags**: Large ice cube bags  
- **Ice Cups**: Individual ice cups

## 📱 WhatsApp Integration

The system generates formatted summaries ready for WhatsApp sharing:

```
Summary - North Coast - macOS 14.0:
Production: 3kg=500kg, 5kg=1000kg, Cups=0
Stock: 3kg=1000kg, 5kg=1500kg, Cups=200
Delivered: بير الماظة (Almaza), 100×3kg, 200×5kg, Rep: Akrm, Driver: Tariq, Time: 14:30:00
Alert: ساشي الماظة (Zone: Almaza, 8 freezers) needs refill!
```

## 🌐 Live Deployment

**Production URL:** `https://sahel-2025-order-tracker-agey5by29-momoussas-projects.vercel.app`

**Vercel Dashboard:** `https://vercel.com/momoussas-projects/sahel-2025-order-tracker`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the ISC License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

For support and questions about the SAHEL 2025 Order Tracker, please contact the development team.

---

**Built with ❤️ for the North Coast Ice Cream Business 2025** 