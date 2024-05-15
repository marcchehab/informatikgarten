---
title: "00: Denkhilfe & Übersicht"
---
> [!success] Lernziele
> 
> - Sie können den Unterschied zwischen **Abstraktion** und **Implementierung** eines Moduls beschreiben.
> - Sie können Benutzer, Anwendungsprogramme, Betriebssystem und Hardware nach "Abstraktheit" sortieren und wissen, was mit "Abstraktheit" in diesem Kontext gemeint ist.
> - Sie können erklären, wieso es ein Betriebssystem als Schnittstelle zwischen Hardware und Anwenderprogrammen braucht.
## Abstraktion und Implementation von Modulen unterscheiden

> Sie fragen sich vielleicht, wie es möglich ist, ein komplettes Computersystem von Grund auf zu konstruieren, das mit nichts anderem als elementarsten Schaltkreisen beginnt. Das muss ein gigantisches Unterfangen sein! Wir gehen mit dieser Komplexität um, indem wir **das System in Module aufteilen**. Jedes Modul wird ... separat in einem eigenständigen Projekt aufgebaut. Sie werden sich vielleicht fragen, wie es möglich ist, diese Module isoliert zu beschreiben und zu bauen? Sie sind doch sicher miteinander verbunden! Wie wir ... zeigen werden, impliziert ein gutes modulares Design genau das: Sie können an den einzelnen Modulen unabhängig voneinander arbeiten, während Sie den Rest des Systems völlig ignorieren. Wenn das System gut konzipiert ist, können Sie diese Module in beliebiger Reihenfolge und sogar parallel zueinander aufbauen, wenn Sie im Team arbeiten.
> 
> Die kognitive Fähigkeit des "Divide & Conquer", also ein komplexes System in überschaubare Module aufzuteilen, wird durch einen weiteren kognitiven Kniff gestärkt: unsere **Fähigkeit, zwischen der Abstraktion und der Implementierung der einzelnen Module zu unterscheiden**. In der Informatik nehmen wir diese Worte konkret: Die Abstraktion \[oder Schnittstelle\] beschreibt, was das Modul tut, und die Implementierung beschreibt, wie es dies tut. Mit dieser Unterscheidung im Hinterkopf lautet die wichtigste Regel in der Systemtechnik: Wenn Sie ein Modul als Baustein verwenden - egal welches Modul -, sollten Sie sich ausschliesslich auf die Abstraktion des Moduls konzentrieren und die Implementierungsdetails völlig ignorieren.
> 
> *Nisan, N. & Schocken, S. (2005) The Elements of Computing Systems: Building a Modern Computer from First Principles*

In der Welt der Informatik werden abstrakte **Schnittstellen** standardisiert und vorgeschrieben - z.B. Stecker, Kommunikationsprotokolle, die Parameter einer Funktion, etc. Wie ein Modul dann diese Schnittstelle **implementiert**, ist meist freigestellt. Die konkrete Funktionsweise eines Moduls interessiert uns nur, wenn wir dieses Modul verstehen wollen - ansonsten reicht uns die Schnittstelle.

![[aufbau-00-intro 2024-04-29 22.05.17.excalidraw]]

> [!important] Merken Sie sich
> 
> Bei Modulen kann man ihre **Abstraktion** (oder Schnittstelle) von ihrer **Implementierung** (oder Funktionsweise) unterscheiden. Man nutzt sehr oft Module, ohne ihre Implementierung überhaupt zu kennen!

### Beispiel mit Code

Dazu folgendes Beispiel einer Funktion `multiplizieren`.

```turtle
def multiplizieren(a, b):
	resultat = 0
	for i in range(a):
		resultat = resultat + b
	print(resultat)

multiplizieren(3, 4)
```

> [!example] Kurze Diskussion zu zweit
> 
> 1. Ist die Funktion `multiplizieren` elegant implementiert worden? Könnten Sie das besser?
> 2. Was ändert sich durch Ihre Verbesserung auf Linie 7?

