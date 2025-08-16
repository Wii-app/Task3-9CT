import pandas as pd
import matplotlib.pyplot as plt

DATA_PATH = "Gaming_Behaviour.csv"  # Change to your actual CSV filename
df = pd.read_csv(DATA_PATH)

def display_dataset_preview():
    print("\n--- Dataset Preview ---")
    print(df.head())

def display_visualisation():
    print("\n--- Data Visualisation ---")
    col = input("Enter column name to plot histogram: ").strip()
    if col in df.columns:
        df[col].hist()
        plt.title(f"Histogram of {col}")
        plt.xlabel(col)
        plt.ylabel("Frequency")
        plt.show()
    else:
        print("Column not found.")

def search_data():
    print("\n--- Search/Filter Data ---")
    col = input("Enter column name to search: ").strip()
    val = input("Enter value to search for: ").strip()
    if col in df.columns:
        results = df[df[col].astype(str).str.contains(val, case=False)]
        print(results)
    else:
        print("Column not found.")

def update_data_entry():
    print("\n--- Update Data Entry ---")
    idx = int(input("Enter row index to update: "))
    col = input("Enter column name to update: ").strip()
    new_val = input("Enter new value: ").strip()
    if col in df.columns and 0 <= idx < len(df):
        df.at[idx, col] = new_val
        print("Entry updated.")
    else:
        print("Invalid index or column.")

def save_changes():
    df.to_csv(DATA_PATH, index=False)
    print("Changes saved to CSV.")