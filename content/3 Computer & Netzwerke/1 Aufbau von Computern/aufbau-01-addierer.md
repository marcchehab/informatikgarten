---
title: "01: Wie ein Prozessor rechnet"
---
> [!success] Lernziele
> 
> - Sie wissen, was die Logikgates NAND, AND, OR, XOR tun und können ihre Wahrheitstabellen sowie ihre Symbole in einer Schaltung identifizieren.
> - Sie können aus einfachen logischen Schaltungen eine Wahrheitstabelle ableiten.
> - Sie können eine logische Schaltung für einen Halbaddierer und einen Addierer zeichnen.

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
#### Halbaddierer
![[Pasted image 20240506070736.png]]

#### Addierer

![[Pasted image 20240506070804.png]]

