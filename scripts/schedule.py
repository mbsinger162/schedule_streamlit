import streamlit as st
from schedulev4sl import main
import datetime

def show():
    st.title("Generate PGY2 Call Schedule")

    st.markdown("### Date Range")
    start_date = st.date_input("Start Date", datetime.date(2023, 7, 1))
    end_date = st.date_input("End Date", datetime.date(2024, 6, 30))

    st.markdown("### Upload csv file containing dates residents are unavailable")
    doctor_data_file = st.file_uploader("", type=['csv'])
    if doctor_data_file:
        st.session_state.uploaded_doctor_data = doctor_data_file

    st.markdown("### Upload csv file which contains holidays")
    excluded_data_file = st.file_uploader(" ", type=['csv'])
    if excluded_data_file:
        st.session_state.uploaded_excluded_data = excluded_data_file

    if doctor_data_file and excluded_data_file:
        with open("temp_doctor_data.csv", "wb") as f:
            f.write(doctor_data_file.getvalue())
        
        with open("temp_excluded_data.csv", "wb") as f:
            f.write(excluded_data_file.getvalue())

        if st.button("Generate Schedule"):
            # Pass the start_date and end_date as arguments to the main function
            main("temp_doctor_data.csv", "temp_excluded_data.csv", start_date, end_date)
            st.success("Schedule successfully generated!")
            
            with open("schedule.csv", "rb") as f:
                csv_data = f.read()
                st.download_button(
                    label="Download Schedule CSV",
                    data=csv_data,
                    file_name="schedule.csv",
                    mime="text/csv"
                )
