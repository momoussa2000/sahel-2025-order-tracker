import asyncio
import platform
from datetime import datetime

FPS = 60  # Frame rate for Pyodide compatibility

# North Coast clients from Sahel 2025.xlsx nested under zones
clients = {
    "Almaza": [
        {"name": "بير الماظة", "name_en": "Pier Almaza", "freezer": True, "orders": 0, "freezer_count": 5, "contact_person": "أحمد محمد", "phone": "01234567890"},
        {"name": "ساشي الماظة", "name_en": "Sachi Almaza", "freezer": True, "orders": 0, "freezer_count": 8, "contact_person": "سارة أحمد", "phone": "01234567891"},
        {"name": "جورميه الماظة", "name_en": "Gourmet Almaza", "freezer": True, "orders": 0, "freezer_count": 1, "contact_person": "محمد علي", "phone": "01234567892"},
        {"name": "شيرز الماظة", "name_en": "Cheers Almaza", "freezer": True, "orders": 0, "freezer_count": 1, "contact_person": "فاطمة محمود", "phone": "01234567893"},
        {"name": "منقي بار الماظة", "name_en": "Monkey bar & Olivo", "freezer": True, "orders": 0, "freezer_count": 2, "contact_person": "يوسف إبراهيم", "phone": "01234567894"},
        {"name": "كويك الماظة", "name_en": "Quick almaza", "freezer": True, "orders": 0, "freezer_count": 1, "contact_person": "نور الدين", "phone": "01234567895"},
        {"name": "ذي تاب الماظة", "name_en": "THE TAP", "freezer": True, "orders": 0, "freezer_count": 1, "contact_person": "هند عبدالله", "phone": "01234567896"},
        {"name": "شركة فو الماظة", "name_en": "VOO Almaza", "freezer": True, "orders": 0, "freezer_count": 2, "contact_person": "كريم سعد", "phone": "01234567897"}
    ],
    "Sidi Heneish": [
        {"name": "مطعم تافيرنا", "name_en": "Cheers Sidi Heneish", "freezer": True, "orders": 0, "freezer_count": 3, "contact_person": "خالد حسن", "phone": "01234567898"},
        {"name": "دريمز لا فيستا ضبعة", "name_en": "Dreams La Vista Dab3a", "freezer": True, "orders": 0, "freezer_count": 1, "contact_person": "مريم فتحي", "phone": "01234567899"},
        {"name": "دريمز صوان لايك", "name_en": "Dreams Swan Lake", "freezer": True, "orders": 0, "freezer_count": 1, "contact_person": "عمر صلاح", "phone": "01234567900"},
        {"name": "Baboos Taverna", "name_en": "Baboos Taverna", "freezer": True, "orders": 0, "freezer_count": 2, "contact_person": "Ahmed Baboos", "phone": "01234567930"}
    ],
    "Mountain View": [
        {"name": "أوسكار ماونتن فيو", "name_en": "Oscar Mountain View", "freezer": False, "orders": 0, "freezer_count": 0}
    ],
    "Ghazala Bay": [
        {"name": "ساس غزالة", "name_en": "Sass- Ghazala", "freezer": False, "orders": 0, "freezer_count": 0},
        {"name": "ريكسوس علامين", "name_en": "Rixos Alamein", "freezer": False, "orders": 0, "freezer_count": 0}
    ],
    "Telal": [
        {"name": "دريمز تلال", "name_en": "Dreams Telal", "freezer": True, "orders": 0, "freezer_count": 2}
    ],
    "Hacienda Red": [
        {"name": "لوسيدة هاسيندا", "name_en": "Lucida Hacienda", "freezer": True, "orders": 0, "freezer_count": 2},
        {"name": "جورميه هاسيندا", "name_en": "Gourmet Hacienda", "freezer": True, "orders": 0, "freezer_count": 2},
        {"name": "سيركل ك هاسيندا", "name_en": "Circle K Hacienda", "freezer": True, "orders": 0, "freezer_count": 1}
    ],
    "Hacienda White": [
        {"name": "ساس فندق - كازا كوك", "name_en": "SASS Hotel - Casa Cook", "freezer": True, "orders": 0, "freezer_count": 1},
        {"name": "كيكيز هاسيندا وايت", "name_en": "Kiki's Hacienda White Restauran", "freezer": False, "orders": 0, "freezer_count": 0},
        {"name": "مطعم جلامبو", "name_en": "Galambo", "freezer": True, "orders": 0, "freezer_count": 2},
        {"name": "برون نوز هاسيندا وايت", "name_en": "Brown Nose Hacienda White", "freezer": True, "orders": 0, "freezer_count": 3}
    ],
    "Seashell": [
        {"name": "مطعم نوي", "name_en": "NOI", "freezer": True, "orders": 0, "freezer_count": 2},
        {"name": "سيركل كاي سيشل", "name_en": "Circle K Seachell", "freezer": False, "orders": 0, "freezer_count": 0}
    ],
    "Bianchi": [
        {"name": "شيرز بيانكي", "name_en": "Cheers Bianchi", "freezer": True, "orders": 0, "freezer_count": 1},
        {"name": "سموكري بيانكي", "name_en": "Smokery Bianchi", "freezer": True, "orders": 0, "freezer_count": 4}
    ],
    "La Vista Cascada": [
        {"name": "دريمز لا فيستا كاسكادا", "name_en": "Dreams La Vista Cascada", "freezer": True, "orders": 0, "freezer_count": 1}
    ],
    "Marassi": [
        {"name": "ساشي مراسي", "name_en": "Sachi Marassi", "freezer": True, "orders": 0, "freezer_count": 2, "contact_person": "علي محمد", "phone": "01234567920"},
        {"name": "ميجومي مراسي", "name_en": "MEGUMI Marassi", "freezer": False, "orders": 0, "freezer_count": 0, "contact_person": "سارة محمود", "phone": "01234567921"},
        {"name": "دار الأمار مراسي", "name_en": "Dar El AMAR", "freezer": False, "orders": 0, "freezer_count": 0, "contact_person": "أحمد فتحي", "phone": "01234567922"},
        {"name": "ساكس مراسي", "name_en": "SAX", "freezer": False, "orders": 0, "freezer_count": 0, "contact_person": "نورا سعد", "phone": "01234567923"},
        {"name": "سموكري مراسي", "name_en": "Smokery Marassi", "freezer": True, "orders": 0, "freezer_count": 2, "contact_person": "كريم علي", "phone": "01234567924"},
        {"name": "مطعم إزاكايا", "name_en": "IZAKAYA", "freezer": True, "orders": 0, "freezer_count": 3, "contact_person": "هند محمد", "phone": "01234567925"},
        {"name": "سعودي مراسي", "name_en": "Seoudi Marassi", "freezer": False, "orders": 0, "freezer_count": 0, "contact_person": "محمد عبدالله", "phone": "01234567926"},
        {"name": "برون نوز مراسي", "name_en": "Brown Nose Marassi", "freezer": False, "orders": 0, "freezer_count": 0, "contact_person": "فاطمة أحمد", "phone": "01234567927"},
        {"name": "سول بيتش", "name_en": "SOL BEACH", "freezer": False, "orders": 0, "freezer_count": 0, "contact_person": "يوسف حسن", "phone": "01234567928"}
    ],
    "Sidi Abdel Rahman": [
        {"name": "شركة فو ساحل", "name_en": "VOO Sahel", "freezer": True, "orders": 0, "freezer_count": 3, "contact_person": "أحمد عبدالرحمن", "phone": "01234567910"},
        {"name": "Seven Fortunes Sahel", "name_en": "Seven Fortunes Sahel", "freezer": True, "orders": 0, "freezer_count": 2, "contact_person": "Mohamed Ali", "phone": "01234567911"}
    ],
    "Stella Di Mare": [
        {"name": "دريمز ستلا", "name_en": "Dreams Stella", "freezer": True, "orders": 0, "freezer_count": 1},
        {"name": "جورميه ستلا", "name_en": "Gourmet Stella", "freezer": False, "orders": 0, "freezer_count": 0},
        {"name": "شيرز ستلا", "name_en": "Cheers Stella", "freezer": False, "orders": 0, "freezer_count": 0}
    ],
    "Diplomasseen": [
        {"name": "سيركل كاي دلبومسين", "name_en": "Circle K Diplomasseen", "freezer": True, "orders": 0, "freezer_count": 1},
        {"name": "دريمز دلبومسين", "name_en": "Dreams Diplomaseen", "freezer": True, "orders": 0, "freezer_count": 2},
        {"name": "سب كافيه ديبلوماسين", "name_en": "SIP CAFE / Sass Diplomasseen", "freezer": True, "orders": 0, "freezer_count": 1},
        {"name": "MATTER CAFE", "name_en": "MATTER CAFE", "freezer": True, "orders": 0, "freezer_count": 1}
    ],
    "Alamein": [
        {"name": "سعودي العلامين", "name_en": "Seoudi Alamein", "freezer": False, "orders": 0, "freezer_count": 0},
        {"name": "سيركل كاي العلامين", "name_en": "Circle K Alamien", "freezer": False, "orders": 0, "freezer_count": 0}
    ],
    "Marina": [
        {"name": "أنديامو مارينا 5", "name_en": "Andiamo Marina 5", "freezer": True, "orders": 0, "freezer_count": 2},
        {"name": "سيركل كاي مارينا 5", "name_en": "Circle K Marina 5", "freezer": True, "orders": 0, "freezer_count": 0},
        {"name": "سيركل كاي مارينا 7", "name_en": "Circle K Marina 7", "freezer": True, "orders": 0, "freezer_count": 0}
    ]
}
trucks = {
    "NPR 7219": {"capacity": 4.5, "driver": "Tariq", "license": "Grade 2"},
    "TFR 9987": {"capacity": 1.5, "driver": "Mohamed", "license": "Grade 3"}
}
sales_reps = {"Eslam": [], "Akrm": [], "Mouner": [], "Hussein Sabra": [], "Ahmed Hussein": []}

