import streamlit as st
import pandas as pd

def main():
    st.markdown("<h1 style='text-align: center; color: white;'>My Streamlit App</h1>", unsafe_allow_html=True)

    # Initializes session state
    if "user" not in st.session_state:
        # Will store the currently logged user
        st.session_state.user = None

    # Case where user is not logged
    menu = ["Admin","Manager","Employee"]
    choice = st.sidebar.selectbox("User",menu)

    if choice == "Admin":
        admid = st.sidebar.text_input("Admin ID")
        passw = st.sidebar.text_input("Password",type='password')

        if st.sidebar.button("Login"):
            result = 1
            if result:
                st.success("Logged In as Admin")
                st.session_state.user = "Admin"
            else:
                st.warning("Incorrect Admin ID/Password")

    elif choice == "Manager":
        manid = st.sidebar.text_input("Manager ID")
        passw = st.sidebar.text_input("Password",type='password')

        if st.sidebar.button("Login"):
            result = 1
            if result:
                st.success("Logged In as Manager")
                st.session_state.user = "Manager"
            else:
                st.warning("Incorrect Manager ID/Password")

    else:
        empid = st.sidebar.text_input("Employee ID")
        passw = st.sidebar.text_input("Password",type='password')

        if st.sidebar.button("Login"):
            result = 1
            if result:
                st.success("Logged In as Employee")
                st.session_state.user = "Employee"
            else:
                st.warning("Incorrect Employee ID/Password")

    # Case where Admin is logged
    if st.session_state.user == "Admin":
        user = st.selectbox("Select User",["Admin","Manager","Employee"])

        if user == "Admin":
            task = st.selectbox("Manage Admin",["View","Add","Delete"])
            if task == "View":
                st.subheader("Admins")
            if task == "Add":
                st.subheader("Add admin")
            if task == "Delete":
                st.subheader("Delete admin")
        elif user == "Manager":
            task = st.selectbox("Manage Manager",["View","Add","Delete"])
            if task == "View":
                st.subheader("Managers")
            if task == "Add":
                st.subheader("Add manager")
            if task == "Delete":
                st.subheader("Delete manager")
        else:
            task = st.selectbox("Manage Employee",["View","Add","Delete"])
            if task == "View":
                st.subheader("Employees")
            if task == "Add":
                st.subheader("Add employee")
            if task == "Delete":
                st.subheader("Delete employee")

    elif st.session_state.user == "Manager":
        st.write("Manager dashboard")

    elif st.session_state.user == "Employee":
        st.write("Employee dashboard")

main()