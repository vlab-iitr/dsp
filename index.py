import streamlit as st
from streamlit_option_menu import option_menu
# from streamlit.components.v1 import html

from parameter.aim_parameter import aim1
from parameter.pre_test import test1
from parameter.pre_test_ans import pre_ans1
from parameter.pre_test_ans import pre_warning1
from parameter.theory_parameter import content1
# from parameter.procedure import procedure1
from parameter.Signal_Generation_1 import dsp_simulator1
from parameter.post_test import post1
from parameter.post_test_ans import post_ans1
from parameter.post_test_ans import post_warning1
from parameter.refer_parameter import ref1
from parameter.contributors import contri1

from spectrum.aim_spectrum import aim2
from spectrum.pre_test import test2
from spectrum.pre_test_ans import pre_ans2
from spectrum.pre_test_ans import pre_warning2
from spectrum.theory_spectrum import content2
# from spectrum.procedure import procedure2
from spectrum.Power_spec import dsp_simulator2
from spectrum.post_test import post2
from spectrum.post_test_ans import post_ans2
from spectrum.post_test_ans import post_warning2
from spectrum.refer_spectrum import ref2
from spectrum.contributors import contri2

from auto.aim import aim3
from auto.pretest import test3
from auto.pre_test_ans import pre_ans3
from auto.pre_test_ans import pre_warning3
from auto.theory_auto import content3
# from auto.procedure import procedure3
from auto.auto_corelation import dsp_simulator3
from auto.post_test import post3
from auto.post_test_ans import post_ans3
from auto.post_test_ans import post_warning3
from auto.references import ref3
from auto.contributors import contri3

from convolution.aim import aim4
from convolution.pretest import test4
from convolution.pre_test_ans import pre_ans4
from convolution.pre_test_ans import pre_warning4
from convolution.theory_convolution import content4
# from convolution.procedure import procedure4
from convolution.Convolution import dsp_simulator4
from convolution.post_test import post4
from convolution.post_test_ans import post_ans4
from convolution.post_test_ans import post_warning4
from convolution.references import ref4
from convolution.contributors import contri4

from transform.aim import aim5
from transform.pretest import test5
from transform.pre_test_ans import pre_ans5
from transform.pre_test_ans import pre_warning5
# from transform.procedure import procedure5
from transform.theory_transform import content5
from transform.Transforms import dsp_simulator5
from transform.post_test import post5
from transform.post_test_ans import post_ans5
from transform.post_test_ans import post_warning5
from transform.references import ref5
from transform.contributors import contri5

from filters.aim import aim6
from filters.pretest import test6
from filters.pre_test_ans import pre_ans6
from filters.pre_test_ans import pre_warning6
# from filters.procedure import procedure6
from filters.theory_filters import content6
from filters.Filters import dsp_simulator6
from filters.post_test import post6
from filters.post_test_ans import post_ans6
from filters.post_test_ans import post_warning6
from filters.references import ref6
from filters.contributors import contri6

from modulation.aim import aim7
from modulation.pretest import test7
from modulation.pre_test_ans import pre_ans7
from modulation.pre_test_ans import pre_warning7
# from modulation.procedure import procedure7
from modulation.theory_modulation import content7
from modulation.Modulation import dsp_simulator7
from modulation.post_test import post7
from modulation.post_test_ans import post_ans7
from modulation.post_test_ans import post_warning7
from modulation.references import ref7
from modulation.contributors import contri7


st.set_page_config(layout="wide")

if 'active_button' not in st.session_state:
    st.session_state.active_button = None

# Ensure the session state is initialized to store the selected option
if "selected_option" not in st.session_state:
    st.session_state.selected_option = "Statistical Parameters"

    
# Create an option menu for navigation
selected_option = option_menu(
    menu_title=None,  # The title of the menu
    options=
    [
        "Statistical Parameters",
        "Power Spectrum",
        "Autocorrelation",
        "Convolution",
        "Transforms",
        "Filters",
        "Modulation"
    ],  # List of options
    menu_icon="cast",  # Icon for the menu itself
    default_index=0,  # Set the default selected option
    #default_index=["Statistical Parameters","Power Spectrum","Convolution","Transforms","Filters","Modulation"].index(st.session_state.selected_option),  # Set default based on session state
    orientation="horizontal",  
    styles={
        "container":{"padding":"0!important", },
        "nav-link":{
            "font-size":"18px",
            "text-align":"left",
            "margin":"10px",
            "--hover-color":"#D8DBE2",
            "font-family": "'Georgia', serif",
            "width":"200px",
            "color":"black",
            "transition": "color 0.3s ease",  # Add smooth transition
        },
        "nav-link-selected":{"background-color":"#035F8A","font-size":"18px","color":"white","font-weight":"100"}
    }
)

st.markdown(
    """
    <style>

    .clicked {
                background-color: #035F8A; 
        color: white;
        border-color: #035F8A;
        }

    h1
    {
    font-size:32px;
    color: #035F8A;
    }

    /*for sidebar parameters*/
    .stHeading>div>h1 
    {
        font-family: Georgia, serif;
        font-size:20px; 
        color:#035F8A;
    }
    .stSelectbox>label>div>p
    {
        font-size:18px; 
        font-weight:bold;
        margin-top: 10px;
    }
    .stSlider>label>div>p
    {
        font-size:18px; 
        font-weight:bold;
        margin-top: 10px;
    }
    
   

    
    /* for text input */
    .stTextInput>label>div>p
    {
    font-size:18px; 
    font-weight:bold;
    margin-top: 10px;
    }

    
    .stNumberInput>label>div>p
    {
        font-size:18px; 
        font-weight:bold;
        margin-top: 10px;
    }
    .stVerticalBlock{
        gap:0.2rem;
    } 



     /*for questions*/

    .stRadio>label>div>p {
        font-size: 20px;
        font-weight:bold;
    }

    .stRadio{
        margin:10px;
    }

    .stHeading>div>h2 {
            font-size: 20px;
            font-weight: bold;
            color:#035F8A;
            text-align:center;
            margin-bottom:5px;
        }
    .stMarkdown>p {
            border-bottom: 2px solid  #035F8A;
            padding-bottom:10px;
        }

    /* button CSS*/

    .stButton>button
        {
            width: 150px;  /* Set the width of all buttons */
            margin-bottom: 10px;  /* Add space between buttons */   
           
        } 

      
    .stButton{
            align-items: center;
            display: flex;
            justify-content: center;
        }
    .stButton>button:hover{
            border-color: #035F8A;  
            color: #035F8A;  
        }
    .stButton>button:active {
            background-color: #035F8A; 
            color: white;
            border-color: #035F8A; 
        }
        
    .stButton>button:focus:not(:active) {
            background-color: #035F8A; 
            color: white;
            border-color: #035F8A;
        }
    

    /* custom classes for theory content*/
    .my-custom-text
    {
    font-size:38px;
    color: #035F8A;
    font-family: Georgia, serif;     font-weight:bold;
    text-align: center;
    padding: 10px 0px;
    }

    .my-custom-sub-text
    {
    text-align: justify;
    font-size: 18px;
    }

    .my-custom-sub-sub-text
    {
    text-align: justify;
    font-size: 18px;
    margin-left:20px;
    margin-top:20px;
    }
    
    .my-custom-h5-text
    {
    font-weight:bold;
    font-size:20px;
    text-align: justify;
        padding: 15px 0px 15px 0px;
    }

     .my-custom-h3-text
    {
    font-weight:bold;
    font-size:28px;
    text-align: justify;
        padding: 15px 0px 15px 0px;
    }

    .custom-subheader {
    font-weight:bold;
    font-size: 1.75rem;
    padding: 0.5rem 0px 1rem;
    }

    /* table */
    .stTable
    {
    width:50%;
    align-items: center;
    margin:auto;
    }

    [data-testid="stTableStyledTable"]
    {
    text-align:center;
    margin:auto;
    }


    </style>
    """, 
    unsafe_allow_html=True
)

clicked = False

# Display content based on selected option

