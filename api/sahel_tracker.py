import asyncio
import platform
from datetime import datetime

FPS = 60  # Frame rate for Pyodide compatibility

# North Coast clients from Sahel 2025.xlsx nested under zones
clients = {
    "Almaza": [
        {"name": "بير الماظة", "freezer": True, "orders": 0, "freezer_count": 5},
        {"name": "ساشي الماظة", "freezer": True, "orders": 0, "freezer_count": 8},
        {"name": "جورميه الماظة", "freezer": True, "orders": 0, "freezer_count": 1},
        {"name": "شيرز الماظة", "freezer": True, "orders": 0, "freezer_count": 1},
        {"name": "منقي بار الماظة", "freezer": True, "orders": 0, "freezer_count": 2},
        {"name": "كويك الماظة", "freezer": True, "orders": 0, "freezer_count": 1},
        {"name": "ذي تاب الماظة", "freezer": True, "orders": 0, "freezer_count": 1},
        {"name": "شركة فو الماظة", "freezer": True, "orders": 0, "freezer_count": 2}
    ],
    "Sidi Heneish": [
        {"name": "مطعم تافيرنا", "freezer": True, "orders": 0, "freezer_count": 3},
        {"name": "دريمز لا فيستا ضبعة", "freezer": True, "orders": 0, "freezer_count": 1},
        {"name": "دريمز صوان لايك", "freezer": True, "orders": 0, "freezer_count": 1}
    ],
    "Mountain View": [
        {"name": "أوسكار ماونتن فيو", "freezer": False, "orders": 0, "freezer_count": 0}
    ],
    "Ghazala Bay": [
        {"name": "ساس غزالة", "freezer": False, "orders": 0, "freezer_count": 0},
        {"name": "ريكسوس علامين", "freezer": False, "orders": 0, "freezer_count": 0}
    ],
    "Telal": [
        {"name": "دريمز تلال", "freezer": True, "orders": 0, "freezer_count": 2}
    ],
    "Hacienda Red": [
        {"name": "لوسيدة هاسيندا", "freezer": True, "orders": 0, "freezer_count": 2},
        {"name": "جورميه هاسيندا", "freezer": True, "orders": 0, "freezer_count": 2},
        {"name": "سيركل ك هاسيندا", "freezer": True, "orders": 0, "freezer_count": 1}
    ],
    "Hacienda White": [
        {"name": "ساس فندق - كازا كوك", "freezer": True, "orders": 0, "freezer_count": 1},
        {"name": "كيكيز هاسيندا وايت", "freezer": False, "orders": 0, "freezer_count": 0},
        {"name": "مطعم جلامبو", "freezer": True, "orders": 0, "freezer_count": 2},
        {"name": "برون نوز هاسيندا وايت", "freezer": True, "orders": 0, "freezer_count": 3}
    ],
    "Seashell": [
        {"name": "مطعم نوي", "freezer": True, "orders": 0, "freezer_count": 2},
        {"name": "سيركل كاي سيشل", "freezer": False, "orders": 0, "freezer_count": 0}
    ],
    "Bianchi": [
        {"name": "شيرز بيانكي", "freezer": True, "orders": 0, "freezer_count": 1},
        {"name": "سموكري بيانكي", "freezer": True, "orders": 0, "freezer_count": 4}
    ],
    "La Vista Cascada": [
        {"name": "دريمز لا فيستا كاسكادا", "freezer": True, "orders": 0, "freezer_count": 1}
    ],
    "Marassi": [
        {"name": "ساشي مراسي", "freezer": True, "orders": 0, "freezer_count": 2},
        {"name": "ميجومي مراسي", "freezer": False, "orders": 0, "freezer_count": 0},
        {"name": "دار الأمار مراسي", "freezer": False, "orders": 0, "freezer_count": 0},
        {"name": "ساكس مراسي", "freezer": False, "orders": 0, "freezer_count": 0},
        {"name": "سموكري مراسي", "freezer": True, "orders": 0, "freezer_count": 2},
        {"name": "مطعم إزاكايا", "freezer": True, "orders": 0, "freezer_count": 3},
        {"name": "سعودي مراسي", "freezer": False, "orders": 0, "freezer_count": 0},
        {"name": "برون نوز مراسي", "freezer": False, "orders": 0, "freezer_count": 0},
        {"name": "سول بيتش", "freezer": False, "orders": 0, "freezer_count": 0}
    ],
    "Sidi Abdel Rahman": [
        {"name": "شركة فو ساحل", "freezer": True, "orders": 0, "freezer_count": 3},
        {"name": "Seven Fortunes Sahel", "freezer": True, "orders": 0, "freezer_count": 2}
    ],
    "Stella Di Mare": [
        {"name": "دريمز ستلا", "freezer": True, "orders": 0, "freezer_count": 1},
        {"name": "جورميه ستلا", "freezer": False, "orders": 0, "freezer_count": 0},
        {"name": "شيرز ستلا", "freezer": False, "orders": 0, "freezer_count": 0}
    ],
    "Diplomasseen": [
        {"name": "سيركل كاي دلبومسين", "freezer": True, "orders": 0, "freezer_count": 1},
        {"name": "دريمز دلبومسين", "freezer": True, "orders": 0, "freezer_count": 2},
        {"name": "سب كافيه ديبلوماسين", "freezer": True, "orders": 0, "freezer_count": 1},
        {"name": "MATTER CAFE", "freezer": True, "orders": 0, "freezer_count": 1}
    ],
    "Alamein": [
        {"name": "سعودي العلامين", "freezer": False, "orders": 0, "freezer_count": 0},
        {"name": "سيركل كاي العلامين", "freezer": False, "orders": 0, "freezer_count": 0}
    ],
    "Marina": [
        {"name": "أنديامو مارينا 5", "freezer": True, "orders": 0, "freezer_count": 2},
        {"name": "سيركل كاي مارينا 5", "freezer": True, "orders": 0, "freezer_count": 0},
        {"name": "سيركل كاي مارينا 7", "freezer": True, "orders": 0, "freezer_count": 0}
    ]
}
trucks = {
    "NPR 7219": {"capacity": 4.5, "driver": "Tariq", "license": "Grade 2"},
    "TFR 9987": {"capacity": 1.5, "driver": "Mohamed", "license": "Grade 3"}
}
sales_reps = {"Eslam": [], "Akrm": [], "Mouner": [], "Hussein Sabra": [], "Ahmed Hussein": []}
stock = {"3kg": 1000, "5kg": 1500, "cups": 200}
production = {"3kg": 0, "5kg": 0, "cups": 0}
deliveries = []

