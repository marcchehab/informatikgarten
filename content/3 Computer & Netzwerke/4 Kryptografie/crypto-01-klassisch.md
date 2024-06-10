---
title: "01: Kryptografie Intro"
---
## Wieso Kryptografie?

> [!example] Praktischer Einstieg
> 
> Setzten Sie sich in 4er- und 5er-Gruppen zusammen. Sie sind alles Spione eines Geheimdienstes und müssen eine Geheimschrift entwickeln, wie Sie **Nachrichten ver- und entschlüsseln** können. Aber Achtung! Ihre Nachrichten können in die falschen Hände geraten. Schaffen Sie es eine Methode zu finden, die **die gegnerischen Geheimdienste nicht knacken können**? 
> 
> Sie haben 15 Minuten Zeit für folgende Aufgaben:
> - Einigen Sie sich auf eine **Methode**
> - Teilen Sie Ihre Gruppe in **zwei Teilgruppen**. Jede Teilgruppe **verschlüsselt** eine hochgeheime Nachricht über ein Treffen mit 3 Sätzen für die andere Teilgruppe.
> - Die andere Teilgruppe **entschlüsselt** die Nachricht, um zu schauen, ob Ihre Methode funktioniert.
> 
> ...doch dann passiert der Super-GAU!
> 
> (Musik fürs [Ambiente](https://open.spotify.com/track/4y8GgkINBu7hH7IX9CBw87?si=16e17ac2221e4b06))

## Kryptografie mit Hilfe von Python

Weite Teile des modernen Internets basieren auf demselben Prinzip: dass Nachrichten geheim übertragen werden können. Wir nähern uns hier diesem Thema an und schauen, wie wir mit Python eine eigene Verschlüsselungsfunktion schreiben können. Zuerst einigen wir uns doch auf die Begriffe:
- **Klartext**: Die Information, die wir verschlüsseln.
- **Geheimtext**: Die verschlüsselte Zeichenkette
- **Schlüssel**: Was man wissen muss, um den Geheimtext in den Klartext umzuwandeln.

Sie müssen als Basis allerdings wissen, wie Computer Texte speichern.

### ASCII und Unicode
Es wird Sie kaum überraschen, dass Texte in Computern letztlich eine Serie von Binärzahlen sind. Die Semantik ist letztlich einfach eine Tabelle, **die jeder Zahl einen Buchstaben zuordnet**. 

Heute verwenden wir dafür weiterhin die sogenannte ASCII-Tabelle, die in den 1960ern standardisiert wurde. Dieser Zeichensatz wurde für die Übertragung so klein wie möglich gehalten, nämlich 7 Bit oder 128 Zeichen.

![[index 2024-06-10 11.09.08.excalidraw]]

Beispiel:
- `A` hat den ASCII-Code 65.
- `a` hat den ASCII-Code 97.

ASCII deckt hauptsächlich die englische Sprache ab und hat somit Einschränkungen für andere Sprachen und Symbole (z.B. `€ — © ™ ∆ Ω 你好 Привіт 😊 🎉`)

Als Reaktion auf die Beschränkungen von ASCII wurde Unicode entwickelt, um alle Schriftzeichen aller Sprachen darzustellen. Unicode kann über 1 Million Zeichen kodieren, von denen bisher über 143'000 definiert sind. 

Binär nutzt Unicode den Umstand, dass die ASCII-Tabelle nur 7 Bit benötigt, also dass ein "normales" ASCII-Byte mit 0 beginnen würde. Unicode sagt nun: Wir signalisieren mit **`1` am Anfang des ersten Byte**, wie viele Bytes wir nutzen, und mit `10` am Anfang der weiteren Bytes, dass sie teil des gleichen Symbols sind.

- **1 Byte** (für Zeichen von U+0000 bis U+007F):
    - Format: `0xxxxxxx`
    - Beispiel: `A` (U+0041) -> `01000001`
- **2 Bytes** (für Zeichen von U+0080 bis U+07FF):
    - Format: `110xxxxx 10xxxxxx`
    - Beispiel: `é` (U+00E9) -> `11000011 10101001`
- **3 Bytes** (für Zeichen von U+0800 bis U+FFFF):
    - Format: `1110xxxx 10xxxxxx 10xxxxxx`
    - Beispiel: `你` (U+4F60) -> `11100100 10111101 10100000`
- **4 Bytes** (für Zeichen von U+10000 bis U+10FFFF):
    - Format: `11110xxx 10xxxxxx 10xxxxxx 10xxxxxx`
    - Beispiel: `𐍈` (U+10348) -> `11110000 10010000 10001101 10001000`

### Wörter sind Listen von Unicode-Symbolen in Python

Beim Erstellen einer Verschlüsselungsfunktion hilft Ihnen der Umstand, dass man in Python **Zeichenketten wie Listen behandeln** kann. Zudem können Sie mit der **Funktion ord()** den Unicode des Buchstabens auslesen und **chr() macht aus einem Unicode wieder den Buchstaben**.

```turtle
satz = "Hallo 😍"

for buchstabe in satz:
	print(buchstabe, " hat den Code ", ord(buchstabe))

print("Ein Beispiel für einen Unicode: ", chr(100))
```

### Caesar-Verschlüsselung

Die Caesar-Verschlüsselung ist eine der einfachsten und bekanntesten Methoden der klassischen Kryptografie. Sie wurde nach Julius Caesar benannt, der diese Methode angeblich verwendet hat, um seine militärischen Nachrichten zu verschlüsseln.

Die Caesar-Verschlüsselung ist eine sogenannte **monoalphabetische Substitution**. Das bedeutet, dass jeder Buchstabe des Klartextes durch einen anderen Buchstaben des Alphabets ersetzt wird. Der Ersatz erfolgt durch eine feste Anzahl von Stellen, die als Schlüssel bezeichnet wird. 
#### Funktionsweise

1. **Alphabetverschiebung**: Jeder Buchstabe im Klartext wird durch den Buchstaben ersetzt, der eine bestimmte Anzahl von Positionen weiter im Alphabet steht.
   - Zum Beispiel: Bei einer Verschiebung um 3 (dem klassischen Schlüssel) wird `A` zu `D`, `B` zu `E`, und so weiter.
2. **Modulares Rechnen**: Da das Alphabet zyklisch ist, wird am Ende des Alphabets wieder von vorne begonnen. 
   - Zum Beispiel: `X` wird zu `A`, `Y` wird zu `B`, und `Z` wird zu `C` bei einer Verschiebung um 3.
#### Beispiel

- **Klartext**: "HELLO"
- **Schlüssel**: 3
- **Verschlüsselter Text**: "KHOOR"

Hierbei wird jeder Buchstabe des Klartextes um drei Positionen im Alphabet verschoben.

#### Vorteile und Nachteile

- **Vorteile**:
  - Einfachheit: Die Caesar-Verschlüsselung ist leicht zu verstehen und umzusetzen.
  - Geschwindigkeit: Aufgrund ihrer Einfachheit kann sie sehr schnell angewendet werden.

- **Nachteile**:
  - Schwache Sicherheit: Die Caesar-Verschlüsselung ist anfällig für einfache Kryptoanalysen. Mit nur 25 möglichen Verschiebungen (bei einem Alphabet von 26 Buchstaben) kann ein Angreifer alle möglichen Schlüssel ausprobieren (Brute-Force-Angriff) oder durch eine Häufigkeitsanalyse den Schlüssel schnell herausfinden.

### Vigenère-Verschlüsselung

Die Vigenère-Verschlüsselung ist eine weiterentwickelte Form der monoalphabetischen Substitution und stellt eine **polyalphabetische Substitution** dar. Sie wurde nach Blaise de Vigenère benannt und ist deutlich sicherer als die Caesar-Verschlüsselung, da sie mehrere Caesar-Verschiebungen kombiniert.

#### Funktionsweise

1. **Schlüsselwort verwenden**: Ein Schlüsselwort bestimmt die Verschiebungen für die einzelnen Buchstaben des Klartextes. Jeder Buchstabe des Schlüsselworts gibt an, um wie viele Positionen der entsprechende Buchstabe des Klartextes verschoben wird.
   - Zum Beispiel: Bei dem Schlüsselwort "KEY" wird der erste Buchstabe des Klartextes um die Position des Buchstabens "K" (10 Positionen), der zweite um "E" (4 Positionen) und der dritte um "Y" (24 Positionen) verschoben. Dieses Muster wiederholt sich, wenn das Schlüsselwort kürzer als der Klartext ist.
2. **Verschiebung berechnen**: Jeder Buchstabe des Klartextes wird basierend auf dem entsprechenden Buchstaben des Schlüsselwortes verschoben.
#### Beispiel

- **Klartext**: "HELLO"
- **Schlüsselwort**: "KEY"
- **Schlüsselwort erweitert**: "KEYKE"
- **Verschlüsselter Text**: "RIJVS"

Hierbei wird jeder Buchstabe des Klartextes unterschiedlich verschoben:

- `H` (Shift 10) -> `R`
- `E` (Shift 4) -> `I`
- `L` (Shift 24) -> `J`
- `L` (Shift 10) -> `V`
- `O` (Shift 4) -> `S`

![[crypto-01-klassisch 2024-06-10 12.39.53.excalidraw]]

#### Vorteile und Nachteile

- **Vorteile**:
  - Erhöhte Sicherheit: Durch die Verwendung eines Schlüsselwortes und die daraus resultierenden variablen Verschiebungen ist die Vigenère-Verschlüsselung weniger anfällig für einfache Kryptoanalysen.
  - Verschleierung der Häufigkeit: Häufigkeitsmuster des Klartextes werden verschleiert, was die Analyse erschwert.

- **Nachteile**:
  - Schlüsselverwaltung: Die Sicherheit hängt stark von der Geheimhaltung und der Komplexität des Schlüsselworts ab.
  - Anfälligkeit für bestimmte Angriffe: Bei sehr langen Texten und kurzen Schlüsselwörtern kann die Vigenère-Verschlüsselung durch bestimmte Kryptoanalysetechniken wie die Kasiski-Untersuchung geknackt werden.

### Scytale-Verschlüsselung

Die Scytale-Verschlüsselung ist eine der ältesten bekannten Verschlüsselungsmethoden und wurde im antiken Griechenland verwendet. Sie ist eine Form der **Transpositionsverschlüsselung**, bei der die Positionen der Zeichen im Klartext verändert werden, ohne die Zeichen selbst zu verändern.

#### Funktionsweise

1. **Scytale-Stab**: Ein Stab oder Zylinder mit einem bestimmten Durchmesser wird verwendet. Die Nachricht wird auf einen Streifen Papier geschrieben, der um den Stab gewickelt wird.
2. **Zeilenweise Lesen**: Nachdem die Nachricht auf den Stab gewickelt wurde, wird sie in Zeilen geschrieben. Der verschlüsselte Text wird dann zeilenweise abgelesen.
![[Pasted image 20240610125006.png]]
#### Beispiel

- **Klartext**: "diesisteinegeheimenachricht"
- **Anzahl der Zeilen**: 5 (wird als Anzahl der "Rails" oder Spalten interpretiert)

**Schritt-für-Schritt-Verfahren**:
1. Schreibe die Nachricht zeilenweise um den Stab:
   ```
   d i e s i
   s t e i n
   e g e h e
   i m e n a
   c h r i c
   h t
   ```

2. Lies die Zeichen spaltenweise ab, um den verschlüsselten Text zu erhalten:
   ```
   Verschlüsselte Nachricht: "dseich itgmht eeeer sihni ineac"
   ```

#### Vorteile und Nachteile

- **Vorteile**:
  - Einfachheit: Die Scytale-Verschlüsselung ist leicht zu verstehen und umzusetzen.
  - Historische Bedeutung: Sie ist eine der ältesten bekannten Verschlüsselungsmethoden und bietet Einblick in frühe Kryptografie.

- **Nachteile**:
  - Schwache Sicherheit: Die Scytale-Verschlüsselung ist anfällig für einfache Kryptoanalysen, da die Transpositionsmuster leicht erkannt und rückgängig gemacht werden können.
  - Begrenzte Anwendung: In modernen Anwendungen bietet die Scytale-Verschlüsselung keinen ausreichenden Schutz.

Die Scytale-Verschlüsselung veranschaulicht grundlegende Konzepte der Transpositionsverschlüsselung und ist ein historisch bedeutendes Beispiel für frühe kryptografische Methoden.

## Python-Funktionen für klassische Verschlüsselungsverfahren

> [!solution]- Eine Caesar-Verschlüsselung
> 
> ```python
> def caesar_verschluesselung(text, verschiebung):
>     # Initialisiere den verschlüsselten Text als leere Zeichenkette
>     verschluesselter_text = ""
>     
>     # Gehe jeden Buchstaben im Eingabetext durch
>     for char in text:
>         # Überprüfe, ob der Buchstabe ein Grossbuchstabe ist
>         if char.isupper():
>             # Berechne die neue Position und sorge dafür, dass sie im Bereich von A-Z bleibt
>             neue_position = (ord(char) + verschiebung - 65) % 26 + 65
>             # Füge den verschlüsselten Buchstaben zum verschlüsselten Text hinzu
>             verschluesselter_text += chr(neue_position)
>         # Überprüfe, ob der Buchstabe ein Kleinbuchstabe ist
>         elif char.islower():
>             # Berechne die neue Position und sorge dafür, dass sie im Bereich von a-z bleibt
>             neue_position = (ord(char) + verschiebung - 97) % 26 + 97
>             # Füge den verschlüsselten Buchstaben zum verschlüsselten Text hinzu
>             verschluesselter_text += chr(neue_position)
>         else:
>             # Wenn es kein Buchstabe ist, füge das Zeichen unverändert hinzu
>             verschluesselter_text += char
>     
>     # Gebe den verschlüsselten Text zurück
>     return verschluesselter_text
> 
> # Beispiel zur Verwendung der Funktion
> text = "Hallo liebe G1b! Können Sie diesen Text entschlüsseln? Liebe Grüsse, Marc Chehab"
> verschiebung = 3
> print(caesar_verschluesselung(text, verschiebung))  # Ausgabe: "Kdoor Zhow"
> ```

