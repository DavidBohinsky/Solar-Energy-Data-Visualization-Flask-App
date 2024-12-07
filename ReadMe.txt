
Solar Energy Data Visualization Flask App

Description
This is a Flask web application that raise solar energy data based on user-inputted coordinates (latitude and longitude).
It visualizes the data using Plotly and provides a monthly output graph of solar power production in kWh/h.

Features
Input geographical coordinates (latitude and longitude).
Raises solar energy production data via the NREL PVWatts API.
Visualize the monthly solar power output using an interactive bar graph.
Handle incorrect input gracefully with error messages.

Technologies Used
Flask: Web framework for handling routes and rendering templates.
Requests: To make API calls to the NREL PVWatts service.
Plotly: For data visualization and creating graphs.
HTML Templates: For rendering the frontend (template must be placed in the templates folder).

***************************************************************************************************
---------------------------------------------------------------------------------------------------
***************************************************************************************************


Názov Projektu
Webová aplikácia na vizualizáciu solárnych dát pomocou Flask-u

Popis
Toto je webová aplikácia postavená na webovom framerworku -Flask, ktorá načítava dáta o produkcii solárnej energie na 
základe súradníc zadaných používateľom (zemepisná šírka a dĺžka). Dáta sú vizualizované pomocou Plotly a zobrazené
vo forme grafu mesačnej produkcie elektrickej energie v kWh/h.

Funkcie
Zadanie zemepisných súradníc (zemepisná šírka a dĺžka).
Získavanie dát o produkcii solárnej energie cez NREL PVWatts API. (NREL - National Renewable Energy Laboratory , USA)
Interaktívna vizualizácia mesačnej produkcie elektrickej energie pomocou grafu.
Ošetrenie nesprávnych vstupov s chybovými hláškami.

Použité Technológie
Flask: Webový framework a renderovanie šablón.
Requests: Na volanie API služby NREL PVWatts.
Plotly: Na vizualizáciu dát a vytváranie grafov.
HTML Šablóny: Pre zobrazenie frontendovej časti (šablóna musí byť uložená v priečinku templates).

, či máte súbor templates.html v priečinku templates.