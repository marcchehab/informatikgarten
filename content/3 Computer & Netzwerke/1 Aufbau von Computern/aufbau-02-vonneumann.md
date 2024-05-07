---
title: "02: Von Neumann Architektur"
---
1945 wurden in den USA und Europa an verschiedenen Universitäten Rechenmaschinen gebaut. Das Mathegenie John von Neumann fasste seine Arbeit am EDVAC-Computer in einem Bericht zusammen, in dem er die Kernprinzipien und die Organisation der Komponenten erklärte und beschrieb. Diese Grundprinzipien sind bis heute die Basis der meisten Allzweckcomputer.

- Daten und Befehle werden beide binär im Primärspeicher gespeichert
- Anweisungen werden nacheinander und in Reihenfolge (seriell) aus dem Speicher geholt
- Der Prozessor dekodiert und führt einen Befehl nach dem anderen aus
- Der Zyklus setzt sich fort, bis keine weiteren Anweisungen mehr verfügbar sind

Die "Von-Neumann-Architektur" besteht im Wesentlichen aus **vier Hauptteilen**:

1. **Steuerwerk (Control Unit, CU)**: Das Steuerwerk koordiniert die Aktivitäten des Computers. Es holt Befehle aus dem Speicher, entschlüsselt sie und gibt dann die Befehle an die ALU und andere Teile des Systems weiter, um sie auszuführen.
2. **Arithmetisch-logische Einheit (ALU)**: Sie führt alle Rechen- und Logikoperationen aus. 
3. **Speicher (Memory)**: Speichert Daten und Befehle. In der Von-Neumann-Architektur gibt es keinen Unterschied zwischen Daten- und Befehlsspeicher, was bedeutet, dass Programme und die von ihnen verarbeiteten Daten im selben Speicherbereich liegen.
4. **Ein-/Ausgabe (I/O)**: Verbindet den Computer mit der Aussenwelt, indem es Interaktionen mit Eingabe- und Ausgabegeräten wie Tastaturen, Mäusen und Bildschirmen ermöglicht.



![[aufbau-02-vonneumann 2024-04-30 08.08.56.excalidraw]]

### Zusammenhang zwischen der ALU und der Von-Neumann-Architektur

Die ALU ist ein zentraler Bestandteil der Von-Neumann-Architektur. Alle arithmetischen und logischen Berechnungen, die für die Ausführung von Programmen notwendig sind, werden in der ALU durchgeführt. Der Addierer in der ALU ist dabei das Basismodul für arithmetische Berechnungen. Die Fähigkeit der ALU, komplexe Berechnungen durchzuführen, ermöglicht es dem Computer, vielfältige Aufgaben effizient zu bearbeiten.

Die Integration der ALU in diese Architektur stellt sicher, dass der Computer in der Lage ist, eine breite Palette von Instruktionen zu verarbeiten, was für die Flexibilität und Leistungsfähigkeit moderner Computer essentiell ist. Somit ist der Addierer, als elementarer Bestandteil der ALU, fundamental für die gesamte Computerarchitektur nach Von Neumann.

Durch den Verständnis des Addierers und seiner Funktion innerhalb der ALU kannst du besser nachvollziehen, wie grundlegende mathematische Operationen von Computern durchgeführt werden und wie diese Operationen in grösseren Berechnungen und Prozessen integriert sind.


## Simulator
https://oinf.ch/interactive/little-man-computer/

1. Führen Sie das Beispielprogramm mehrfach aus und versuchen Sie es mit der Befehlsliste nachzuvollziehen.
	- Laden und Ausführen des Beispiels: Auf Bsp 1 klicken; mit «übertragen» in den Speicher laden; in «Eingabe» zwei Werte untereinander schreiben; mit Play starten.) 
2. Schreiben Sie dann entsprechende Programme für die nachfolgenden Aufgaben.

### Aufgaben
1. Entwickeln Sie ein Programm, das die zwei Inputwerte subtrahiert, dann das Ergebnis ausgibt und stoppt. 
2. Entwickeln Sie ein Programm, das die zwei Inputwerte multipliziert, dann das Ergebnis ausgibt und stoppt. 
3. Entwickeln Sie ein Programm, das die zwei Inputwerte vergleicht, dann das Ergebnis (1 für gleich, 0 für ungleich) ausgibt und stoppt. 
4. Entwickeln Sie ein Programm, das die zwei subtrahiert, wenn sie nicht gleich sind, ansonsten addiert, dann das Ergebnis ausgibt und stoppt. 
5. Entwickeln Sie ein Programm, das (in Zweierschritten) vom ersten Input bis zum zweiten zählt (jeweils ausgeben) und dann stoppt. 
6. Entwickeln Sie ein Programm, das alle ganzen Zahlen von 0 bis 100 zusammenzählt, dann das Ergebnis ausgibt und stoppt.

## Programmiersprachen

Der Little Man Computer (LMC) ist ein idealisiertes Modell eines Computers, das zum Lernen der grundlegenden Mechanismen der Computerprogrammierung genutzt wird. Hier ist eine kurze Erklärung, wie Binärcode zu Assembler und weiter zu höheren Programmiersprachen verarbeitet wird:

**Binärcode**: Der grundlegendste Code, den ein Computer verstehen kann, ist Binärcode – eine Folge von Nullen und Einsen. Diese repräsentieren direkt die Maschinenbefehle, die der Prozessor ausführt. Im Kontext des LMC umfasst dies einfache Befehle wie Laden, Speichern, Addieren, Subtrahieren, Springen, wenn Null, und so weiter.

**Assembler**: Assemblersprache ist eine etwas benutzerfreundlichere Darstellung des Binärcodes. Jeder Maschinenbefehl im Binärcode hat ein Äquivalent in der Assemblersprache, das durch mnemonische Codes (wie LDA für "load", STA für "store") dargestellt wird. Ein Assembler ist ein Programm, das diese mnemonischen Codes in Binärcode übersetzt, den der Computer direkt ausführen kann. Dieser Schritt macht den Code menschenlesbarer, bleibt aber sehr hardwarenah.

**Höhere Programmiersprachen (C-Familie)**: Sprachen wie C sind weiter von der Maschinensprache entfernt und bieten Konstrukte wie Funktionen, Kontrollstrukturen (if-else, Schleifen) und komplexe Datentypen, die das Programmieren erleichtern. Ein Compiler übersetzt den in einer solchen höheren Sprache geschriebenen Code in Assembler oder direkt in Binärcode. Der Code in C und ähnlichen Sprachen ist effizient und ermöglicht eine präzise Kontrolle über die Hardware, was in systemnaher Programmierung nützlich ist.

**Noch höhere Programmiersprachen (Python)**: Python ist eine hochgradig abstrakte Sprache, die viele komplexe Funktionen in einfache Befehle kapselt. Python-Programme sind einfacher zu schreiben und zu lesen als C-Programme, jedoch wird ein Interpreter benötigt, der Python-Code zur Laufzeit in Maschinenbefehle umsetzt. Für zusätzliche Effizienz kann Python-Code auch in C-Code übersetzt und dann kompiliert werden, um eine nähere Maschinensteuerung zu ermöglichen.

Diese Übersetzung von niedrigeren zu höheren Ebenen der Programmiersprachen erleichtert das Programmieren erheblich, da sie Entwicklern erlaubt, sich auf die Logik und Funktionen ihrer Programme zu konzentrieren, anstatt auf die spezifische Hardware-Steuerung.