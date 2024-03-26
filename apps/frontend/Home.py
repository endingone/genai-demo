import streamlit as st

st.header("Azure OpenAI Workbench - Web Frontend")

st.markdown("---")
st.markdown("""
    This engine finds information from the following:
    - 6 PDFs : "Benefit_Options.pdf", "employee_handbook.pdf", "Northwind_Health_Plus_Benefits_Details.pdf", "Northwind_Standard_Benefits_Details.pdf", "PerksPlus.pdf", "role_library.pdf"
    - 5 Books: "Azure_Cognitive_Search_Documentation.pdf", "Boundaries_When_to_Say_Yes_How_to_Say_No_to_Take_Control_of_Your_Life.pdf", "Fundamentals_of_Physics_Textbook.pdf", "Made_To_Stick.pdf", "Pere_Riche_Pere_Pauvre.pdf" (French version of Rich Dad Poor Dad).
    
    **👈 Select a demo from the sidebar** to see an example of a Search Interface, and a Bot Interface.

    ### Want to learn more?
    - Check out [Github Repo](https://github.com/endingone/Azure-AI-Search-Azure-OpenAI-Workbench)
    - Jump into [Azure OpenAI documentation](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/)

"""
)
st.markdown("---")
