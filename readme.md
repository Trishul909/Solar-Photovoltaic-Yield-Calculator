# Solar Photovoltaic Yield & Thermal Efficiency Calculator

## Overview

This project estimates photovoltaic (PV) energy generation while accounting for temperature-dependent efficiency losses using a thermal derating model.

The program takes solar irradiance and ambient temperature data, estimates solar cell temperature, calculates theoretical and actual power output, and visualizes system performance through engineering-focused plots.

---

## Features

- User-defined solar panel specifications
- Hourly solar irradiance and temperature analysis
- Cell temperature estimation using NOCT model
- Thermal derating calculations
- Power and energy generation calculations
- Performance visualization using Matplotlib
- Daily performance summary

---

## Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib

---

## Engineering Concepts Used

### Cell Temperature Estimation

Cell temperature is estimated using:

Tcell = Tambient + ((NOCT - 20) / 800) × Irradiance

where:

- Tcell = Cell temperature (°C)
- Tambient = Ambient temperature (°C)
- NOCT = Nominal Operating Cell Temperature

### Thermal Derating

Power loss due to temperature is modeled using:

Derating Factor = 1 + γ × (Tcell - Tref)

where:

- γ = Temperature coefficient (-0.004 / °C)
- Tref = 25°C

### Actual Power Output

Actual Power = Base Power × Derating Factor

---

## Example Input

### Panel Specifications

| Parameter | Value |
|------------|--------|
| Panel Area | 1.6 m² |
| Panel Efficiency | 20 % |
| Duration | 1 hour |

### Environmental Data

| Hour | Ambient Temp (°C) | Irradiance (W/m²) |
|------|------:|------:|
| 1 | 22 | 100 |
| 2 | 24 | 250 |
| 3 | 26 | 450 |
| 4 | 29 | 650 |
| 5 | 32 | 850 |
| 6 | 35 | 1000 |
| 7 | 36 | 950 |
| 8 | 34 | 700 |
| 9 | 30 | 450 |
| 10 | 27 | 150 |

---

## Output Dashboard

![Dashboard](dashboard.png)

---

## Sample Output

| Hour | Cell Temp (°C) | Actual Power (W) | Efficiency (%) |
|------|------:|------:|------:|
| 1 | 25.13 | 31.98 | 20.00 |
| 2 | 31.81 | 78.63 | 19.45 |
| 3 | 40.06 | 139.58 | 18.79 |
| 4 | 49.31 | 195.81 | 18.06 |
| 5 | 58.56 | 249.03 | 17.31 |

*Values shown are representative output from the calculator.*

---

## Generated Visualizations

The project generates four engineering-focused visualizations:

1. Solar Irradiance vs Hour
2. Actual Power Output vs Hour
3. Base Power vs Actual Power
4. Efficiency vs Cell Temperature

These plots help visualize photovoltaic performance and temperature-related power losses.

---

## Future Improvements

- CSV weather data input
- Real-world weather station datasets
- Streamlit dashboard interface
- Monthly and yearly energy yield estimation
- PDF report generation
- Comparison of multiple solar panel configurations

---

## How to Run

Install required libraries:

```bash
pip install -r requirements.txt
```

Run the program:

```bash
python solar_pv_calculator.py
```

---
