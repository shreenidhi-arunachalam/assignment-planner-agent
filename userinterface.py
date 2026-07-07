import streamlit as st
from app import get_plan


st.set_page_config(
    page_title="AI Assignment Planner Agent",
    page_icon="",
    layout="wide"
)


st.markdown("""
<style>

.main {
    background-color: #0e1117;
}

.block {
    padding: 16px;
    border-radius: 12px;
    background-color: #1c1f26;
    border: 1px solid #2a2f3a;
    margin-bottom: 12px;
}

.title {
    font-size: 42px;
    font-weight: 700;
}

.subtitle {
    color: #9aa4b2;
    font-size: 16px;
}

.agent-step {
    padding: 8px;
    margin: 5px 0;
    border-left: 4px solid #4f8bf9;
    background-color: #151922;
    border-radius: 8px;
}

</style>
""", unsafe_allow_html=True)



# Title
st.markdown(
    "<div class='title'>AI Assignment Planner Agent</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Turns messy assignments into structured study + execution plans</div>",
    unsafe_allow_html=True
)


st.divider()



# User Input
user_input = st.text_area(
    "Enter your assignment details",
    placeholder="e.g. COMP2010 assignment due July 20 on graphs and algorithms",
    height=120
)



if st.button("Generate plan"):

    if not user_input.strip():
        st.warning("Please enter an assignment first")
        st.stop()


    st.markdown("## Agent Pipeline")


   
    st.markdown(
        "<div class='agent-step'>Step 1: Parsing assignment...</div>",
        unsafe_allow_html=True
    )


    with st.spinner("Planner agent creating plan..."):

        st.markdown(
            "<div class='agent-step'>Step 2: Building structured plan...</div>",
            unsafe_allow_html=True
        )

        result = get_plan(user_input)


        st.markdown(
            "<div class='agent-step'>Step 3: Critic reviewing and refining...</div>",
            unsafe_allow_html=True
        )


        st.markdown(
            "<div class='agent-step'>Step 4: Final agent polishing output...</div>",
            unsafe_allow_html=True
        )


    st.success("Plan generated successfully!")


    st.divider()



    # Layout
    col1, col2 = st.columns([2, 1])


    with col1:

        st.subheader("Generated Plan")


        # Only show final plan
        st.markdown(result["final_plan"])



    with col2:

        st.subheader("Summary Panel")


        st.info("Generated using Gemini Multi-Agent System")


        st.markdown("""
        **Agents Used:**

         Planner Agent  
        - Breaks assignment into tasks  
        - Creates timeline  
        - Estimates workload  


        Critic Agent  
        - Finds weak planning assumptions  
        - Improves structure  
        - Adds missing steps  


         Final Refiner Agent  
        - Improves readability  
        - Removes repetition  
        - Produces final output  
        """)


        st.success("Ready for execution")



    st.divider()



   
    st.download_button(
        label=" Download Plan as Text",
        data=result["final_plan"],
        file_name="assignment_plan.txt",
        mime="text/plain"
    )