# Cyber-Threat-Statistical-Analysis

## Overview

This project performs statistical analysis on cyber threat data using the CICIDS2017 dataset. It involves merging multiple network traffic CSV files, cleaning the data, creating a sample dataset, loading it into a SQLite database, and performing SQL queries and statistical analysis via a Jupyter notebook.

## Dataset

The dataset used is the CICIDS2017 (Canadian Institute for Cybersecurity Intrusion Detection System 2017) dataset, which contains network traffic data captured over five days, including various types of attacks such as DDoS, PortScan, Infiltration, and Web Attacks.

The raw data files are located in the `data/` directory:
- Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv
- Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv
- Friday-WorkingHours-Morning.pcap_ISCX.csv
- Monday-WorkingHours.pcap_ISCX.csv
- Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv
- Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv
- Tuesday-WorkingHours.pcap_ISCX.csv
- Wednesday-workingHours.pcap_ISCX.csv

## Prerequisites

- Python 3.x
- Required libraries: pandas, numpy, sqlite3 (built-in), jupyter (for notebook)

Install dependencies using pip:
```
pip install pandas numpy jupyter
```

## Setup and Usage

1. **Merge and Clean Data:**
   Run the file merger script to combine all CSV files, clean the data, and create a 10% sample.
   ```
   python CTSA_file_merger.py
   ```
   This generates `CTSA_cleaned_sample.csv`.

2. **Load Data into Database:**
   Run the database manager script to create a SQLite database and load the sample data.
   ```
   python CTSA_database_manager.py
   ```
   This creates `cyber_security_logs.db` with a table `network_traffic`.

3. **Perform Analysis:**
   Open and run the Jupyter notebook for SQL queries and statistical analysis.
   ```
   jupyter notebook SQL_Query_Notebook.ipynb
   ```
   The notebook includes queries for data exploration, statistical summaries, and outlier detection.

## Project Structure

- `CTSA_file_merger.py`: Script to merge CSV files, clean data, and create a sample.
- `CTSA_database_manager.py`: Script to load the sample data into a SQLite database.
- `SQL_Query_Notebook.ipynb`: Jupyter notebook for querying and analyzing the data.
- `CTSA_cleaned_sample.csv`: The cleaned 10% sample dataset.
- `data/`: Directory containing the original CICIDS2017 CSV files.
- `README.md`: This file.

## License

This project is for educational purposes. Please refer to the CICIDS2017 dataset license for data usage.