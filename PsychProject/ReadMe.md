# Psychoanalytic Ontology Project

The purpose of this project is to craft an ontology that can model data from a ficticious survey of 150 psychoanalytic patients.

## Description

I began by prompting Google's Bard with creating a fictional dataset of 150 psychotherapy patients. Then, I used the Pandas library to find and correlations or patterns in the data. Currently, I'm crafting an ontology to model the data, called Psy_Core.ttl, and soon I will write SHACL shapes to validate new data future (ficticious) researchers might model.

## File Guide

### 1. PsychoAnalysis.py

This is the core data analytic file where I used various Python libraries to find patterns in the dataset.

### 2. PsychData.csv and AlterPsychData.csv

These are two files containing 150 lines of patient data each. After getting the first dataset from Bard (PsychData.csv), I wanted more quantitative measures, so I prompted Bard again to get a second dataset, and in my python file (PsychoAnalysis.py) I stitched the two together.

### 3. Psy_Core.ttl

This is my core ontology that models the data. It's build out of the Mental Functioning Ontology (MFO) and its extension, the Mental Disease Ontology (MD). Soon, I will add portions from the Symptom Ontology and the Information Entity Ontology to capture more terms from the data.

### 4. Psychoanalytic_Ontology_Project.pdf

This document outlines the steps I tool while analyzing the data, curating an ontology to model it, crafting SHACL shapes and SPARQL queries, and my thought process along the way.
