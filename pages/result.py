import streamlit as st

from logic.emission_calculator import (
    calculate_total_emission, 
    category_breakdown, 
    severity_level,
    get_suggestions
)

def show():

    st.title("Carbon Footprint Result")

    raw_data = st.session_state.activities

    # Convert stored data into usable format
    clean_data = {}

    for key, (activity, value) in raw_data.items():
        clean_data[activity] = clean_data.get(activity, 0) + value

    total = calculate_total_emission(clean_data)
    breakdown = category_breakdown(clean_data)
    level = severity_level(total)

    #Shows the total CO2 produced and the level of it
    st.metric("Total CO2 Produced (kg)", round(total, 2))
    
    if level == "Low":  
        st.success(f"Level: **{level}**")
    
    elif level == "Moderate":
        st.info(f"Level: **{level}**")
        
    elif level == "High":
        st.warning(f"Level: **{level}**")
        
    else :
        st.error(f"Level: **{level}**")
    
    st.markdown("---")

    col1, col2, col3 = st.columns(3)
    
    with col1 :
        #Suggestion message
        st.subheader("Suggestions")
        suggestion = get_suggestions(breakdown)
    
        for i in suggestion:
            st.write(f"- {i}")
        

            
    with col2 :
                  
        #Comparison to Malaysian and Global production
        st.subheader("Comparison")
        
        c1,c2,c3 = st.columns(3)
    
        c1.metric("You", round(total, 2))
        c2.metric("Malaysian Avg", 9.1)
        c3.metric("Global Avg", 10.1)
        
        st.markdown("---")
        
        #Equivalent impact to trees and cost in RM
        trees = total / 22
        cost = total * 0.20

        st.subheader("This is equivalent to:")

        st.write(f"🌳 {round(trees)} tress needed")
        st.write(f"💰 RM {round(cost, 2)} carbon offset")
             
    with col3 :
        # Bar Chart to show which activity produced CO2 the most
        st.subheader("Breakdown")
        st.bar_chart(breakdown)
        
    
    st.markdown("---")

    if st.button("Back"):
        st.session_state.page = "input"
        st.rerun()