#------(1)
if selected_option == "Statistical Parameters":
    st.session_state.simulation_clicked2 = False
    st.session_state.pre_clicked2 = False
    st.session_state.post_clicked2 = False

    st.session_state.simulation_clicked3 = False
    st.session_state.pre_clicked3 = False
    st.session_state.post_clicked3 = False

    st.session_state.simulation_clicked4 = False
    st.session_state.pre_clicked4 = False
    st.session_state.post_clicked4 = False

    st.session_state.simulation_clicked5 = False
    st.session_state.pre_clicked5 = False
    st.session_state.post_clicked5 = False

    st.session_state.simulation_clicked6 = False
    st.session_state.pre_clicked6 = False
    st.session_state.post_clicked6 = False

    st.session_state.simulation_clicked7 = False
    st.session_state.pre_clicked7 = False
    st.session_state.post_clicked7 = False
    
    st.sidebar.header('Statistical Parameters')
    aim = st.sidebar.button('Aim', key='aim')
    if aim:
        st.session_state.active_button = 'aim'
        aim1()
        clicked = True
        st.session_state.simulation_clicked1 = False
        st.session_state.pre_clicked1 = False
        st.session_state.post_clicked1 = False 
        st.session_state.pre_ans1 = False
        st.session_state.post_ans1 = False
    
    Theory = st.sidebar.button('Theory', key='Theory')
    if Theory:
        st.session_state.active_button = 'Theory'
        content1()
        clicked=True
        st.session_state.simulation_clicked1 = False
        st.session_state.pre_clicked1 = False
        st.session_state.post_clicked1 = False 
        st.session_state.pre_ans1 = False
        st.session_state.post_ans1 = False
    
    Pretest = st.sidebar.button('Pretest', key='Pretest')
    if Pretest:
        st.session_state.active_button = 'Pretest'
        clicked=True
        st.session_state.simulation_clicked1 = False
        st.session_state.pre_clicked1 = True
        st.session_state.post_clicked1 = False  
        st.session_state.pre_ans1 = False
        st.session_state.post_ans1 = False
    
    # Procedure = st.sidebar.button('Procedure', key='Procedure')
    # if Procedure:
    #     st.session_state.active_button = 'Procedure'
    #     procedure1()
    #     clicked=True
    #     st.session_state.simulation_clicked1 = False
    #     st.session_state.pre_clicked1 = False
    #     st.session_state.post_clicked1 = False 
    #     st.session_state.pre_ans1 = False
    #     st.session_state.post_ans1 = False
    
    Simulation = st.sidebar.button('Simulation', key='Simulation')
    if Simulation:
        st.session_state.active_button = 'Simulation'
        clicked=True
        st.session_state.simulation_clicked1 = True
        st.session_state.pre_clicked1 = False
        st.session_state.post_clicked1 = False 
        st.session_state.pre_ans1 = False
        st.session_state.post_ans1 = False
    
    Posttest = st.sidebar.button('Posttest', key='Posttest')
    if Posttest:
        st.session_state.active_button = 'Posttest'
        clicked=True
        st.session_state.simulation_clicked1 = False
        st.session_state.post_clicked1 = True 
        st.session_state.pre_clicked1 = False
        st.session_state.pre_ans1 = False
        st.session_state.post_ans1 = False
    
    Contributors = st.sidebar.button('Contributors', key='Contributors')
    if Contributors:
        st.session_state.active_button = 'Contributors'
        contri1()
        clicked=True
        st.session_state.simulation_clicked1 = False
        st.session_state.pre_clicked1 = False
        st.session_state.post_clicked1 = False 
        st.session_state.pre_ans1 = False
        st.session_state.post_ans1 = False
        
    References = st.sidebar.button('References', key='References')
    if References:
        st.session_state.active_button = 'References'
        ref1()
        clicked=True
        st.session_state.simulation_clicked1 = False
        st.session_state.pre_clicked1 = False
        st.session_state.post_clicked1 = False 
        st.session_state.pre_ans1 = False
        st.session_state.post_ans1 = False

    # Content for dsp_simulator() should go below the sidebar content
    if getattr(st.session_state, 'simulation_clicked1', False):
        clicked=True
        dsp_simulator1()
             

    def submit_pre_ans1():
        if all(item is not None for item in st.session_state.user_answers):
                st.session_state.pre_clicked1 = False
                st.session_state.pre_ans1 = True
                st.session_state.pre_ans_warning1 = False
        else:
            st.session_state.pre_ans_warning1 = True
            
    if getattr(st.session_state, 'pre_clicked1', False):
        test1()
        clicked=True
        st.session_state.pre_clicked1 = True
        st.button("Submit", on_click=submit_pre_ans1)     

    def restart_pre():
        st.session_state.pre_ans1 = False
        st.session_state.pre_clicked1 = True

    if getattr(st.session_state, 'pre_ans1', False):
        st.session_state.pre_clicked1 = False
        clicked=True
        pre_ans1()
        st.button('Restart', on_click=restart_pre)
  
    if getattr(st.session_state, 'pre_ans_warning1', False):
        clicked=True
        pre_warning1()
        st.session_state.pre_ans_warning1 = False
        
    def submit_post_ans1():
        if all(item is not None for item in st.session_state.user_answers):
                st.session_state.post_clicked1 = False
                st.session_state.post_ans1 = True
                st.session_state.post_ans_warning1 = False
        else:
            st.session_state.post_ans_warning1 = True
            
    if getattr(st.session_state, 'post_clicked1', False):
        post1()
        clicked=True
        st.session_state.post_clicked1 = True
        st.button("Submit", on_click=submit_post_ans1)

    def restart_post():
        st.session_state.post_ans1 = False
        st.session_state.post_clicked1 = True

    if getattr(st.session_state, 'post_ans1', False):
        st.session_state.post_clicked1 = False
        clicked=True
        post_ans1()
        st.button('Restart', on_click=restart_post)
  
    if getattr(st.session_state, 'post_ans_warning1', False):
        clicked=True
        post_warning1()
        st.session_state.post_ans_warning1 = False
    
    if not clicked:
        st.session_state.active_button=''
        st.markdown('<div class="my-custom-text">Generation of Standard Signals and their Statistical Analysis</div>',unsafe_allow_html=True)

