---
title: "04: Prüfungsvorbereitung"
---
## Lernziele
Hier die zusammengetragenen Lernziele der Lektionen:

> [!success] Lernziele für die Prüfung über Computersysteme
>
> #### [Intro](aufbau-00-intro)
> - Sie können den Unterschied zwischen **Abstraktion** und **Implementierung** eines Moduls beschreiben.
> - Sie können Benutzer, Anwendungsprogramme, **Betriebssystem** und Hardware nach "Abstraktheit" sortieren.
> - Sie können erklären, wieso es ein Betriebssystem als **Schnittstelle zwischen Hardware und Anwenderprogrammen** braucht.
> 
>  #### [Logikgates & Addierer](aufbau-01-addierer) 
>  - Sie wissen, was die **Logikgates** NAND, AND, OR, XOR tun und kennen ihre **Wahrheitstabellen** und **Symbole**.
> - Sie können aus einfachen logischen **Schaltungen** eine **Wahrheitstabelle ableiten**.
> - Sie können eine logische Schaltung für einen Halbaddierer und einen Addierer mit den korrekten Symbolen zeichnen und nachvollziehen.
> 
> #### [Von-Neumann-Architektur](aufbau-02-vonneumann)
> - Sie wissen, was die Schritte des **Fetch-Decode-Execute-Zyklus** tun.
>  - Sie wissen, was folgende Teile der Von-Neumann-Architektur sind: **CPU, CU, ALU, Register (PC und ACC), RAM, Bus**
> - Sie können ein [einfaches Programm wie Bsp 1 im **LMC**](https://oinf.ch/interactive/little-man-computer/) verstehen oder schreiben.
> 
> #### [Hardwarekomponenten](aufbau-03-hwoverview) (falls besprochen)
> - Sie können die sechs besprochenen Komponenten in einem Desktopcomputer identifizieren
> - Sie können von den Komponenten die Kernfunktion und Kenngrösse sinngemäss zusammenfassen
 
## Übungsaufgaben zu [Intro](aufbau-00-intro)

Sie schreiben ein Programm, das Sie auf vielen Computern installieren möchten. Beantworten Sie mit wahr oder falsch: **Welche Information über die Computer brauchen Sie?**
- Was für einen Prozessor sie benutzen
- Der vorhandene Speicherplatz
- Das Betriebssystem

> [!solution]- Lösung
> 
> Sie müssen nur das Betriebssystem kennen, weil das Betriebssystem die Details der Hardware "web-abstrahiert".

Sortieren Sie Anwendungsprogramme, Anwender, Hardware und Betriebssystem nach Abstraktheit.

> [!solution]- Lösung
> 
> - Anwender (am abstraktesten)
> - Anwendungsprogramme
> - Betriebssystem
> - Hardware (am wenigsten abstrakt)

Füllen Sie ein: In der Informatik teilen wir Dinge gern in Module auf, um Ordnung im Kopf zu schaffen. Wenn wir ein Modul verwenden, können wir uns nämlich ausschliesslich auf die **???** des Moduls konzentrieren und die Details der **???** komplett  ignorieren.

> [!solution]- Lösung
> 
> Wenn wir ein Modul verwenden, können wir uns nämlich ausschliesslich auf die **Abstraktion/Schnittstelle** des Moduls konzentrieren und die Details der **Implementierung/Funktionsweise** komplett  ignorieren.

## Übungsaufgaben zu [Logikgates & Addierern](aufbau-01-addierer)

Ein OR-Gate habe zwei Inputs "A" und "B" sowie einen Output "out". Schreiben Sie die Wahrheitstabelle auf.

> [!solution]- Lösung
> 
> | A | B | out |
> | ----- | ----- | ------ |
> | 0     | 0     | 0      |
> | 0     | 1     | 1      |
> | 1     | 0     | 1      |
> | 1     | 1     | 1      |
> 

Schreiben Sie Wahrheitstabellen für diese Schaltungen

![[aufbau-04-prüfungsvorbereitung 2024-05-15 11.39.19.excalidraw]]

> [!solution]- Lösung mit Videoerklärung
> 
> Die Wahrheitstabelle:
> 
> | A | B | out |
> | ----- | ----- | ------ |
> | 0     | 0     | 0      |
> | 0     | 1     | 0      |
> | 1     | 0     | 1      |
> | 1     | 1     | 0      |
> 
> [Eine Videoerklärung finden Sie hier](https://kswe-my.sharepoint.com/:v:/g/personal/cha_kswe_ch/EWZB9ZwqY1RArXxD96ZAeF0B3fmknz41AAH7QdbZQIhy-A?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=ybDhhU) und hier eine Herleitung mit Farben:
> 
> ![[aufbau-04-prüfungsvorbereitung 2024-05-15 11.44.16.excalidraw]]

![[aufbau-04-prüfungsvorbereitung 2024-05-15 11.55.58.excalidraw]]

> [!solution]- Lösung mit Videoerklärung
> 
> Die Wahrheitstabelle:
> 
> | A | B | out |
> | ----- | ----- | ------ |
> | 0     | 0     | 0      |
> | 0     | 1     | 1      |
> | 1     | 0     | 0      |
> | 1     | 1     | 0      |
> 
> [Eine Videoerklärung finden Sie hier](https://kswe-my.sharepoint.com/:v:/g/personal/cha_kswe_ch/EfqvjtXz-99Bk6JXppP7LCoB6Toi02PPXPUwQ8JOJkteog?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=5b3jqL) und hier eine Herleitung mit Farben:
> 
> ![[aufbau-04-prüfungsvorbereitung 2024-05-15 12.00.22.excalidraw]]

![[aufbau-04-prüfungsvorbereitung 2024-05-15 12.50.15.excalidraw]]
> [!solution]- Lösung mit Videoerklärung
> 
> Die Wahrheitstabelle:
> 
> | A   | B   | C   | out |
> | --- | --- | --- | --- |
> | 0   | 0   | 0   | 0   |
> | 0   | 0   | 1   | 1   |
> | 0   | 1   | 0   | 1   |
> | 0   | 1   | 1   | 1   |
> | 1   | 0   | 0   | 1   |
> | 1   | 0   | 1   | 1   |
> | 1   | 1   | 0   | 0   |
> | 1   | 1   | 1   | 1   |
> 
> [Eine Videoerklärung finden Sie hier](https://kswe-my.sharepoint.com/:v:/g/personal/cha_kswe_ch/EXlpzcE_7-FHqbR4DDcCilsBtQ0gYKS4wLz-vwGOx4iybw?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=iPS0H2) und hier eine Herleitung mit Farben:
> 
> ![[aufbau-04-prüfungsvorbereitung 2024-05-15 12.07.28.excalidraw]]

Vervollständigen Sie: Ein Halbaddierer besteht aus (Anzahl) **???** Logikgates, nämlich einem **???** und einem **???**.

> [!solution]- Lösung
> 
> Ein Halbaddierer besteht aus **zwei** Gates, nämlich ein **AND** und ein **XOR**.

Na toll... Meine Katze hat wieder mit meinem Addierer gespielt und alle Verbindungen rausgerissen 😭 Helfen Sie mir bitte und zeichnen Sie die richtigen Verbindungen ein!

![[aufbau-04-prüfungsvorbereitung 2024-05-15 15.54.09.excalidraw]]
> [!solution]- Lösung
> 
> Zum Üben habe ich die Logikgates wieder schön arrangiert. 
> 
> ![[aufbau-04-prüfungsvorbereitung 2024-05-15 15.57.33.excalidraw]]

## Übungsaufgaben zur [Von-Neumann-Architektur](aufbau-02-vonneumann)

Benennen Sie folgende sechs Teile der Von-Neumann-Architektur.
![[aufbau-04-prüfungsvorbereitung 2024-05-15 16.10.32.excalidraw]]

> [!solution]- Lösung
> 
> 1. Control Unit (CU) oder Steuerwerk
> 2. Arithmetic Logic Unit (ALU)
> 3. Register
> 4. Program Counter (PC) oder Speicherzähler (auch Instructionpointer (IP) / Speicherzeiger wären ok)
> 5. Systembus
> 6. Arbeitsspeicher (RAM)

Im Speicherzähler des Prozessors befindet sich:
- ein Befehl
- eine Adresse
- ein Zwischenergebnis

> [!solution]- Lösung
> 
> Eine **Adresse** ist richtig

Im Fetch-Schritt des FDE-Zyklus wird von wo nach wo was transferiert?

> [!solution]- Lösung
> 
> Die aktuelle Adresse im Speicherzähler (PC) Register bestimmt, welche Speicherzelle im Arbeitsspeicher (RAM) gelesen wird. Der Inhalt dieser Speicherzelle wird in ein Register im Prozessor kopiert.

Sie haben einen kleinen Prozessor gebaut, der folgende Befehle und sogar negative Zahlen beherrscht. Wenn Sie nun das Programm rechts ausführen: Welcher Wert steht am Schluss im Akkumulator?

![[Pasted image 20240515163823.png]]
> [!solution]- Lösung
> 
> **505**. 
> 
> Falls Sie **-191** gesagt hätten: Dieser Wert wird ausgegeben. Aber das Programm lädt bei Speicherzelle 04 (Inhalt: 500) den Wert der Speicherzelle 00 in den Akkumulator, also 505.

Was müssten Sie bei folgendem Programm tun, damit die Zahlenreihe nicht bei 0 sondern bei 7 beginnt?

![[Pasted image 20240515164421.png]]
> [!solution]- Lösung
> 
> Den Inhalt der Speicherzellen 00 und 01 vertauschen.


## Übungsaufgaben zu [Hardwarekomponenten](aufbau-03-hwoverview) (falls besprochen)

Wie kann es sein, dass ein Prozessor trotz niedrigerer Taktfrequenz schneller ist, als einer mit einer höheren Taktfrequenz?

> [!solution]- Lösung
> 
> Wenn ein Prozessor mehre Prozessor**kerne** hat, kann er Operationen parallel durchführen. Der gesamte Prozessor kann so trotz niedrigerer Taktfrequenz insgesamt schneller sein.
> 
> Details zum Verständnis: Solche Prozessorkerne funktionieren, als hätten Sie mehrere Prozessoren in einem Computer, die parallel rechnen können (wenn die Programme dafür gemacht sind).

Wie heisst die Komponente, die alle anderen Komponenten mit Strom versorgt?

> [!solution]- Lösung
> 
> Das Netzteil

Die wichtigsten Komponenten (z.B. das RAM, die Grafikkarte) können über den Systembus direkt mit der CPU kommunizieren. Über welchen Verteiler auf dem Mainboard sind andere, weniger wichtige Komponenten angeschlossen?

> [!solution]- Lösung
> 
> Das Chipset.

Sie haben einen Arbeitsspeicher in der Hand. Wo würden Sie ihn auf diesem Mainboard einstecken?

![[aufbau-04-prüfungsvorbereitung 2024-05-28 00.05.49.excalidraw]]


> [!solution]- Lösung
> 
> ![[aufbau-04-prüfungsvorbereitung 2024-05-28 00.00.16.excalidraw]]
