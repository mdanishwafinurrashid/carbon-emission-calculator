import streamlit as st
from data.factors import Activities

with st.container():
    
    def show():
        
        st.title("EcoStep 🍂")
        st.caption("Calculate your CO2 daily emission")
        st.markdown("---")
        
        if "rows" not in st.session_state:
            st.session_state.rows = 4

        activities_data = {}
        
        for i in range(st.session_state.rows):

            col1, col2 = st.columns(2)

        #For the input value selectiom rows
            with col1:
                activity = st.selectbox(
                    f"Activity {i+1}",
                    list(Activities.keys()),
                    key=f"activity_{i}"
                )


            with col2:
                    value = st.number_input(
                        "Distance (km)/ Duration (hour)",
                        min_value=0.0,
                        key=f"value_{i}"
                    )

            activities_data[f"{activity}_{i}"] = (activity, value)
            
        col1,col2= st.columns(2)
        
        with col1: 
            #Add button(max 10)
            if st.button("Add Activity"):

                if st.session_state.rows < 10:
                    st.session_state.rows += 1
        
        with col2  :
                #Remove button(min 4)
                if st.button("Remove Activity"):
                
                    if st.session_state.rows > 4:
                        st.session_state.rows -= 1
        
        if st.button("Calculate"):

                st.session_state.activities = activities_data
                st.session_state.page = "output"
                st.rerun()
            
           

        