#------(2) 
elif selected_option == "Power Spectrum":
    st.session_state.simulation_clicked1 = False
    st.session_state.pre_clicked1 = False
    st.session_state.post_clicked1 = False

    st.session_state.simulation_clicked3 = False
    st.session_state.pre_clicked3 = False
    st.session_state.post_clicked3 = False

    st.session_state.simulation_clicked4 = False
    st.session_state.pre_clicked4 = False
    st.session_state.post_clicked4 = False

    st.session_state.simulation_clicked5 = False
    st.session_state.pre_clicked5 = False
    st.session_state.post_clicked5 = False

    st.session_state.simulation_clicked6 = False
    st.session_state.pre_clicked6 = False
    st.session_state.post_clicked6 = False

    st.session_state.simulation_clicked7 = False
    st.session_state.pre_clicked7 = False
    st.session_state.post_clicked7 = False

    st.sidebar.header('Power Spectrum')
    aim = st.sidebar.button('Aim', key='aim2')
    if aim:
        st.session_state.active_button = 'aim2'
        aim2()
        clicked=True
        st.session_state.pre_clicked2 = False
        st.session_state.post_clicked2 = False 
        st.session_state.simulation_clicked2 = False  # Reset the flag
        st.session_state.pre_ans2 = False
        st.session_state.post_ans2 = False
    
    Theory = st.sidebar.button('Theory', key='Theory2')
    if Theory:
        st.session_state.active_button = 'Theory2'
        content2()
        clicked=True
        st.session_state.pre_clicked2 = False
        st.session_state.post_clicked2 = False 
        st.session_state.simulation_clicked2 = False  # Reset the flag
        st.session_state.pre_ans2 = False
        st.session_state.post_ans2 = False
    
    Pretest = st.sidebar.button('Pretest', key='Pretest2')
    if Pretest:
        st.session_state.active_button = 'Pretest2'
        clicked=True
        st.session_state.pre_clicked2 = True
        st.session_state.post_clicked2 = False 
        st.session_state.simulation_clicked2 = False  # Reset the flag 
        st.session_state.pre_ans2 = False
        st.session_state.post_ans2 = False
    
    # Procedure = st.sidebar.button('Procedure', key='Procedure2')
    # if Procedure:
    #     st.session_state.active_button = 'Procedure2'
    #     procedure2()
    #     clicked=True
    #     st.session_state.pre_clicked2 = False
    #     st.session_state.post_clicked2 = False 
    #     st.session_state.simulation_clicked2 = False  # Reset the flag
    #     st.session_state.pre_ans2 = False
    #     st.session_state.post_ans2 = False
    
    Simulation = st.sidebar.button('Simulation', key='Simulation2')
    if Simulation:
        st.session_state.active_button = 'Simulation2'
        clicked=True
        st.session_state.simulation_clicked2 = True
        st.session_state.pre_clicked2 = False
        st.session_state.post_clicked2 = False 
        st.session_state.pre_ans2 = False
        st.session_state.post_ans2 = False
    
    Posttest = st.sidebar.button('Posttest', key='Posttest2')
    if Posttest:
        st.session_state.active_button = 'Posttest2'
        clicked=True
        st.session_state.post_clicked2 = True 
        st.session_state.pre_clicked2 = False
        st.session_state.simulation_clicked2 = False  # Reset the flag
        st.session_state.pre_ans2 = False
        st.session_state.post_ans2 = False
    
    Contributors = st.sidebar.button('Contributors', key='Contributors2')
    if Contributors:
        st.session_state.active_button = 'Contributors2'
        contri2()
        clicked=True
        st.session_state.simulation_clicked2 = False 
        st.session_state.pre_clicked2 = False
        st.session_state.post_clicked2 = False 
        st.session_state.pre_ans2 = False
        st.session_state.post_ans2 = False

    References = st.sidebar.button('References', key='References2')
    if References:
        st.session_state.active_button = 'References2'
        ref2()
        clicked=True
        st.session_state.simulation_clicked2 = False 
        st.session_state.pre_clicked2 = False
        st.session_state.post_clicked2 = False 
        st.session_state.pre_ans2 = False
        st.session_state.post_ans2 = False


    if getattr(st.session_state, 'simulation_clicked2', False):
        clicked=True
        dsp_simulator2()
    
    def submit_pre_ans2():
        if all(item is not None for item in st.session_state.user_answers):
                st.session_state.pre_clicked2 = False
                st.session_state.pre_ans2 = True
                st.session_state.pre_ans_warning2 = False
        else:
            st.session_state.pre_ans_warning2 = True

    if getattr(st.session_state, 'pre_clicked2', False):
        test2()
        clicked=True
        st.session_state.pre_clicked2 = True
        st.button("Submit", on_click=submit_pre_ans2) 
    
    def restart_pre():
        st.session_state.pre_ans2 = False
        st.session_state.pre_clicked2 = True


    if getattr(st.session_state, 'pre_ans2', False):
        st.session_state.pre_clicked2 = False
        clicked=True
        pre_ans2()
        st.button('Restart', on_click=restart_pre)
  
    if getattr(st.session_state, 'pre_ans_warning2', False):
        clicked=True
        pre_warning2()
        st.session_state.pre_ans_warning2 = False
        
    def submit_post_ans2():
        if all(item is not None for item in st.session_state.user_answers):
                st.session_state.post_clicked2 = False
                st.session_state.post_ans2 = True
                st.session_state.post_ans_warning2 = False
        else:
            st.session_state.post_ans_warning2 = True

    if getattr(st.session_state, 'post_clicked2', False):
        post2()
        clicked=True
        st.session_state.post_clicked2 = True
        st.button("Submit", on_click=submit_post_ans2)

    def restart_post2():
        st.session_state.post_ans2 = False
        st.session_state.post_clicked2 = True

    if getattr(st.session_state, 'post_ans2', False):
        st.session_state.post_clicked2 = False
        clicked=True
        post_ans2()
        st.button('Restart', on_click=restart_post2)
  
    if getattr(st.session_state, 'post_ans_warning2', False):
        clicked=True
        post_warning2()
        st.session_state.post_ans_warning2 = False
    
    if not clicked:
        st.session_state.active_button=''
        st.markdown('<div class="my-custom-text">Study the Power Spectrum Analysis</div>',unsafe_allow_html=True)

#------(3)
elif selected_option == "Autocorrelation":
    st.session_state.simulation_clicked1 = False
    st.session_state.pre_clicked1 = False
    st.session_state.post_clicked1 = False

    st.session_state.simulation_clicked2 = False
    st.session_state.pre_clicked2 = False
    st.session_state.post_clicked2 = False

    st.session_state.simulation_clicked4 = False
    st.session_state.pre_clicked4 = False
    st.session_state.post_clicked4 = False

    st.session_state.simulation_clicked5 = False
    st.session_state.pre_clicked5 = False
    st.session_state.post_clicked5 = False

    st.session_state.simulation_clicked6 = False
    st.session_state.pre_clicked6 = False
    st.session_state.post_clicked6 = False

    st.session_state.simulation_clicked7 = False
    st.session_state.pre_clicked7 = False
    st.session_state.post_clicked7 = False

    st.sidebar.header('Autocorrelation')
    aim = st.sidebar.button('Aim', key='aim3')
    if aim:
        st.session_state.active_button = 'aim3'
        aim3()
        clicked=True
        st.session_state.pre_clicked3 = False
        st.session_state.post_clicked3 = False 
        st.session_state.simulation_clicked3 = False  # Reset the flag
        st.session_state.pre_ans3 = False
        st.session_state.post_ans3 = False
    
    Theory= st.sidebar.button('Theory', key='Theory3')
    if Theory:
        st.session_state.active_button = 'Theory3'
        content3()
        clicked=True
        st.session_state.pre_clicked3 = False
        st.session_state.post_clicked3 = False 
        st.session_state.simulation_clicked3 = False  # Reset the flag
        st.session_state.pre_ans3 = False
        st.session_state.post_ans3 = False
    
    Pretest = st.sidebar.button('Pretest', key='Pretest3')
    if Pretest:
        st.session_state.active_button = 'Pretest3'
        clicked=True
        st.session_state.pre_clicked3 = True
        st.session_state.post_clicked3 = False 
        st.session_state.simulation_clicked3 = False  # Reset the flag 
        st.session_state.pre_ans3 = False
        st.session_state.post_ans3 = False
    
    # Procedure = st.sidebar.button('Procedure', key='Procedure3')
    # if Procedure:
    #     st.session_state.active_button = 'Procedure3'
    #     procedure3()
    #     clicked=True
    #     st.session_state.pre_clicked3 = False
    #     st.session_state.post_clicked3 = False 
    #     st.session_state.simulation_clicked3 = False  # Reset the flag
    #     st.session_state.pre_ans3 = False
    #     st.session_state.post_ans3 = False
    
    Simulation = st.sidebar.button('Simulation', key='Simulation3')
    if Simulation:
        st.session_state.active_button = 'Simulation3'
        clicked=True
        st.session_state.simulation_clicked3 = True
        st.session_state.pre_clicked3 = False
        st.session_state.post_clicked3 = False 
        st.session_state.pre_ans3 = False
        st.session_state.post_ans3 = False
    
    Posttest = st.sidebar.button('Posttest', key='Posttest3')
    if Posttest:
        st.session_state.active_button = 'Posttest3'
        clicked=True
        st.session_state.post_clicked3 = True 
        st.session_state.pre_clicked3 = False
        st.session_state.simulation_clicked3 = False  # Reset the flag
        st.session_state.pre_ans3 = False
        st.session_state.post_ans3 = False
    
    Contributors = st.sidebar.button('Contributors', key='Contributors3')
    if Contributors:
        st.session_state.active_button = 'Contributors3'
        contri3()
        clicked=True
        st.session_state.simulation_clicked3 = False 
        st.session_state.pre_clicked3 = False
        st.session_state.post_clicked3 = False 
        st.session_state.pre_ans3 = False
        st.session_state.post_ans3 = False

    References = st.sidebar.button('References', key='References3')
    if References:
        st.session_state.active_button = 'References3'
        ref3()
        clicked=True
        st.session_state.simulation_clicked3 = False 
        st.session_state.pre_clicked3 = False
        st.session_state.post_clicked3 = False 
        st.session_state.pre_ans3 = False
        st.session_state.post_ans3 = False

    if getattr(st.session_state, 'simulation_clicked3', False):
        clicked=True
        dsp_simulator3()
    
    def submit_pre_ans3():
        if all(item is not None for item in st.session_state.user_answers):
                st.session_state.pre_clicked3 = False
                st.session_state.pre_ans3 = True
                st.session_state.pre_ans_warning3 = False
        else:
            st.session_state.pre_ans_warning3 = True
            

    if getattr(st.session_state, 'pre_clicked3', False):
        test3()
        clicked=True
        st.session_state.pre_clicked3 = True
        st.button("Submit", on_click=submit_pre_ans3)     

    def restart_pre():
        st.session_state.pre_ans3 = False
        st.session_state.pre_clicked3 = True


    if getattr(st.session_state, 'pre_ans3', False):
        st.session_state.pre_clicked3 = False
        clicked=True
        pre_ans3()
        st.button('Restart', on_click=restart_pre)
  
    if getattr(st.session_state, 'pre_ans_warning3', False):
        clicked=True
        pre_warning3()
        st.session_state.pre_ans_warning3 = False
        
    def submit_post_ans3():
        if all(item is not None for item in st.session_state.user_answers):
                st.session_state.post_clicked3 = False
                st.session_state.post_ans3 = True
                st.session_state.post_ans_warning3 = False
        else:
            st.session_state.post_ans_warning3 = True
            
    if getattr(st.session_state, 'post_clicked3', False):
        post3()
        clicked=True
        st.session_state.post_clicked3 = True
        st.button("Submit", on_click=submit_post_ans3)

    def restart_post():
        st.session_state.post_ans3 = False
        st.session_state.post_clicked3 = True


    if getattr(st.session_state, 'post_ans3', False):
        st.session_state.post_clicked3 = False
        clicked=True
        post_ans3()
        st.button('Restart', on_click=restart_post)
  
    if getattr(st.session_state, 'post_ans_warning3', False):
        clicked=True
        post_warning3()
        st.session_state.post_ans_warning3 = False

    if not clicked:
        st.session_state.active_button=''
        st.markdown('<div class="my-custom-text">Study the Autocorrelation Analysis</div>',unsafe_allow_html=True)

                