async def main():
    while True:
        # Input production
        print("Enter daily production (kg):")
        prod_3kg = int(input("3kg: ") or 0)
        prod_5kg = int(input("5kg: ") or 0)
        prod_cups = int(input("Cups: ") or 0)
        production["3kg"] += prod_3kg
        production["5kg"] += prod_5kg
        production["cups"] += prod_cups
        stock["3kg"] += prod_3kg
        stock["5kg"] += prod_5kg
        stock["cups"] += prod_cups

        # Plan and log delivery
        print("Plan delivery (Zone, Client Index, Truck, Sales Rep, Orders in kg):")
        zone = input("Zone (e.g., Almaza): ")
        if zone in clients:
            print(f"Clients in {zone}: {len(clients[zone])}")
            for i, client in enumerate(clients[zone]):
                print(f"{i}: {client['name']}")
            client_idx = int(input("Client Index (0-based): "))
            if 0 <= client_idx < len(clients[zone]):
                truck = input("Truck (e.g., NPR 7219): ")
                rep = input("Sales Rep (e.g., Akrm): ")
                orders_3kg = int(input("3kg Orders: ") or 0)
                orders_5kg = int(input("5kg Orders: ") or 0)
                delivered_time = input("Delivered Time (HH:MM:SS, e.g., 14:30:00): ")
                
                if truck in trucks and (orders_3kg * 3 + orders_5kg * 5) <= trucks[truck]["capacity"] * 1000:
                    client = clients[zone][client_idx]
                    client["orders"] += orders_3kg + orders_5kg
                    stock["3kg"] -= orders_3kg
                    stock["5kg"] -= orders_5kg
                    deliveries.append({
                        "zone": zone,
                        "client": client["name"],
                        "sales_rep": rep,
                        "driver": trucks[truck]["driver"],
                        "delivered_time": delivered_time,
                        "orders_3kg": orders_3kg,
                        "orders_5kg": orders_5kg
                    })
                    sales_reps[rep].append(client["name"])
                    print(f"Delivery logged: {zone}, {client['name']}, {orders_3kg}×3kg, {orders_5kg}×5kg, {rep}, {trucks[truck]['driver']}, {delivered_time}")
                else:
                    print("Invalid truck or overload!")
        else:
            print("Invalid zone!")

        # Check freezer clients
        for zone in clients:
            for client in clients[zone]:
                if client["freezer"] and client["orders"] == 0:
                    print(f"Alert: {client['name']} (Zone: {zone}, {client['freezer_count']} freezers) needs refill!")

        # WhatsApp summary
        summary = f"Summary - North Coast - {platform.system()} {platform.release()}:\n"
        summary += f"Production: 3kg={production['3kg']}kg, 5kg={production['5kg']}kg, Cups={production['cups']}\n"
        summary += f"Stock: 3kg={stock['3kg']}kg, 5kg={stock['5kg']}kg, Cups={stock['cups']}\n"
        for delivery in deliveries:
            summary += f"Delivered: {delivery['client']} ({delivery['zone']}), {delivery['orders_3kg']}×3kg, {delivery['orders_5kg']}×5kg, Rep: {delivery['sales_rep']}, Driver: {delivery['driver']}, Time: {delivery['delivered_time']}\n"
        for zone in clients:
            for client in clients[zone]:
                if client["freezer"] and client["orders"] == 0:
                    summary += f"Alert: {client['name']} (Zone: {zone}, {client['freezer_count']} freezers) needs refill!\n"
        print(summary)  # Copy to WhatsApp manually

        await asyncio.sleep(1.0 / FPS)  # Control loop for Pyodide

if platform.system() == "Emscripten":
    asyncio.ensure_future(main())
else:
    if __name__ == "__main__":
        asyncio.run(main()) 