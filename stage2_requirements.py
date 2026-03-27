"""

# A2. INF2008 Group Project (Stage 2)

### Project Objective

Stage 1 focused on data validation, and baseline feasibility using default classical models with minimal feature engineering / finetuning. Stage 2 extends this beyond basic feasibility, transitioning to pipeline engineering, ablation studies and decision making.
The objective is not to brute-force a high accuracy score (eg by running thousands of hyperparameter tuning) or chasing leaderboard rankings. The objective is to demonstrate data preparation via pipelines, logical model selection, controlled experimentation, and a mechanical understanding of model failures before translating probabilistic or continuous outputs into actionable business policies.

### Scope and Hard Constraints

Stage 2 lifts specific constraints from Stage 1 while introducing new strict engineering boundaries.

**Allowed (Stage 2 Expansion):**
* **Advanced Data Preparation:** Feature scaling, advanced encoding (e.g., target encoding), complex imputation, and data imbalance mitigation (e.g., SMOTE).
* **Model Ensembling:** Classical ensemble methods (e.g., Random Forest, Gradient Boosting, Model Stacking) are now permitted.
* **Hyperparameter Tuning:** Permitted, but you should justify what you search and also the parameters. You can consider roughly 3 parameters per model, with grid/random searches of 50 total iterations.

**Strictly Prohibited (Stage 2 Restrictions):**
* **Deep Learning / LLMs:** Language models or deep learning models remain prohibited as the primary predictive component. You can use them for feature engineering but not for prediction.
* **Massive Automated Search:** Unjustified computational brute-forcing (e.g., 100+ grid points).
* **Test Set Overuse:** The hold-out test set may only be evaluated *once* to generate the final deployment metrics. All model selection and tuning must utilize cross-validation on the training set.

### Task Requirements

The assignment is split into four parts.

#### Part A: Advanced Data Preparation & Pipeline Engineering

* **Requirement:** Finalize CRISP-DM Phase 3. Implement robust handling for scaling, encoding, and missing values that go beyond the minimal basic cleaning required in Stage 1.
* **Constraint:** All data transformations and the estimator must be strictly encapsulated within a formal pipeline object (e.g., sklearn.pipeline.Pipeline). This proves the prevention of data leakage during validation.

#### Part B: Champion Model Selection
* **Requirement:** Compare 2 to 3 distinct algorithmic families (e.g., a Linear/Distance-based model versus a Tree-based ensemble). You may also consider using a variety of them using model stacking approaches.
* **Deliverable:** Evaluate these base models using k-fold cross-validation (e.g., 5-fold) or a time-series split. Declare one model as the "Champion" based on the mean and standard deviation of your primary evaluation metric.

Do note that it is absolutely critical that Pipeline Engineering comes before Champion Model Selection. This ensures a "fair race" that all the models are seeing the same type of standardized data preprocessing pipeline.

#### Part C: Controlled Ablations & Tuning (The Champion)
* **Requirement:** Perform a maximum of 4 controlled experiments exclusively on the chosen Champion model. This may involve adding a specific engineered feature, applying a class balancing technique, or tuning a specific set of hyperparameters.
* **Deliverable:** An Ablation Log (Table) explicitly detailing: *Hypothesis, Controlled Change, CV Metric Impact (Mean ± Std Dev), and Conclusion*.

#### Part D: Mechanical Failure Analysis
* **Requirement:** Aggregate metrics obscure underlying model flaws. Inspect the raw validation data where the model was confidently incorrect.
* **For Classification:** Extract 5 to 10 instances of False Positives or False Negatives with high prediction confidence. Mechanically explain *why* the model failed on these specific instances based on their feature values, and propose a targeted technical fix.
* **For Regression:** Extract the 5 to 10 instances from your validation set that exhibit the highest absolute error (extreme under/over-predictions). Analyze the feature values of these specific extreme outliers to explain the failure and propose a technical fix.

#### Part E: Decision Making
* Requirement: A model's raw output must be translated into a business decision. Default thresholds (0.5) are rarely optimal in the real world. You must logically evaluate the risks of your model's errors based on the context defined in Stage 1.
+2

* For Classification:
   * Identify which error is more damaging to the business: a False Positive or a False Negative.

  * Based on this, logically argue whether your operating threshold should be shifted higher (to be more conservative) or lower (to be more aggressive) than the default 0.5. You do not need to calculate the exact optimal threshold, but you must justify the direction of the shift.

* For Regression:

  * Identify which error carries a heavier operational penalty: over-predicting or under-predicting the target variable.

  * Logically argue whether the business should apply a "safety margin" (e.g., systematically adding or subtracting a buffer to your raw predictions) before acting on the model's output.

### Deliverables and Slide Mapping
The deadline for Stage 2 submission is 3rd April 2026 2359. Each group is required to submit a single slide report in PDF format.

**Submission requirements:**
* File name format: groupXX_labYY_stage2.pdf
* Maximum of 12 slides containing main content.

**Suggested slide mapping:**
* **Slide 1:** Title, team members, roles, and link to code repository.
* **Slide 2:** Executive Summary & Stage 1 Baseline Recap.
* **Slide 3:** Stage 2 Data Engineering (Upgrades from Baseline).
* **Slide 4:** Pipeline Architecture (Demonstrating mitigation of data leakage).
* **Slide 5:** Model Selection (Cross-validation comparison of 2-3 algorithmic families).
* **Slide 6:** Justification of the "Champion" Model.
* **Slide 7:** Controlled Ablation & Tuning Log (Table).
* **Slide 8:** Final Model Stability Metrics (Cross-validation Mean ± Std deviation).
* **Slide 9:** Mechanical Failure Analysis (Row-level error inspection).
* **Slide 10:** Proposed Fixes for Observed Failures.
* **Slide 11:** Business Decision Reasoning (Qualitative justification for shifting thresholds or applying safety margins based on real-world costs).
* **Slide 12:** Individual Contributions (Mandatory specifying individual tasks, not group-level tasks).

"""

