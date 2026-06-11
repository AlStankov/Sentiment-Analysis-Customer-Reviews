# Installation Manual

## 1. Introduction

This document describes the installation and deployment procedure for the Sentiment Analysis Tool. The tool is implemented in Python and uses a trained Logistic Regression model to classify airline customer reviews into five sentiment categories.

The tool consists of:

* sentiment_analysis_tool.py
* sentiment_tool.joblib
* Supporting Python libraries

---

## 2. System Requirements

### Hardware Requirements

Minimum requirements:

* Dual-core processor
* 4 GB RAM
* 500 MB available storage

---

### Software Requirements

The tool was developed and tested using:

* Python 3.12
* Jupyter Lab
* PyCharm Community Edition

Supported operating systems:

* Windows 10 / 11
* Linux
* macOS

---

## 3. Installation Procedure

### Step 1: Install Python

Download and install Python from:

https://www.python.org/downloads/

### Step 2: Create a Project Directory

Create a project directory and place the following files inside:

```text
SentimentTool/

├── sentiment_analysis_tool.py
├── sentiment_tool.joblib
└── README.md
```

---

### Step 3: Install Required Libraries

Open a terminal in the project directory and install the required Python packages:

# Installation Manual

## 1. Introduction

This document describes the installation and deployment procedure for the Sentiment Analysis Tool. The tool is implemented in Python and uses a trained Logistic Regression model to classify airline customer reviews into five sentiment categories.

The tool consists of:

* sentiment_analysis_tool.py
* sentiment_tool.joblib
* Supporting Python libraries

---

## 2. System Requirements

### Hardware Requirements

Minimum requirements:

* Dual-core processor
* 4 GB RAM
* 500 MB available storage

Recommended requirements:

* Quad-core processor
* 8 GB RAM or more

---

### Software Requirements

The tool was developed and tested using:

* Python 3.12
* Jupyter Lab
* PyCharm Community Edition

Supported operating systems:

* Windows 10 / 11
* Linux
* macOS

---

## 3. Installation Procedure

### Step 1: Install Python

Download and install Python from:

https://www.python.org/downloads/

Verify the installation:

```bash
py --version
```

or

```bash
python --version
```

---

### Step 2: Create a Project Directory

Create a project directory and place the following files inside:

```text
SentimentTool/

├── sentiment_analysis_tool.py
├── sentiment_tool.joblib
├── requirements.txt
├── to_classify.csv (not required, but can be used to test the functionalities)
└── README.md
```

---

### Step 3: Install Required Libraries

Open a terminal in the project directory and install the required Python packages:

```sh
pip install -r requirements.txt
```
---

## 4. Model Deployment

The trained model is stored in the file:

```text
sentiment_tool.joblib
```

This file contains:

* Logistic Regression classifier
* Text preprocessing pipeline
* TF-IDF vectorizer
* One-hot encoders
* Label encoder

The model is automatically loaded when the application starts.

No additional configuration is required.

---

## 5. Input Data Requirements

The input data must be supplied as a CSV file.

Required columns:

| Column                 |
| ---------------------- |
| review_text            |
| seat_comfort           |
| cabin_staff_service    |
| ground_service         |
| value_for_money        |
| food&beverages         |
| inflight_entertainment |
| wifi&connectivity      |
| recommended            |
| date_flown             |

The application automatically:

* Standardizes column names
* Removes unnecessary features
* Creates temporal features
* Applies preprocessing
* Performs sentiment prediction

---

## 6. Running the Application

Place the input file in the project directory.

Example:

```text
SentimentTool/

├── sentiment_analysis_tool.py
├── sentiment_tool.joblib
└── to_classify.csv
```

Execute:

```bash
py sentiment_analysis_tool.py to_classify.csv
```

---

## 7. Output Files

After successful execution, the application generates:

### predictions.csv

Contains:

* Original review data
* Predicted sentiment labels

### summary_report.txt

Contains:

* Total number of reviews
* Sentiment distribution
* Most common sentiment category

### sentiment_distribution.png

Contains:

* Bar chart showing sentiment distribution

---

## 8. System Architecture

The application follows a modular architecture:

```text
Dataset and Data Ingestion
            ↓
Text Preprocessing
            ↓
Negation and Multipolarity Handling
            ↓
Feature Extraction
            ↓
Sentiment Classification
            ↓
Validation and Evaluation
            ↓
Output and Reporting
```

The Logistic Regression classifier operates on a combined feature space consisting of:

* TF-IDF text features
* Customer rating features
* Temporal features

---

## 9. Troubleshooting



### Missing Input Columns

If a required column is missing, verify that the uploaded CSV file contains all required fields.

---

### Model File Missing

If the system cannot locate:

```text
sentiment_tool.joblib
```

ensure that the model file is stored in the same directory as the application.

---

## 10. Maintenance

If a new model is trained in the future, the existing model file can be replaced by a newly exported:

```text
sentiment_tool.joblib
```

without modifying the application code.

This allows the tool to be updated while maintaining the same user workflow.
