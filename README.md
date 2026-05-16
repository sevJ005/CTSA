# Cyber-Threat-Statistical-Analysis (CTSA)

## Overview

This project engineers a Python + SQL data pipeline to ingest, clean, and analyze large-scale network traffic from the CICIDS2017 dataset. The pipeline merges daily CSV captures, performs cleaning and statistical outlier detection using Z-scores, loads results into a SQLite database, and produces alert exports that can feed a SOC dashboard (Tableau or similar).

## Key Project Accomplishments

- **Enterprise Scale:** Scaled the pipeline to process the full dataset of **2,830,743 records** locally.
- **Statistical Rigor:** Implemented an automated Z-score based outlier detector that isolated **87,580** high-fidelity anomalies using a |Z| > 3 threshold.
- **Behavioural Fingerprinting:** Mapped target vectors to distinguish volumetric web-layer floods from stealthy infiltration and reconnaissance scans.

## Dataset

The project uses the **CICIDS2017** dataset (Canadian Institute for Cybersecurity). 

*(Note: Due to GitHub file size constraints, the raw CSV data directory is excluded from source control via .gitignore and must be acquired separately).* 

Raw CSV files are expected in the `data/` directory:

- `Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv`
- `Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv`
- `Friday-WorkingHours-Morning.pcap_ISCX.csv`
- `Monday-WorkingHours.pcap_ISCX.csv`
- `Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv`
- `Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv`
- `Tuesday-WorkingHours.pcap_ISCX.csv`
- `Wednesday-workingHours.pcap_ISCX.csv`

## Prerequisites

- Python 3.x
- Libraries: `pandas`, `numpy`, `scipy`, `jupyter` (and `sqlite3` which is built-in)

Install dependencies:
```bash
pip install pandas numpy scipy jupyter
```

## Setup & Usage

1. Merge and clean the CSV files (Merges all +2.8M records):

```bash
python CTSA_file_merger.py
```

This produces `CTSA_cleaned_whole.csv` (the entire, cleaned output). Adjust `CTSA_file_merger.py` if you want the sample merged file instead of the entire output.

2. Load the master dataset into a local SQLite database:

```bash
python CTSA_database_manager.py
```

This creates `cyber_security_logs.db` and a `network_traffic` table.

3. Run the analysis notebook for SQL queries and statistical analysis:

```bash
jupyter notebook SQL_Query_Notebook.ipynb
```

The notebook contains exploratory SQL, summary statistics, and the outlier detection steps. The pipeline can export a filtered alerts CSV (example output name used in this project: `CTSA_full_alerts_2.8M.csv`) containing the flagged anomalies.

## Security Insights & Visualizations

- **Threat Distribution (Log Scale):** Use logarithmic scales to surface low-frequency, high-impact threat types (e.g., Heartbleed, Infiltration) alongside volumetric noise.

  <img width="1563" height="1287" alt="image" src="https://github.com/user-attachments/assets/b2f847fd-92ed-4fd6-85a9-c49ae4e86f3c" />
- **Attack Vector Fingerprinting:** Visualize destination ports vs. labels to separate web floods (HTTP/80), SSH brute force (22), and port-scan patterns (wide port ranges).

   <img width="2145" height="532" alt="image" src="https://github.com/user-attachments/assets/daaa72bd-c3c0-42d1-b8a2-082c44dfad32" />

   <img width="306" height="139" alt="image" src="https://github.com/user-attachments/assets/2a9bca65-6cc0-4312-b46b-e53be58513f7" />

- **Proportional Composition:** Compare exploit variant volumes after excluding background traffic to highlight true attacker activity.
  
   <img width="1312" height="1282" alt="image" src="https://github.com/user-attachments/assets/659ab5d7-3b37-4e55-a468-46c29761e6b8" />

### Notes on Visuals

- Web floods concentrate on port 80 and show large, bursty volumes.
- Port scans display horizontal fingerprints across many destination ports (e.g., 873–55055).
- Authentication attacks cluster around port 22 and often show repeated connection attempts from small IP ranges.

## Statistical Methodology

To detect anomalies, we apply a Z-score across continuous connection features. For a feature value $x$:

$$
Z = \frac{x - \mu}{\sigma}
$$

where $\mu$ is the feature mean and $\sigma$ is the standard deviation. Records with $|Z| > 3$ (third-sigma) are flagged as outliers and exported for downstream visualization and review.

## Project Structure

- `CTSA_file_merger.py` — Merge CSV files, clean headers, handle infinities/NaNs, and create a sampled output.
- `CTSA_database_manager.py` — Load the cleaned dataset into SQLite (`cyber_security_logs.db`).
- `SQL_Query_Notebook.ipynb` — Jupyter notebook with SQL queries, visualizations, and outlier detection.
- `CTSA_cleaned_whole.csv` — The cleaned dataset (output of the merger).
- `data/` — Raw CICIDS2017 CSV files.
- `README.md` — Project documentation (this file).

## Output Examples

- `cyber_security_logs.db` — SQLite database with the `network_traffic` table.
- `CTSA_full_alerts_2.8M.csv` — Example alert export containing the filtered anomalies used for BI.

## License

This repository is intended for educational and research use. See the CICIDS2017 dataset licensing for data usage restrictions.