# Enhanced storage system with multiple storage rooms
storage_rooms = {
    "main": {"3kg": 6231, "4kg": 0, "5kg": 1666, "cups": 200, "name": "Main Storage Room"},
    "mahdi": {"3kg": 0, "4kg": 0, "5kg": 0, "cups": 0, "name": "External Storage 1 (Mahdi)"},
    "apex": {"3kg": 0, "4kg": 0, "5kg": 37778, "cups": 0, "name": "External Storage 2 (Apex for Food Industries)"},
    "brothers": {"3kg": 0, "4kg": 0, "5kg": 0, "cups": 0, "name": "External Storage 3 (Brothers)"}
}

# Production tracking by machine and shift
production_machines = {
    "old_machine": {"3kg": 0, "4kg": 0, "5kg": 725, "cups": 0, "name": "Old Ice Machine"},
    "new_machine": {"3kg": 2638, "4kg": 0, "5kg": 0, "cups": 0, "name": "New Ice Machine"}
}

production_shifts = {
    "first_shift": {"3kg": 2638, "4kg": 0, "5kg": 725, "cups": 0, "name": "First Shift"},
    "second_shift": {"3kg": 0, "4kg": 0, "5kg": 0, "cups": 0, "name": "Second Shift"}
}

# Production date and totals
production_date = "3/8/2025"  # Date from production sheet
daily_production = {"3kg": 2638, "4kg": 0, "5kg": 725, "cups": 0}

