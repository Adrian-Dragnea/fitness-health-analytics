Clean Data Contract

Dataset: Comprehensive Fitness and Health Tracking Dataset
Layer: Clean / Processed
Owner: Data Engineering
Status: Locked
Version: 1.0

1. Purpose

This dataset provides daily, user-level fitness metrics derived from raw XLS sources.
It is intended for:

analytics

BI dashboards

downstream ML features

PostgreSQL storage

Raw data must not be queried directly.

2. Grain 

One row represents one user on one calendar day.

All metrics in a row refer to the same user and same date.

3. Raw schema invetory

'User_ID', Keep (Natural primary key)
'Full Name', Drop
'Date',  Keep
'Age',  Keep
'Gender',  Keep
'Height (cm)', Keep
'Weight (kg)',  Keep
'Steps_Taken',  Keep
'Calories_Burned',  Keep
'Hours_Slept', Keep
'Water_Intake (Liters)',  Keep
'Active_Minutes',  Keep
'Heart_Rate (bpm)', Keep
'Workout_Type',  Keep
'Stress_Level (1-10)',  Keep
'Mood' Keep

4. Primary Key (user_id, date)
Guarantees:

exactly one row per user per day

no duplicates allowed

5. Schema Definition

| Column              | Type     | Nullable | Description            |
| ------------------- | -------- | -------- | ---------------------- |
| user_id             | int64    | No        | Unique user identifier |
| date                | date     | No        | Observation date       |
| age                 | int64    | No        | User age (years)       |
| gender              | category | No        | User gender            |
| height_cm           | int64    | No        | Height in centimeters  |
| weight_kg           | float64  | No        | Weight in kilograms    |
| steps_taken         | int64    | No        | Daily steps count      |
| calories_burned     | float64  | No        | Calories burned        |
| hours_slept         | float64  | Yes        | Sleep duration (hours) |
| water_intake_liters | float64  | Yes       | Water intake (liters)  |
| active_minutes      | float64  | Yes       | Active minutes         |
| heart_rate_bpm      | float64  | Yes       | Average heart rate     |
| workout_type        | category | Yes       | Workout category       |
| stress_level        | int64    | No       | Stress score           |
| mood                | category | No        | Self-reported mood     |

6. Allowed Values (Enums)
gender in (male, female, other)

Workout_Type in (yoga, cardion, strenght)

mood in (sad, neutral, happy, stressed)

7. Constraints & Business Rules
(user_id, date) must be unique

age BETWEEN 0 AND 120
height_cm > 0
weight_kg > 0
steps_taken >= 0
calories_burned >= 0
hours_slept BETWEEN 0 AND 24
water_intake_liters >= 0
active_minutes >= 0
heart_rate_bpm BETWEEN 40 AND 220
stress_level BETWEEN 1 AND 10

user_id NOT NULL
date NOT NULL
age NOT NULL
gender NOT NULL

Nullable metrics indicate missing measurements, not invalid records.

8. Exclusions 

The following are not included in the clean dataset:

Free-text notes

Personally identifiable information (PII)

Raw source identifiers

Duplicate or aggregated rows

Raw data is preserved in the raw layer only.

