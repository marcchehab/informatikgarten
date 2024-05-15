---
title: "01: Wie ein Prozessor rechnet"
---
> [!success] Lernziele
> 
> - Sie wissen, was die Logikgates NAND, AND, OR, XOR tun und kennen ihre Wahrheitstabellen und Symbole.
> - Sie können aus einfachen logischen Schaltungen eine Wahrheitstabelle ableiten.
> - Sie können eine logische Schaltung für einen Halbaddierer und einen Addierer mit den korrekten Symbolen zeichnen und nachvollziehen.

Ihr Computer ist eine Rechenmaschine, die auf purer Logik aufgebaut ist. Es gibt keine Magie, kein "Geist" in der Maschine - alles ist von Grund auf nachvollziehbar. In dieser Lektion bauen wir einen Rechner, der zwei binäre Zahlen addieren kann.

Im Folgenden machen wir uns daran, einen Addierer zu bauen. Damit Sie die Übersicht nicht verlieren: Wir werden zuerst 
1. aus Transistoren die nötigen **Logikgates** bauen 
2. und dann aus diesen Logikgates den **Addierer**.

**Der wichtige Teil für Sie ist Nummer 2**: Wie man aus Logikgates einen Addierer baut. In der Sprache von Modulen gesprochen:
- Sie müssen Logikgates nur nutzen können (die Schnittstelle genügt, die Funktionsweise müssen Sie sich nicht merken).
- Sie müssen den Addierer mit Logikgates implementieren können (also die Funktionsweise wirklich verstehen).

![[aufbau-01-cpu 2024-04-29 11.51.26.excalidraw]]

## 1. Aus Transistoren bauen wir Logikbausteine
### Intuitive Annäherung

Sie sehen also: Wir brauchen elementare Logikbausteine wie UND und ODER. Wie könnten wir eine Maschine bauen, die diese Logik umsetzten kann? 

Auch hier eine intuitive Annäherung: Wir könnten uns A und B als zwei Lichtschalter vorstellen, die in einem Stromkreis eine Lampe zum leuchten bringen (1) oder nicht (0).

Wenn beide Schalter parallel geschalten sind, muss A **oder** B geschlossen werden, damit die Lampe leuchtet.

![[aufbau-01-cpu 2024-04-29 11.26.42.excalidraw]]

Wenn beide Schalter seriell geschalten sind, muss A **und** B geschlossen werden, damit die Lampe leuchtet.
![[aufbau-01-cpu 2024-04-29 11.34.53.excalidraw]]
Sie können sich also vorstellen, dass wenn der Stromkreis kompliziert genug ist, Sie damit rechnen können.

### Umsetzung

