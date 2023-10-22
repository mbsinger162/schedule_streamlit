import streamlit as st
import validatesl  # Assuming it's in the main directory

def show():
    st.title("Validate Schedule")
    
    if st.session_state.uploaded_doctor_data and st.session_state.uploaded_excluded_data:
        # Use the temp file paths directly
        doctor_data_file = "temp_doctor_data.csv"
        excluded_data_file = "temp_excluded_data.csv"

        results = validatesl.main("schedule.csv", doctor_data_file, excluded_data_file)

        st.subheader("Validation Results")
        st.write(results["validation_results"])
        st.subheader("Weekday Counts")
        st.write(results["weekday_counts"])
        st.subheader("Saturday Counts")
        st.write(results["saturday_counts"])
        st.subheader("Sunday Counts")
        st.write(results["sunday_counts"])
    else:
        st.warning("Please generate the schedule on the Schedule page first.")
