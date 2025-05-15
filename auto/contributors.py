import streamlit as st
import pandas as pd

def contri3():
    st.markdown('<div class="my-custom-text">Study the Autocorrelation Analysis</div>',unsafe_allow_html=True)
    st.divider()
    st.markdown("### Lab Proposer / Subject Matter Experts")
    st.markdown("<br>", unsafe_allow_html=True) 
 
    st.markdown("""
    <style>
        .custom-table {
            text-align: left;
            border-collapse: collapse;
        }
        .custom-table th, .custom-table td {
            border: 1px solid #ccc;
            padding: 8px;
        }
    </style>

    <div style='text-align: left'>
        <table class="custom-table">
            <tr style="background-color:#035F8A;color:white">
                <th>S. No.</th>
                <th>Name</th>
                <th>Email</th>
                <th>Institute</th>
                <th>Position</th>
            </tr>
            <tr>
                <td>1</td>
                <td>Dr. R S Anand</td>
                <td>anandfee@gmail.com</td>
                <td>IIT Roorkee</td>
                <td>Professor</td>
            </tr>
        </table>
    </div>
""", unsafe_allow_html=True)
    


    st.markdown("<br>", unsafe_allow_html=True) 
    st.markdown("### Persons Associated in the Lab Development")
    st.markdown("<br>", unsafe_allow_html=True) 

    st.markdown("""
    <style>
        .custom-table {
            text-align: left;
            border-collapse: collapse;
            width: auto;
        }
        .custom-table th, .custom-table td {
            border: 1px solid #ccc;
            padding: 8px 12px;
            vertical-align: top;
        }
    </style>

    <table class="custom-table">
        <tr style="background-color:#035F8A;color:white">
            <th>S. No.</th>
            <th>Name</th>
            <th>Email</th>
            <th>Institute</th>
            <th>Position</th>
        </tr>
        <tr>
            <td>1</td>
            <td>Dr. Rajeev Kumar</td>
            <td>rajeevkumar@pec.edu.in <br>rajeev.kumar@ee.iitr.ac.in</td>
            <td>PEC Chandigarh</td>
            <td>Assistant Professor</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Ms. Pragya Daksh</td>
            <td>prgdaksh@gmail.com</td>
            <td>IIT Roorkee</td>
            <td>Project Associate</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Mr. Harshit Bhat</td>
            <td>harshitbhat988@gmail.com</td>
            <td>SDM College of Engineering and Technology,<br> Dharwad, Karnataka</td>
            <td>Intern</td>
        </tr>
    </table>
    """, unsafe_allow_html=True)