Wir verwenden das [Nand-Game](https://nandgame.com/) um folgende Logikgates zu bauen. Dieser Teil wird [in diesem Video](https://kswe-my.sharepoint.com/:v:/g/personal/cha_kswe_ch/EbHUTNcJsntBnlMyQgKc-mABkhzEVL-gBPmd_baop__Eqw?e=Zu0OBg&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D) erklärt.


![[Drawing 2024-04-29 07.05.53.excalidraw]]

## 2. Aus Logikbausteinen bauen wir den Rechner
### Intuitive Annäherung

Führen Sie sich folgende binäre Addition von zwei Bits vor Augen. Achtung: Wir sind im **Binärsystem**!
![[aufbau-01-cpu 2024-04-29 11.03.55.excalidraw]]

Ich habe immer zwei Stellen beim Ergebnis hingeschrieben, damit wir uns folgendes überlegen können: Was ist die Logik beider Stellen?

Überlegen Sie sich nun die Logik:
1. Wann gibt es bei den 2ern (blau) eine 1 im Ergebnis?
2. Wann gibt es bei den 1ern (grün) eine 1 im Ergebnis?
> [!NOTE]- Lösung
> 
> 1. Bei den 2ern gibt es eine 1, wenn A und B 1 sind.
> 2. Bei den 1ern gibt es eine 1, wenn nur A oder nur B 1 sind.

### Umsetzung

Dieser Teil wird [in diesem Video](https://kswe-my.sharepoint.com/:v:/g/personal/cha_kswe_ch/EXzMMEBOos5KlShPEygNtnIBKK5X_iYTH_lDxmyQ8VwMJQ?e=810XJS&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D) erklärt.
#### Halbaddierer (und wieso das nicht reicht)

Wir haben zuerst einen sogenannten Halbaddierer gebaut, der zwei Bits "A" und "B" zusammenzählt, wie oben bei der Rechnung. "Low" ist die tiefere Stelle, "high" die höhere Stelle.
![[aufbau-01-addierer 2024-05-15 13.05.51.excalidraw]]
Damit können wir nur eine einzelne Stelle einer binären Zahl addieren. Für eine Addition von längeren Zahlen müssten wir **nicht zwei sondern drei Bits addieren** können. Wieso?

Schauen Sie sich dazu folgende schriftliche Addition zweier Binärzahlen an:

![[aufbau-01-addierer 2024-05-15 13.28.23.excalidraw]]
Man könnte denken, dass man die 1er, 2er, 4er und 8er nacheinander mit dem Halbaddierer addieren kann - es sind ja jeweils zwei Bits.

| Stelle                         | Rechnung | Ergebnis |
| ------------------------------ | -------- | -------- |
| Bei den 1ern geht das:         | 1+0      | = 1      |
| Bei den 2ern auch:             | 0+1      | = 1      |
| Aber die 4ern machen Probleme! | 1+1      | = 10     |
Sie würden das als Mensch mit einem "Behalte" oder "Überschlag" auf die nächste Stelle lösen. Auf Englisch wird das "Carry" genannt, deswegen schreiben wir im Folgenden "C". Überlegen wir uns also die Rechnung:

- Bei den 4ern würden Sie also 0 ins Ergebnis schreiben, aber ein Behalte 1 in die nächste Stelle - die 8er (blauer Pfeil). 
- Bei den 8er hätten Sie dann entsprechend drei Einsen, die Sie addieren.

![[aufbau-01-addierer 2024-05-15 13.45.26.excalidraw]]

Sie sehen: Um zwei Binärzahlen mit mehreren Stellen addieren zu können, müssen wir pro Stelle **nicht zwei sondern drei Bits addieren können**: wegen dem "Behalte". Und das macht der Addierer (oder Volladdierer).
#### Addierer

Um die Schaltung für den (Voll-)Addierer zu verstehen, schlage ich vor, dass Sie auf dem Halbaddierer aufbauen und sich die beiden Outputs getrennt überlegen. Denken wir zuerst über den Punkt nach, den ich mit einem "X" markiert habe, und **überlegen uns nur die 1er (low)** des Ergebnisses.

- Wenn A+B=1, ist das XOR 1.
- Wenn A+B=0 oder A+B=10<sub>2</sub>, ist das XOR 0.

Isoliert für die 1er (low) können wir diese Zahl also einfach **als einzelne Zahl verwenden** und sie zu C hinzuaddieren. Wie? Mit einem zweiten Halbaddierer!


![[aufbau-01-addierer 2024-05-15 13.59.54.excalidraw]]

Jetzt überlegen wir uns die 2er (high):
- Wenn A+B=10<sub>2</sub> (d.h. 2<sub>10</sub>) gibt, dann wissen wir bereits: Wir brauchen die 2er (high).
- Wenn A+B=1 **und** C=1 gilt, dann wissen wir ebenfalls: Wir brauchen einen 2er (high).

Diese beiden Fälle schliessen sich aus: Entweder trifft der eine **oder** der andere zu. Wir können einfach ein OR verwenden, um sie zu verknüpfen (oder ein XOR, aber das ist nicht optimal).

