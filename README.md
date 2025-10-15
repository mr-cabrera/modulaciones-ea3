# Modulación Digital y Simulaciones en GNU Radio

Este repositorio contiene **simulaciones y proyectos en GNU Radio** orientados al estudio práctico de distintas **técnicas de modulación digital**, incluyendo transmisiones y recepciones implementadas con **SDR Pluto**.  

El objetivo principal es comprender y visualizar el comportamiento de las modulaciones más comunes en sistemas de comunicación digital, evaluando su desempeño en términos de **eficiencia espectral, robustez frente al ruido** y **complejidad de implementación**.

---

## 📘 Fundamentos Teóricos

A continuación se presenta un resumen de las principales modulaciones incluidas en el proyecto:

### 🔹 Frequency Shift Keying (FSK)
La información se transmite variando la **frecuencia** de la portadora entre dos o más valores discretos.  
- **Ventajas:** simple implementación, buena inmunidad al ruido de amplitud.  
- **Desventajas:** bajo aprovechamiento espectral.  
- **Aplicaciones:** Bluetooth clásico, RFID, telemetría.

### 🔹 Phase Shift Keying (PSK)
Los bits se codifican mediante variaciones discretas de la **fase** de la portadora.  
- **Ventajas:** buena eficiencia espectral.  
- **Desventajas:** requiere sincronización precisa de fase.  
- **Aplicaciones:** comunicaciones satelitales, Wi-Fi, LTE.

### 🔹 Binary Phase Shift Keying (BPSK)
Versión binaria de PSK con dos fases (0° y 180°).  
- **Ventajas:** alta robustez frente al ruido.  
- **Desventajas:** transmite solo 1 bit por símbolo.  
- **Aplicaciones:** GPS, enlaces satelitales, sistemas militares.

### 🔹 Quadrature Phase Shift Keying (QPSK)
Extiende BPSK usando cuatro fases (0°, 90°, 180°, 270°), codificando 2 bits por símbolo.  
- **Ventajas:** duplica la eficiencia espectral respecto a BPSK.  
- **Desventajas:** requiere sincronización coherente.  
- **Aplicaciones:** Wi-Fi, LTE, DVB-S, GPS.

### 🔹 Quadrature Amplitude Modulation (QAM)
Combina modulación en **fase y amplitud** para aumentar la densidad de información.  
- **Ventajas:** alta eficiencia espectral.  
- **Desventajas:** sensible al ruido y distorsión no lineal.  
- **Aplicaciones:** Wi-Fi, 5G, DOCSIS, TV digital.

### 🔹 16-QAM
Caso específico de QAM con 16 símbolos (4 bits por símbolo).  
- **Ventajas:** excelente balance entre capacidad y eficiencia.  
- **Desventajas:** requiere alta SNR para bajo BER.  
- **Aplicaciones:** LTE, 5G, módems de banda ancha.

---

## 🧩 Contenido del Repositorio

- **/simulaciones/** → Flujos de GNU Radio para cada técnica de modulación.  
- **/proyectos_sdr/** → Implementaciones prácticas con SDR Pluto (transmisión y recepción).  


## 👤 Autores

**5to Electronica**  
Proyecto académico y experimental sobre **modulación digital con GNU Radio y SDR Pluto**.  
