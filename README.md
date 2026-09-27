# Smart Road Safety & Accident Analytics Platform

Big Data Analytics college project — Group 15, guided by Ms. Geethu Gopan.

## Tech Stack
- HDFS (storage)
- Apache Pig (data cleaning)
- Apache Hive (SQL analysis + simulated HBase lookups)
- Apache Spark MLlib (severity prediction, Random Forest)
- Google Cloud Dataproc (cluster infrastructure)

## Pipeline
1. Raw data (UK Accident/Vehicle Information datasets) loaded into HDFS
2. Cleaned using Apache Pig (`clean_accidents.pig`, `clean_vehicles.pig`)
3. Analyzed using Hive SQL — hotspots, severity trends, contributing factors
4. Hotspot/risk scores stored in a Hive lookup table (simulating HBase due to cluster resource constraints)
5. Severity prediction model built with Spark MLlib Random Forest (`severity_model.py`) — 86.76% accuracy
6. Visualizations generated with matplotlib (`make_charts.py`)

## Files
- `clean_accidents.pig` / `clean_vehicles.pig` — Pig cleaning scripts
- `severity_model.py` — Spark ML severity prediction
- `make_charts.py` — Visualization generation
- `*.png` — Output charts

