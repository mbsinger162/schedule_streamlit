import streamlit as st
import scripts.home
import scripts.schedule
import scripts.validate
import scripts.format

st.set_page_config(
    page_title="Yale PGY2 Resident Call Schedule Generator",
    layout="wide",
)

if 'uploaded_doctor_data' not in st.session_state:
    st.session_state.uploaded_doctor_data = None
if 'uploaded_excluded_data' not in st.session_state:
    st.session_state.uploaded_excluded_data = None

PAGES = {
    "Home": scripts.home,
    "Schedule": scripts.schedule,
    "Validate": scripts.validate,
    "Format for Google Calendar": scripts.format
}


def main():
    st.sidebar.title("Navigation")
    choice = st.sidebar.radio("Go to", list(PAGES.keys()))
    
    # Run the selected page
    page = PAGES[choice]
    page.show()

if __name__ == "__main__":
    main()
