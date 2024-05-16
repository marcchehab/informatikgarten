---
title: "02: Von Neumann Architektur"
---
> [!success] Lernziele
> 
> - Sie wissen, was die Schritte des **Fetch-Decode-Execute-Zyklus** tun.
>  - Sie wissen, was folgende Teile der Von-Neumann-Architektur sind: **CPU, CU, ALU, Register (PC und ACC), RAM, Bus**
> - Sie können ein [einfaches Programm wie Bsp 1 im **LMC**](https://oinf.ch/interactive/little-man-computer/) verstehen oder schreiben.

1945 wurden in den USA und Europa an verschiedenen Universitäten Rechenmaschinen gebaut. Das Mathegenie John von Neumann fasste seine Arbeit am EDVAC-Computer in einem Bericht zusammen, in dem er die Kernprinzipien und die Organisation der Komponenten erklärte und beschrieb. Diese Grundprinzipien sind bis heute **die Basis der meisten Allzweckcomputer**.

![[aufbau-02-vonneumann 2024-04-30 08.08.56.excalidraw]]

Ich habe Ihnen im violetten Teil eine moderne Input- und Output-Infrastruktur angehängt. In dieser Lektion ist aber nur der obere Teil wichtig: die klassische **Von-Neumann-Architektur**.

Konzentrieren wir uns zuerst auf den Ablauf:
- Die Control Unit (CU) steuert den Prozess: Anweisungen werden **nacheinander über einen Bus aus dem Speicher geholt (fetch), dekodiert (decode) und ausgeführt (execute)**.
- Daten und Befehle werden **beide zusammen** und **binär** im selben Speicher (RAM) gespeichert
- Der Zyklus setzt sich automatisch fort bis zu einer **Stopp-Anweisung**

Um das zu bewerkstelligen, definiert die Von-Neumann-Architektur **vier Hauptteilen**:
1. **Control Unit, CU**: Koordiniert den Ablauf, wie oben beschrieben.
2. **Arithmetisch-logische Einheit (ALU)**: Führt alle Rechen- und Logikoperationen aus. Hier befindet sich der Addierer, den wir [[aufbau-01-addierer|in der Lektion dazu]] bauen.
3. **Arbeitsspeicher (RAM)**: Speichert Daten **und** Befehle. 
4. **Input/Output (I/O)**: Verbindet diesen Kern des Computers mit anderen Geräten wie Massenspeicher (SSD, Festplatten), Grafikkarten, USB-Geräte und Peripheriegeräte.

## LMC-Simulator
https://oinf.ch/interactive/little-man-computer/

1. Führen Sie das Beispielprogramm mehrfach aus und versuchen Sie es mit der Befehlsliste nachzuvollziehen.
	- Laden und Ausführen des Beispiels: Auf Bsp 1 klicken; mit «übertragen» in den Speicher laden; in «Eingabe» zwei Werte untereinander schreiben; mit Play starten.) 
2. Schreiben Sie dann entsprechende Programme für die nachfolgenden Aufgaben.

### Aufgaben
1. **Substrahieren** Sie zwei Inputwerte und geben Sie das Ergebnis aus
2. Addieren Sie einen Inputwert **unendlich lange zu sich selbst**, e.g. (Input 3 => 3, 6, 9, 12,...)
3. Entwickeln Sie ein Programm, das zwei Inputwerte **multipliziert**, dann das Ergebnis ausgibt und stoppt. 
4. Entwickeln Sie ein Programm, das die zwei Inputwerte vergleicht, dann das Ergebnis (1 für gleich, 0 für ungleich) ausgibt und stoppt. 
5. Entwickeln Sie ein Programm, das die zwei subtrahiert, wenn sie nicht gleich sind, ansonsten addiert, dann das Ergebnis ausgibt und stoppt. 
6. Entwickeln Sie ein Programm, das (in Zweierschritten) vom ersten Input bis zum zweiten zählt (jeweils ausgeben) und dann stoppt. 
7. Entwickeln Sie ein Programm, das alle ganzen Zahlen von 0 bis 100 zusammenzählt, dann das Ergebnis ausgibt und stoppt.

## Zusatzinfo: Programmiersprachen von Bits zu Python

Der Little Man Computer (LMC) ist ein idealisiertes Modell eines Computers, das zum Lernen der grundlegenden Mechanismen der Computerprogrammierung genutzt wird. Hier ist eine kurze Erklärung, wie Binärcode zu Assembler und weiter zu höheren Programmiersprachen verarbeitet wird:

![[aufbau-02-vonneumann 2024-05-13 08.27.30.excalidraw]]

**Binärcode**: Der grundlegendste Code, den ein Computer verstehen kann, ist Binärcode – eine Folge von Nullen und Einsen. Diese repräsentieren direkt die Maschinenbefehle, die der Prozessor ausführt. Im Kontext des LMC umfasst dies einfache Befehle wie Laden, Speichern, Addieren, Subtrahieren, Springen, wenn Null, und so weiter.

**Assembler**: Assemblersprache ist eine etwas benutzerfreundlichere Darstellung des Binärcodes. Jeder Maschinenbefehl im Binärcode hat ein Äquivalent in der Assemblersprache, das durch mnemonische Codes (wie LDA für "load", STA für "store") dargestellt wird. Ein Assembler ist ein Programm, das diese mnemonischen Codes in Binärcode übersetzt, den der Computer direkt ausführen kann. Dieser Schritt macht den Code menschenlesbarer, bleibt aber sehr hardwarenah.

**Höhere Programmiersprachen (C-Familie)**: Sprachen wie C sind weiter von der Maschinensprache entfernt und bieten Konstrukte wie Funktionen, Kontrollstrukturen (if-else, Schleifen) und komplexe Datentypen, die das Programmieren erleichtern. Ein Compiler übersetzt den in einer solchen höheren Sprache geschriebenen Code in Assembler oder direkt in Binärcode. Der Code in C und ähnlichen Sprachen ist effizient und ermöglicht eine präzise Kontrolle über die Hardware, was in systemnaher Programmierung nützlich ist.

**Noch höhere Programmiersprachen (Python)**: Python ist eine hochgradig abstrakte Sprache, die viele komplexe Funktionen in einfache Befehle kapselt. Python-Programme sind einfacher zu schreiben und zu lesen als C-Programme, jedoch wird ein Interpreter benötigt, der Python-Code zur Laufzeit in Maschinenbefehle umsetzt. Für zusätzliche Effizienz kann Python-Code auch in C-Code übersetzt und dann kompiliert werden, um eine nähere Maschinensteuerung zu ermöglichen.

Diese Übersetzung von niedrigeren zu höheren Ebenen der Programmiersprachen erleichtert das Programmieren erheblich, da sie Entwicklern erlaubt, sich auf die Logik und Funktionen ihrer Programme zu konzentrieren, anstatt auf die spezifische Hardware-Steuerung.