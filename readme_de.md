# Passwortgenerator

Ein Python-Skript zum Generieren von zufälligen Passwörtern mit benutzerdefinierten Optionen.

## Sprachversionen
[![Englisch](https://img.shields.io/badge/Englisch-Englisch-blau)](readme.md)
[![Deutsch](https://img.shields.io/badge/Deutsch-Deutsch-blau)](readme_de.md)
[![Spanisch](https://img.shields.io/badge/Spanisch-Spanisch-blau)](readme_es.md)

## Einführung

Dieses Python-Skript ermöglicht es Ihnen, zufällige Passwörter mit spezifischen Optionen zu generieren, wie der Passwortlänge und der Einbeziehung erweiterter Zeichensätze. Sie können dieses Tool verwenden, um starke und sichere Passwörter für Ihre Anwendungen oder Konten zu erstellen.

## Funktionen

- Generieren von zufälligen Passwörtern mit einer festgelegten Länge.
- Einbeziehen erweiterter Zeichensätze für stärkere Passwörter.
- Anpassen von Zeichensätzen, um Ihren Anforderungen gerecht zu werden.

## Erste Schritte

### Voraussetzungen

Um dieses Skript zu verwenden, müssen Sie Python auf Ihrem System installiert haben. Sie können Python von der offiziellen Website herunterladen und installieren: [Python-Downloads](https://www.python.org/downloads/).

### Installation

1. Klonen Sie das Repository auf Ihre lokale Maschine mit folgendem Befehl:

    ```bash
    git clone https://github.com/david-star-git/keyshuffler.git
    ```

2. Ändern Sie das Arbeitsverzeichnis in den Projektordner:

    ```bash
    cd KeyShuffler
    ```

3. Führen Sie das Skript mit den gewünschten Optionen aus (siehe [Verwendung](#verwendung)).

## Verwendung

Um ein Passwort zu generieren, führen Sie das Skript mit folgendem Befehl aus:

```bash
python password_generator.py
```

Standardmäßig wird dies ein Passwort mit 50 Zeichen und nur standardmäßigen ASCII-Zeichen generieren. Sie können die Passwortlänge und den Zeichensatz mit den folgenden Optionen anpassen:

- **-l** oder **--länge**: Geben Sie die Länge des Passworts an.
- **-e** oder **--erweitert**: Enthalten Sie erweiterte Zeichensätze für stärkere Passwörter.

Beispielverwendungen:

- Generieren Sie ein 12-Zeichen-Passwort mit erweiterten Zeichen:

```bash
python password_generator.py -l 12 -e
```

## Anpassung

Sie können die Zeichensätze für normale und erweiterte Zeichen anpassen, indem Sie die Variablen `normal_chars` und `extended_chars` im Skript bearbeiten. Die Standardwerte bieten eine vernünftige Auswahl an Zeichen zum Generieren von Passwörtern, aber Sie können sie nach Ihren Bedürfnissen anpassen.

```py
normal_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+=-[]{}|;:'\"<>,.?/~"
extended_chars = " ¡⅛£¤⅜⅝⅞™±°¿˛¯˘˚ÞØı↑¥Ŧ®€§ΩÆẞÐªŊĦ ̇&Ł ̣ˇ—÷×º’‘‚©‹›ˍ|»«¢„“”µ·…–^˝łĸ ̣ħŋđðſæ@ſ€¶ŧ←↓→øþ¨’¸\}][{¬½¼³²¹⁴⁵⁶⁷⁸⁹⁰}]"
```

## Lizenz

Dieses Projekt steht unter der [GNU General Public License, Version 3.0](LICENSE). Den vollständigen Lizenztext finden Sie [hier](https://www.gnu.org/licenses/gpl-3.0.html).