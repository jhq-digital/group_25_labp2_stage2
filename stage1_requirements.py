# -*- coding: utf-8 -*-
"""
# A1. INF2008 Group Project (Stage 1)

## Project description
The objective of this project is to provide students with hands-on experience in developing a machine learning application, with emphasis on applying the CRISP-DM methodology in a structured and disciplined manner. Through this project, students are expected to integrate concepts learned in class across the full CRISP-DM workflow, including problem formulation, data understanding, data preparation, baseline modelling, and evaluation.

Each group is given the flexibility to define its own problem and select an appropriate dataset, subject to the scope and constraints specified for the project stage. The focus of the project is not on maximising model performance, but on demonstrating sound analytical reasoning, technical correctness, and alignment with the CRISP-DM process.

## Problem statement and data collection
At this stage, groups are required to translate the project objective into a concrete and defensible problem formulation, following the CRISP-DM Business Understanding and Data Understanding phases.

Specifically, groups must demonstrate:
- Business Understanding: a clearly articulated problem objective, including what is being predicted or analysed, why it matters, and how the output would be used in a decision or analysis context.
- Data Understanding: identification of the data source(s), an initial assessment of data suitability, and clarity on what the data represents and does not represent.
- Analytical Framing: explicit definition of the target variable and the corresponding task type (e.g. classification or regression), together with any assumptions or constraints implied by this formulation.

By the end of this stage, each group should have a clear project plan that demonstrates alignment between problem intent, data characteristics, and the CRISP-DM workflow, rather than a list of isolated choices.

## Stage 1 covers CRISP-DM Phases 1–5:
Stage 1 focuses on analytical framing, data validation, and baseline feasibility, rather than performance optimisation. Students are expected to demonstrate correct application of the CRISP-DM methodology and sound technical judgement.

Stage 1 includes the following CRISP-DM phases, applied at a baseline level:
- Business Understanding: defining the problem, decision context, assumptions, risks, and success metrics
- Data Understanding: examining data sources, target definition, task type, and data limitations
- Data Preparation (minimal): basic cleaning and splitting only; feature engineering and advanced transformations are not permitted
- Baseline Modelling (default settings only): simple classical models used to establish a reference point, without tuning or optimisation
- Initial Evaluation: evaluation of baseline results to assess feasibility, limitations, and next-step decisions

Completion of Stage 1 should result in a plan for the next steps for the project.

## Hard Constraints (Stage 1)

To ensure methodological consistency and fairness across all groups, the following constraints apply strictly to Stage 1 of the project.

Allowed (Stage 1)
- Basic data cleaning (e.g. handling missing values, removing duplicates)
- Basic encoding of categorical variables
- Train/test data splitting
- Baseline machine learning models using default parameter settings only
- Feature extraction or feature engineering beyond basic encoding

Not Allowed (Stage 1)
- Hyperparameter tuning (e.g. grid search, random search)
- Dimensionality reduction techniques (e.g. PCA)
- Deep learning models
- Model ensembling

These restrictions are intentional and are designed to keep the focus on CRISP-DM discipline, analytical framing, and baseline feasibility, rather than performance optimisation.

## Deliverables

The deadline for Stage 1 submission is 23:59 on 13 February 2026.

Each group is required to submit a single slide report in PDF format, converted from PowerPoint.

## Suggested slide mapping (for your 10-slide deck)
The following slide mapping is recommended to help teams structure their presentation in alignment with CRISP-DM Stage 1. Teams may adapt the structure where appropriate, provided that all required CRISP-DM components are clearly and coherently addressed.

- Slide 1: Title, team members, roles, and link to Colab notebook / github.
- Slide 2: Business Understanding (problem objective, decision context, success criteria)
- Slide 3: Data Understanding (dataset overview and target definition)
- Slide 4: Data Understanding (data quality, assumptions, risks, and potential leakage)
- Slide 5: Data Preparation (minimal) (cleaning, encoding, train/test split)
- Slide 6: Baseline Modelling (dummy baseline and 1–2 classical models, default settings only)
- Slide 7: Results (baseline comparison table)
- Slide 8: Initial Evaluation (sanity checks, interpretation)
- Slide 9: Next Steps (plans for Stage 2)
- Slide 10: References, tools used, and links (handled according to course instructions)
- Slide 11: Individual Contributions. Please ensure that all team members’ names and student IDs are clearly listed on this slide. Each member must specify their own individual contributions (not group-level tasks). Individual contributions will be assessed as part of the grading. Team members without clear or substantive individual contributions may receive a significant reduction in marks.

## What Stage 1 explicitly does NOT do
Stage 1 focuses on establishing problem feasibility and analytical correctness using the early phases of the CRISP-DM methodology. To maintain consistency and fairness, the following are outside the scope of Stage 1:
- Hyperparameter tuning (e.g. grid search, random search, Bayesian optimisation)
- Deep learning models
- Model ensembling

If baseline performance is weak, the appropriate response at this stage is to revisit problem formulation, data suitability, or assumptions, rather than to introduce more complex techniques.

Techniques outside this scope may be introduced only when explicitly permitted in later stages.
"""

