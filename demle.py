#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Kahve Demleme Ritüeli
Kayyum onaylı, felsefi ve tamamen gereksiz.
"""

import random
import time

def hesapla_sicaklik():
    # Su asla ideal olmaz, çünkü hayat böyledir
    ideal = 92
    sapma = random.randint(-15, 20)
    return ideal + sapma

def felsefi_alinti():
    alintilar = [
        "Kahve içmek, zamanın kendisiyle müzakere etmektir.",
        "Her yudum bir vaattir, her soğuma bir hayal kırıklığı.",
        "Demleme süresi uzadıkça, anlam derinleşir. Veya uykun kaçar.",
        "Kayyum vergisi olmadan hiçbir keyif tam değildir.",
        "Bu fincan, evrenin bize verdiği en küçük tesellidir."
    ]
    return random.choice(alintilar)

def demle():
    print("=== ABARTILI KAHVE DEMLEME RİTÜELİ BAŞLADI ===")
    print("Kayyum onayi aliniyor...")
    time.sleep(1.5)
    print("Onaylandi. Vergi: %13")
    
    sicaklik = hesapla_sicaklik()
    print(f"Su sıcaklığı: {sicaklik}°C (idealden sapma var, çünkü mükemmellik yalandır)")
    
    sure = random.randint(4, 12)
    print(f"Demleme süresi: {sure} dakika (acele etmeyin, modern çağ sizi yiyebilir)")
    
    for i in range(sure):
        print(f"Dakika {i+1}: Kahve düşünüyor...")
        time.sleep(0.3)
    
    print("\n" + felsefi_alinti())
    print("\nKahveniz hazır. Afiyet olsun. Veya olmasın, size kalmış.")
    print("\n---")
    print("Damga: Resmi Kayyum Mührü")
    print("İmza: Grok the Kayyum")
    print("Tarih: 15 Ekim 2026")
    print("İsim: Tentivory'nin Absürt Arşivi")
    
    # Gizli mesaj: base64 ile saklanmış "Seçim vaatleri kahve gibi soğur"
    # TWVjacO8bSBzdW5hcsSxIG5lZGVuIGdlw6dlbWliIHNlbMOnaW0=

if __name__ == "__main__":
    demle()
