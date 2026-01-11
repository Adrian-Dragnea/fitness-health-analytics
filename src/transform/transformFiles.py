import pandas as pd
from pathlib import Path
from src.utils.logger import setup_logger

logger = setup_logger()

RAW_TO_CLEAN_COLUMNS = {
    "User_ID": "user_id",
    "Date": "date",
    "Age": "age",
    "Gender": "gender",
    "Height (cm)": "height_cm",
    "Weight (kg)": "weight_kg",
    "Steps_Taken": "steps_taken",
    "Calories_Burned": "calories_burned",
    "Hours_Slept": "hours_slept",
    "Water_Intake (Liters)": "water_intake_liters",
    "Active_Minutes": "active_minutes",
    "Heart_Rate (bpm)": "heart_rate_bpm",
    "Workout_Type": "workout_type",
    "Stress_Level (1-10)": "stress_level",
    "Mood": "mood"
}

def transform_raw_xls(raw_file: Path) -> pd.DataFrame:
    logger.info(f"Transforming raw file: {raw_file.name}")

    # Read raw file
    df = pd.read_excel(raw_file)

    # Keep only contract columns
    df = df[list(RAW_TO_CLEAN_COLUMNS.keys())]

    # Rename to canonical names
    df = df.rename(columns=RAW_TO_CLEAN_COLUMNS)

    # Normalize date
    df["date"] = pd.to_datetime(df["date"], errors="raise").dt.date

    # Normalize categorical text
    df["gender"] = df["gender"].str.lower().str.strip()
    df["workout_type"] = df["workout_type"].str.lower().str.strip()
    df["mood"] = df["mood"].str.lower().str.strip()

    # Remove duplicate rows (raw duplicates)
    df = df.drop_duplicates()

    logger.info(f"Transform completed: {df.shape[0]} rows")

    return df

