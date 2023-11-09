![Python](https://img.shields.io/badge/python-v3.7-blue)
![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)
![Status](https://img.shields.io/badge/status-up-brightgreen)
## Abstract

Leukemia is one of the major harmful cancer diseases that confers mortality and morbidity in different age groups. The diagnostic challenge is caused by several factors, one of the main ones being the incorrect classification of disease subtypes. Therefore, it becomes essential to discover the genetic diseases that occurred that caused a certain disease. Consequently, the use of machine learning can be applied to solve problems related to leukemia. Considering this context, the objective of this paper is to develop data pipelines that allow the classification of multiclasses of leukemia using gene expression data. Therefore, we propose the use of different approaches and classifiers in order to determine optimized machine learning models with high accuracy. The models used have canonical and hierarchical approaches, in addition to using feature selection techniques for their training. Highly accurate results were obtained in experiments carried out compared to results obtained in the literature, making it possible to compare different approaches, techniques and feature selections.

## Authors

* Alvaro Pedroso Queiroz, Leonardo Canuto Junior, Ana Beatriz Miranda Valentin, Márcio Dorn, Glaucia Maria Bressan, Elisângela Aparecida da Silva Lizzi, Danilo Sipoli Sanches.

* **Correspondence:** alvaroq@alunos.utfpr.edu.br


## Publication

In process...

## List of files

 - **notebooks:** It has python notebooks to carry out experiments;
 - **results:** It has spreadsheets with experiment results;
 - **scripts:** It has important python scripts for carrying out experiments;

## Data
- **Raw datas:** https://drive.google.com/drive/folders/1CgQYvzoJApajpeBxjcKCm_rcJRIAXYQY?usp=sharing
- **Processed datas:** https://drive.google.com/drive/folders/1eYPaWGxCNYP_f-d5nUo_y-mpTSdBf-WW?usp=sharing
- **Variance Correlation Filter:** https://drive.google.com/drive/folders/1VxuIBD6bQigMFDvE8ZFvQYHVWR6HZBPx?usp=sharing


## GUI

The application that trains canonical and hierarchical models and seeks to find interpretability between the features used by the models is available for free at: https://huggingface.co/spaces/alvaropq/explainable_classification


The figure presents an example of the developed application.



It allows you to train a machine learning model in a canonical or hierarchical way using Decision Tree, Random Forest, SVM and AdaBoosting techniques and analyze the impact results of the features for class classification.

The sidebar presents the step-by-step guide for training the model, consisting of importing the data, then it is possible to train a model that can be downloaded and the impacts of the features in different visual forms can be analyzed in the next step. Finally, it is also possible to make inferences with the models that were developed in the application for unknown data, where graphical forms of explainability of the reasons for the models' decisions will be shown.

The application develops the concepts covered in this article and allows easy access to the application of machine learning models and feature analysis and model explainability through the SHapley Additive exPlanations (SHAP) method, which uses individual predictions based on Shapley values of game theory, identifying the contribution of each feature to the prediction.
