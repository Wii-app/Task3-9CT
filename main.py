import pandas as pd
import matplotlib.pyplot as plt

DATA_PATH = "Gaming_Behaviour.csv"
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

def show_columns():
    print("\n--- Columns in Dataset ---")
    print(list(df.columns))

def main_menu():
    while True:
        print("\n=== Data Viewer Interface ===")
        print("0. Show column names")
        print("1. View dataset")
        print("2. View visualisation")
        print("3. Search or filter data")
        print("4. Update a data entry")
        print("5. Save changes")
        print("6. Exit")

        choice = input("Select an option (0-6): ").strip()

        if choice == '0':
            show_columns()
        elif choice == '1':
            display_dataset_preview()
        elif choice == '2':
            display_visualisation()
        elif choice == '3':
            search_data()
        elif choice == '4':
            update_data_entry()
        elif choice == '5':
            save_changes()
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid selection. Please choose a number between 0 and 6.")

if __name__ == "__main__":
    main_menu()
