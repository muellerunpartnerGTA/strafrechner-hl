<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Strafkatalog mit Rechner</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 20px;
        }
        input {
            padding: 10px;
            width: 300px;
            margin-bottom: 20px;
        }
        table {
            width: 90%;
            margin: auto;
            border-collapse: collapse;
            margin-top: 1rem;
        }
        th, td {
            border: 1px solid black;
            padding: 10px;
        }
        th {
            background-color: #f2f2f2;
        }
        .btn {
            padding: 5px 10px;
            margin: 2px;
            cursor: pointer;
            border: 1px solid #333;
            background-color: #e8e8e8;
        }
        .btn:hover {
            background-color: #ccc;
        }
        .summary {
            margin-top: 1rem;
        }
        .summary table {
            margin-top: 0;
        }
    </style>
</head>
<body>
    <h1>Strafkatalog mit Rechner</h1>

    <!-- Suchfeld für Paragraphen, Gesetze, etc. -->
    <input type="text" id="search" placeholder="Nach Paragraph suchen (z.B. §1)">

    <!-- Tabelle mit den Suchergebnissen -->
    <table>
        <thead>
            <tr>
                <th>Gesetz</th>
                <th>Paragraph</th>
                <th>Beschreibung</th>
                <th>Min. Bußgeld</th>
                <th>Max. Bußgeld</th>
                <th>Min. Haft</th>
                <th>Max. Haft</th>
                <th>StVO-Punkte</th>
                <th>Hinzufügen</th>
            </tr>
        </thead>
        <tbody id="table-body"></tbody>
    </table>

    <!-- Tabelle mit der Auswahl und Zusammenfassung -->
    <div class="summary">
        <h2>Ausgewählte Straftaten</h2>
        <table>
            <thead>
                <tr>
                    <th>Gesetz</th>
                    <th>Paragraph</th>
                    <th>Beschreibung</th>
                    <th>Min. Bußgeld</th>
                    <th>Max. Bußgeld</th>
                    <th>Min. Haft</th>
                    <th>Max. Haft</th>
                    <th>StVO-Punkte</th>
                    <th>Entfernen</th>
                </tr>
            </thead>
            <tbody id="selected-body"></tbody>
        </table>

        <!-- Zusammenfassung der Summen  -->
        <h2>Gesamtstrafmaß</h2>
        <table>
            <thead>
                <tr>
                    <th>Gesamt Min. Bußgeld</th>
                    <th>Gesamt Max. Bußgeld</th>
                    <th>Gesamt Min. Haft</th>
                    <th>Gesamt Max. Haft</th>
                    <th>Gesamt StVO-Punkte</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td id="sum-min-bussgeld">0</td>
                    <td id="sum-max-bussgeld">0</td>
                    <td id="sum-min-haft">0</td>
                    <td id="sum-max-haft">0</td>
                    <td id="sum-points">0</td>
                </tr>
            </tbody>
        </table>
    </div>

    <script>
        // Daten aus dem bisherigen Skript
        const data = [
            { law: "StGB", paragraph: "§1", description: "Diebstahl", min_bussgeld: "25'000", max_bussgeld: "60'000", min_haft: 10, max_haft: 10, points: 0 },
            { law: "StGB", paragraph: "§2", description: "Raubüberfall", min_bussgeld: "25'000", max_bussgeld: "60'000", min_haft: 15, max_haft: 30, points: 0 },
            { law: "StGB", paragraph: "§3", description: "Bewaffneter Raubüberfall", min_bussgeld: "50'000", max_bussgeld: "125'000", min_haft: 20, max_haft: 40, points: 0 },
            { law: "StGB", paragraph: "§4", description: "Erpressung", min_bussgeld: "45'000", max_bussgeld: "110'000", min_haft: 10, max_haft: 20, points: 0 },
            { law: "StGB", paragraph: "§5", description: "Bestechung von Staatsbeamten", min_bussgeld: "25'000", max_bussgeld: "60'000", min_haft: 10, max_haft: 25, points: 0 },
            { law: "StGB", paragraph: "§6", description: "Betrug", min_bussgeld: "50'000", max_bussgeld: "150'000", min_haft: 10, max_haft: 30, points: 0 },
            { law: "StGB", paragraph: "§7", description: "Fahrlässige Körperverletzung", min_bussgeld: "50'000", max_bussgeld: "125'000", min_haft: 0, max_haft: 10, points: 0 },
            { law: "StGB", paragraph: "§8", description: "Vorsätzliche Körperverletzung", min_bussgeld: "50'000", max_bussgeld: "125'000", min_haft: 20, max_haft: 30, points: 0 },
            { law: "StGB", paragraph: "§9", description: "Sachbeschädigung an Städtischen Objekten", min_bussgeld: "25'000", max_bussgeld: "60'000", min_haft: 0, max_haft: 0, points: 0 },
            { law: "StGB", paragraph: "§10", description: "Totschlag", min_bussgeld: "200'000", max_bussgeld: "450'000", min_haft: 10, max_haft: 50, points: 0 },
            { law: "StGB", paragraph: "§11", description: "Mord", min_bussgeld: "375'000", max_bussgeld: "950'000", min_haft: 90, max_haft: 90, points: 0 },
            { law: "StGB", paragraph: "§12", description: "Unterlassene Hilfeleistung", min_bussgeld: "50'000", max_bussgeld: "125'000", min_haft: 15, max_haft: 35, points: 0 },
            { law: "StGB", paragraph: "§13", description: "Beleidigung", min_bussgeld: "15'000", max_bussgeld: "40'000", min_haft: 0, max_haft: 0, points: 0 },
            { law: "StGB", paragraph: "§14", description: "Üble Nachrede", min_bussgeld: "25'000", max_bussgeld: "60'000", min_haft: 0, max_haft: 0, points: 0 },
            { law: "StGB", paragraph: "§15", description: "Drohung", min_bussgeld: "35'000", max_bussgeld: "90'000", min_haft: 10, max_haft: 25, points: 0 },
            { law: "StGB", paragraph: "§16", description: "Hausfriedensbruch", min_bussgeld: "20'000", max_bussgeld: "55'000", min_haft: 0, max_haft: 0, points: 0 },
            { law: "StGB", paragraph: "§17", description: "Freiheitsberaubung", min_bussgeld: "75'000", max_bussgeld: "190'000", min_haft: 15, max_haft: 50, points: 0 },
            { law: "StGB", paragraph: "§18", description: "Widerstand gegen die Staatsbehörden", min_bussgeld: "75'000", max_bussgeld: "125'000", min_haft: 15, max_haft: 30, points: 0 },
            { law: "StGB", paragraph: "§19", description: "Amtsanmassung", min_bussgeld: "75'000", max_bussgeld: "190'000", min_haft: 25, max_haft: 50, points: 0 },
            { law: "StGB", paragraph: "§20", description: "Missbräuchlicher Notruf", min_bussgeld: "20'000", max_bussgeld: "50'000", min_haft: 0, max_haft: 0, points: 0 },
            { law: "StGB", paragraph: "§21", description: "Missachtung des Verschleierungsverbots/Vermummungsverbot", min_bussgeld: "10'000", max_bussgeld: "30'000", min_haft: 0, max_haft: 0, points: 0 },
            { law: "StGB", paragraph: "§22", description: "Verweigerung der Identitätsfeststellung", min_bussgeld: "15'000", max_bussgeld: "40'000", min_haft: 0, max_haft: 0, points: 0 },
            { law: "StGB", paragraph: "§23", description: "Geiselnahme", min_bussgeld: "100'000", max_bussgeld: "250'000", min_haft: 25, max_haft: 70, points: 0 },
            { law: "StGB", paragraph: "§24", description: "Besitz illegaler Gegenstände", min_bussgeld: "25'000", max_bussgeld: "60'000", min_haft: 10, max_haft: 10, points: 0 },
            { law: "StGB", paragraph: "§25", description: "Urkundenfälschung", min_bussgeld: "50'000", max_bussgeld: "125'000", min_haft: 10, max_haft: 20, points: 0 },
            { law: "StGB", paragraph: "§26", description: "Sperrzonen", min_bussgeld: "250'000", max_bussgeld: "625'000", min_haft: 25, max_haft: 60, points: 0 },
            { law: "StGB", paragraph: "§27", description: "Erregung öffentlichen Ärgernisses", min_bussgeld: "25'000", max_bussgeld: "60'000", min_haft: 0, max_haft: 0, points: 0 },
            { law: "StGB", paragraph: "§28", description: "Meineid", min_bussgeld: "125'000", max_bussgeld: "325'000", min_haft: 20, max_haft: 50, points: 0 },
            { law: "StGB", paragraph: "§29", description: "Hochverat", min_bussgeld: "150'000", max_bussgeld: "450'000", min_haft: 90, max_haft: 90, points: 0 },
            { law: "StGB", paragraph: "§30", description: "Terroristischer Akt", min_bussgeld: "450'000", max_bussgeld: "625'000", min_haft: 90, max_haft: 90, points: 0 },
            { law: "StGB", paragraph: "§31", description: "Missachtung Polizeilicher Anweisungen", min_bussgeld: "25'000", max_bussgeld: "60'000", min_haft: 10, max_haft: 25, points: 0 },

            // BtMG
            { law: "BtMG", paragraph: "§3 Abs.1.c", description: "Besitz von Material zum Anbau von BTM", min_bussgeld: "30'000", max_bussgeld: "125'000", min_haft: 10, max_haft: 10, points: 0 },
            { law: "BtMG", paragraph: "§3 Abs.1.b", description: "Besitz von Material zur Herstellung von BTM", min_bussgeld: "40'000", max_bussgeld: "150'000", min_haft: 15, max_haft: 15, points: 0 },
            { law: "BtMG", paragraph: "§3 Abs.1.c (2)", description: "Anbau von BTM", min_bussgeld: "50'000", max_bussgeld: "200'000", min_haft: 20, max_haft: 20, points: 0 },
            { law: "BtMG", paragraph: "§3 Abs.1.d", description: "Herstellung von BTM", min_bussgeld: "70'000", max_bussgeld: "250'000", min_haft: 30, max_haft: 30, points: 0 },
            { law: "BtMG", paragraph: "§4 Abs.2.a", description: "Besitz von BTM 0-20g", min_bussgeld: "30'000", max_bussgeld: "100'000", min_haft: 0, max_haft: 0, points: 0 },
            { law: "BtMG", paragraph: "§4 Abs.2.a (2)", description: "Besitz von BTM 20-100g", min_bussgeld: "50'000", max_bussgeld: "150'000", min_haft: 10, max_haft: 10, points: 0 },
            { law: "BtMG", paragraph: "§4 Abs.2.a (3)", description: "Besitz von BTM 100-200g", min_bussgeld: "75'000", max_bussgeld: "200'000", min_haft: 15, max_haft: 15, points: 0 },
            { law: "BtMG", paragraph: "§4 Abs.2.a (4)", description: "Besitz von BTM 200-1000g", min_bussgeld: "125'000", max_bussgeld: "250'000", min_haft: 25, max_haft: 25, points: 0 },
            { law: "BtMG", paragraph: "§4 Abs.2.a (5)", description: "Besitz von BTM >1000g", min_bussgeld: "300'000", max_bussgeld: "450'000", min_haft: 40, max_haft: 40, points: 0 },
            { law: "BtMG", paragraph: "§5 Abs.1.a", description: "Verkauf von BTM 0-20g", min_bussgeld: "50'000", max_bussgeld: "150'000", min_haft: 15, max_haft: 15, points: 0 },
            { law: "BtMG", paragraph: "§5 Abs.1.b", description: "Verkauf von BTM >20g", min_bussgeld: "175'000", max_bussgeld: "300'000", min_haft: 30, max_haft: 30, points: 0 },
            { law: "BtMG", paragraph: "§5 Abs.1.c", description: "Ankauf von BTM 0-20g", min_bussgeld: "50'000", max_bussgeld: "150'000", min_haft: 15, max_haft: 15, points: 0 },
            { law: "BtMG", paragraph: "§5 Abs.1.d", description: "Ankauf von BTM >20g", min_bussgeld: "175'000", max_bussgeld: "300'000", min_haft: 30, max_haft: 30, points: 0 },
            { law: "BtMG", paragraph: "§6", description: "Drogenkonsum", min_bussgeld: "25'000", max_bussgeld: "50'000", min_haft: 0, max_haft: 0, points: 0 },

            // WaffG
            { law: "WaffG", paragraph: "§32", description: "Führen einer legalen Waffe ohne Lizenz", min_bussgeld: "25'000", max_bussgeld: "50'000", min_haft: 15, max_haft: 15, points: 0 },
            { law: "WaffG", paragraph: "§33", description: "Besitz einer illegalen Waffe oder Munition", min_bussgeld: "60'000", max_bussgeld: "120'000", min_haft: 10, max_haft: 25, points: 0 },
            { law: "WaffG", paragraph: "§33 Abs.1.a", description: "Besitz einer illegalen Waffe Klasse A", min_bussgeld: "40'000", max_bussgeld: "100'000", min_haft: 10, max_haft: 20, points: 0 },
            { law: "WaffG", paragraph: "§33 Abs.1.b", description: "Besitz einer illegalen Waffe Klasse B", min_bussgeld: "80'000", max_bussgeld: "150'000", min_haft: 10, max_haft: 30, points: 0 },
            { law: "WaffG", paragraph: "§33 Abs.1.c", description: "Besitz einer illegalen Waffe Klasse C", min_bussgeld: "120'000", max_bussgeld: "200'000", min_haft: 10, max_haft: 50, points: 0 },
            { law: "WaffG", paragraph: "§34", description: "Waffenhandel", min_bussgeld: "150'000", max_bussgeld: "250'000", min_haft: 50, max_haft: 90, points: 0 },
            { law: "WaffG", paragraph: "§35", description: "Unberechtigter Waffengebrauch", min_bussgeld: "80'000", max_bussgeld: "100'000", min_haft: 15, max_haft: 30, points: 0 },

            // StVO
            { law: "StVO", paragraph: "§1 Abs.5", description: "Nicht Mitführen von Verbandsmaterial im Fahrzeug", min_bussgeld: "25'000", max_bussgeld: "50'000", min_haft: 0, max_haft: 0, points: 0 },
            { law: "StVO", paragraph: "§1 Abs.6", description: "Verstoß gegen die Anschnallpflicht", min_bussgeld: "25'000", max_bussgeld: "50'000", min_haft: 0, max_haft: 0, points: 1 },
            { law: "StVO", paragraph: "§2 Abs.1", description: "Fahren ohne Fahrerlaubnis", min_bussgeld: "55'000", max_bussgeld: "125'000", min_haft: 0, max_haft: 0, points: 3 },
            { law: "StVO", paragraph: "§3 Abs.1", description: "Verstoß gegen das Rechtsfahrgebot", min_bussgeld: "10'000", max_bussgeld: "25'000", min_haft: 0, max_haft: 0, points: 1 },
            { law: "StVO", paragraph: "§3 Abs.3", description: "Fahren abseits von befestigten Straßen/Feldwege/Waldwege", min_bussgeld: "7'500", max_bussgeld: "12'500", min_haft: 0, max_haft: 0, points: 0 },
            { law: "StVO", paragraph: "§4", description: "Gefährlicher Eingriff in den Straßenverkehr", min_bussgeld: "40'000", max_bussgeld: "95'000", min_haft: 5, max_haft: 20, points: 2 },
            { law: "StVO", paragraph: "§5 (1)", description: "Geschwindigkeitsüberschreitung 20 bis 50", min_bussgeld: "20'000", max_bussgeld: "50'000", min_haft: 0, max_haft: 0, points: 0 },
            { law: "StVO", paragraph: "§5 (2)", description: "Geschwindigkeitsüberschreitung 50 bis 100", min_bussgeld: "44'000", max_bussgeld: "75'000", min_haft: 0, max_haft: 0, points: 1 },
            { law: "StVO", paragraph: "§5 (3)", description: "Geschwindigkeitsüberschreitung 100 bis 150", min_bussgeld: "40'000", max_bussgeld: "150'000", min_haft: 0, max_haft: 0, points: 2 },
            { law: "StVO", paragraph: "§5 (4)", description: "Geschwindigkeitsüberschreitung 150 bis 250", min_bussgeld: "100'000", max_bussgeld: "200'000", min_haft: 0, max_haft: 0, points: 4 },
            { law: "StVO", paragraph: "§5 (5)", description: "Geschwindigkeitsüberschreitung 250 bis <<>>", min_bussgeld: "125'000", max_bussgeld: "250'000", min_haft: 0, max_haft: 0, points: 8 },
            { law: "StVO", paragraph: "§6 Abs.1", description: "Nicht Zugelassenes Fahrzeug auf der Autobahn", min_bussgeld: "50'000", max_bussgeld: "100'000", min_haft: 0, max_haft: 0, points: 1 },
            { law: "StVO", paragraph: "§7 Abs.1", description: "Nicht beachten von Verkehrsschildern", min_bussgeld: "25'000", max_bussgeld: "50'000", min_haft: 0, max_haft: 0, points: 1 },
            { law: "StVO", paragraph: "§9 Abs.1", description: "Überholen von Rechts", min_bussgeld: "10'000", max_bussgeld: "25'000", min_haft: 0, max_haft: 0, points: 1 },
            { law: "StVO", paragraph: "§10 Abs.1", description: "Missachtung von Vorfahrtsregelungen", min_bussgeld: "20'000", max_bussgeld: "50'000", min_haft: 0, max_haft: 0, points: 1 },
            { law: "StVO", paragraph: "§11", description: "Falschparken", min_bussgeld: "15'000", max_bussgeld: "30'000", min_haft: 0, max_haft: 0, points: 0 },
            { law: "StVO", paragraph: "§12", description: "Verbotenes Nutzen von Warnzeichen", min_bussgeld: "12'500", max_bussgeld: "35'000", min_haft: 0, max_haft: 0, points: 0 },
            { law: "StVO", paragraph: "§13 Abs.1", description: "Blockieren von Ein- / Ausfahrten", min_bussgeld: "10'000", max_bussgeld: "40'000", min_haft: 0, max_haft: 0, points: 0 },
            { law: "StVO", paragraph: "§14 Abs.1", description: "Fahren unter BTM / Alkohol", min_bussgeld: "40'000", max_bussgeld: "95'000", min_haft: 20, max_haft: 20, points: 0 },
            { law: "StVO", paragraph: "§16 Abs.1", description: "Fahrerflucht", min_bussgeld: "75'000", max_bussgeld: "125'000", min_haft: 15, max_haft: 15, points: 0 },
            { law: "StVO", paragraph: "§17 Abs.1 / Abs.2", description: "Missbrauch von Sonder- / Wegerechten", min_bussgeld: "100'000", max_bussgeld: "250'000", min_haft: 0, max_haft: 0, points: 0 },
            { law: "StVO", paragraph: "§18 Abs.3", description: "Missachtung von Sonder- / Wegerechten.", min_bussgeld: "80'000", max_bussgeld: "150'000", min_haft: 0, max_haft: 0, points: 1 },
            { law: "StVO", paragraph: "§15 Abs.1", description: "Verbotenes Kraftfahrzeugrennen", min_bussgeld: "125'000", max_bussgeld: "250'000", min_haft: 30, max_haft: 30, points: 3 },
            { law: "StVO", paragraph: "(§11 & 13)", description: "Landen außerhalb von vorgeschriebenen Landeflächen", min_bussgeld: "150'000", max_bussgeld: "300'000", min_haft: 0, max_haft: 0, points: 0 },

            // Extra
            { law: "StGB", paragraph: "§32", description: "Führen einer legalen Waffe ohne Lizenz" , min_bussgeld: "10'000", max_bussgeld: "30'000", min_haft: 0, max_haft: 0, points: 0 },
            { law: "StGB", paragraph: "§33", description: "Besitz einer illegalen Waffe oder Munition (Duplikat)", min_bussgeld: "30'000", max_bussgeld: "75'000", min_haft: 10, max_haft: 20, points: 0 },
            { law: "StGB", paragraph: "§33 Abs.1.a-2", description: "Besitz einer illegalen Waffe Klasse A (Duplikat)", min_bussgeld: "20'000", max_bussgeld: "50'000", min_haft: 10, max_haft: 20, points: 0 },
            { law: "StGB", paragraph: "§33 Abs.1.b-2", description: "Besitz einer illegalen Waffe Klasse B (Duplikat)", min_bussgeld: "40'000", max_bussgeld: "100'000", min_haft: 10, max_haft: 30, points: 0 },
            { law: "StGB", paragraph: "§33 Abs.1.c-2", description: "Besitz einer illeglalen Waffe Klasse C (Duplikat)", min_bussgeld: "60'000", max_bussgeld: "150'000", min_haft: 10, max_haft: 50, points: 0 },
            { law: "StGB", paragraph: "§34-2", description: "Waffenhandel (Duplikat)", min_bussgeld: "75'000", max_bussgeld: "190'000", min_haft: 50, max_haft: 90, points: 0 },
            { law: "StGB", paragraph: "§35-2", description: "Unberechtigter Waffengebrauch (Duplikat)", min_bussgeld: "40'000", max_bussgeld: "100'000", min_haft: 15, max_haft: 30, points: 0 },
            { law: "StGB", paragraph: "§36", description: "Landfriedensbruch", min_bussgeld: "125'000", max_bussgeld: "250'000", min_haft: 5, max_haft: 50, points: 0 },
            { law: "StGB", paragraph: "§37", description: "Entzug Polizeilicher Maßnahmen", min_bussgeld: "50'000", max_bussgeld: "100'000", min_haft: 10, max_haft: 20, points: 0 },
            { law: "StGB", paragraph: "§38", description: "Korruption", min_bussgeld: "500'000", max_bussgeld: "625'000", min_haft: 90, max_haft: 90, points: 0 },
            { law: "StGB", paragraph: "§39", description: "Leichtes Dienstvergehen", min_bussgeld: "125'000", max_bussgeld: "325'000", min_haft: 0, max_haft: 0, points: 0 },
            { law: "StGB", paragraph: "§40", description: "Schweres Dienstvergehen", min_bussgeld: "500'000", max_bussgeld: "625'000", min_haft: 20, max_haft: 90, points: 0 },
            { law: "StGB", paragraph: "§41", description: "Bruch der Schweigepflicht", min_bussgeld: "40'000", max_bussgeld: "100'000", min_haft: 10, max_haft: 15, points: 0 },
            { law: "StGB", paragraph: "§42", description: "Störung der Amtshandlung", min_bussgeld: "25'000", max_bussgeld: "60'000", min_haft: 10, max_haft: 25, points: 0 },
            { law: "StGB", paragraph: "§43", description: "Arbeitsverweigerung eines öffentlichen Amtes", min_bussgeld: "35'000", max_bussgeld: "95'000", min_haft: 0, max_haft: 0, points: 0 },
            { law: "StGB", paragraph: "§44", description: "Erschleichen von Leistungen", min_bussgeld: "15'000", max_bussgeld: "45'000", min_haft: 0, max_haft: 0, points: 0 },
            { law: "StGB", paragraph: "§45", description: "Missbrauch von geschützten Berufsbezeichnungen", min_bussgeld: "25'000", max_bussgeld: "60'000", min_haft: 10, max_haft: 20, points: 0 },
            { law: "StGB", paragraph: "§46", description: "Ausstellen fälschlicher Gesundheitszeugnisse", min_bussgeld: "50'000", max_bussgeld: "125'000", min_haft: 50, max_haft: 50, points: 0 },
            { law: "StGB", paragraph: "§47", description: "Störung einer Behandlung", min_bussgeld: "25'000", max_bussgeld: "60'000", min_haft: 10, max_haft: 15, points: 0 },
            { law: "StGB", paragraph: "§48", description: "Belästigung", min_bussgeld: "75'000", max_bussgeld: "190'000", min_haft: 20, max_haft: 40, points: 0 },
            { law: "StGB", paragraph: "§50", description: "Flucht aus staatlichem Gewahrsam", min_bussgeld: "50'000", max_bussgeld: "125'000", min_haft: 30, max_haft: 60, points: 0 },
            { law: "StGB", paragraph: "§51", description: "Besitz von nicht offiziellen Geldmitteln", min_bussgeld: "30'000", max_bussgeld: "75'000", min_haft: 10, max_haft: 25, points: 0 },
            { law: "StGB", paragraph: "§52", description: "Inverkehrbringen von nicht offiziellen Geldmitteln", min_bussgeld: "60'000", max_bussgeld: "150'000", min_haft: 25, max_haft: 50, points: 0 },
            { law: "StGB", paragraph: "§53", description: "Missachtung von gerichtlichen Anordnungen", min_bussgeld: "40'000", max_bussgeld: "100'000", min_haft: 10, max_haft: 25, points: 0 },
            { law: "StGB", paragraph: "§54", description: "Angriff auf staatliche Einrichtungen", min_bussgeld: "75'000", max_bussgeld: "190'000", min_haft: 90, max_haft: 90, points: 0 }
        ];

        // Array für ausgewählte Einträge
        let selectedItems = [];

        // Suchfunktion
        const searchInput = document.getElementById("search");
        const tableBody = document.getElementById("table-body");

        // HTML-Elemente für die Ausgabe
        const selectedBody = document.getElementById("selected-body");
        const sumMinBussgeld = document.getElementById("sum-min-bussgeld");
        const sumMaxBussgeld = document.getElementById("sum-max-bussgeld");
        const sumMinHaft = document.getElementById("sum-min-haft");
        const sumMaxHaft = document.getElementById("sum-max-haft");
        const sumPoints = document.getElementById("sum-points");

        // Hilfsfunktion, um Bußgeld-Strings (z.B. "25'000") in Zahlen zu konvertieren
        function parseBussgeld(str) {
            // Entfernt alle ' Zeichen und wandelt in eine Zahl um
            return parseInt(str.replaceAll("'", ""), 10) || 0;
        }

        // Aktualisiert die Summen in der Zusammenfassung
        function updateSummary() {
            let totalMinBussgeld = 0;
            let totalMaxBussgeld = 0;
            let totalMinHaft = 0;
            let totalMaxHaft = 0;
            let totalPoints = 0;

            selectedItems.forEach(item => {
                totalMinBussgeld += parseBussgeld(item.min_bussgeld);
                totalMaxBussgeld += parseBussgeld(item.max_bussgeld);
                totalMinHaft += item.min_haft;
                totalMaxHaft += item.max_haft;
                totalPoints += item.points;
            });

            sumMinBussgeld.textContent = totalMinBussgeld.toLocaleString("de-DE");
            sumMaxBussgeld.textContent = totalMaxBussgeld.toLocaleString("de-DE");
            sumMinHaft.textContent = totalMinHaft;
            sumMaxHaft.textContent = totalMaxHaft;
            sumPoints.textContent = totalPoints;
        }

        // Funktion zum Entfernen eines Items aus der Auswahl
        function removeItem(index) {
            selectedItems.splice(index, 1);
            renderSelected();
        }

        // Rendert die Auswahl in der Tabelle "selected-body"
        function renderSelected() {
            selectedBody.innerHTML = "";

            selectedItems.forEach((item, idx) => {
                const row = document.createElement("tr");
                row.innerHTML = `
                    <td>${item.law}</td>
                    <td>${item.paragraph}</td>
                    <td>${item.description}</td>
                    <td>${item.min_bussgeld}</td>
                    <td>${item.max_bussgeld}</td>
                    <td>${item.min_haft}</td>
                    <td>${item.max_haft}</td>
                    <td>${item.points}</td>
                    <td><button class="btn" onclick="removeItem(${idx})">Entfernen</button></td>
                `;
                selectedBody.appendChild(row);
            });

            updateSummary();
        }

        // Fügt ein Item zur Auswahl hinzu
        function addItem(item) {
            // Verhindern, dass doppelte Einträge hinzugefügt werden (optional)
            // Man könnte hier checken, ob paragraph schon in selectedItems enthalten ist
            // Hier fügen wir es immer hinzu
            selectedItems.push(item);
            renderSelected();
        }

        // Filtert die Daten und erstellt Tabellenzeilen
        function renderTable(query) {
            tableBody.innerHTML = "";

            const filteredData = data.filter(item => {
                const lowLaw = item.law.toLowerCase();
                const lowParagraph = item.paragraph.toLowerCase();
                const lowDesc = item.description.toLowerCase();
                return (
                    lowLaw.includes(query) ||
            },
            {
                law: "StGB",
                paragraph: "§27",
                description: "Erregung öffentlichen Ärgernisses",
                min_bussgeld: "25'000",
                max_bussgeld: "60'000",
                min_haft: 0,
                max_haft: 0,
                points: 0
            },
            {
                law: "StGB",
                paragraph: "§28",
                description: "Meineid",
                min_bussgeld: "125'000",
                max_bussgeld: "325'000",
                min_haft: 20,
                max_haft: 50,
                points: 0
            },
            {
                law: "StGB",
                paragraph: "§29",
                description: "Hochverat",
                min_bussgeld: "150'000",
                max_bussgeld: "450'000",
                min_haft: 90,
                max_haft: 90,
                points: 0
            },
            {
                law: "StGB",
                paragraph: "§30",
                description: "Terroristischer Akt",
                min_bussgeld: "450'000",
                max_bussgeld: "625'000",
                min_haft: 90,
                max_haft: 90,
                points: 0
            },
            {
                law: "StGB",
                paragraph: "§31",
                description: "Missachtung Polizeilicher Anweisungen",
                min_bussgeld: "25'000",
                max_bussgeld: "60'000",
                min_haft: 10,
                max_haft: 25,
                points: 0
            },

            // =========== BtMG ===========
            {
                law: "BtMG",
                paragraph: "§3 Abs.1.c",
                description: "Besitz von Material zum Anbau von BTM",
                min_bussgeld: "30'000",
                max_bussgeld: "125'000",
                min_haft: 10,
                max_haft: 10,
                points: 0
            },
            {
                law: "BtMG",
                paragraph: "§3 Abs.1.b",
                description: "Besitz von Material zur Herstellung von BTM",
                min_bussgeld: "40'000",
                max_bussgeld: "150'000",
                min_haft: 15,
                max_haft: 15,
                points: 0
            },
            {
                law: "BtMG",
                paragraph: "§3 Abs.1.c (2)",
                description: "Anbau von BTM",
                min_bussgeld: "50'000",
                max_bussgeld: "200'000",
                min_haft: 20,
                max_haft: 20,
                points: 0
            },
            {
                law: "BtMG",
                paragraph: "§3 Abs.1.d",
                description: "Herstellung von BTM",
                min_bussgeld: "70'000",
                max_bussgeld: "250'000",
                min_haft: 30,
                max_haft: 30,
                points: 0
            },
            {
                law: "BtMG",
                paragraph: "§4 Abs.2.a",
                description: "Besitz von BTM 0-20g",
                min_bussgeld: "30'000",
                max_bussgeld: "100'000",
                min_haft: 0,
                max_haft: 0,
                points: 0
            },
            {
                law: "BtMG",
                paragraph: "§4 Abs.2.a (2)",
                description: "Besitz von BTM 20-100g",
                min_bussgeld: "50'000",
                max_bussgeld: "150'000",
                min_haft: 10,
                max_haft: 10,
                points: 0
            },
            {
                law: "BtMG",
                paragraph: "§4 Abs.2.a (3)",
                description: "Besitz von BTM 100-200g",
                min_bussgeld: "75'000",
                max_bussgeld: "200'000",
                min_haft: 15,
                max_haft: 15,
                points: 0
            },
            {
                law: "BtMG",
                paragraph: "§4 Abs.2.a (4)",
                description: "Besitz von BTM 200-1000g",
                min_bussgeld: "125'000",
                max_bussgeld: "250'000",
                min_haft: 25,
                max_haft: 25,
                points: 0
            },
            {
                law: "BtMG",
                paragraph: "§4 Abs.2.a (5)",
                description: "Besitz von BTM >1000g",
                min_bussgeld: "300'000",
                max_bussgeld: "450'000",
                min_haft: 40,
                max_haft: 40,
                points: 0
            },
            {
                law: "BtMG",
                paragraph: "§5 Abs.1.a",
                description: "Verkauf von BTM 0-20g",
                min_bussgeld: "50'000",
                max_bussgeld: "150'000",
                min_haft: 15,
                max_haft: 15,
                points: 0
            },
            {
                law: "BtMG",
                paragraph: "§5 Abs.1.b",
                description: "Verkauf von BTM >20g",
                min_bussgeld: "175'000",
                max_bussgeld: "300'000",
                min_haft: 30,
                max_haft: 30,
                points: 0
            },
            {
                law: "BtMG",
                paragraph: "§5 Abs.1.c",
                description: "Ankauf von BTM 0-20g",
                min_bussgeld: "50'000",
                max_bussgeld: "150'000",
                min_haft: 15,
                max_haft: 15,
                points: 0
            },
            {
                law: "BtMG",
                paragraph: "§5 Abs.1.d",
                description: "Ankauf von BTM >20g",
                min_bussgeld: "175'000",
                max_bussgeld: "300'000",
                min_haft: 30,
                max_haft: 30,
                points: 0
            },
            {
                law: "BtMG",
                paragraph: "§6",
                description: "Drogenkonsum",
                min_bussgeld: "25'000",
                max_bussgeld: "50'000",
                min_haft: 0,
                max_haft: 0,
                points: 0
            },

            // =========== WaffG ===========
            {
                law: "WaffG",
                paragraph: "§32",
                description: "Führen einer legalen Waffe ohne Lizenz",
                min_bussgeld: "25'000",
                max_bussgeld: "50'000",
                min_haft: 15,
                max_haft: 15,
                points: 0
            },
            {
                law: "WaffG",
                paragraph: "§33",
                description: "Besitz einer illegalen Waffe oder Munition",
                min_bussgeld: "60'000",
                max_bussgeld: "120'000",
                min_haft: 10,
                max_haft: 25,
                points: 0
            },
            {
                law: "WaffG",
                paragraph: "§33 Abs.1.a",
                description: "Besitz einer illegalen Waffe Klasse A",
                min_bussgeld: "40'000",
                max_bussgeld: "100'000",
                min_haft: 10,
                max_haft: 20,
                points: 0
            },
            {
                law: "WaffG",
                paragraph: "§33 Abs.1.b",
                description: "Besitz einer illegalen Waffe Klasse B",
                min_bussgeld: "80'000",
                max_bussgeld: "150'000",
                min_haft: 10,
                max_haft: 30,
                points: 0
            },
            {
                law: "WaffG",
                paragraph: "§33 Abs.1.c",
                description: "Besitz einer illegalen Waffe Klasse C",
                min_bussgeld: "120'000",
                max_bussgeld: "200'000",
                min_haft: 10,
                max_haft: 50,
                points: 0
            },
            {
                law: "WaffG",
                paragraph: "§34",
                description: "Waffenhandel",
                min_bussgeld: "150'000",
                max_bussgeld: "250'000",
                min_haft: 50,
                max_haft: 90,
                points: 0
            },
            {
                law: "WaffG",
                paragraph: "§35",
                description: "Unberechtigter Waffengebrauch",
                min_bussgeld: "80'000",
                max_bussgeld: "100'000",
                min_haft: 15,
                max_haft: 30,
                points: 0
            },

            // =========== StVO ===========
            {
                law: "StVO",
                paragraph: "§1 Abs.5",
                description: "Nicht Mitführen von Verbandsmaterial im Fahrzeug",
                min_bussgeld: "25'000",
                max_bussgeld: "50'000",
                min_haft: 0,
                max_haft: 0,
                points: 0
            },
            {
                law: "StVO",
                paragraph: "§1 Abs.6",
                description: "Verstoß gegen die Anschnallpflicht",
                min_bussgeld: "25'000",
                max_bussgeld: "50'000",
                min_haft: 0,
                max_haft: 0,
                points: 1
            },
            {
                law: "StVO",
                paragraph: "§2 Abs.1",
                description: "Fahren ohne Fahrerlaubnis",
                min_bussgeld: "55'000",
                max_bussgeld: "125'000",
                min_haft: 0,
                max_haft: 0,
                points: 3
            },
            {
                law: "StVO",
                paragraph: "§3 Abs.1",
                description: "Verstoß gegen das Rechtsfahrgebot",
                min_bussgeld: "10'000",
                max_bussgeld: "25'000",
                min_haft: 0,
                max_haft: 0,
                points: 1
            },
            {
                law: "StVO",
                paragraph: "§3 Abs.3",
                description: "Fahren abseits von befestigten Straßen/Feldwege/Waldwege",
                min_bussgeld: "7'500",
                max_bussgeld: "12'500",
                min_haft: 0,
                max_haft: 0,
                points: 0
            },
            {
                law: "StVO",
                paragraph: "§4",
                description: "Gefährlicher Eingriff in den Straßenverkehr",
                min_bussgeld: "40'000",
                max_bussgeld: "95'000",
                min_haft: 5,
                max_haft: 20,
                points: 2
            },
            {
                law: "StVO",
                paragraph: "§5 (1)",
                description: "Geschwindigkeitsüberschreitung 20 bis 50",
                min_bussgeld: "20'000",
                max_bussgeld: "50'000",
                min_haft: 0,
                max_haft: 0,
                points: 0
            },
            {
                law: "StVO",
                paragraph: "§5 (2)",
                description: "Geschwindigkeitsüberschreitung 50 bis 100",
                min_bussgeld: "44'000",
                max_bussgeld: "75'000",
                min_haft: 0,
                max_haft: 0,
                points: 1
            },
            {
                law: "StVO",
                paragraph: "§5 (3)",
                description: "Geschwindigkeitsüberschreitung 100 bis 150",
                min_bussgeld: "40'000",
                max_bussgeld: "150'000",
                min_haft: 0,
                max_haft: 0,
                points: 2
            },
            {
                law: "StVO",
                paragraph: "§5 (4)",
                description: "Geschwindigkeitsüberschreitung 150 bis 250",
                min_bussgeld: "100'000",
                max_bussgeld: "200'000",
                min_haft: 0,
                max_haft: 0,
                points: 4
            },
            {
                law: "StVO",
                paragraph: "§5 (5)",
                description: "Geschwindigkeitsüberschreitung 250 bis <<>>",
                min_bussgeld: "125'000",
                max_bussgeld: "250'000",
                min_haft: 0,
                max_haft: 0,
                points: 8
            },
            {
                law: "StVO",
                paragraph: "§6 Abs.1",
                description: "Nicht Zugelassenes Fahrzeug auf der Autobahn",
                min_bussgeld: "50'000",
                max_bussgeld: "100'000",
                min_haft: 0,
                max_haft: 0,
                points: 1
            },
            {
                law: "StVO",
                paragraph: "§7 Abs.1",
                description: "Nicht beachten von Verkehrsschildern",
                min_bussgeld: "25'000",
                max_bussgeld: "50'000",
                min_haft: 0,
                max_haft: 0,
                points: 1
            },
            {
                law: "StVO",
                paragraph: "§9 Abs.1",
                description: "Überholen von Rechts",
                min_bussgeld: "10'000",
                max_bussgeld: "25'000",
                min_haft: 0,
                max_haft: 0,
                points: 1
            },
            {
                law: "StVO",
                paragraph: "§10 Abs.1",
                description: "Missachtung von Vorfahrtsregelungen",
                min_bussgeld: "20'000",
                max_bussgeld: "50'000",
                min_haft: 0,
                max_haft: 0,
                points: 1
            },
            {
                law: "StVO",
                paragraph: "§11",
                description: "Falschparken",
                min_bussgeld: "15'000",
                max_bussgeld: "30'000",
                min_haft: 0,
                max_haft: 0,
                points: 0
            },
            {
                law: "StVO",
                paragraph: "§12",
                description: "Verbotenes Nutzen von Warnzeichen",
                min_bussgeld: "12'500",
                max_bussgeld: "35'000",
                min_haft: 0,
                max_haft: 0,
                points: 0
            },
            {
                law: "StVO",
                paragraph: "§13 Abs.1",
                description: "Blockieren von Ein- / Ausfahrten",
                min_bussgeld: "10'000",
                max_bussgeld: "40'000",
                min_haft: 0,
