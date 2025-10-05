# Minecraft Datapack Converter

Dieses Python-Skript konvertiert `.mcfunction`-Dateien in einem Minecraft-Datapack so, dass allen Befehlen automatisch das Präfix `minecraft:` hinzugefügt wird (sofern es noch nicht vorhanden ist).
Die konvertierten Datapacks werden anschließend wieder als ZIP-Datei gespeichert.

---

## 🔧 Funktionsweise

1. Das Skript sucht im Ordner `./input` nach einer ZIP-Datei (z. B. `datapack.zip`).
2. Diese ZIP-Datei wird entpackt.
3. Alle `.mcfunction`-Dateien werden durchsucht und jeder Befehl, der **kein Namespace** enthält, erhält automatisch das Präfix `minecraft:`.
4. Der bearbeitete Inhalt wird als neue ZIP-Datei im Ordner `./output` gespeichert.
   Der neue Dateiname entspricht dem ursprünglichen, jedoch mit der Endung **`_converted`**
   Beispiel:
   `input/datapack.zip → output/datapack_converted.zip`
5. Temporäre Dateien werden nach der Verarbeitung gelöscht.

---

## 📁 Ordnerstruktur

```
projektordner/
│
├─ input/        # Hier kommt deine originale ZIP-Datei hinein
├─ output/       # Hier erscheint die konvertierte ZIP-Datei
├─ data/         # Wird temporär zum Entpacken verwendet (automatisch gelöscht)
└─ main.py       # Das Hauptskript
```

---

## ▶️ Verwendung

1. **Python 3 installieren**
   Stelle sicher, dass Python 3 auf deinem System installiert ist.

2. **Abhängigkeiten installieren**

   ```
   pip install tqdm
   ```

3. **ZIP-Datei in den Input-Ordner legen**

   ```
   ./input/mein_datapack.zip
   ```

4. **Skript ausführen**

   ```
   python main.py
   ```

5. **Ergebnis finden**
   Nach der Ausführung findest du die konvertierte Datei im `output`-Ordner:
   `./output/mein_datapack_converted.zip`

---

## 💡 Beispiel

**Vorher (Zeile in einer `.mcfunction`):**

```
give @p diamond 1
```

**Nachher:**

```
minecraft:give @p diamond 1
```

---

## ⚙️ Anforderungen

* Python 3.8 oder höher
* Modul: `tqdm`

---

## 🧹 Aufräumen

Das Skript löscht den temporären Ordner `./data` automatisch nach der Verarbeitung.
