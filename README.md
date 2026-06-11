# Úkolníček (To-Do Application)

Jednoduchá desktopová aplikace pro správu každodenních úkolů s moderním tmavým vzhledem (Dark Mode) a automatickým ukládáním dat.

## Hlavní funkce

* **Správa úkolů:** Přidávání nových úkolů s možností určení času/termínu.
* **Označování hotového:** Možnost kliknutím přepínat stav úkolu (Hotovo / Nehotovo) s vizuální fajfkou `✔`.
* **Trvalé ukládání (Perzistence dat):** Úkoly se automaticky ukládají do souboru `tasks.json`. Po zavření a znovuotevření aplikace data nezmizí.
* **Ochrana dat (Zpětná kompatibilita):** Kód obsahuje kontrolu struktury JSON souboru, takže aplikace nespadne ani při načtení starší verze databáze.
* **Počítadlo:** Dynamické zobrazení pokroku (např. *Hotové: 2 / 5*).
* **Hromadné mazání:** Možnost vymazat celý seznam s bezpečnostním potvrzovacím oknem.
* **Dark Mode:** Uživatelské rozhraní stylizované do tmavých barev šetrných pro oči.

## Použité technologie a knihovny

Aplikace je napsána v jazyce **Python 3** s využitím následujících modulů:

* **`tkinter`** – Využit pro kompletní tvorbu grafického uživatelského rozhraní (okna, tlačítka, textová pole, listbox).
* **`json`** – Použit pro serializaci a deserializaci dat (převod seznamu úkolů do textového souboru a zpět).
* **`os`** – Slouží ke kontrole existence datového souboru v systému.

## Struktura projektu

* `main.py` (nebo název tvého skriptu) – Hlavní zdrojový kód aplikace obsahující logiku i GUI.
* `tasks.json` – Datový soubor (databáze), kam se ukládají úkoly ve formátu JSON (vytvoří se automaticky při prvním uložení).

##  Ukázka datové struktury (tasks.json)
