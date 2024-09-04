import pandas as pd
import datetime
import matplotlib.pyplot as plt

# Constants for CSV files and columns
GYM_DATA_FILE = "gym_data.csv"
FEES_DATA_FILE = "fees_data.csv"
MEMBER_COUNT_FILE = "member_count.csv"
COLUMNS = ["MemberID", "Name", "Age", "MobileNumber", "Membership_Type"]  # Added "MobileNumber"
FEES_COLUMNS = ["ID", "Name", "FeesPaid"]

# Function to load gym data from the CSV file
def load_gym_data():
    try:
        df = pd.read_csv(GYM_DATA_FILE)
        return df
    except FileNotFoundError:
        return pd.DataFrame(columns=COLUMNS)

# Function to load fees data from the CSV file
def load_fees_data():
    try:
        df = pd.read_csv(FEES_DATA_FILE)
        return df
    except FileNotFoundError:
        return pd.DataFrame(columns=FEES_COLUMNS)

# Function to load member count data from the CSV file
def load_member_count():
    try:
        df = pd.read_csv(MEMBER_COUNT_FILE)
        return df
    except FileNotFoundError:
        return pd.DataFrame(columns=["Date", "MemberCount"])

# Function to add a new member to the gym data
def add_member(member_id, name, age, mobile_number, membership_type):  # Updated function signature
    df = load_gym_data()
    new_member = pd.DataFrame([[member_id, name, age, mobile_number, membership_type]], columns=COLUMNS)
    df = pd.concat([df, new_member], ignore_index=True)
    df.to_csv(GYM_DATA_FILE, index=False)

# Function to add fees payment record
def add_fees_record(member_id, name, fees_paid):
    df = load_fees_data()
    new_record = pd.DataFrame([[member_id, name, fees_paid]], columns=FEES_COLUMNS)
    df = pd.concat([df, new_record], ignore_index=True)
    df.to_csv(FEES_DATA_FILE, index=False)

# Function to display all gym members
def display_members():
    df = load_gym_data()
    if not df.empty:
        print(df)
    else:
        print("No members found.")

# Function to display fees payment records
def display_fees_records():
    df = load_fees_data()
    if not df.empty:
        print(df)
    else:
        print("No fees records found.")

# Function to find a member by name
def find_member_by_name(name):
    df = load_gym_data()
    result = df[df["Name"].str.contains(name, case=False)]
    if not result.empty:
        print(result)
    else:
        print("Member not found.")

# Function to change fees data by ID
def change_fees_by_id(member_id, new_fees_paid):
    df = load_fees_data()
    df.loc[df["ID"] == member_id, "FeesPaid"] = new_fees_paid
    df.to_csv(FEES_DATA_FILE, index=False)

# Function to set FeesPaid to "no" for all rows in fees table
def set_all_fees_to_no():
    df = load_fees_data()
    df["FeesPaid"] = "no"
    df.to_csv(FEES_DATA_FILE, index=False)

# Function to save member count and date to CSV
def save_member_count():
    df = load_member_count()
    date_input = input("Enter the date (YYYY-MM-DD): ")
    try:
        date_today = datetime.datetime.strptime(date_input, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please use the format (YYYY-MM-DD).")
        return

    member_count = int(input("Enter the member count: "))
    new_record = pd.DataFrame([[date_today, member_count]], columns=["Date", "MemberCount"])
    df = pd.concat([df, new_record], ignore_index=True)
    df.to_csv(MEMBER_COUNT_FILE, index=False)
    print("Member count and date saved successfully!")

# Function to create and display graph of members
def create_members_graph():
    df = load_member_count()
    if not df.empty:
        plt.plot(df["Date"], df["MemberCount"])
        plt.xlabel("Date")
        plt.ylabel("Number of Members")
        plt.title("Gym Member Count Over Time")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    else:
        print("No member count data available. Please save member count first.")
def change_membership_type_by_id(member_id):
    df = load_gym_data()
    membership_type = input("Enter new Membership Type: ")
    df.loc[df["MemberID"] == member_id, "Membership_Type"] = membership_type
    df.to_csv(GYM_DATA_FILE, index=False)
    print("Membership type updated successfully!")

# Main function to interact with the gym management software
def main():
    print("Welcome to the Gym Management Software!")

    while True:
        print("\nMenu:")
        print("1. Add a new member")
        print("2. Display all members")
        print("3. Add fees payment record")
        print("4. Display fees payment records")
        print("5. Find member by name")
        print("6. Change fees by ID")
        print("7. Set all fees to 'no'")
        print("8. Save member count and date")
        print("9. Create and display graph of members")
        print("10. Change membership type by ID")  # New choice
        print("11. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6/7/8/9/10/11): ")

        if choice == "1":
            member_id = int(input("Enter Member ID: "))
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            mobile_number = input("Enter Mobile Number: ")  # Prompt for Mobile Number
            membership_type = input("Enter Membership Type: ")
            add_member(member_id, name, age, mobile_number, membership_type)  # Updated function call
            print("Member added successfully!")
            input("press enter to continue")

        elif choice == "2":
            print("\nAll Members:")
            display_members()
            input("press enter to continue")

        elif choice == "3":
            member_id = int(input("Enter Member ID: "))
            name = input("Enter Name: ")
            fees_paid = input("Enter Fees Paid: ")
            add_fees_record(member_id, name, fees_paid)
            print("Fees payment record added successfully!")
            input("press enter to continue")

        elif choice == "4":
            print("\nFees Payment Records:")
            display_fees_records()
            input("press enter to continue")

        elif choice == "5":
            search_name = input("Enter the name to search for: ")
            print("\nSearch Results:")
            find_member_by_name(search_name)
            input("press enter to continue")

        elif choice == "6":
            member_id = int(input("Enter Member ID: "))
            new_fees_paid = input("Enter new Fees Paid: ")
            change_fees_by_id(member_id, new_fees_paid)
            print("Fees updated successfully!")
            input("press enter to continue")

        elif choice == "7":
            set_all_fees_to_no()
            print("All fees set to 'no' successfully!")
            input("press enter to continue")

        elif choice == "8":
            save_member_count()
            print("member added successfullly")
            input("press enter to continue")

        elif choice == "9":
            create_members_graph()

        elif choice == "10":
            member_id = int(input("Enter Member ID: "))
            change_membership_type_by_id(member_id)

        elif choice == "11":
            answer = input("Are you sure you want to exit (y/n): ")
            if answer.lower() == "y":
                print("Exiting Gym Management Software. Goodbye!")
                break
            else:
                continue

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
