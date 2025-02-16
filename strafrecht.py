#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
strafrecht_python_komplett.py

Dies ist eine reine Python-Version des kompletten Strafkatalog-Skripts (ursprünglich HTML/JS).
Du kannst das Skript in der Konsole ausführen, um:
- Nach Gesetzen/Paragraphen/Beschreibungen zu suchen
- Gefundene Einträge in eine Auswahl-Liste aufzunehmen
- Einträge aus der Auswahl zu entfernen
- Summen (Bußgelder, Haftzeiten, Punkte) anzuzeigen

Starte es einfach per:
    python strafrecht_python_komplett.py
"""

# --- Datengrundlage: Liste von Dicts (vollständiger Strafkatalog) ---
STRAF_KATALOG = [
    #==================== StGB ====================
    {"law": "StGB", "paragraph": "§1",  "description": "Diebstahl",
     "min_bussgeld": "25'000",  "max_bussgeld": "60'000",
     "min_haft": 10,  "max_haft": 10,  "points": 0},

    {"law": "StGB", "paragraph": "§2",  "description": "Raubüberfall",
     "min_bussgeld": "25'000",  "max_bussgeld": "60'000",
     "min_haft": 15,  "max_haft": 30,  "points": 0},

    {"law": "StGB", "paragraph": "§3",  "description": "Bewaffneter Raubüberfall",
     "min_bussgeld": "50'000",  "max_bussgeld": "125'000",
     "min_haft": 20,  "max_haft": 40,  "points": 0},

    {"law": "StGB", "paragraph": "§4",  "description": "Erpressung",
     "min_bussgeld": "45'000",  "max_bussgeld": "110'000",
     "min_haft": 10,  "max_haft": 20,  "points": 0},

    {"law": "StGB", "paragraph": "§5",  "description": "Bestechung von Staatsbeamten",
     "min_bussgeld": "25'000",  "max_bussgeld": "60'000",
     "min_haft": 10,  "max_haft": 25,  "points": 0},

    {"law": "StGB", "paragraph": "§6",  "description": "Betrug",
     "min_bussgeld": "50'000",  "max_bussgeld": "150'000",
     "min_haft": 10,  "max_haft": 30,  "points": 0},

    {"law": "StGB", "paragraph": "§7",  "description": "Fahrlässige Körperverletzung",
     "min_bussgeld": "50'000",  "max_bussgeld": "125'000",
     "min_haft": 0,   "max_haft": 10,  "points": 0},

    {"law": "StGB", "paragraph": "§8",  "description": "Vorsätzliche Körperverletzung",
     "min_bussgeld": "50'000",  "max_bussgeld": "125'000",
     "min_haft": 20,  "max_haft": 30,  "points": 0},

    {"law": "StGB", "paragraph": "§9",  "description": "Sachbeschädigung an Städtischen Objekten",
     "min_bussgeld": "25'000",  "max_bussgeld": "60'000",
     "min_haft": 0,   "max_haft": 0,   "points": 0},

    {"law": "StGB", "paragraph": "§10", "description": "Totschlag",
     "min_bussgeld": "200'000", "max_bussgeld": "450'000",
     "min_haft": 10,  "max_haft": 50,  "points": 0},

    {"law": "StGB", "paragraph": "§11", "description": "Mord",
     "min_bussgeld": "375'000", "max_bussgeld": "950'000",
     "min_haft": 90,  "max_haft": 90,  "points": 0},

    {"law": "StGB", "paragraph": "§12", "description": "Unterlassene Hilfeleistung",
     "min_bussgeld": "50'000",  "max_bussgeld": "125'000",
     "min_haft": 15,  "max_haft": 35,  "points": 0},

    {"law": "StGB", "paragraph": "§13", "description": "Beleidigung",
     "min_bussgeld": "15'000",  "max_bussgeld": "40'000",
     "min_haft": 0,   "max_haft": 0,   "points": 0},

    {"law": "StGB", "paragraph": "§14", "description": "Üble Nachrede",
     "min_bussgeld": "25'000",  "max_bussgeld": "60'000",
     "min_haft": 0,   "max_haft": 0,   "points": 0},

    {"law": "StGB", "paragraph": "§15", "description": "Drohung",
     "min_bussgeld": "35'000",  "max_bussgeld": "90'000",
     "min_haft": 10,  "max_haft": 25,  "points": 0},

    {"law": "StGB", "paragraph": "§16", "description": "Hausfriedensbruch",
     "min_bussgeld": "20'000",  "max_bussgeld": "55'000",
     "min_haft": 0,   "max_haft": 0,   "points": 0},

    {"law": "StGB", "paragraph": "§17", "description": "Freiheitsberaubung",
     "min_bussgeld": "75'000",  "max_bussgeld": "190'000",
     "min_haft": 15,  "max_haft": 50,  "points": 0},

    {"law": "StGB", "paragraph": "§18", "description": "Widerstand gegen die Staatsbehörden",
     "min_bussgeld": "75'000",  "max_bussgeld": "125'000",
     "min_haft": 15,  "max_haft": 30,  "points": 0},

    {"law": "StGB", "paragraph": "§19", "description": "Amtsanmassung",
     "min_bussgeld": "75'000",  "max_bussgeld": "190'000",
     "min_haft": 25,  "max_haft": 50,  "points": 0},

    {"law": "StGB", "paragraph": "§20", "description": "Missbräuchlicher Notruf",
     "min_bussgeld": "20'000",  "max_bussgeld": "50'000",
     "min_haft": 0,   "max_haft": 0,   "points": 0},

    {"law": "StGB", "paragraph": "§21", "description": "Missachtung des Verschleierungsverbots/Vermummungsverbot",
     "min_bussgeld": "10'000",  "max_bussgeld": "30'000",
     "min_haft": 0,   "max_haft": 0,   "points": 0},

    {"law": "StGB", "paragraph": "§22", "description": "Verweigerung der Identitätsfeststellung",
     "min_bussgeld": "15'000",  "max_bussgeld": "40'000",
     "min_haft": 0,   "max_haft": 0,   "points": 0},

    {"law": "StGB", "paragraph": "§23", "description": "Geiselnahme",
     "min_bussgeld": "100'000", "max_bussgeld": "250'000",
     "min_haft": 25,  "max_haft": 70,  "points": 0},

    {"law": "StGB", "paragraph": "§24", "description": "Besitz illegaler Gegenstände",
     "min_bussgeld": "25'000",  "max_bussgeld": "60'000",
     "min_haft": 10,  "max_haft": 10,  "points": 0},

    {"law": "StGB", "paragraph": "§25", "description": "Urkundenfälschung",
     "min_bussgeld": "50'000",  "max_bussgeld": "125'000",
     "min_haft": 10,  "max_haft": 20,  "points": 0},

    {"law": "StGB", "paragraph": "§26", "description": "Sperrzonen",
     "min_bussgeld": "250'000", "max_bussgeld": "625'000",
     "min_haft": 25,  "max_haft": 60,  "points": 0},

    {"law": "StGB", "paragraph": "§27", "description": "Erregung öffentlichen Ärgernisses",
     "min_bussgeld": "25'000",  "max_bussgeld": "60'000",
     "min_haft": 0,   "max_haft": 0,   "points": 0},

    {"law": "StGB", "paragraph": "§28", "description": "Meineid",
     "min_bussgeld": "125'000", "max_bussgeld": "325'000",
     "min_haft": 20,  "max_haft": 50,  "points": 0},

    {"law": "StGB", "paragraph": "§29", "description": "Hochverat",
     "min_bussgeld": "150'000", "max_bussgeld": "450'000",
     "min_haft": 90,  "max_haft": 90,  "points": 0},

    {"law": "StGB", "paragraph": "§30", "description": "Terroristischer Akt",
     "min_bussgeld": "450'000", "max_bussgeld": "625'000",
     "min_haft": 90,  "max_haft": 90,  "points": 0},

    {"law": "StGB", "paragraph": "§31", "description": "Missachtung Polizeilicher Anweisungen",
     "min_bussgeld": "25'000",  "max_bussgeld": "60'000",
     "min_haft": 10,  "max_haft": 25,  "points": 0},

    #==================== BtMG ====================
    {"law": "BtMG", "paragraph": "§3 Abs.1.c",    "description": "Besitz von Material zum Anbau von BTM",
     "min_bussgeld": "30'000",  "max_bussgeld": "125'000",
     "min_haft": 10,  "max_haft": 10,  "points": 0},

    {"law": "BtMG", "paragraph": "§3 Abs.1.b",    "description": "Besitz von Material zur Herstellung von BTM",
     "min_bussgeld": "40'000",  "max_bussgeld": "150'000",
     "min_haft": 15,  "max_haft": 15,  "points": 0},

    {"law": "BtMG", "paragraph": "§3 Abs.1.c (2)","description": "Anbau von BTM",
     "min_bussgeld": "50'000",  "max_bussgeld": "200'000",
     "min_haft": 20,  "max_haft": 20,  "points": 0},

    {"law": "BtMG", "paragraph": "§3 Abs.1.d",    "description": "Herstellung von BTM",
     "min_bussgeld": "70'000",  "max_bussgeld": "250'000",
     "min_haft": 30,  "max_haft": 30,  "points": 0},

    {"law": "BtMG", "paragraph": "§4 Abs.2.a",    "description": "Besitz von BTM 0-20g",
     "min_bussgeld": "30'000",  "max_bussgeld": "100'000",
     "min_haft": 0,   "max_haft": 0,   "points": 0},

    {"law": "BtMG", "paragraph": "§4 Abs.2.a (2)","description": "Besitz von BTM 20-100g",
     "min_bussgeld": "50'000",  "max_bussgeld": "150'000",
     "min_haft": 10,  "max_haft": 10,  "points": 0},

    {"law": "BtMG", "paragraph": "§4 Abs.2.a (3)","description": "Besitz von BTM 100-200g",
     "min_bussgeld": "75'000",  "max_bussgeld": "200'000",
     "min_haft": 15,  "max_haft": 15,  "points": 0},

    {"law": "BtMG", "paragraph": "§4 Abs.2.a (4)","description": "Besitz von BTM 200-1000g",
     "min_bussgeld": "125'000", "max_bussgeld": "250'000",
     "min_haft": 25,  "max_haft": 25,  "points": 0},

    {"law": "BtMG", "paragraph": "§4 Abs.2.a (5)","description": "Besitz von BTM >1000g",
     "min_bussgeld": "300'000", "max_bussgeld": "450'000",
     "min_haft": 40,  "max_haft": 40,  "points": 0},

    {"law": "BtMG", "paragraph": "§5 Abs.1.a",    "description": "Verkauf von BTM 0-20g",
     "min_bussgeld": "50'000",  "max_bussgeld": "150'000",
     "min_haft": 15,  "max_haft": 15,  "points": 0},

    {"law": "BtMG", "paragraph": "§5 Abs.1.b",    "description": "Verkauf von BTM >20g",
     "min_bussgeld": "175'000", "max_bussgeld": "300'000",
     "min_haft": 30,  "max_haft": 30,  "points": 0},

    {"law": "BtMG", "paragraph": "§5 Abs.1.c",    "description": "Ankauf von BTM 0-20g",
     "min_bussgeld": "50'000",  "max_bussgeld": "150'000",
     "min_haft": 15,  "max_haft": 15,  "points": 0},

    {"law": "BtMG", "paragraph": "§5 Abs.1.d",    "description": "Ankauf von BTM >20g",
     "min_bussgeld": "175'000", "max_bussgeld": "300'000",
     "min_haft": 30,  "max_haft": 30,  "points": 0},

    {"law": "BtMG", "paragraph": "§6",            "description": "Drogenkonsum",
     "min_bussgeld": "25'000",  "max_bussgeld": "50'000",
     "min_haft": 0,   "max_haft": 0,   "points": 0},

    #==================== WaffG ====================
    {"law": "WaffG", "paragraph": "§32",           "description": "Führen einer legalen Waffe ohne Lizenz",
     "min_bussgeld": "25'000", "max_bussgeld": "50'000",
     "min_haft": 15, "max_haft": 15, "points": 0},

    {"law": "WaffG", "paragraph": "§33",           "description": "Besitz einer illegalen Waffe oder Munition",
     "min_bussgeld": "60'000", "max_bussgeld": "120'000",
     "min_haft": 10, "max_haft": 25, "points": 0},

    {"law": "WaffG", "paragraph": "§33 Abs.1.a",   "description": "Besitz einer illegalen Waffe Klasse A",
     "min_bussgeld": "40'000", "max_bussgeld": "100'000",
     "min_haft": 10, "max_haft": 20, "points": 0},

    {"law": "WaffG", "paragraph": "§33 Abs.1.b",   "description": "Besitz einer illegalen Waffe Klasse B",
     "min_bussgeld": "80'000", "max_bussgeld": "150'000",
     "min_haft": 10, "max_haft": 30, "points": 0},

    {"law": "WaffG", "paragraph": "§33 Abs.1.c",   "description": "Besitz einer illegalen Waffe Klasse C",
     "min_bussgeld": "120'000","max_bussgeld": "200'000",
     "min_haft": 10, "max_haft": 50, "points": 0},

    {"law": "WaffG", "paragraph": "§34",           "description": "Waffenhandel",
     "min_bussgeld": "150'000","max_bussgeld": "250'000",
     "min_haft": 50, "max_haft": 90, "points": 0},

    {"law": "WaffG", "paragraph": "§35",           "description": "Unberechtigter Waffengebrauch",
     "min_bussgeld": "80'000", "max_bussgeld": "100'000",
     "min_haft": 15, "max_haft": 30, "points": 0},

    #==================== StVO ====================
    {"law": "StVO", "paragraph": "§1 Abs.5",  "description": "Nicht Mitführen von Verbandsmaterial im Fahrzeug",
     "min_bussgeld": "25'000", "max_bussgeld": "50'000",
     "min_haft": 0,  "max_haft": 0,  "points": 0},

    {"law": "StVO", "paragraph": "§1 Abs.6",  "description": "Verstoß gegen die Anschnallpflicht",
     "min_bussgeld": "25'000", "max_bussgeld": "50'000",
     "min_haft": 0,  "max_haft": 0,  "points": 1},

    {"law": "StVO", "paragraph": "§2 Abs.1",  "description": "Fahren ohne Fahrerlaubnis",
     "min_bussgeld": "55'000", "max_bussgeld": "125'000",
     "min_haft": 0,  "max_haft": 0,  "points": 3},

    {"law": "StVO", "paragraph": "§3 Abs.1",  "description": "Verstoß gegen das Rechtsfahrgebot",
     "min_bussgeld": "10'000", "max_bussgeld": "25'000",
     "min_haft": 0,  "max_haft": 0,  "points": 1},

    {"law": "StVO", "paragraph": "§3 Abs.3",  "description": "Fahren abseits von befestigten Straßen/Feldwege/Waldwege",
     "min_bussgeld": "7'500",  "max_bussgeld": "12'500",
     "min_haft": 0,  "max_haft": 0,  "points": 0},

    {"law": "StVO", "paragraph": "§4",        "description": "Gefährlicher Eingriff in den Straßenverkehr",
     "min_bussgeld": "40'000", "max_bussgeld": "95'000",
     "min_haft": 5,  "max_haft": 20, "points": 2},

    {"law": "StVO", "paragraph": "§5 (1)",    "description": "Geschwindigkeitsüberschreitung 20 bis 50",
     "min_bussgeld": "20'000", "max_bussgeld": "50'000",
     "min_haft": 0,  "max_haft": 0,  "points": 0},

    {"law": "StVO", "paragraph": "§5 (2)",    "description": "Geschwindigkeitsüberschreitung 50 bis 100",
     "min_bussgeld": "44'000", "max_bussgeld": "75'000",
     "min_haft": 0,  "max_haft": 0,  "points": 1},

    {"law": "StVO", "paragraph": "§5 (3)",    "description": "Geschwindigkeitsüberschreitung 100 bis 150",
     "min_bussgeld": "40'000", "max_bussgeld": "150'000",
     "min_haft": 0,  "max_haft": 0,  "points": 2},

    {"law": "StVO", "paragraph": "§5 (4)",    "description": "Geschwindigkeitsüberschreitung 150 bis 250",
     "min_bussgeld": "100'000","max_bussgeld": "200'000",
     "min_haft": 0,  "max_haft": 0,  "points": 4},

    {"law": "StVO", "paragraph": "§5 (5)",    "description": "Geschwindigkeitsüberschreitung 250 bis <<>>",
     "min_bussgeld": "125'000","max_bussgeld": "250'000",
     "min_haft": 0,  "max_haft": 0,  "points": 8},

    {"law": "StVO", "paragraph": "§6 Abs.1",  "description": "Nicht Zugelassenes Fahrzeug auf der Autobahn",
     "min_bussgeld": "50'000", "max_bussgeld": "100'000",
     "min_haft": 0,  "max_haft": 0,  "points": 1},

    {"law": "StVO", "paragraph": "§7 Abs.1",  "description": "Nicht beachten von Verkehrsschildern",
     "min_bussgeld": "25'000", "max_bussgeld": "50'000",
     "min_haft": 0,  "max_haft": 0,  "points": 1},

    {"law": "StVO", "paragraph": "§9 Abs.1",  "description": "Überholen von Rechts",
     "min_bussgeld": "10'000", "max_bussgeld": "25'000",
     "min_haft": 0,  "max_haft": 0,  "points": 1},

    {"law": "StVO", "paragraph": "§10 Abs.1", "description": "Missachtung von Vorfahrtsregelungen",
     "min_bussgeld": "20'000", "max_bussgeld": "50'000",
     "min_haft": 0,  "max_haft": 0,  "points": 1},

    {"law": "StVO", "paragraph": "§11",       "description": "Falschparken",
     "min_bussgeld": "15'000", "max_bussgeld": "30'000",
     "min_haft": 0,  "max_haft": 0,  "points": 0},

    {"law": "StVO", "paragraph": "§12",       "description": "Verbotenes Nutzen von Warnzeichen",
     "min_bussgeld": "12'500", "max_bussgeld": "35'000",
     "min_haft": 0,  "max_haft": 0,  "points": 0},

    {"law": "StVO", "paragraph": "§13 Abs.1", "description": "Blockieren von Ein- / Ausfahrten",
     "min_bussgeld": "10'000", "max_bussgeld": "40'000",
     "min_haft": 0,  "max_haft": 0,  "points": 0},

    {"law": "StVO", "paragraph": "§14 Abs.1", "description": "Fahren unter BTM / Alkohol",
     "min_bussgeld": "40'000", "max_bussgeld": "95'000",
     "min_haft": 20, "max_haft": 20, "points": 0},

    {"law": "StVO", "paragraph": "§16 Abs.1", "description": "Fahrerflucht",
     "min_bussgeld": "75'000", "max_bussgeld": "125'000",
     "min_haft": 15, "max_haft": 15, "points": 0},

    {"law": "StVO", "paragraph": "§17 Abs.1 / Abs.2",
     "description": "Missbrauch von Sonder- / Wegerechten",
     "min_bussgeld": "100'000","max_bussgeld": "250'000",
     "min_haft": 0,  "max_haft": 0,  "points": 0},

    {"law": "StVO", "paragraph": "§18 Abs.3", "description": "Missachtung von Sonder- / Wegerechten.",
     "min_bussgeld": "80'000", "max_bussgeld": "150'000",
     "min_haft": 0,  "max_haft": 0,  "points": 1},

    {"law": "StVO", "paragraph": "§15 Abs.1", "description": "Verbotenes Kraftfahrzeugrennen",
     "min_bussgeld": "125'000","max_bussgeld": "250'000",
     "min_haft": 30, "max_haft": 30, "points": 3},

    {"law": "StVO", "paragraph": "(§11 & 13)","description": "Landen außerhalb von vorgeschriebenen Landeflächen",
     "min_bussgeld": "150'000","max_bussgeld": "300'000",
     "min_haft": 0,  "max_haft": 0,  "points": 0},

    #==================== Extra-Duplikate (aus dem Original) ====================
    {"law": "StGB", "paragraph": "§32", "description": "Führen einer legalen Waffe ohne Lizenz",
     "min_bussgeld": "10'000", "max_bussgeld": "30'000",
     "min_haft": 0,  "max_haft": 0,  "points": 0},

    {"law": "StGB", "paragraph": "§33", "description": "Besitz einer illegalen Waffe oder Munition (Duplikat)",
     "min_bussgeld": "30'000", "max_bussgeld": "75'000",
     "min_haft": 10, "max_haft": 20, "points": 0},

    {"law": "StGB", "paragraph": "§33 Abs.1.a-2", "description": "Besitz einer illegalen Waffe Klasse A (Duplikat)",
     "min_bussgeld": "20'000", "max_bussgeld": "50'000",
     "min_haft": 10, "max_haft": 20, "points": 0},

    {"law": "StGB", "paragraph": "§33 Abs.1.b-2", "description": "Besitz einer illegalen Waffe Klasse B (Duplikat)",
     "min_bussgeld": "40'000", "max_bussgeld": "100'000",
     "min_haft": 10, "max_haft": 30, "points": 0},

    {"law": "StGB", "paragraph": "§33 Abs.1.c-2", "description": "Besitz einer illeglalen Waffe Klasse C (Duplikat)",
     "min_bussgeld": "60'000", "max_bussgeld": "150'000",
     "min_haft": 10, "max_haft": 50, "points": 0},

    {"law": "StGB", "paragraph": "§34-2",        "description": "Waffenhandel (Duplikat)",
     "min_bussgeld": "75'000", "max_bussgeld": "190'000",
     "min_haft": 50, "max_haft": 90, "points": 0},

    {"law": "StGB", "paragraph": "§35-2",        "description": "Unberechtigter Waffengebrauch (Duplikat)",
     "min_bussgeld": "40'000", "max_bussgeld": "100'000",
     "min_haft": 15, "max_haft": 30, "points": 0},

    {"law": "StGB", "paragraph": "§36",          "description": "Landfriedensbruch",
     "min_bussgeld": "125'000","max_bussgeld": "250'000",
     "min_haft": 5,  "max_haft": 50, "points": 0},

    {"law": "StGB", "paragraph": "§37",          "description": "Entzug Polizeilicher Maßnahmen",
     "min_bussgeld": "50'000", "max_bussgeld": "100'000",
     "min_haft": 10, "max_haft": 20, "points": 0},

    {"law": "StGB", "paragraph": "§38",          "description": "Korruption",
     "min_bussgeld": "500'000","max_bussgeld": "625'000",
     "min_haft": 90, "max_haft": 90, "points": 0},

    {"law": "StGB", "paragraph": "§39",          "description": "Leichtes Dienstvergehen",
     "min_bussgeld": "125'000","max_bussgeld": "325'000",
     "min_haft": 0,  "max_haft": 0,  "points": 0},

    {"law": "StGB", "paragraph": "§40",          "description": "Schweres Dienstvergehen",
     "min_bussgeld": "500'000","max_bussgeld": "625'000",
     "min_haft": 20, "max_haft": 90, "points": 0},

    {"law": "StGB", "paragraph": "§41",          "description": "Bruch der Schweigepflicht",
     "min_bussgeld": "40'000", "max_bussgeld": "100'000",
     "min_haft": 10, "max_haft": 15, "points": 0},

    {"law": "StGB", "paragraph": "§42",          "description": "Störung der Amtshandlung",
     "min_bussgeld": "25'000", "max_bussgeld": "60'000",
     "min_haft": 10, "max_haft": 25, "points": 0},

    {"law": "StGB", "paragraph": "§43",          "description": "Arbeitsverweigerung eines öffentlichen Amtes",
     "min_bussgeld": "35'000", "max_bussgeld": "95'000",
     "min_haft": 0,  "max_haft": 0,  "points": 0},

    {"law": "StGB", "paragraph": "§44",          "description": "Erschleichen von Leistungen",
     "min_bussgeld": "15'000", "max_bussgeld": "45'000",
     "min_haft": 0,  "max_haft": 0,  "points": 0},

    {"law": "StGB", "paragraph": "§45",          "description": "Missbrauch von geschützten Berufsbezeichnungen",
     "min_bussgeld": "25'000", "max_bussgeld": "60'000",
     "min_haft": 10, "max_haft": 20, "points": 0},

    {"law": "StGB", "paragraph": "§46",          "description": "Ausstellen fälschlicher Gesundheitszeugnisse",
     "min_bussgeld": "50'000", "max_bussgeld": "125'000",
     "min_haft": 50, "max_haft": 50, "points": 0},

    {"law": "StGB", "paragraph": "§47",          "description": "Störung einer Behandlung",
     "min_bussgeld": "25'000", "max_bussgeld": "60'000",
     "min_haft": 10, "max_haft": 15, "points": 0},

    {"law": "StGB", "paragraph": "§48",          "description": "Belästigung",
     "min_bussgeld": "75'000", "max_bussgeld": "190'000",
     "min_haft": 20, "max_haft": 40, "points": 0},

    {"law": "StGB", "paragraph": "§50",          "description": "Flucht aus staatlichem Gewahrsam",
     "min_bussgeld": "50'000", "max_bussgeld": "125'000",
     "min_haft": 30, "max_haft": 60, "points": 0},

    {"law": "StGB", "paragraph": "§51",          "description": "Besitz von nicht offiziellen Geldmitteln",
     "min_bussgeld": "30'000", "max_bussgeld": "75'000",
     "min_haft": 10, "max_haft": 25, "points": 0},

    {"law": "StGB", "paragraph": "§52",          "description": "Inverkehrbringen von nicht offiziellen Geldmitteln",
     "min_bussgeld": "60'000", "max_bussgeld": "150'000",
     "min_haft": 25, "max_haft": 50, "points": 0},

    {"law": "StGB", "paragraph": "§53",          "description": "Missachtung von gerichtlichen Anordnungen",
     "min_bussgeld": "40'000", "max_bussgeld": "100'000",
     "min_haft": 10, "max_haft": 25, "points": 0},

    {"law": "StGB", "paragraph": "§54",          "description": "Angriff auf staatliche Einrichtungen",
     "min_bussgeld": "75'000", "max_bussgeld": "190'000",
     "min_haft": 90, "max_haft": 90, "points": 0},
]

# Aktuelle Auswahl in einer Liste
ausgewaehlt = []

# ---------------------------------------------------
# Hilfsfunktion: Bußgeld-String in Integer konvertieren
def parse_bussgeld(betrag_str):
    """
    Entfernt die Hochkommata (') aus dem Bußgeld-String und wandelt in int um.
    """
    return int(betrag_str.replace("'", ""))

# ---------------------------------------------------
# Suchfunktion
def suche_eintraege(keyword):
    """
    Sucht in STRAF_KATALOG nach dem Suchbegriff (case-insensitive).
    Treffer werden als Liste (index_in_strafkatalog, dict_eintrag) zurückgegeben.
    """
    keyword = keyword.lower()
    ergebnisse = []
    for i, e in enumerate(STRAF_KATALOG):
        if (keyword in e["law"].lower()
            or keyword in e["paragraph"].lower()
            or keyword in e["description"].lower()):
            ergebnisse.append((i, e))
    return ergebnisse

def zeige_suchergebnisse(suchergebnisse):
    """
    Zeigt Suchergebnisse formatiert in der Konsole an.
    """
    if not suchergebnisse:
        print("\nKeine Treffer gefunden.")
        return
    print("\n--- Suchergebnisse ---")
    for idx, eintrag in suchergebnisse:
        print(f"[Index {idx}] {eintrag['law']} {eintrag['paragraph']}: {eintrag['description']}")
        print(f"    Min. Bußgeld: {eintrag['min_bussgeld']} | Max. Bußgeld: {eintrag['max_bussgeld']}")
        print(f"    Min. Haft: {eintrag['min_haft']}        | Max. Haft: {eintrag['max_haft']}")
        print(f"    Punkte: {eintrag['points']}")
        print("--------------------")

# ---------------------------------------------------
# Eintrag zur Auswahl hinzufügen
def add_to_auswahl(index_in_katalog):
    """
    Nimmt den Eintrag aus STRAF_KATALOG (per Index) in die Auswahl 'ausgewaehlt' auf.
    """
    try:
        eintrag = STRAF_KATALOG[index_in_katalog]
        ausgewaehlt.append(eintrag)
        print(f"\nEintrag '{eintrag['description']}' wurde hinzugefügt.")
    except IndexError:
        print("\nIndex außerhalb des Katalogs. Eintrag nicht gefunden.")

# ---------------------------------------------------
# Eintrag aus der Auswahl entfernen
def remove_from_auswahl(index_in_auswahl):
    """
    Entfernt einen Eintrag aus der Liste 'ausgewaehlt' (per Index in der Auswahl).
    """
    try:
        geloescht = ausgewaehlt.pop(index_in_auswahl)
        print(f"\nEintrag '{geloescht['description']}' wurde entfernt.")
    except IndexError:
        print("\nIndex außerhalb deiner aktuellen Auswahl. Vorgang abgebrochen.")

# ---------------------------------------------------
# Auswahl + Summen anzeigen
def zeige_auswahl_und_summe():
    """
    Zeigt alle ausgewählten Einträge an + berechnet und zeigt die Summen (Bußgeld, Haft, Punkte).
    """
    if not ausgewaehlt:
        print("\nDeine Auswahl ist leer.")
        return

    print("\n--- Ausgewählte Einträge ---")
    for i, e in enumerate(ausgewaehlt):
        print(f"[Auswahl-Index {i}] {e['law']} {e['paragraph']}: {e['description']}")
        print(f"    Min. Bußgeld: {e['min_bussgeld']} | Max. Bußgeld: {e['max_bussgeld']}")
        print(f"    Min. Haft: {e['min_haft']}        | Max. Haft: {e['max_haft']}")
        print(f"    Punkte: {e['points']}")
        print("--------------------")

    # Summen berechnen
    total_min_bussgeld = 0
    total_max_bussgeld = 0
    total_min_haft = 0
    total_max_haft = 0
    total_points = 0

    for eintrag in ausgewaehlt:
        total_min_bussgeld += parse_bussgeld(eintrag["min_bussgeld"])
        total_max_bussgeld += parse_bussgeld(eintrag["max_bussgeld"])
        total_min_haft += eintrag["min_haft"]
        total_max_haft += eintrag["max_haft"]
        total_points += eintrag["points"]

    print("\n--- Zusammenfassung ---")
    print(f"Gesamt Min. Bußgeld: {total_min_bussgeld}")
    print(f"Gesamt Max. Bußgeld: {total_max_bussgeld}")
    print(f"Gesamt Min. Haft:    {total_min_haft}")
    print(f"Gesamt Max. Haft:    {total_max_haft}")
    print(f"Gesamt Punkte:       {total_points}")

# ---------------------------------------------------
# Hauptmenü in einer Schleife
def main():
    print("Willkommen im Strafkatalog (Python-Version).")
    print("Gib eine Zahl aus dem Menü ein, um fortzufahren.\n")

    while True:
        print("\n--- Hauptmenü ---")
        print("[1] Suche nach Einträgen")
        print("[2] Eintrag zur Auswahl hinzufügen (Index in STRAF_KATALOG)")
        print("[3] Eintrag aus Auswahl entfernen (Index in der aktuellen Auswahl)")
        print("[4] Aktuelle Auswahl + Summen anzeigen")
        print("[5] Beenden")

        wahl = input("Deine Wahl: ").strip()

        if wahl == "1":
            suchbegriff = input("Suchbegriff eingeben: ")
            ergebnisse = suche_eintraege(suchbegriff)
            zeige_suchergebnisse(ergebnisse)

        elif wahl == "2":
            try:
                idx_katalog = int(input("Index aus STRAF_KATALOG eingeben (z.B. 0, 1, 2...): "))
                add_to_auswahl(idx_katalog)
            except ValueError:
                print("\nBitte eine ganze Zahl eingeben.")

        elif wahl == "3":
            try:
                idx_auswahl = int(input("Index aus deiner Auswahl eingeben (z.B. 0, 1, 2...): "))
                remove_from_auswahl(idx_auswahl)
            except ValueError:
                print("\nBitte eine ganze Zahl eingeben.")

        elif wahl == "4":
            zeige_auswahl_und_summe()

        elif wahl == "5":
            print("\nProgramm wird beendet. Auf Wiedersehen!")
            break

        else:
            print("\nUngültige Eingabe. Bitte 1-5 auswählen.")

# ---------------------------------------------------
if __name__ == "__main__":
    main()