#------(4)
elif selected_option == "Convolution":
    st.session_state.simulation_clicked1 = False
    st.session_state.pre_clicked1 = False
    st.session_state.post_clicked1 = False

    st.session_state.simulation_clicked2 = False
    st.session_state.pre_clicked2 = False
    st.session_state.post_clicked2 = False

    st.session_state.simulation_clicked3 = False
    st.session_state.pre_clicked3 = False
    st.session_state.post_clicked3 = False

    st.session_state.simulation_clicked5 = False
    st.session_state.pre_clicked5 = False
    st.session_state.post_clicked5 = False

    st.session_state.simulation_clicked6 = False
    st.session_state.pre_clicked6 = False
    st.session_state.post_clicked6 = False

    st.session_state.simulation_clicked7 = False
    st.session_state.pre_clicked7 = False
    st.session_state.post_clicked7 = False

    st.sidebar.header('Convolution')
    aim = st.sidebar.button('Aim', key='aim4')
    if aim:
        st.session_state.active_button = 'aim4'
        aim4()
        clicked=True
        st.session_state.pre_clicked4 = False
        st.session_state.post_clicked4 = False 
        st.session_state.simulation_clicked4 = False
        st.session_state.pre_ans4 = False
        st.session_state.post_ans4 = False
    
    Theory = st.sidebar.button('Theory', key='Theory4')
    if Theory:
        st.session_state.active_button = 'Theory4'
        content4()
        clicked=True
        st.session_state.pre_clicked4 = False
        st.session_state.post_clicked4 = False 
        st.session_state.simulation_clicked4 = False
        st.session_state.pre_ans4 = False
        st.session_state.post_ans4 = False
    
    Pretest = st.sidebar.button('Pretest', key='Pretest4')
    if Pretest:
        st.session_state.active_button = 'Pretest4'
        clicked=True
        st.session_state.pre_clicked4 = True
        st.session_state.post_clicked4 = False 
        st.session_state.simulation_clicked4 = False
        st.session_state.pre_ans4 = False
        st.session_state.post_ans4 = False 
    
    # Procedure = st.sidebar.button('Procedure', key='Procedure4')
    # if Procedure:
    #     st.session_state.active_button = 'Procedure4'
    #     procedure4()
    #     clicked=True
    #     st.session_state.pre_clicked4 = False
    #     st.session_state.post_clicked4 = False 
    #     st.session_state.simulation_clicked4 = False
    #     st.session_state.pre_ans4 = False
    #     st.session_state.post_ans4 = False
    
    Simulation = st.sidebar.button('Simulation', key='Simulation4')
    if Simulation:
        st.session_state.active_button = 'Simulation4'
        clicked=True
        st.session_state.simulation_clicked4 = True
        st.session_state.pre_clicked4 = False
        st.session_state.post_clicked4 = False 
        st.session_state.pre_ans4 = False
        st.session_state.post_ans4 = False
    
    Posttest = st.sidebar.button('Posttest', key='Posttest4')
    if Posttest:
        st.session_state.active_button = 'Posttest4'
        clicked=True
        st.session_state.post_clicked4 = True 
        st.session_state.pre_clicked4 = False
        st.session_state.simulation_clicked4 = False
        st.session_state.pre_ans4 = False
        st.session_state.post_ans4 = False
    
    Contributors = st.sidebar.button('Contributors', key='Contributors4')
    if Contributors:
        st.session_state.active_button = 'Contributors4'
        contri4()
        clicked=True
        st.session_state.pre_clicked4 = False
        st.session_state.post_clicked4 = False 
        st.session_state.simulation_clicked4 = False
        st.session_state.pre_ans4 = False
        st.session_state.post_ans4 = False

    References = st.sidebar.button('References', key='References4')
    if References:
        st.session_state.active_button = 'References4'
        ref4()
        clicked=True
        st.session_state.pre_clicked4 = False
        st.session_state.post_clicked4 = False 
        st.session_state.simulation_clicked4 = False
        st.session_state.pre_ans4 = False
        st.session_state.post_ans4 = False

        # Content for dsp_simulator() should go below the sidebar content
    if getattr(st.session_state, 'simulation_clicked4', False):
        clicked=True
        dsp_simulator4()
    
    def submit_pre_ans4():
        if all(item is not None for item in st.session_state.user_answers):
                st.session_state.pre_clicked4 = False
                st.session_state.pre_ans4 = True
                st.session_state.pre_ans_warning4 = False
        else:
            st.session_state.pre_ans_warning4 = True
            

    if getattr(st.session_state, 'pre_clicked4', False):
        test4()
        clicked=True
        st.session_state.pre_clicked4 = True
        st.button("Submit", on_click=submit_pre_ans4)     

    def restart_pre():
        st.session_state.pre_ans4 = False
        st.session_state.pre_clicked4 = True


    if getattr(st.session_state, 'pre_ans4', False):
        st.session_state.pre_clicked4 = False
        clicked=True
        pre_ans4()
        st.button('Restart', on_click=restart_pre)
  
    if getattr(st.session_state, 'pre_ans_warning4', False):
        clicked=True
        pre_warning4()
        st.session_state.pre_ans_warning4 = False
        
    def submit_post_ans4():
        if all(item is not None for item in st.session_state.user_answers):
                st.session_state.post_clicked4 = False
                st.session_state.post_ans4 = True
                st.session_state.post_ans_warning4 = False
        else:
            st.session_state.post_ans_warning4 = True
            
    if getattr(st.session_state, 'post_clicked4', False):
        post4()
        clicked=True
        st.session_state.post_clicked4 = True
        st.button("Submit", on_click=submit_post_ans4)

    def restart_post():
        st.session_state.post_ans4 = False
        st.session_state.post_clicked4 = True


    if getattr(st.session_state, 'post_ans4', False):
        st.session_state.post_clicked4 = False
        clicked=True
        post_ans4()
        st.button('Restart', on_click=restart_post)
  
    if getattr(st.session_state, 'post_ans_warning4', False):
        clicked=True
        post_warning4()
        st.session_state.post_ans_warning4 = False
    
    if not clicked:
        st.session_state.active_button=''
        st.markdown('<div class="my-custom-text">Study the Linear and Circular Convolution of Two Signals</div>',unsafe_allow_html=True)
     
