#Dataset Description: Edge Weights of SARS-CoV-2 Spike RBD Protein Phenotypes#

This dataset contains edge interaction weights for various phenotypes of the SARS-CoV-2 Spike Receptor-Binding Domain (RBD), specifically focusing on the wildtype and several key mutations: K417N, N440K, L452R, T478K, N501Y, and E484A. The data represents interaction strengths or weights across 50 different observations for each phenotype, providing insights into the structural or functional impacts of these mutations on the Spike protein's behavior.

The dataset is structured as a CSV file with columns corresponding to the wildtype and each mutant variant, where each row captures a set of edge weight values. Summary statistics reveal a mean edge weight of approximately 0.092 across all phenotypes, with values ranging from a minimum of 0.00244 (in N440K) to a maximum of 0.24808, indicating significant variability in interaction strengths.

This dataset can be used for analyses such as hierarchical clustering to explore relationships between different mutations and their impact on protein interactions. It is ideal for researchers studying the molecular dynamics of SARS-CoV-2 variants and their potential effects on binding affinity or immune evasion. The accompanying Python code for hierarchical clustering is also available for further data exploration and visualization.
