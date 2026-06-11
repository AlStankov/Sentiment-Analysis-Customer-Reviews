import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import re
import sys


# =========================

# LOAD MODEL

# =========================

bundle = joblib.load("sentiment_analysis.joblib")

model = bundle["model"]
label_encoder = bundle["label_encoder"]

# =========================

# DATA PREPARATION

# =========================

def prepare_dataset(df):

    # Standardize column names
    def name_pythonizer(column_name):

        column_name = re.sub(
            r'(?<=[a-z0-9])([A-Z])',
            r'_\1',
            column_name
        )

        column_name = column_name.lower()

        column_name = (
            column_name
            .replace('.', '_')
            .replace(' ', '_')
        )

        return column_name

    df.columns = df.columns.map(
        name_pythonizer
    )

    # Remove unnecessary columns if present
    columns_to_drop = [
        'verified_review',
        'review_header',
        'aircraft',
        'unnamed:_0',
        'route',
        'name',
        'type_of_traveller',
        'seat_type'
    ]

    existing_columns = [
        col
        for col in columns_to_drop
        if col in df.columns
    ]

    df = df.drop(
        columns=existing_columns
    )

    return df
    
# =========================

# FEATURE ENGINEERING

# =========================

def create_time_features(df):

    df["date_flown"] = pd.to_datetime(
        df["date_flown"],
        errors="coerce"
    )

    df["flight_year"] = df["date_flown"].dt.year

    df["flight_month"] = df["date_flown"].dt.month

    df["month_sin"] = np.sin(
        2 * np.pi * df["flight_month"] / 12
    )

    df["month_cos"] = np.cos(
        2 * np.pi * df["flight_month"] / 12
    )

    season_map = {
        12: "winter",
        1: "winter",
        2: "winter",
        3: "spring",
        4: "spring",
        5: "spring",
        6: "summer",
        7: "summer",
        8: "summer",
        9: "autumn",
        10: "autumn",
        11: "autumn"
    }

    df["flight_season"] = (
        df["flight_month"]
        .map(season_map)
    )

    return df


# =========================

# REPORTING

# =========================

def generate_summary_report(df):

    counts = (
        df["predicted_sentiment"]
        .value_counts()
        .sort_index()
    )

    percentages = (
        counts / len(df) * 100
    )

    report_lines = []

    report_lines.append(
        f"Total Reviews: {len(df)}"
    )

    report_lines.append("\nSentiment Distribution\n")

    for sentiment in counts.index:

        report_lines.append(
            f"{sentiment}: "
            f"{counts[sentiment]} "
            f"({percentages[sentiment]:.1f}%)"
        )

    report_lines.append(
        f"\nMost Common Sentiment: "
        f"{counts.idxmax()}"
    )

    with open(
        "summary_report.txt",
        "w",
        encoding="utf-8"
    ) as f:

        f.write("\n".join(report_lines))


def generate_sentiment_chart(df):

    sentiment_counts = (
        df["predicted_sentiment"]
        .value_counts()
        .sort_index()
    )

    plt.figure(figsize=(8,5))

    sentiment_counts.plot(
        kind="bar"
    )

    plt.title(
        "Predicted Sentiment Distribution"
    )

    plt.ylabel(
        "Number of Reviews"
    )

    plt.tight_layout()

    plt.savefig(
        "sentiment_distribution.png"
    )

    plt.close()

# =========================

# MAIN FUNCTION

# =========================

def analyze_reviews(input_file):

    reviews = pd.read_csv(input_file)

    reviews = prepare_dataset(reviews)

    reviews = create_time_features(
        reviews
    )

    predictions = model.predict(
        reviews
    )

    reviews["predicted_sentiment"] = (
        label_encoder.inverse_transform(
            predictions
        )
    )

    reviews.to_csv(
        "predictions.csv",
        index=False
    )

    generate_summary_report(
        reviews
    )

    generate_sentiment_chart(
        reviews
    )

    print(
        "Analysis completed successfully."
    )

    print(
        "Generated files:"
    )

    print(
        "- predictions.csv"
    )

    print(
        "- summary_report.txt"
    )

    print(
        "- sentiment_distribution.png"
    )


if __name__ == "__main__":

    input_file = sys.argv[1]

    analyze_reviews(input_file)