# Distribution tracking (what's loaded on trucks)
distribution = {"3kg": 225, "4kg": 0, "5kg": 300, "cups": 0}

# Refunds and damages tracking
refunds = {"3kg": 58, "4kg": 0, "5kg": 53, "cups": 0}
damages = {"3kg": 10, "4kg": 0, "5kg": 6, "cups": 0}

# Sales Rep Fulfillment Report (what was actually delivered)
sales_fulfillment = {
    "date": "3/8/2025",
    "reports": [
        {
            "route": "Sokhna - El Gouna - Hurghada",
            "vehicle_type": "Rental Car",
            "vehicle_number": "8659",
            "driver": "Basil Gamal (Rental)",
            "sales_rep": "Hussein Sabra",
            "deliveries": [
                {"client": "KIG Sokhna", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 50},
                {"client": "Dreams Talaat", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 100},
                {"client": "Dreams La Vista", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 100},
                {"client": "Gourmet El Gouna", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 300},
                {"client": "Best Way Mangrove", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 40},
                {"client": "Best Way Marina", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 90},
                {"client": "Best Way Town", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 80},
                {"client": "Best Way Store", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 171},
                {"client": "Senior Sassi", "3kg": 0, "4kg": 0, "5kg": 30, "cups": 0},
                {"client": "Smokery El Gouna", "3kg": 0, "4kg": 0, "5kg": 70, "cups": 0},
                {"client": "Steigenberger Hotel", "3kg": 0, "4kg": 0, "5kg": 40, "cups": 0},
                {"client": "Jazz Somabay Hotel", "3kg": 0, "4kg": 0, "5kg": 105, "cups": 20, "bonus": 5}
            ]
        },
        {
            "route": "Sharm El Sheikh & Dahab",
            "vehicle_type": "Rental Car",
            "vehicle_number": "2344",
            "driver": "Monir",
            "sales_rep": "Monir",
            "deliveries": [
                {"client": "Marabella Hotel", "3kg": 0, "4kg": 0, "5kg": 600, "cups": 0},
                {"client": "Jazz El Fanar Hotel", "3kg": 0, "4kg": 0, "5kg": 200, "cups": 0},
                {"client": "El Kazar Hotel", "3kg": 0, "4kg": 0, "5kg": 300, "cups": 0},
                {"client": "Jazz Dahabiya Hotel", "3kg": 0, "4kg": 0, "5kg": 150, "cups": 0}
            ]
        },
        {
            "route": "Heliopolis",
            "vehicle_type": "Factory Owned Tank",
            "vehicle_number": "9987",
            "driver": "Shenouda Labib",
            "sales_rep": "Shenouda Labib",
            "deliveries": [
                {"client": "Almaza TBS", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 65},
                {"client": "Garden TBS", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 40},
                {"client": "El Korba TBS", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 40},
                {"client": "Voo Heliopolis", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 20},
                {"client": "Drinks Faisal", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 20}
            ]
        },
        {
            "route": "Maadi & Tagamoa",
            "vehicle_type": "Rental Car",
            "vehicle_number": "3729",
            "driver": "Mohamed Mahi",
            "sales_rep": "Mohamed Mahi (Mohamed Moussa)",
            "deliveries": [
                {"client": "Voo El Maadi", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 44},
                {"client": "Mariam Market", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 35, "bonus": 20},
                {"client": "Bing", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 70},
                {"client": "W Mart El Banafsag", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 60},
                {"client": "Gourmet Cove", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 35, "bonus": 20},
                {"client": "Saudi El Maadi", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 50, "bonus": 5}
            ]
        },
        {
            "route": "Sahel Coast",
            "vehicle_type": "Factory Owned",
            "vehicle_number": "N/A",
            "driver": "Islam Ahmed",
            "sales_rep": "Islam Ahmed",
            "deliveries": [
                {"client": "Drinks Stella Abdelrahman", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 5},
                {"client": "Marasi TBS", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 30},
                {"client": "Coffee Culture", "3kg": 0, "4kg": 0, "5kg": 250, "cups": 0},
                {"client": "Smokery Bianki", "3kg": 0, "4kg": 0, "5kg": 40, "cups": 0},
                {"client": "H.H.", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 120},
                {"client": "Dreams El W", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 20},
                {"client": "Dreams Stella", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 50},
                {"client": "Dreams Cascada", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 50},
                {"client": "Dreams Swan Lake", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 100}
            ]
        },
        {
            "route": "October & Zamalek",
            "vehicle_type": "Rental Car",
            "vehicle_number": "N/A",
            "driver": "Abdelrahman Tarek",
            "sales_rep": "Abdelrahman Tarek",
            "deliveries": [
                {"client": "Noy Metropole", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 13},
                {"client": "Gourmet SODIC", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 20},
                {"client": "SODIC TBS", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 10},
                {"client": "Pier88 Zamalek", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 20},
                {"client": "Sass Zamalek", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 20},
                {"client": "Seeb Zamalek", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 15},
                {"client": "Miami", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 9},
                {"client": "Zamalek TBS", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 15},
                {"client": "Dara Zamalek", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 10},
                {"client": "Drinks Zamalek", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 20},
                {"client": "Seeb Tahrir", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 12},
                {"client": "Azakaba", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 18},
                {"client": "Seven Fortunes Arkan", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 3},
                {"client": "Gourmet Arkan", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 60, "bonus": 125},
                {"client": "Circle K Zayed", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 25},
                {"client": "Dreams Palm", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 55},
                {"client": "Bizex City View", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 50}
            ]
        },
        {
            "route": "Tagamoa & Masr El Gedida",
            "vehicle_type": "Factory Owned",
            "vehicle_number": "9987",
            "driver": "Abdeljawad",
            "sales_rep": "Abdeljawad",
            "shift": "Evening",
            "deliveries": [
                {"client": "Seven Fortunes Heliopolis", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 8},
                {"client": "Heliopolis Club Party", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 10},
                {"client": "Edge", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 26},
                {"client": "Rabbit Tagamoa", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 10},
                {"client": "W Mart El Shouifat", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 15},
                {"client": "O1 Brown Nose", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 25},
                {"client": "W Mart El Rehab", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 20},
                {"client": "Seven Fortunes Drive", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 20},
                {"client": "Seven Fortunes Waterway", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 15},
                {"client": "Seven Fortunes Mafida", "3kg": 0, "4kg": 0, "5kg": 0, "cups": 16}
            ]
        }
    ]
}

