# Sentiment Analysis Tool

## Overview

The Sentiment Analysis Tool is designed to automatically classify customer reviews into one of five sentiment categories:

* Very Negative
* Negative
* Neutral
* Positive
* Very Positive

The tool processes a CSV file containing customer reviews (consisting of textual review and ratings between 1 and 10) and generates sentiment predictions together with summary reports that can be used by the marketing department to monitor customer satisfaction.

---

## Purpose

The purpose of this tool is to assist the marketing department in quickly analyzing large volumes of customer feedback and identifying overall customer sentiment trends without the need for manual review.

---

## Input Requirements

The input data must be provided as a CSV file.

The CSV file must contain the following columns:

| Column Name            | Description                                          |
| ---------------------- | ---------------------------------------------------- |
| review_body            | Customer review text                                 |
| seat_comfort           | Seat comfort rating                                  |
| cabin_staff_service    | Cabin staff service rating                           |
| ground_service         | Ground service rating                                |
| value_for_money        | Value for money rating                               |
| food&beverages         | Food and beverages rating                            |
| inflight_entertainment | In-flight entertainment rating                       |
| wifi&connectivity      | Wi-Fi and connectivity rating                        |
| recommended            | Whether the customer recommends the airline (yes/no) |
| date_flown             | Date of the flight                                   |

Additional columns are permitted and will be ignored by the system where appropriate.

---

## Running the Tool

Place the following files in the same folder:

* sentiment_analysis_tool.py
* sentiment_analysis.joblib
* input CSV file

Example:

```text
SentimentTool/

├── sentiment_analysis_tool.py
├── sentiment_analysis.joblib
└── to_classify.csv
```

Open a terminal in the project directory and execute:

```bash
py sentiment_analysis_tool.py to_classify.csv
```

---

## Generated Outputs

After successful execution, the tool generates the following files:

### 1. predictions.csv

Contains the original reviews together with the predicted sentiment.

Example:

| review_text                        | predicted_sentiment |
| ---------------------------------- | ------------------- |
| Excellent flight and friendly crew | Very Positive       |
| Poor service and long delays       | Very Negative       |

---

### 2. summary_report.txt

Provides a summary of sentiment distribution.

Example:

```text
Total Reviews: 500

Very Positive: 120 (24.0%)
Positive: 220 (44.0%)
Neutral: 90 (18.0%)
Negative: 50 (10.0%)
Very Negative: 20 (4.0%)

Most Common Sentiment: Positive
```

---

### 3. sentiment_distribution.png

Bar chart visualizing the distribution of predicted sentiment classes.

---


## Troubleshooting

### Missing Required Columns

If the tool reports missing columns, verify that the input CSV contains all required fields listed in the Input Requirements section.

### Model File Not Found

Verify that sentiment_analysis.joblib is located in the same directory as sentiment_analysis_tool.py.

---