> [!solution]- Lösung
> 
> 1. Nein, überhaupt nicht. Die **Implementierung ist ineffizient und fehleranfällig** (z.B. bei negativen Nummern).
> 2. Nichts, solange sich **die Schnittstelle (der Funktionsname und die Parameter)** nicht ändern.

### Beispiele ohne Programmieren

> [!example] Jetzt sind Sie dran!
> 
> Überlegen Sie sich bei folgenden Beispielen, was für Sie die Abstraktion / Schnittstelle ist, was die Funktionsweise / Implementierung, und wie beide zusammenhängen.

![[Pasted image 20230807161447.png]]
> [!question]- Sie tauschen Ihren Computer-Prozessor (**CPU**) aus...
> 
> Sie können ihren Prozessor austauschen und, sofern der neue Prozessor eine kompatible Schnittstelle hat, läuft ihr problemlos Computer weiter! Dies, obwohl die Funktionsweise des neuen Prozessors eine andere ist: hoffentlich besser, schneller, oder effizienter.
> 
> **Abstraktion / Schnittstelle**: Das Format des "Steckers" (man spricht vom Sockel) und die Funktionen, die der Prozessor kann.
> 
> **Implementierung / Funktionsweise**: Wie der Prozessor  gebaut wurde und wie er funktioniert. Das ist teilweise ein Geschäftsgeheimnis der Hersteller.

![[Pasted image 20230807173548.png]]
> [!question]- Sie kreieren eine **Webseite**, die auf den gängigen Browsern richtig angezeigt werden soll.
>
>Sie nehmen einfach an, dass alle Ihre Besucher Geräte mit einem modernen Browser besitzen. 
>
>**Abstraktion / Schnittstelle**: Moderne Internet- und Webstandards (wie TCP/IP, HTTPS, HTML, CSS, Javascript, etc.)
>
>**Implementierung / Funktionsweise**: Wie der spezifische Browser oder die Geräte ihrer Benutzer funktionieren, können Sie gar nicht wissen und darf ihnen auch egal sein - das ist Sache der Benutzer.


![[Pasted image 20230807173846.png]]

> [!question]- Sie versenden eine **E-Mail** an eine unbekannte Adresse.
> 
> Hand aufs Herz: Wann haben Sie das letzte Mal darüber nachgedacht, wie Ihr E-Mail-Programm wohl funktioniert? 😅 Eben. Sie müssen das gar nicht wissen. Das Programm muss einfach die E-Mail-Standards korrekt implementieren und Sie müssen darauf vertrauen, dass das E-Mail-Programm des Empfängers dasselbe tut.
> 
> **Abstraktion / Schnittstelle**: Moderne Internet- und E-Mail-Standards (wie TCP/IP, SMTP, IMAP, POP...).
> 
> **Implementierung / Funktionsweise**: Wie Ihr E-Mail-Programm programmiert wurde. Das ist unter Umständen ebenfalls ein Geschäftsgeheimnis (e.g. Microsoft legt nicht offen, wie Outlook programmiert wurde).

🧑‍💻
> [!question]- Ein und dieselbe Anwendung wird auf Tausenden Computern installiert
> 
> Anwendungen sind meistens nicht von spezifischer Hardware abhängig, sondern sie nutzen einfach die Schnittstellen eines spezifischen Betriebsystems, das alle nötigen Funktionen aller verschiedenen Hardware-Komponenten mit standardisierten Schnittstellen  zur Verfügung stellen sollte.
> 
> **Abstraktion / Schnittstelle**: Standardisierte Schnittstellen des Betriebssystems.
> 
> **Implementierung / Funktionsweise**: Wie das Betriebsystem die Hardware mit Treibern bedient.

## Vereinfachte Übersicht

Dieses Denken in Modulen hilft uns nun, eine (simplifizierte) Übersicht eines jeden Computers zu wagen und auf den Begriff des Betriebssystems einzugehen.