#------(5)
elif selected_option == "Transforms":
    st.session_state.simulation_clicked1 = False
    st.session_state.pre_clicked1 = False
    st.session_state.post_clicked1 = False

    st.session_state.simulation_clicked2 = False
    st.session_state.pre_clicked2 = False
    st.session_state.post_clicked2 = False

    st.session_state.simulation_clicked3 = False
    st.session_state.pre_clicked3 = False
    st.session_state.post_clicked3 = False

    st.session_state.simulation_clicked4 = False
    st.session_state.pre_clicked4 = False
    st.session_state.post_clicked4 = False

    st.session_state.simulation_clicked6 = False
    st.session_state.pre_clicked6 = False
    st.session_state.post_clicked6 = False

    st.session_state.simulation_clicked7 = False
    st.session_state.pre_clicked7 = False
    st.session_state.post_clicked7 = False

    st.sidebar.header('Transforms')
    aim = st.sidebar.button('Aim', key='aim5')
    if aim:
        st.session_state.active_button = 'aim5'
        aim5()
        clicked=True
        st.session_state.pre_clicked5 = False
        st.session_state.post_clicked5 = False
        st.session_state.simulation_clicked5 = False 
        st.session_state.pre_ans5 = False
        st.session_state.post_ans5 = False
    
    Theory = st.sidebar.button('Theory', key='Theory5')
    if Theory:
        st.session_state.active_button = 'Theory5'
        content5()
        clicked=True
        st.session_state.pre_clicked5 = False
        st.session_state.post_clicked5 = False 
        st.session_state.simulation_clicked5 = False
        st.session_state.pre_ans5 = False
        st.session_state.post_ans5 = False
    
    Pretest = st.sidebar.button('Pretest', key='Pretest5')
    if Pretest:
        st.session_state.active_button = 'Pretest5'
        clicked=True
        st.session_state.pre_clicked5 = True
        st.session_state.post_clicked5 = False 
        st.session_state.simulation_clicked5 = False 
        st.session_state.pre_ans5 = False
        st.session_state.post_ans5 = False
    
    # Procedure = st.sidebar.button('Procedure', key='Procedure5')
    # if Procedure:
    #     st.session_state.active_button = 'Procedure5'
    #     procedure5()
    #     clicked=True
    #     st.session_state.pre_clicked5 = False
    #     st.session_state.post_clicked5 = False 
    #     st.session_state.simulation_clicked5 = False
    #     st.session_state.pre_ans5 = False
    #     st.session_state.post_ans5 = False
    
    Simulation = st.sidebar.button('Simulation', key='Simulation5')
    if Simulation:
        st.session_state.active_button = 'Simulation5'
        clicked=True
        st.session_state.simulation_clicked5 = True
        st.session_state.pre_clicked5 = False
        st.session_state.post_clicked5 = False 
        st.session_state.pre_ans5 = False
        st.session_state.post_ans5 = False
    
    Posttest = st.sidebar.button('Posttest', key='Posttest5')
    if Posttest:
        st.session_state.active_button = 'Posttest5'
        clicked=True
        st.session_state.post_clicked5 = True 
        st.session_state.pre_clicked5 = False
        st.session_state.simulation_clicked5 = False
        st.session_state.pre_ans5 = False
        st.session_state.post_ans5 = False
    
    Contributors = st.sidebar.button('Contributors', key='Contributors5')
    if Contributors:
        st.session_state.active_button = 'Contributors5'
        contri5()
        clicked=True
        st.session_state.pre_clicked5 = False
        st.session_state.post_clicked5 = False 
        st.session_state.simulation_clicked5 = False
        st.session_state.pre_ans5 = False
        st.session_state.post_ans5 = False

    References = st.sidebar.button('References', key='References5')
    if References:
        st.session_state.active_button = 'References5'
        ref5()
        clicked=True
        st.session_state.pre_clicked5 = False
        st.session_state.post_clicked5 = False 
        st.session_state.simulation_clicked5 = False
        st.session_state.pre_ans5 = False
        st.session_state.post_ans5 = False

    
        # Content for dsp_simulator() should go below the sidebar content
    if getattr(st.session_state, 'simulation_clicked5', False):
        clicked = True  
        dsp_simulator5()
    
    def submit_pre_ans5():
        if all(item is not None for item in st.session_state.user_answers):
                st.session_state.pre_clicked5 = False
                st.session_state.pre_ans5 = True
                st.session_state.pre_ans_warning5 = False
        else:
            st.session_state.pre_ans_warning5 = True
            

    if getattr(st.session_state, 'pre_clicked5', False):
        test5()
        clicked=True
        st.session_state.pre_clicked5 = True
        st.button("Submit", on_click=submit_pre_ans5)     

    def restart_pre():
        st.session_state.pre_ans5 = False
        st.session_state.pre_clicked5 = True


    if getattr(st.session_state, 'pre_ans5', False):
        st.session_state.pre_clicked5 = False
        clicked=True
        pre_ans5()
        st.button('Restart', on_click=restart_pre)
  
    if getattr(st.session_state, 'pre_ans_warning5', False):
        clicked=True
        pre_warning5()
        st.session_state.pre_ans_warning5 = False
        
    def submit_post_ans5():
        if all(item is not None for item in st.session_state.user_answers):
                st.session_state.post_clicked5 = False
                st.session_state.post_ans5 = True
                st.session_state.post_ans_warning5 = False
        else:
            st.session_state.post_ans_warning5 = True
            
    if getattr(st.session_state, 'post_clicked5', False):
        post5()
        clicked=True
        st.session_state.post_clicked5 = True
        st.button("Submit", on_click=submit_post_ans5)

    def restart_post():
        st.session_state.post_ans5 = False
        st.session_state.post_clicked5 = True


    if getattr(st.session_state, 'post_ans5', False):
        st.session_state.post_clicked5 = False
        clicked=True
        post_ans5()
        st.button('Restart', on_click=restart_post)
  
    if getattr(st.session_state, 'post_ans_warning5', False):
        clicked=True
        post_warning5()
        st.session_state.post_ans_warning5 = False

    if not clicked:
        st.session_state.active_button=''
        st.markdown('<div class="my-custom-text">Spectral Analysis of Signals using Signal Transform Functions</div>',unsafe_allow_html=True)