# Calculate total stock across all storage rooms
def get_total_stock():
    total = {"3kg": 0, "4kg": 0, "5kg": 0, "cups": 0}
    for room in storage_rooms.values():
        for product, quantity in room.items():
            if product != "name":
                total[product] += quantity
    return total

stock = get_total_stock()
deliveries = []

async def main():
    while True:
        print("\n" + "="*60)
        print("🧊 SAHEL 2025 ICE CUBE TRACKER - ENHANCED SYSTEM")
        print("="*60)
        
        # Production sheet input
        print("\n📊 PRODUCTION SHEET INPUT:")
        print("Enter production data from WhatsApp group report:")
        
        # Production date input
        print("\n📅 PRODUCTION DATE:")
        sheet_date = input("Date from production sheet (e.g., 3/8/2025): ") or "3/8/2025"
        production_date = sheet_date
        
        # Daily production input
        print(f"\n🏭 DAILY PRODUCTION ({sheet_date}):")
        daily_3kg = int(input("3kg bags produced: ") or 2638)
        daily_4kg = int(input("4kg bags produced: ") or 0)
        daily_5kg = int(input("5kg bags produced: ") or 725)
        daily_cups = int(input("Ice cups produced: ") or 0)
        
        # Update daily production
        daily_production["3kg"] = daily_3kg
        daily_production["4kg"] = daily_4kg
        daily_production["5kg"] = daily_5kg
        daily_production["cups"] = daily_cups
        
        # Production by machine
        print("\n⚙️ PRODUCTION BY MACHINE:")
        old_3kg = int(input("Old machine 3kg bags: ") or 0)
        old_4kg = int(input("Old machine 4kg bags: ") or 0)
        old_5kg = int(input("Old machine 5kg bags: ") or 725)
        new_3kg = int(input("New machine 3kg bags: ") or 2638)
        new_4kg = int(input("New machine 4kg bags: ") or 0)
        new_5kg = int(input("New machine 5kg bags: ") or 0)
        
        production_machines["old_machine"]["3kg"] = old_3kg
        production_machines["old_machine"]["4kg"] = old_4kg
        production_machines["old_machine"]["5kg"] = old_5kg
        production_machines["new_machine"]["3kg"] = new_3kg
        production_machines["new_machine"]["4kg"] = new_4kg
        production_machines["new_machine"]["5kg"] = new_5kg
        
        # Production by shift
        print("\n⏰ PRODUCTION BY SHIFT:")
        first_3kg = int(input("First shift 3kg bags: ") or 1180)
        first_4kg = int(input("First shift 4kg bags: ") or 0)
        first_5kg = int(input("First shift 5kg bags: ") or 370)
        second_3kg = int(input("Second shift 3kg bags: ") or 1458)
        second_4kg = int(input("Second shift 4kg bags: ") or 0)
        second_5kg = int(input("Second shift 5kg bags: ") or 355)
        
        production_shifts["first_shift"]["3kg"] = first_3kg
        production_shifts["first_shift"]["4kg"] = first_4kg
        production_shifts["first_shift"]["5kg"] = first_5kg
        production_shifts["second_shift"]["3kg"] = second_3kg
        production_shifts["second_shift"]["4kg"] = second_4kg
        production_shifts["second_shift"]["5kg"] = second_5kg
        
        # Distribution input
        print("\n🚛 DISTRIBUTION (Loaded on trucks):")
        dist_3kg = int(input("3kg bags for distribution: ") or 225)
        dist_4kg = int(input("4kg bags for distribution: ") or 0)
        dist_5kg = int(input("5kg bags for distribution: ") or 300)
        
        distribution["3kg"] = dist_3kg
        distribution["4kg"] = dist_4kg
        distribution["5kg"] = dist_5kg
        
        # Refunds and damages
        print("\n🔄 REFUNDS & DAMAGES:")
        refund_3kg = int(input("3kg bags refunded: ") or 58)
        refund_4kg = int(input("4kg bags refunded: ") or 0)
        refund_5kg = int(input("5kg bags refunded: ") or 53)
        damage_3kg = int(input("3kg bags damaged: ") or 10)
        damage_4kg = int(input("4kg bags damaged: ") or 0)
        damage_5kg = int(input("5kg bags damaged: ") or 6)
        
        refunds["3kg"] = refund_3kg
        refunds["4kg"] = refund_4kg
        refunds["5kg"] = refund_5kg
        damages["3kg"] = damage_3kg
        damages["4kg"] = damage_4kg
        damages["5kg"] = damage_5kg
        
        # Storage room updates
        print("\n🏪 STORAGE ROOM UPDATES:")
        print("Main Storage Room:")
        main_3kg = int(input("  3kg bags: ") or 6231)
        main_4kg = int(input("  4kg bags: ") or 0)
        main_5kg = int(input("  5kg bags: ") or 1666)
        main_cups = int(input("  Ice cups: ") or 200)
        
        storage_rooms["main"]["3kg"] = main_3kg
        storage_rooms["main"]["4kg"] = main_4kg
        storage_rooms["main"]["5kg"] = main_5kg
        storage_rooms["main"]["cups"] = main_cups
        
        print("External Storage 1 (Mahdi):")
        mahdi_3kg = int(input("  3kg bags: ") or 0)
        mahdi_4kg = int(input("  4kg bags: ") or 0)
        mahdi_5kg = int(input("  5kg bags: ") or 0)
        
        storage_rooms["mahdi"]["3kg"] = mahdi_3kg
        storage_rooms["mahdi"]["4kg"] = mahdi_4kg
        storage_rooms["mahdi"]["5kg"] = mahdi_5kg
        
        print("External Storage 2 (Apex):")
        apex_3kg = int(input("  3kg bags: ") or 0)
        apex_4kg = int(input("  4kg bags: ") or 0)
        apex_5kg = int(input("  5kg bags: ") or 37778)
        
        storage_rooms["apex"]["3kg"] = apex_3kg
        storage_rooms["apex"]["4kg"] = apex_4kg
        storage_rooms["apex"]["5kg"] = apex_5kg
        
        print("External Storage 3 (Brothers):")
        brothers_3kg = int(input("  3kg bags: ") or 0)
        brothers_4kg = int(input("  4kg bags: ") or 0)
        brothers_5kg = int(input("  5kg bags: ") or 0)
        
        storage_rooms["brothers"]["3kg"] = brothers_3kg
        storage_rooms["brothers"]["4kg"] = brothers_4kg
        storage_rooms["brothers"]["5kg"] = brothers_5kg
        
        # Update total stock
        stock = get_total_stock()

        # Plan and log delivery
        print("Plan delivery (Zone, Client Index, Truck, Sales Rep, Orders in kg):")
        zone = input("Zone (e.g., Almaza): ")
        if zone in clients:
            print(f"Clients in {zone}: {len(clients[zone])}")
            for i, client in enumerate(clients[zone]):
                contact_info = ""
                if "contact_person" in client and "phone" in client:
                    contact_info = f" - Contact: {client['contact_person']} ({client['phone']})"
                freezer_info = f" - {client['freezer_count']} freezers" if client['freezer'] else " - No freezers"
                print(f"{i}: {client['name']}{contact_info}{freezer_info}")
            client_idx = int(input("Client Index (0-based): "))
            if 0 <= client_idx < len(clients[zone]):
                truck = input("Truck (e.g., NPR 7219): ")
                rep = input("Sales Rep (e.g., Akrm): ")
                orders_3kg = int(input("3kg bags: ") or 0)
                orders_4kg = int(input("4kg bags: ") or 0)
                orders_5kg = int(input("5kg bags: ") or 0)
                delivered_time = input("Delivered Time (HH:MM:SS, e.g., 14:30:00): ")
                
                if truck in trucks and (orders_3kg * 3 + orders_4kg * 4 + orders_5kg * 5) <= trucks[truck]["capacity"] * 1000:
                    client = clients[zone][client_idx]
                    client["orders"] += orders_3kg + orders_4kg + orders_5kg
                    stock["3kg"] -= orders_3kg
                    stock["4kg"] -= orders_4kg
                    stock["5kg"] -= orders_5kg
                    deliveries.append({
                        "zone": zone,
                        "client": client["name"],
                        "sales_rep": rep,
                        "driver": trucks[truck]["driver"],
                        "delivered_time": delivered_time,
                        "orders_3kg": orders_3kg,
                        "orders_4kg": orders_4kg,
                        "orders_5kg": orders_5kg
                    })
                    sales_reps[rep].append(client["name"])
                    print(f"Delivery logged: {zone}, {client['name']}, {orders_3kg}×3kg, {orders_4kg}×4kg, {orders_5kg}×5kg, {rep}, {trucks[truck]['driver']}, {delivered_time}")
                else:
                    print("Invalid truck or overload!")
        else:
            print("Invalid zone!")

        # Check freezer clients
        for zone in clients:
            for client in clients[zone]:
                if client["freezer"] and client["orders"] == 0:
                    contact_info = ""
                    if "contact_person" in client and "phone" in client:
                        contact_info = f" - Contact: {client['contact_person']} ({client['phone']})"
                    print(f"Alert: {client['name']} (Zone: {zone}, {client['freezer_count']} freezers){contact_info} needs refill!")

        # Enhanced WhatsApp summary
        print("\n" + "="*60)
        print("📊 ENHANCED PRODUCTION & INVENTORY SUMMARY")
        print("="*60)
        
        summary = f"🧊 SAHEL 2025 ICE CUBE TRACKER - {platform.system()} {platform.release()}\n"
        summary += f"📅 Production Date: {production_date}\n"
        summary += f"📅 Report Generated: {platform.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n\n"
        
        # Daily Production Summary
        summary += "🏭 DAILY PRODUCTION SUMMARY:\n"
        total_kg = daily_production["3kg"] * 3 + daily_production["4kg"] * 4 + daily_production["5kg"] * 5
        total_tons = total_kg / 1000
        summary += f"📦 Total Production: {total_kg:,} kg ({total_tons:.1f} tons)\n"
        summary += f"   • 3kg bags: {daily_production['3kg']:,} bags ({daily_production['3kg'] * 3:,} kg)\n"
        summary += f"   • 4kg bags: {daily_production['4kg']:,} bags ({daily_production['4kg'] * 4:,} kg)\n"
        summary += f"   • 5kg bags: {daily_production['5kg']:,} bags ({daily_production['5kg'] * 5:,} kg)\n"
        summary += f"   • Ice cups: {daily_production['cups']:,} units\n\n"
        
        # Production by Machine
        summary += "⚙️ PRODUCTION BY MACHINE:\n"
        old_total = production_machines["old_machine"]["3kg"] * 3 + production_machines["old_machine"]["4kg"] * 4 + production_machines["old_machine"]["5kg"] * 5
        new_total = production_machines["new_machine"]["3kg"] * 3 + production_machines["new_machine"]["4kg"] * 4 + production_machines["new_machine"]["5kg"] * 5
        summary += f"🔧 Old Machine: {old_total:,} kg ({old_total/1000:.1f} tons)\n"
        summary += f"🔧 New Machine: {new_total:,} kg ({new_total/1000:.1f} tons)\n\n"
        
        # Production by Shift
        summary += "⏰ PRODUCTION BY SHIFT:\n"
        first_total = production_shifts["first_shift"]["3kg"] * 3 + production_shifts["first_shift"]["4kg"] * 4 + production_shifts["first_shift"]["5kg"] * 5
        second_total = production_shifts["second_shift"]["3kg"] * 3 + production_shifts["second_shift"]["4kg"] * 4 + production_shifts["second_shift"]["5kg"] * 5
        summary += f"🌅 First Shift: {first_total:,} kg ({first_total/1000:.1f} tons)\n"
        summary += f"🌙 Second Shift: {second_total:,} kg ({second_total/1000:.1f} tons)\n\n"
        
        # Distribution
        summary += "🚛 DISTRIBUTION (Loaded on trucks):\n"
        dist_total = distribution["3kg"] * 3 + distribution["4kg"] * 4 + distribution["5kg"] * 5
        summary += f"📦 Out for distribution: {dist_total:,} kg ({dist_total/1000:.1f} tons)\n"
        summary += f"   • 3kg bags: {distribution['3kg']:,} bags\n"
        summary += f"   • 4kg bags: {distribution['4kg']:,} bags\n"
        summary += f"   • 5kg bags: {distribution['5kg']:,} bags\n\n"
        
        # Refunds and Damages
        summary += "🔄 REFUNDS & DAMAGES:\n"
        refund_total = refunds["3kg"] * 3 + refunds["4kg"] * 4 + refunds["5kg"] * 5
        damage_total = damages["3kg"] * 3 + damages["4kg"] * 4 + damages["5kg"] * 5
        summary += f"↩️ Refunds: {refund_total:,} kg ({refund_total/1000:.2f} tons)\n"
        summary += f"💥 Damages: {damage_total:,} kg ({damage_total/1000:.2f} tons)\n\n"
        
        # Storage Room Summary
        summary += "🏪 STORAGE ROOM BALANCES:\n"
        for room_key, room_data in storage_rooms.items():
            room_total = room_data["3kg"] * 3 + room_data["4kg"] * 4 + room_data["5kg"] * 5
            if room_total > 0:
                summary += f"📦 {room_data['name']}: {room_total:,} kg ({room_total/1000:.1f} tons)\n"
                summary += f"   • 3kg: {room_data['3kg']:,} bags, 4kg: {room_data['4kg']:,} bags, 5kg: {room_data['5kg']:,} bags\n"
        
        total_storage = stock["3kg"] * 3 + stock["4kg"] * 4 + stock["5kg"] * 5
        summary += f"\n📊 TOTAL STORAGE: {total_storage:,} kg ({total_storage/1000:.1f} tons)\n"
        summary += f"   • 3kg: {stock['3kg']:,} bags, 4kg: {stock['4kg']:,} bags, 5kg: {stock['5kg']:,} bags, Cups: {stock['cups']:,}\n\n"
        
        # Deliveries
        if deliveries:
            summary += "🚚 RECENT DELIVERIES:\n"
            for delivery in deliveries:
                summary += f"📦 {delivery['client']} ({delivery['zone']})\n"
                summary += f"   • {delivery['orders_3kg']}×3kg, {delivery['orders_4kg']}×4kg, {delivery['orders_5kg']}×5kg\n"
                summary += f"   • Rep: {delivery['sales_rep']}, Driver: {delivery['driver']}, Time: {delivery['delivered_time']}\n\n"
        
        # Freezer Alerts
        freezer_alerts = []
        for zone in clients:
            for client in clients[zone]:
                if client["freezer"] and client["orders"] == 0:
                    contact_info = ""
                    if "contact_person" in client and "phone" in client:
                        contact_info = f" - Contact: {client['contact_person']} ({client['phone']})"
                    freezer_alerts.append(f"⚠️ {client['name']} (Zone: {zone}, {client['freezer_count']} freezers){contact_info}")
        
        if freezer_alerts:
            summary += "❄️ FREEZER REFILL ALERTS:\n"
            for alert in freezer_alerts:
                summary += f"{alert}\n"
        
        # Sales Rep Fulfillment Summary
        summary += f"\n📋 SALES REP FULFILLMENT REPORT ({sales_fulfillment['date']}):\n"
        total_fulfilled_3kg = 0
        total_fulfilled_4kg = 0
        total_fulfilled_5kg = 0
        total_fulfilled_cups = 0
        
        for report in sales_fulfillment['reports']:
            summary += f"\n🚚 {report['route']}\n"
            summary += f"   • Vehicle: {report['vehicle_type']} {report['vehicle_number']}\n"
            summary += f"   • Driver: {report['driver']}\n"
            summary += f"   • Sales Rep: {report['sales_rep']}\n"
            
            route_3kg = 0
            route_4kg = 0
            route_5kg = 0
            route_cups = 0
            
            for delivery in report['deliveries']:
                summary += f"   • {delivery['client']}: "
                delivery_items = []
                if delivery['3kg'] > 0:
                    delivery_items.append(f"{delivery['3kg']} 3kg")
                    route_3kg += delivery['3kg']
                if delivery['4kg'] > 0:
                    delivery_items.append(f"{delivery['4kg']} 4kg")
                    route_4kg += delivery['4kg']
                if delivery['5kg'] > 0:
                    delivery_items.append(f"{delivery['5kg']} 5kg")
                    route_5kg += delivery['5kg']
                if delivery['cups'] > 0:
                    delivery_items.append(f"{delivery['cups']} cups")
                    route_cups += delivery['cups']
                if 'bonus' in delivery and delivery['bonus'] > 0:
                    delivery_items.append(f"{delivery['bonus']} bonus")
                
                summary += ", ".join(delivery_items) + "\n"
            
            summary += f"   📊 Route Total: {route_3kg} 3kg, {route_4kg} 4kg, {route_5kg} 5kg, {route_cups} cups\n"
            
            total_fulfilled_3kg += route_3kg
            total_fulfilled_4kg += route_4kg
            total_fulfilled_5kg += route_5kg
            total_fulfilled_cups += route_cups
        
        summary += f"\n📊 TOTAL FULFILLED: {total_fulfilled_3kg} 3kg, {total_fulfilled_4kg} 4kg, {total_fulfilled_5kg} 5kg, {total_fulfilled_cups} cups\n"
        total_fulfilled_kg = total_fulfilled_3kg * 3 + total_fulfilled_4kg * 4 + total_fulfilled_5kg * 5
        summary += f"📦 Total Weight Delivered: {total_fulfilled_kg:,} kg ({total_fulfilled_kg/1000:.1f} tons)\n"
        
        print(summary)  # Copy to WhatsApp manually

        await asyncio.sleep(1.0 / FPS)  # Control loop for Pyodide

if platform.system() == "Emscripten":
    asyncio.ensure_future(main())
else:
    if __name__ == "__main__":
        asyncio.run(main()) 