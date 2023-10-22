import streamlit as st
import csv

def show():
    st.title("Transform Schedule for Google Calendar")

    st.markdown("### Define Doctor Names for Each Column in schedule.csv")
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        doctor_name_0 = st.text_input("Name for Doctor in Column 1 (corresponds to ID 0):")
    with col2:
        doctor_name_1 = st.text_input("Name for Doctor in Column 2 (corresponds to ID 1):")
    with col3:
        doctor_name_2 = st.text_input("Name for Doctor in Column 3 (corresponds to ID 2):")
    with col4:
        doctor_name_3 = st.text_input("Name for Doctor in Column 4 (corresponds to ID 3):")
    with col5:
        doctor_name_4 = st.text_input("Name for Doctor in Column 5 (corresponds to ID 4):")

    doctor_name_legend = {
        0: doctor_name_0,
        1: doctor_name_1,
        2: doctor_name_2,
        3: doctor_name_3,
        4: doctor_name_4
    }

    st.markdown("### Upload the generated schedule.csv file")
    uploaded_file = st.file_uploader(" ", type="csv")
    if uploaded_file:
        with open("temp_schedule.csv", "wb") as f:
            f.write(uploaded_file.getbuffer())

        transformed_file_path = transform_schedule("temp_schedule.csv", doctor_name_legend)

        st.success(f"Transformed file saved to {transformed_file_path}!")

        with open(transformed_file_path, "rb") as f:
            st.download_button(
                label="Download Transformed Schedule for Google Calendar",
                data=f,
                file_name="google_calendar_schedule.csv",
                mime="text/csv"
            )


def transform_schedule(schedule_csv_path, doctor_name_legend):
    output_file_path = "google_calendar_schedule.csv"
    
    # Read the schedule from the input CSV file
    with open(schedule_csv_path, "r") as infile:
        reader = csv.reader(infile)

        # Skip the header row
        next(reader)

        # Write the updated schedule to the output CSV file
        with open(output_file_path, "w") as outfile:
            writer = csv.writer(outfile)

            # Write the header row
            writer.writerow(["Subject", "Start Date", "End Date", "All Day Event", "Description"])

            # Process the data rows
            for row in reader:
                date, doctor_id = row
                doctor_name = doctor_name_legend[int(doctor_id)]
                writer.writerow([f'On-call: {doctor_name}', date, date, "True", ""])

    return output_file_path

if __name__ == "__main__":
    show()
