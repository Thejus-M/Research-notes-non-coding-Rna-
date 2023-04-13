#  Finding Coding RNA using Machine Learning

This repository contains the code and data for a project aimed at finding whether a given DNA sequence is coding RNA or non-coding RNA using machine learning models. The project uses various features of the DNA sequence to train the models

# Features
-  ORF length
-  protein coding potential
-  G-C content
-  K-mer periodicity
-  Minimal Free Energy
-  Transcript length
-  CpG islands
-  BLAST similarity
-  Conservation Score
-  Nucleotide Frequencies
-  Hexamer score  
-  Fickett Score  

# Dataset

The dataset used in this project contains both coding and non-coding RNA sequences. The sequences are in FASTA format and have been pre-processed to extract various features such as ORF length, protein coding potential, etc. The dataset is split into training and testing sets, with 80% of the data used for training and the remaining 20% used for testing.

# Models

The following machine learning models have been implemented for this project:

-    Logistic Regression
-    Support Vector Machine (SVM)
-    Naive Bayes
-    Random Forest

These models have been trained using the features extracted from the dataset and are used to predict whether a given DNA sequence is coding RNA or non-coding RNA.

# Requirements

To run the code in this repository, you will need:

-    Python 3.x
-    NumPy
-    Pandas
-    Scikit-learn
-    Matplotlib
-    Biopython

# Usage

To use the code in this repository, follow these steps:

 -   Clone the repository to your local machine.
 -   Install the required dependencies using pip.
 -   Use the trained models to predict whether a given DNA sequence is coding RNA or non-coding RNA.

# Conclusion

This project shows that machine learning models can be used to accurately classify DNA sequences as coding or non-coding RNA based on various features. The models implemented in this project can be further optimized and used in various biological applications, such as identifying potential drug targets and understanding gene expression.