#------(6)
elif selected_option == "Filters":
    st.session_state.simulation_clicked1 = False
    st.session_state.pre_clicked1 = False
    st.session_state.post_clicked1 = False
    
    st.session_state.simulation_clicked2 = False
    st.session_state.pre_clicked2 = False
    st.session_state.post_clicked2 = False

    st.session_state.simulation_clicked3 = False
    st.session_state.pre_clicked3 = False
    st.session_state.post_clicked3 = False

    st.session_state.simulation_clicked4 = False
    st.session_state.pre_clicked4 = False
    st.session_state.post_clicked4 = False

    st.session_state.simulation_clicked5 = False
    st.session_state.pre_clicked5 = False
    st.session_state.post_clicked5 = False

    st.session_state.simulation_clicked7 = False
    st.session_state.pre_clicked7 = False
    st.session_state.post_clicked7 = False
    
    st.sidebar.header('Filters')
    aim = st.sidebar.button('Aim', key='aim6')
    if aim:
        st.session_state.active_button = 'aim6'
        aim6()
        clicked=True
        st.session_state.pre_clicked6 = False
        st.session_state.post_clicked6 = False 
        st.session_state.simulation_clicked6 = False
        st.session_state.pre_ans6 = False
        st.session_state.post_ans6 = False
    
    Theory = st.sidebar.button('Theory', key='Theory6')
    if Theory:
        st.session_state.active_button = 'Theory6'
        content6()
        clicked=True
        st.session_state.pre_clicked6 = False
        st.session_state.post_clicked6 = False 
        st.session_state.simulation_clicked6 = False
        st.session_state.pre_ans6 = False
        st.session_state.post_ans6 = False
    
    Pretest = st.sidebar.button('Pretest', key='Pretest6')
    if Pretest:
        st.session_state.active_button = 'Pretest6'
        clicked=True
        st.session_state.pre_clicked6 = True
        st.session_state.post_clicked6 = False  
        st.session_state.simulation_clicked6 = False
        st.session_state.pre_ans6 = False
        st.session_state.post_ans6 = False
    
    # Procedure = st.sidebar.button('Procedure', key='Procedure6')
    # if Procedure:
    #     st.session_state.active_button = 'Procedure6'
    #     procedure6()
    #     clicked=True
    #     st.session_state.pre_clicked6 = False
    #     st.session_state.post_clicked6 = False 
    #     st.session_state.simulation_clicked6 = False
    #     st.session_state.pre_ans6 = False
    #     st.session_state.post_ans6 = False
    
    Simulation = st.sidebar.button('Simulation', key='Simulation6')
    if Simulation:
        st.session_state.active_button = 'Simulation6'
        clicked=True
        st.session_state.simulation_clicked6 = True
        st.session_state.pre_clicked6 = False
        st.session_state.post_clicked6 = False 
        st.session_state.pre_ans6 = False
        st.session_state.post_ans6 = False
    
    Posttest = st.sidebar.button('Posttest', key='Posttest6')
    if Posttest:
        st.session_state.active_button = 'Posttest6'
        clicked=True
        st.session_state.post_clicked6 = True 
        st.session_state.pre_clicked6 = False
        st.session_state.simulation_clicked6 = False
        st.session_state.pre_ans6 = False
        st.session_state.post_ans6 = False
    
    Contributors = st.sidebar.button('Contributors', key='Contributors6')
    if Contributors:
        st.session_state.active_button = 'Contributors6'
        contri6()
        clicked=True
        st.session_state.pre_clicked6 = False
        st.session_state.post_clicked6 = False 
        st.session_state.simulation_clicked6 = False
        st.session_state.pre_ans6 = False
        st.session_state.post_ans6 = False

    References = st.sidebar.button('References', key='References6')
    if References:
        st.session_state.active_button = 'References6'
        ref6()
        clicked=True
        st.session_state.pre_clicked6 = False
        st.session_state.post_clicked6 = False 
        st.session_state.simulation_clicked6 = False
        st.session_state.pre_ans6 = False
        st.session_state.post_ans6 = False

    

        # Content for dsp_simulator() should go below the sidebar content
    
    if getattr(st.session_state, 'simulation_clicked6', False):
        clicked = True  
        dsp_simulator6()

    def submit_pre_ans6():
        if all(item is not None for item in st.session_state.user_answers):
                st.session_state.pre_clicked6 = False
                st.session_state.pre_ans6 = True
                st.session_state.pre_ans_warning6 = False
        else:
            st.session_state.pre_ans_warning6 = True
            

    if getattr(st.session_state, 'pre_clicked6', False):
        test6()
        clicked=True
        st.session_state.pre_clicked6 = True
        st.button("Submit", on_click=submit_pre_ans6)     

    def restart_pre():
        st.session_state.pre_ans6 = False
        st.session_state.pre_clicked6 = True


    if getattr(st.session_state, 'pre_ans6', False):
        st.session_state.pre_clicked6 = False
        clicked=True
        pre_ans6()
        st.button('Restart', on_click=restart_pre)
  
    if getattr(st.session_state, 'pre_ans_warning6', False):
        clicked=True
        pre_warning6()
        st.session_state.pre_ans_warning6 = False
        
    def submit_post_ans6():
        if all(item is not None for item in st.session_state.user_answers):
                st.session_state.post_clicked6 = False
                st.session_state.post_ans6 = True
                st.session_state.post_ans_warning6 = False
        else:
            st.session_state.post_ans_warning6 = True
            
    if getattr(st.session_state, 'post_clicked6', False):
        post6()
        clicked=True
        st.session_state.post_clicked6 = True
        st.button("Submit", on_click=submit_post_ans6)

    def restart_post():
        st.session_state.post_ans6 = False
        st.session_state.post_clicked6 = True


    if getattr(st.session_state, 'post_ans6', False):
        st.session_state.post_clicked6 = False
        clicked=True
        post_ans6()
        st.button('Restart', on_click=restart_post)
  
    if getattr(st.session_state, 'post_ans_warning6', False):
        clicked=True
        post_warning6()
        st.session_state.post_ans_warning6 = False
    if not clicked:
        st.session_state.active_button=''
        st.markdown('<div class="my-custom-text">Design of FIR and IIR Filters and Demonstrate the Filtering Operation</div>',unsafe_allow_html=True)
    
#------(7)
elif selected_option == "Modulation":
    st.session_state.simulation_clicked1 = False
    st.session_state.pre_clicked1 = False
    st.session_state.post_clicked1 = False
    
    st.session_state.simulation_clicked2 = False
    st.session_state.pre_clicked2 = False
    st.session_state.post_clicked2 = False

    st.session_state.simulation_clicked3 = False
    st.session_state.pre_clicked3 = False
    st.session_state.post_clicked3 = False

    st.session_state.simulation_clicked4 = False
    st.session_state.pre_clicked4 = False
    st.session_state.post_clicked4 = False

    st.session_state.simulation_clicked5 = False
    st.session_state.pre_clicked5 = False
    st.session_state.post_clicked5 = False

    st.session_state.simulation_clicked6 = False
    st.session_state.pre_clicked6 = False
    st.session_state.post_clicked6 = False

    st.sidebar.header('Modulation')
    
    aim = st.sidebar.button('Aim', key='aim7')
    if aim:
        st.session_state.active_button = 'aim7'
        aim7()
        clicked=True
        st.session_state.pre_clicked7 = False
        st.session_state.post_clicked7 = False 
        st.session_state.simulation_clicked7 = False
        st.session_state.pre_ans7 = False
        st.session_state.post_ans7 = False
    
    Theory = st.sidebar.button('Theory', key='Theory7')
    if Theory:
        st.session_state.active_button = 'Theory7'
        content7()
        clicked=True
        st.session_state.pre_clicked7 = False
        st.session_state.post_clicked7 = False 
        st.session_state.simulation_clicked7 = False
        st.session_state.pre_ans7 = False
        st.session_state.post_ans7 = False
    
    Pretest = st.sidebar.button('Pretest', key='Pretest7')
    if Pretest:
        st.session_state.active_button = 'Pretest7'
        clicked=True
        st.session_state.pre_clicked7 = True
        st.session_state.post_clicked7 = False  
        st.session_state.simulation_clicked7 = False
        st.session_state.pre_ans7 = False
        st.session_state.post_ans7 = False
   
    # Procedure = st.sidebar.button('Procedure', key='Procedure7')
    # if Procedure:
    #     st.session_state.active_button = 'Procedure7'
    #     procedure7()
    #     clicked=True
    #     st.session_state.pre_clicked7 = False
    #     st.session_state.post_clicked7 = False
    #     st.session_state.simulation_clicked7 = False 
    #     st.session_state.pre_ans7 = False
    #     st.session_state.post_ans7 = False
    
    Simulation = st.sidebar.button('Simulation', key='Simulation7')
    if Simulation:
        st.session_state.active_button = 'Simulation7'
        clicked=True
        st.session_state.simulation_clicked7 = True
        st.session_state.pre_clicked7 = False
        st.session_state.post_clicked7 = False 
        st.session_state.pre_ans7 = False
        st.session_state.post_ans7 = False
    
    Posttest = st.sidebar.button('Posttest', key='Posttest7')
    if Posttest:
        st.session_state.active_button = 'Posttest7'
        clicked=True
        st.session_state.post_clicked7 = True 
        st.session_state.pre_clicked7 = False
        st.session_state.simulation_clicked7 = False
        st.session_state.pre_ans7 = False
        st.session_state.post_ans7 = False
    
    Contributors = st.sidebar.button('Contributors', key='Contributors7')
    if Contributors:
        st.session_state.active_button = 'Contributors7'
        contri7()
        clicked=True
        st.session_state.pre_clicked7 = False
        st.session_state.post_clicked7 = False
        st.session_state.simulation_clicked7 = False 
        st.session_state.pre_ans7 = False
        st.session_state.post_ans7 = False

    References = st.sidebar.button('References', key='References7')
    if References:
        st.session_state.active_button = 'References7'
        ref7()
        clicked=True
        st.session_state.pre_clicked7 = False
        st.session_state.post_clicked7 = False
        st.session_state.simulation_clicked7 = False 
        st.session_state.pre_ans7 = False
        st.session_state.post_ans7 = False


    # Content for dsp_simulator() should go below the sidebar content
    if getattr(st.session_state, 'simulation_clicked7', False):
        clicked = True  # Reset the flag
        dsp_simulator7()
    
    def submit_pre_ans7():
        if all(item is not None for item in st.session_state.user_answers):
                st.session_state.pre_clicked7 = False
                st.session_state.pre_ans7 = True
                st.session_state.pre_ans_warning7 = False
        else:
            st.session_state.pre_ans_warning7 = True
            

    if getattr(st.session_state, 'pre_clicked7', False):
        test7()
        clicked=True
        st.session_state.pre_clicked7 = True
        st.button("Submit", on_click=submit_pre_ans7)     

    def restart_pre():
        st.session_state.pre_ans7 = False
        st.session_state.pre_clicked7 = True


    if getattr(st.session_state, 'pre_ans7', False):
        st.session_state.pre_clicked7 = False
        clicked=True
        pre_ans7()
        st.button('Restart', on_click=restart_pre)
  
    if getattr(st.session_state, 'pre_ans_warning7', False):
        clicked=True
        pre_warning7()
        st.session_state.pre_ans_warning7 = False
        
    def submit_post_ans7():
        if all(item is not None for item in st.session_state.user_answers):
                st.session_state.post_clicked7 = False
                st.session_state.post_ans7 = True
                st.session_state.post_ans_warning7 = False
        else:
            st.session_state.post_ans_warning7 = True
            
    if getattr(st.session_state, 'post_clicked7', False):
        post7()
        clicked=True
        st.session_state.post_clicked7 = True
        st.button("Submit", on_click=submit_post_ans7)

    def restart_post():
        st.session_state.post_ans7 = False
        st.session_state.post_clicked7 = True

    if getattr(st.session_state, 'post_ans7', False):
        st.session_state.post_clicked7 = False
        clicked=True
        post_ans7()
        st.button('Restart', on_click=restart_post)
  
    if getattr(st.session_state, 'post_ans_warning7', False):
        clicked=True
        post_warning7()
        st.session_state.post_ans_warning7 = False
    
    if not clicked:
        st.session_state.active_button=''
        st.markdown('<div class="my-custom-text">Study and Demonstrate the Amplitude, Frequency and Phase Modulation</div>',unsafe_allow_html=True)
                
                

