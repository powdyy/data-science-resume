# Bulldozer Price Regression (End-to-End ML Project)

This repository contains a complete, end-to-end machine learning project for predicting bulldozer sale prices, based on the [Bluebook for Bulldozers Kaggle competition](https://www.kaggle.com/c/bluebook-for-bulldozers). The main deliverable is a Jupyter notebook demonstrating all stages of a structured-data regression pipeline—from data loading and preprocessing to model evaluation and generating submission-ready predictions.

---

## 📋 Table of Contents

* [🚀 Project Overview](#-project-overview)
* [✨ Key Features](#-key-features)
* [⚙️ Requirements](#️-requirements)
* [💾 Data](#-data)
* [🛠️ Installation & Setup](#️-installation--setup)
* [📖 Usage](#-usage)
* [🔍 Notebook Breakdown](#-notebook-breakdown)
* [📈 Results](#-results)
* [🤝 Contributing](#-contributing)
* [📝 License](#-license)

---

## 🚀 Project Overview

The goal is to build a regression model to predict the sale price (`SalePrice`) of bulldozers using historical auction data. This notebook (`end-to-end-bluebook-bulldozer-price-regression-v2.ipynb`) covers:

1. **Problem definition**: Formulating a supervised regression task.
2. **Data exploration**: Inspecting distributions, missing values, and time-based trends.
3. **Feature engineering**: Parsing dates, encoding categories, and handling missingness.
4. **Modeling**: Training baseline and Random Forest regressors, hyperparameter tuning.
5. **Evaluation**: Using RMSLE on a hold-out validation set to measure performance.
6. **Submission**: Generating predictions for a test set (`Test.csv`) ready for Kaggle submission.

---

## ✨ Key Features

* End-to-end pipeline demonstrating best practices in a regression workflow.
* Time-aware split: validation set based on sale date to avoid data leakage.
* Comprehensive preprocessing: date parsing, imputation strategies, and encoding.
* Benchmark models and hyperparameter tuning example.
* Visualization of feature importances and error diagnostics.

---

## ⚙️ Requirements

* Python 3.8+
* Jupyter Notebook
* Key libraries:

  * pandas
  * numpy
  * matplotlib
  * scikit-learn
  * category\_encoders (optional)

You can install dependencies via:

```bash
pip install -r requirements.txt
```

---

## 💾 Data

Download the data from Kaggle (requires a Kaggle account):

1. Go to the [Bluebook for Bulldozers competition page](https://www.kaggle.com/c/bluebook-for-bulldozers/data).
2. Accept the competition rules and download `Train.csv`, `Valid.csv`, and `Test.csv`.
3. Place the CSVs in a `data/` directory at the project root:

```
project-root/
├── data/
│   ├── Train.csv
│   ├── Valid.csv
│   └── Test.csv
└── notebooks/
    └── end-to-end-bluebook-bulldozer-price-regression-v2.ipynb
```

---

## 🛠️ Installation & Setup

1. **Clone this repository**

   ```bash
   ```

git clone [https://github.com/mrdbourke/zero-to-mastery-ml.git](https://github.com/mrdbourke/zero-to-mastery-ml.git)
cd zero-to-mastery-ml/section-3-structured-data-projects/end-to-end-bluebook-bulldozer-price-regression-v2

````

2. **Create a virtual environment** (recommended)
   ```bash
python -m venv .env
source .env/bin/activate   # Linux/macOS
.env\Scripts\activate      # Windows
````

3. **Install dependencies**

   ```bash
   ```

pip install -r requirements.txt

````

4. **Launch Jupyter Notebook**
   ```bash
jupyter notebook
````

Open `end-to-end-bluebook-bulldozer-price-regression-v2.ipynb` to follow along.

---

## 📖 Usage

1. Run each cell in order to replicate data preprocessing, feature engineering, and model training.
2. Adjust hyperparameters in the modeling section to experiment with different settings.
3. Inspect the validation RMSLE to gauge performance improvements.
4. Generate final predictions for `Test.csv` and save the output as `submission.csv`:

   ```python
   submission = pd.DataFrame({
       "SalesID": test_df.SalesID,
       "SalePrice": model.predict(test_prepared)
   })
   submission.to_csv("submission.csv", index=False)
   ```

---

## 🔍 Notebook Breakdown

| Section      | Description                                         |
| ------------ | --------------------------------------------------- |
| 1. Setup     | Imports, constants, configuration                   |
| 2. Data Load | Reading `Train.csv`, `Valid.csv`, `Test.csv`        |
| 3. EDA       | Exploratory data analysis and visualization         |
| 4. Preproc   | Handling missing values, feature encoding           |
| 5. Modeling  | Baselines, RandomForest, hyperparameter tuning      |
| 6. Eval      | Validation metrics, error analysis, feature import. |
| 7. Submit    | Generating `submission.csv` for Kaggle              |

---

## 📈 Results

* **Validation RMSLE**: \~0.25 (will vary by seed/hyperparameters)
* **Top features**: YearMade, EngineHours, MachineHoursCurrentMeter, etc.

Visualizations are included in the notebook under the "Evaluation" section.

---

