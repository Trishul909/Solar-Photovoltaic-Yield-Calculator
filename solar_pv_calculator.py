import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
print("=" * 60)
print("SOLAR PHOTOVOLTAIC YIELD & THERMAL EFFICIENCY CALCULATOR")
print("=" * 60)
REFERENCE_TEMP = 25
NOCT = 45
TEMP_COEFFICIENT = -0.004
def get_panel_details():
    panel_area = float(input("Enter panel area (m²): "))
    panel_efficiency = (float(input("Enter panel efficiency (%): ")) / 100)
    duration = float(input("Enter duration represented by each reading (hours): "))
    num_readings = int(input("How many hourly readings do you want to enter? "))
    return (
        panel_area,
        panel_efficiency,
        duration,
        num_readings
    )
def collect_hourly_data(num_readings):
    hours = []
    ambient_temperatures = []
    irradiance_values = []
    for hour in range(1, num_readings + 1):
        print(f"\nHour {hour}")
        ambient_temp = float(input("Ambient Temperature (°C): "))
        irradiance = float( input("Solar Irradiance (W/m²): "))
        hours.append(hour)
        ambient_temperatures.append(ambient_temp)
        irradiance_values.append(irradiance)
    return (
        hours,
        ambient_temperatures,
        irradiance_values
    )
def calculate_values(
    panel_area,
    panel_efficiency,
    duration,
    ambient_temperatures,
    irradiance_values
):
    cell_temperatures = []
    base_powers = []
    derating_factors = []
    actual_powers = []
    energy_generated = []
    actual_efficiencies = []
    for ambient_temp, irradiance in zip( ambient_temperatures,irradiance_values):
        cell_temp = (ambient_temp+ ((NOCT - 20) / 800) * irradiance)
        base_power = (irradiance * panel_area * panel_efficiency)
        derating_factor = (1  + TEMP_COEFFICIENT* (cell_temp - REFERENCE_TEMP))
        derating_factor = max(0,derating_factor)
        actual_power = (base_power * derating_factor)
        energy = (actual_power * duration)
        actual_efficiency = (panel_efficiency* derating_factor* 100)

        cell_temperatures.append(cell_temp)
        base_powers.append(base_power)
        derating_factors.append(derating_factor)
        actual_powers.append(actual_power)
        energy_generated.append(energy)
        actual_efficiencies.append(actual_efficiency)
    return (
        cell_temperatures,
        base_powers,
        derating_factors,
        actual_powers,
        energy_generated,
        actual_efficiencies
    )
def create_dataframe(
    hours,
    ambient_temperatures,
    irradiance_values,
    cell_temperatures,
    base_powers,
    derating_factors,
    actual_powers,
    energy_generated,
    actual_efficiencies
):
    df = pd.DataFrame({
        "Hour": hours,
        "Ambient Temp (°C)": ambient_temperatures,
        "Solar Irradiance (W/m²)": irradiance_values,
        "Cell Temp (°C)": cell_temperatures,
        "Base Power (W)": base_powers,
        "Derating Factor": derating_factors,
        "Actual Power (W)": actual_powers,
        "Energy (Wh)": energy_generated,
        "Efficiency (%)": actual_efficiencies
    })
    return df.round(2)
def display_summary(df):
    total_energy = df["Energy (Wh)"].sum()
    total_energy_kwh = total_energy / 1000
    maximum_power = df["Actual Power (W)"].max()
    highest_temperature = df["Cell Temp (°C)"].max()
    average_temperature = df["Cell Temp (°C)"].mean()
    average_efficiency = df["Efficiency (%)"].mean()
    print("\n" + "=" * 45)
    print("DAILY SUMMARY")
    print("=" * 45)
    print(
        f"Total Energy Generated : "
        f"{total_energy:.2f} Wh ({total_energy_kwh:.2f} kWh)"
    )
    print(f"Maximum Power Output   : {maximum_power:.2f} W")
    print(f"Highest Cell Temp      : {highest_temperature:.2f} °C")
    print(f"Average Cell Temp      : {average_temperature:.2f} °C")
    print(f"Average Efficiency     : {average_efficiency:.2f} %")
    print("=" * 45)
def plot_graphs(df):
    # Graph 1 : Solar Irradiance vs Hour
    plt.figure(figsize=(8,5))
    plt.plot(
        df["Hour"],
        df["Solar Irradiance (W/m²)"],
        marker="o",
        linewidth=2
    )
    plt.title("Solar Irradiance Throughout the Day")
    plt.xlabel("Hour")
    plt.ylabel("Solar Irradiance (W/m²)")
    plt.grid(True)
    plt.show()
    # Graph 2 : Actual Power vs Hour
    plt.figure(figsize=(8,5))
    plt.plot(
        df["Hour"],
        df["Actual Power (W)"],
        marker="s",
        linewidth=2
    )
    plt.title("Actual Power Output")
    plt.xlabel("Hour")
    plt.ylabel("Power (W)")
    plt.grid(True)
    plt.show()
    # Graph 3 : Base Power vs Actual Power
    plt.figure(figsize=(8,5))
    plt.plot(
        df["Hour"],
        df["Base Power (W)"],
        marker="o",
        linewidth=2,
        label="Base Power"
    )
    plt.plot(
        df["Hour"],
        df["Actual Power (W)"],
        marker="s",
        linewidth=2,
        label="Actual Power"
    )
    plt.title("Base Power vs Actual Power")
    plt.xlabel("Hour")
    plt.ylabel("Power (W)")
    plt.legend()
    plt.grid(True)
    plt.show()
    # Graph 4 : Efficiency vs Cell Temperature
    plt.figure(figsize=(8,5))
    plt.scatter(
        df["Cell Temp (°C)"],
        df["Efficiency (%)"]
    )
    plt.title("Efficiency vs Cell Temperature")
    plt.xlabel("Cell Temperature (°C)")
    plt.ylabel("Efficiency (%)")
    plt.grid(True)
    plt.show()
def main():
    panel_area, panel_efficiency, duration, num_readings = get_panel_details()
    hours, ambient_temperatures, irradiance_values = collect_hourly_data(num_readings)
    (
        cell_temperatures,
        base_powers,
        derating_factors,
        actual_powers,
        energy_generated,
        actual_efficiencies
    ) = calculate_values(
        panel_area,
        panel_efficiency,
        duration,
        ambient_temperatures,
        irradiance_values
    )
    df = create_dataframe(
        hours,
        ambient_temperatures,
        irradiance_values,
        cell_temperatures,
        base_powers,
        derating_factors,
        actual_powers,
        energy_generated,
        actual_efficiencies
    )
    print("\nCalculated Results\n")
    print(df.to_string(index=False))

    display_summary(df)

    plot_graphs(df)
if __name__ == "__main__":main()