if st.session_state.active_button == 'aim':
        cs="""
         <style>
         .st-key-aim>.stButton>button {
        background-color: #035F8A; 
            color: white;
            border-color: #035F8A;
        }</style>"""

        st.markdown(cs, unsafe_allow_html=True)

elif st.session_state.active_button == 'Theory':
        cs="""
         <style>
         .st-key-Theory>.stButton>button {
        background-color: #035F8A; 
            color: white;
            border-color: #035F8A;
        }</style>"""

        st.markdown(cs, unsafe_allow_html=True)     

elif st.session_state.active_button == 'Pretest':
        cs="""
         <style>
         .st-key-Pretest>.stButton>button {
        background-color: #035F8A; 
            color: white;
            border-color: #035F8A;
        }</style>"""

        st.markdown(cs, unsafe_allow_html=True)  
    
# elif st.session_state.active_button == 'Procedure':
#         cs="""
#          <style>
#          .st-key-Procedure>.stButton>button {
#         background-color: #035F8A; 
#             color: white;
#             border-color: #035F8A;
#         }</style>"""

#         st.markdown(cs, unsafe_allow_html=True)  

elif st.session_state.active_button == 'Simulation':
        cs="""
         <style>
         .st-key-Simulation>.stButton>button {
        background-color: #035F8A; 
            color: white;
            border-color: #035F8A;
        }</style>"""

        st.markdown(cs, unsafe_allow_html=True)  

elif st.session_state.active_button == 'Posttest':
        cs="""
         <style>
         .st-key-Posttest>.stButton>button {
        background-color: #035F8A; 
            color: white;
            border-color: #035F8A;
        }</style>"""

        st.markdown(cs, unsafe_allow_html=True) 

elif st.session_state.active_button == 'Contributors':
        cs="""
         <style>
         .st-key-Contributors>.stButton>button {
        background-color: #035F8A; 
            color: white;
            border-color: #035F8A;
        }</style>"""

        st.markdown(cs, unsafe_allow_html=True) 

elif st.session_state.active_button == 'References':
        cs="""
         <style>
         .st-key-References>.stButton>button {
        background-color: #035F8A; 
            color: white;
            border-color: #035F8A;
        }</style>"""

        st.markdown(cs, unsafe_allow_html=True) 


elif st.session_state.active_button == 'aim2':
        cs="""
         <style>
         .st-key-aim2>.stButton>button {
        background-color: #035F8A; 
            color: white;
            border-color: #035F8A;
        }</style>"""

        st.markdown(cs, unsafe_allow_html=True)

elif st.session_state.active_button == 'Theory2':
        cs="""
         <style>
         .st-key-Theory2>.stButton>button {
        background-color: #035F8A; 
            color: white;
            border-color: #035F8A;
        }</style>"""

        st.markdown(cs, unsafe_allow_html=True)     

elif st.session_state.active_button == 'Pretest2':
        cs="""
         <style>
         .st-key-Pretest2>.stButton>button {
        background-color: #035F8A; 
            color: white;
            border-color: #035F8A;
        }</style>"""

        st.markdown(cs, unsafe_allow_html=True)  
    
# elif st.session_state.active_button == 'Procedure2':
#         cs="""
#          <style>
#          .st-key-Procedure2>.stButton>button {
#         background-color: #035F8A; 
#             color: white;
#             border-color: #035F8A;
#         }</style>"""

#         st.markdown(cs, unsafe_allow_html=True)  

elif st.session_state.active_button == 'Simulation2':
        cs="""
         <style>
         .st-key-Simulation2>.stButton>button {
        background-color: #035F8A; 
            color: white;
            border-color: #035F8A;
        }</style>"""

        st.markdown(cs, unsafe_allow_html=True)  

elif st.session_state.active_button == 'Posttest2':
        cs="""
         <style>
         .st-key-Posttest2>.stButton>button {
        background-color: #035F8A; 
            color: white;
            border-color: #035F8A;
        }</style>"""

        st.markdown(cs, unsafe_allow_html=True) 

elif st.session_state.active_button == 'Contributors2':
        cs="""
         <style>
         .st-key-Contributors2>.stButton>button {
        background-color: #035F8A; 
            color: white;
            border-color: #035F8A;
        }</style>"""

        st.markdown(cs, unsafe_allow_html=True) 

elif st.session_state.active_button == 'References2':
      cs="""
         <style>
         .st-key-References2>.stButton>button {
        background-color: #035F8A; 
            color: white;
            border-color: #035F8A;
        }</style>"""
      st.markdown(cs, unsafe_allow_html=True) 


if st.session_state.active_button == 'aim3':
        cs="""
         <style>
         .st-key-aim3>.stButton>button {
        background-color: #035F8A; 
            color: white;
            border-color: #035F8A;
        }</style>"""

        st.markdown(cs, unsafe_allow_html=True)

elif st.session_state.active_button == 'Theory3':
        cs="""
         <style>
         .st-key-Theory3>.stButton>button {
        background-color: #035F8A; 
            color: white;
            border-color: #035F8A;
        }</style>"""

        st.markdown(cs, unsafe_allow_html=True)     

elif st.session_state.active_button == 'Pretest3':
        cs="""
         <style>
         .st-key-Pretest3>.stButton>button {
        background-color: #035F8A; 
            color: white;
            border-color: #035F8A;
        }</style>"""

        st.markdown(cs, unsafe_allow_html=True)  
    
# elif st.session_state.active_button == 'Procedure3':
#         cs="""
#          <style>
#          .st-key-Procedure3>.stButton>button {
#         background-color: #035F8A; 
#             color: white;
#             border-color: #035F8A;
#         }</style>"""

#         st.markdown(cs, unsafe_allow_html=True)  

elif st.session_state.active_button == 'Simulation3':
        cs="""
         <style>
         .st-key-Simulation3>.stButton>button {
        background-color: #035F8A; 
            color: white;
            border-color: #035F8A;
        }</style>"""

        st.markdown(cs, unsafe_allow_html=True)  

elif st.session_state.active_button == 'Posttest3':
        cs="""
         <style>
         .st-key-Posttest3>.stButton>button {
        background-color: #035F8A; 
            color: white;
            border-color: #035F8A;
        }</style>"""

        st.markdown(cs, unsafe_allow_html=True) 


elif st.session_state.active_button == 'Contributors3':
        cs="""
         <style>
         .st-key-Contributors3>.stButton>button {
        background-color: #035F8A; 
            color: white;
            border-color: #035F8A;
        }</style>"""

        st.markdown(cs, unsafe_allow_html=True) 


elif st.session_state.active_button == 'References3':
        cs="""
        <style>
                .st-key-References3>.stButton>button {
                background-color: #035F8A; 
                    color: white;
                    border-color: #035F8A;
                }</style>"""
        st.markdown(cs, unsafe_allow_html=True) 

if st.session_state.active_button == 'aim4':
        cs="""
         <style>
         .st-key-aim4>.stButton>button {
        background-color: #035F8A; 
            color: white;
            border-color: #035F8A;
        }</style>"""

        st.markdown(cs, unsafe_allow_html=True)

elif st.session_state.active_button == 'Theory4':
        cs="""
         <style>
         .st-key-Theory4>.stButton>button {
        background-color: #035F8A; 
            color: white;
            border-color: #035F8A;
        }</style>"""

        st.markdown(cs, unsafe_allow_html=True)     

