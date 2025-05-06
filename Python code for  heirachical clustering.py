# -*- coding: utf-8 -*-
"""
Created on Tue May  6 12:34:51 2025

@author: Samuel Kakraba 
"""

############ Python code to generate the dendrogram
import subprocess
import sys
import pkg_resources

# Function to check if a package is installed
def check_package(package_name):
    try:
        pkg_resources.get_distribution(package_name)
        return True
    except pkg_resources.DistributionNotFound:
        return False

# Function to install a package using pip
def install_package(package_name):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        print(f"{package_name} has been successfully installed.")
    except subprocess.CalledProcessError:
        print(f"Failed to install {package_name}. Please install it manually.")

# List of required packages
required_packages = ["pandas", "matplotlib", "scipy"]

# Check and install required packages if not present
for package in required_packages:
    if not check_package(package):
        print(f"{package} is not installed. Attempting to install it now...")
        install_package(package)

# Import required libraries after installation check
import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

# Load the data
file_path = 'covid_edgeinteraction.csv'
data = pd.read_csv(file_path)

# Transpose data for clustering (variants as rows)
data_t = data.T

# Perform hierarchical clustering using Euclidean distance and single linkage
linked = linkage(data_t, method='single', metric='euclidean')

# Define labels with mutated phenotypes
labels = [
    'N501Y (Alpha/Beta/Gamma/Omicron)',
    'L452R (Delta/Epsilon)',
    'E484A (Omicron)',
    'T478K (Delta/Omicron)',
    'K417N (Beta/Gamma)',
    'Wildtype (Reference)',
    'N440K (Immune escape)'
]

# Plot dendrogram with bold fonts for axis numbering and labels
plt.figure(figsize=(10, 6), dpi=300)
dendro = dendrogram(linked, labels=labels, orientation='top')
plt.ylabel('Distance (Euclidean)', fontsize=14, fontweight='bold')
plt.xlabel('Protein Variants (Mutated Phenotype)', fontsize=14, fontweight='bold')
plt.xticks(fontsize=12, fontweight='bold', rotation=30, ha='right')
plt.yticks(fontsize=12, fontweight='bold')
plt.tight_layout()
plt.show()
