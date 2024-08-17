import os
import datetime

# Directory where reports will be stored
REPORTS_DIR = "patient_reports"

# Create directory if it does not exist
if not os.path.exists(REPORTS_DIR):
    os.makedirs(REPORTS_DIR)

# Example database of medications, food, exercise, and recommendations
health_recommendations = {
    "Lisinopril": {
        "usage": "Treats high blood pressure",
        "food": "Low-sodium diet, more fruits and vegetables",
        "exercise": "30 minutes of cardio exercise, 5 times a week",
        "next_step": "Monitor blood pressure regularly. If symptoms persist, consider increasing dosage."
    },
    "Metformin": {
        "usage": "Treats type 2 diabetes",
        "food": "Low-carb diet, avoid sugary foods",
        "exercise": "Daily 30-minute walk, strength training twice a week",
        "next_step": "Monitor blood sugar levels. If not controlled, consider adding another medication."
    },

}

def get_current_date():
    """Returns the current date in YYYY-MM-DD format."""
    return datetime.datetime.now().strftime("%Y-%m-%d")

def add_report(patient_name, diagnosis, doctor_name, prescription):
    """Add a new diagnosis report for the patient with additional details."""
    filename = os.path.join(REPORTS_DIR, f"{patient_name}.txt")
    with open(filename, "a") as file:  # Append mode
        file.write(f"Date: {get_current_date()}\n")
        file.write(f"Doctor: {doctor_name}\n")
        file.write(f"Diagnosis: {diagnosis}\n")
        file.write(f"Prescription: {prescription}\n")
        file.write(f"{'-'*40}\n")
    print(f"Diagnosis report for {patient_name} has been updated.\n")
    suggest_health_plan(prescription)

def suggest_health_plan(prescription):
    """Suggest food, exercise, based on the medication."""
    medications = prescription.split(", ")
    print("\nHealth Plan Recommendations:")
    for med in medications:
        if med in health_recommendations:
            print(f"- {med}:")
            print(f"  Usage: {health_recommendations[med]['usage']}")
            print(f"  Recommended Food: {health_recommendations[med]['food']}")
            print(f"  Recommended Exercise: {health_recommendations[med]['exercise']}")
            print(f"  Next Steps: {health_recommendations[med]['next_step']}")
        else:
            print(f"- {med}: No specific recommendations available.")
    print("\n")

def suggest_medication_changes(report_data):
    """Suggest medication changes based on the diagnosis history and medication usage."""
    # Analyze the report data for previous medications and conditions
    if "Lisinopril" in report_data:
        print("- Consider increasing Lisinopril dosage if blood pressure remains uncontrolled.")
    if "Metformin" in report_data:
        print("- If blood sugar levels are not stable, consider adding insulin or another medication.")


def view_reports(patient_name):
    """View all diagnosis reports for the patient and suggest any necessary changes."""
    filename = os.path.join(REPORTS_DIR, f"{patient_name}.txt")
    if os.path.exists(filename):
        print(f"\nDiagnosis reports for {patient_name}:")
        with open(filename, "r") as file:
            report_data = file.read()
            print(report_data)
            suggest_medication_changes(report_data)
    else:
        print(f"No reports found for {patient_name}.\n")

def search_reports(patient_name, keyword):
    """Search for specific diagnosis"""
    filename = os.path.join(REPORTS_DIR, f"{patient_name}.txt")
    if os.path.exists(filename):
        found = False
        with open(filename, "r") as file:
            reports = file.readlines()
            print(f"\nSearch results for '{keyword}' in {patient_name}'s reports:")
            for i, line in enumerate(reports):
                if keyword.lower() in line.lower():
                    print(f"Line {i+1}: {line.strip()}")
                    found = True
        if not found:
            print(f"No matches found for '{keyword}'.\n")
    else:
        print(f"No reports found for {patient_name}.\n")

def validate_input(prompt, field_name):

    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        else:
            print(f"{field_name} cannot be empty. Please try again.")

def main():
    while True:
        print("\nAutomatic Health Monitoring System")
        print("1. Add Diagnosis Report")
        print("2. View Diagnosis Reports")
        print("3. Search in Diagnosis Reports")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            patient_name = validate_input("Enter patient name: ", "Patient name")
            diagnosis = validate_input("Enter diagnosis details: ", "Diagnosis details")
            doctor_name = validate_input("Enter doctor's name: ", "Doctor's name")
            prescription = validate_input("Enter medical prescription (separate multiple meds with commas): ", "Medical prescription")
            add_report(patient_name, diagnosis, doctor_name, prescription)
        elif choice == '2':
            patient_name = validate_input("Enter patient name: ", "Patient name")
            view_reports(patient_name)
        elif choice == '3':
            patient_name = validate_input("Enter patient name: ", "Patient name")
            keyword = validate_input("Enter search keyword: ", "Search keyword")
            search_reports(patient_name, keyword)
        elif choice == '4':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