![[aufbau-01-os 2024-04-22 00.00.53.excalidraw]]

Wenn wir das radikal vereinfachen, können wir uns diese vier Module als Bauteile überlegen, die aufeinander aufbauen - und sehen: Aha, das ist ja wieder ein **Schichtmodell**!

![[aufbau-00-intro 2024-04-22 06.42.20.excalidraw]]

## Was macht das Betriebssystem?

Das Betriebssystem (z.B. Windows , MacOS oder eine der vielen Linux-Varianten) ist selbst eine Software - man kann es auf einen USB-Stick speichern oder aus dem Internet herunterladen und auf verschiedenen Computern installieren - aber es hat sehr spezielle Aufgaben: in der Hauptsache ist das Betriebssystem **dafür zuständig, dass andere Programme die Hardware des Computers über standardisierte Schnittstellen auf geordnete Weise benutzen können**. 


> [!example] Ein Beispiel: Word speichert eine Datei
> 
> Ein normales Anwendungsprogramm wie Word **speichert eine Datei nicht selbst** auf der Festplatte, sondern es nutzt die **Schnittstelle des Betriebssystems**, um das zu tun. So kann das Betriebssystem die Ordnung wahren: Stellen Sie sich nur einmal das Chaos vor, wenn alle Programme der Welt wann und wie auch immer auf Ihre Festplatte schreiben könnten - totales Chaos! Das wäre so desorganisiert wie Schlangen im Coop 🤷 Das Betriebssystem überwacht und verhindert, dass sich die Programme beim Laden oder Speichern in die Quere kommen.
> 
> Das hat einen weiteren Vorteil: Normale Anwendungsprogramme müssen gar nicht wissen, was für ein Speicher in Ihrem Computer eingebaut ist - oder was für ein Prozessor, Arbeitsspeicher, oder Bildschirm. Sie schreiben ein Programm für die Schnittstellen des Betriebssystems und müssen sich nicht um alle möglichen Hardwarekombinationen kümmern.
> 
> Diese komplizierte Arbeit wird also vom Betriebssystem übernommen und "gegen oben" (im Schichtmodell) bietet es einheitliche Schnittstellen an. Informatiker würden dazu sagen: **Die Hardware wird vom Betriebssystem "weg-abstrahiert"**. 
> 
> Um mit allen möglichen Hardwarekomponenten kommunizieren zu können, nutzen Betriebssysteme sogenannte **Treiber** (Englisch: driver). Meistens installieren sie diese automatisch, wenn ein neues Gerät erkannt wird (das nennt man "plug & play"). 

Diese Kernfunktion sehen Sie in vielen Aufgaben, die das Betriebssystem übernimmt: 
- Speicherverwaltung: Es organisiert und verwaltet Speichermedien wie RAM und Festplatte, und bietet geordneten Schreib- und Lesezugriff.
- Prozessverwaltung: Es regelt den Zugriff von Programmen auf den Prozessor (Central Processing Unit, CPU) und andere Ressourcen, sodass die Hardware optimal ausgelastet ist.
- Netzwerkkommunikation: Es organisiert den Datenaustausch, implementiert die TCP/IP-Schichten und bietet Programmen eine Schnittstelle dazu.
- Anwendungsverwaltung: Es installiert, startet, beendet und verwaltet Anwendungsprogramme.
- Benutzerverwaltung: Es verwaltet Benutzer und deren Rechte.
- Systemstart und -herunterfahren: Es startet und beendet den Betrieb des Computers.
- Hardware- und Ressourcensteuerung: Es verwaltet alle Hardwarekomponenten, Peripheriegeräte und Systemressourcen, und bietet Zugriff darauf.
- GUI-Bereitstellung (optional): Es stellt eine grafische Benutzeroberfläche bereit, über die der Benutzer mit dem Computer interagieren kann.