elif st.session_state.active_button == 'Pretest4':
        cs="""
         <style>
         .st-key-Pretest4>.stButton>button {
        background-color: #035F8A; 
            color: white;
            border-color: #035F8A;
        }</style>"""

        st.markdown(cs, unsafe_allow_html=True)  
    
# elif st.session_state.active_button == 'Procedure4':
#         cs="""
#          <style>
#          .st-key-Procedure4>.stButton>button {
#         background-color: #035F8A; 
#             color: white;
#             border-color: #035F8A;
#         }</style>"""

#         st.markdown(cs, unsafe_allow_html=True)  

elif st.session_state.active_button == 'Simulation4':
        cs="""
         <style>
         .st-key-Simulation4>.stButton>button {
        background-color: #035F8A; 
            color: white;
            border-color: #035F8A;
        }</style>"""

        st.markdown(cs, unsafe_allow_html=True)  

elif st.session_state.active_button == 'Posttest4':
        cs="""
         <style>
         .st-key-Posttest4>.stButton>button {
        background-color: #035F8A; 
            color: white;
            border-color: #035F8A;
        }</style>"""

        st.markdown(cs, unsafe_allow_html=True) 

elif st.session_state.active_button == 'Contributors4':
        cs="""
         <style>
         .st-key-Contributors4>.stButton>button {
        background-color: #035F8A; 
            color: white;
            border-color: #035F8A;
        }</style>"""

        st.markdown(cs, unsafe_allow_html=True)

elif st.session_state.active_button == 'References4':
        cs="""
        <style>
                .st-key-References4>.stButton>button {
                background-color: #035F8A; 
                    color: white;
                    border-color: #035F8A;
                }</style>"""
        st.markdown(cs, unsafe_allow_html=True) 

 
if st.session_state.active_button == 'aim5':
        cs="""
         <style>
         .st-key-aim5>.stButton>button {
        background-color: #035F8A; 
            color: white;
            border-color: #035F8A;
        }</style>"""

        st.markdown(cs, unsafe_allow_html=True)

elif st.session_state.active_button == 'Theory5':
        cs="""
         <style>
         .st-key-Theory5>.stButton>button {
        background-color: #035F8A; 
            color: white;
            border-color: #035F8A;
        }</style>"""

        st.markdown(cs, unsafe_allow_html=True)     

elif st.session_state.active_button == 'Pretest5':
        cs="""
         <style>
         .st-key-Pretest5>.stButton>button {
        background-color: #035F8A; 
            color: white;
            border-color: #035F8A;
        }</style>"""

        st.markdown(cs, unsafe_allow_html=True)  
    
# elif st.session_state.active_button == 'Procedure5':
#         cs="""
#          <style>
#          .st-key-Procedure5>.stButton>button {
#         background-color: #035F8A; 
#             color: white;
#             border-color: #035F8A;
#         }</style>"""

#         st.markdown(cs, unsafe_allow_html=True)  

elif st.session_state.active_button == 'Simulation5':
        cs="""
         <style>
         .st-key-Simulation5>.stButton>button {
        background-color: #035F8A; 
            color: white;
            border-color: #035F8A;
        }</style>"""

        st.markdown(cs, unsafe_allow_html=True)  

elif st.session_state.active_button == 'Posttest5':
        cs="""
         <style>
         .st-key-Posttest5>.stButton>button {
        background-color: #035F8A; 
            color: white;
            border-color: #035F8A;
        }</style>"""

        st.markdown(cs, unsafe_allow_html=True) 


elif st.session_state.active_button == 'Contributors5':
        cs="""
         <style>
         .st-key-Contributors5>.stButton>button {
        background-color: #035F8A; 
            color: white;
            border-color: #035F8A;
        }</style>"""

        st.markdown(cs, unsafe_allow_html=True)

elif st.session_state.active_button == 'References5':
        cs="""
        <style>
                .st-key-References5>.stButton>button {
                background-color: #035F8A; 
                    color: white;
                    border-color: #035F8A;
                }</style>"""
        st.markdown(cs, unsafe_allow_html=True) 
 

if st.session_state.active_button == 'aim6':
        cs="""
         <style>
         .st-key-aim6>.stButton>button {
        background-color: #035F8A; 
            color: white;
            border-color: #035F8A;
        }</style>"""

        st.markdown(cs, unsafe_allow_html=True)

elif st.session_state.active_button == 'Theory6':
        cs="""
         <style>
         .st-key-Theory6>.stButton>button {
        background-color: #035F8A; 
            color: white;
            border-color: #035F8A;
        }</style>"""

        st.markdown(cs, unsafe_allow_html=True)     

elif st.session_state.active_button == 'Pretest6':
        cs="""
         <style>
         .st-key-Pretest6>.stButton>button {
        background-color: #035F8A; 
            color: white;
            border-color: #035F8A;
        }</style>"""

        st.markdown(cs, unsafe_allow_html=True)  
    
# elif st.session_state.active_button == 'Procedure6':
#         cs="""
#          <style>
#          .st-key-Procedure6>.stButton>button {
#         background-color: #035F8A; 
#             color: white;
#             border-color: #035F8A;
#         }</style>"""

#         st.markdown(cs, unsafe_allow_html=True)  

elif st.session_state.active_button == 'Simulation6':
        cs="""
         <style>
         .st-key-Simulation6>.stButton>button {
        background-color: #035F8A; 
            color: white;
            border-color: #035F8A;
        }</style>"""

        st.markdown(cs, unsafe_allow_html=True)  

elif st.session_state.active_button == 'Posttest6':
        cs="""
         <style>
         .st-key-Posttest6>.stButton>button {
        background-color: #035F8A; 
            color: white;
            border-color: #035F8A;
        }</style>"""

        st.markdown(cs, unsafe_allow_html=True) 

elif st.session_state.active_button == 'Contributors6':
        cs="""
         <style>
         .st-key-Contributors6>.stButton>button {
        background-color: #035F8A; 
            color: white;
            border-color: #035F8A;
        }</style>"""

        st.markdown(cs, unsafe_allow_html=True) 

elif st.session_state.active_button == 'References6':
        cs="""
        <style>
                .st-key-References6>.stButton>button {
                background-color: #035F8A; 
                    color: white;
                    border-color: #035F8A;
                }</style>"""
        st.markdown(cs, unsafe_allow_html=True) 


if st.session_state.active_button == 'aim7':
        cs="""
         <style>
         .st-key-aim7>.stButton>button {
        background-color: #035F8A; 
            color: white;
            border-color: #035F8A;
        }</style>"""

        st.markdown(cs, unsafe_allow_html=True)

elif st.session_state.active_button == 'Theory7':
        cs="""
         <style>
         .st-key-Theory7>.stButton>button {
        background-color: #035F8A; 
            color: white;
            border-color: #035F8A;
        }</style>"""

        st.markdown(cs, unsafe_allow_html=True)     

elif st.session_state.active_button == 'Pretest7':
        cs="""
         <style>
         .st-key-Pretest7>.stButton>button {
        background-color: #035F8A; 
            color: white;
            border-color: #035F8A;
        }</style>"""

        st.markdown(cs, unsafe_allow_html=True)  
    
# elif st.session_state.active_button == 'Procedure7':
#         cs="""
#          <style>
#          .st-key-Procedure7>.stButton>button {
#         background-color: #035F8A; 
#             color: white;
#             border-color: #035F8A;
#         }</style>"""

#         st.markdown(cs, unsafe_allow_html=True)  

elif st.session_state.active_button == 'Simulation7':
        cs="""
         <style>
         .st-key-Simulation7>.stButton>button {
            background-color: #035F8A; 
            color: white;
            border-color: #035F8A;
        }</style>"""

        st.markdown(cs, unsafe_allow_html=True)  

elif st.session_state.active_button == 'Posttest7':
        cs="""
         <style>
         .st-key-Posttest7>.stButton>button {
        background-color: #035F8A; 
            color: white;
            border-color: #035F8A;
        }</style>"""

        st.markdown(cs, unsafe_allow_html=True) 


elif st.session_state.active_button == 'Contributors7':
        cs="""
         <style>
         .st-key-Contributors7>.stButton>button {
        background-color: #035F8A; 
            color: white;
            border-color: #035F8A;
        }</style>"""

        st.markdown(cs, unsafe_allow_html=True)

elif st.session_state.active_button == 'References7':
        cs="""
        <style>
                .st-key-References7>.stButton>button {
                background-color: #035F8A; 
                    color: white;
                    border-color: #035F8A;
                }</style>"""
        st.markdown(cs, unsafe_allow_html=True) 

 