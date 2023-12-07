# Portfolio

Welcome to my portfolio! I am an ontologist working for CUBRC Inc, developing BFO-CCO ontologies. I received a Master's degree from the University at Buffalo in spring 2023, where I studied the philosophy of applied ontology with Dr. Barry Smith and Dr. John Beverly.

In this repository, you can find projects I have built to demonstrate my skills with Python, Protege, SHACL, SPARQL, and other data/ontology development tools. My other repositories include my work on the extensions to the CCO [Common Core Extensions](https://github.com/cameronmore/CCOExtensions), the Mental Functioning Ontology (MFO), and a Psychoanalysis Data Project. Below, I describe the files that can be found in this personal portfolio.

## File Guide

### 1. Psychology Project

In my latest project, I am developing an ontology for a set of ficticious data gathered from psychoanalytic patients. First, I have already merged two files (generated by Google's LLM Bard), then I will use various Python libraries (including Pandas and Matplotlib) to visualize and try to find patterns in it. Next, I will populate a small ontology (based on the Mental Functioning Ontology) with the data instances. Finally, I will set up set of SHACL shapes to validate new data that future (fictitious) researchers may want to add to the ontology. My main file is titled 'PsychoAnalysis.py'.

### 2. UsefulRDFLibFunctions.py

A few useful RDFLib functions in Python, including grabbing all definitions and elucidations and putting them in a list, and a find and replace function.

### 3. ROBOT GUI

I created a simple graphical user interface for using ROBOT, the command line ontology tool. It has a few commands hard-coded, so people who only need one or two commands can use it and avoid having to work at the command line. It relies of PySimpleGUI, and I will be adding more hard-coded ROBOT command options.

### 4. Zebra Puzzle (Protege and Owl)

The Zebra Puzzle is a logical puzzle, supposedly invented by Albert Einstein. From a series of clues, one is able to infer the location of a zebra among five distinctly colored houses. Each house has its own occupant, pet, cigarette brand, and drink. To solve the puzzle, I built an ontology that describes the classes of things (occupants, houses, colors, etc), and asserted the relationships between the classes (all occupants occupy houses) and the particular relations (the clues below). By running a reasoner on the ontology, we can infer the location of the zebra. The Owl file can be found in this repo. I have listed the clues below:

```
1. The Englishman lives in the Red house.
2. The Spaniard owns the Dog.
3. Coffee is drunk in the Green house.
4. The Ukrainian drinks Tea.
5. The Green house is immediately to the right of the Ivory house.
6. The Old Gold smoker owns Snails.
7. Kools are smoked in the Yellow house.
8. Milk is drunk in the middle house.
9. The Norwegian lives in the first house.
10. The man who smokes Chesterfields lives in the house next to the man with the Fox.
11. Kools are smoked in the house next to the house where the Horse is kept.
12. The Lucky Strike smoker drinks Orange juice.
13. The Japanese smokes Parliaments.
14. The Norwegian lives next to the Blue house.
```

### 5. Neural Network Linear Regression (PyTorch)

Although there are much better functions out there to generate linear regression algorithms, I tried my hand at making one using PyTorch.

### 6. Unconscious Extension of the Mental Functioning Ontology (Ontology Engineering)

I have attached a copy of a paper that outlines a possible extension project for the Mental Functioning Ontology that captures unconscious data and returns disease-course models and up-to-date research articles for queries.

### 7. Soccer Visualization (Data Visualization)

As a part of a UDemy course I took to learn Python a few months ago, I did some simple visualization of data from the soccer video game Fifa. I found the most undervalues player by taking the players' value and subtracting it from their wages, which involved turning those two columns into integers. I then plotted it on a graph. I have attached the dataset in this portfolio.

### 8. Iris Machine Learning (Simple SciKit-learn Algorithm)

A small project I did while taking a Python UDemy course; a simple species prediction algorithm with the Iris dataset.

### 9. Wyrdl! (Python)

I wrote a simple Python Wordle copy.
