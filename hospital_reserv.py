import streamlit as st
import pandas as pd
from datetime import datetime

#)title
st.title(':orange[💮SIMPLE HOSPITAL RESERVATION - PYTHON PROJECT🌳]')

#) to display the available doctors for
st.subheader("\n:violet[The multispeciality hospital XYZ - doctors are available for]")
 
#) general doctor slot
gen_slot_dic={
        'slot1': "12:01",
        'slot2': "12:16",
        'slot3': "12:31",
        'slot4': "12:46"
        }
#) general doctor slot df
gen_slot_df = [gen_slot_dic]


if (st.checkbox("general")):
    st.markdown("\n#### :green[1.1 general doctor available slots]")
    st.dataframe(gen_slot_df)
    
    #) input visitor details
    visitor_name= st.text_input(":red[**Enter your name:**]")
    if (visitor_name):
        visitor_age = st.number_input(":red[**Enter your age:**]")
        if (visitor_age):
            visitor_address = st.text_input(":red[**Enter your address:**]")
            if (visitor_address):
                visitor_problem = st.text_input(":red[**Enter your problem:**]")
                if (visitor_problem): 
                    gen_book_slot= st.text_input(":red[**Enter your slot of choice:**]")
                    if (gen_book_slot):
                        #) visitor details df
                        st.markdown("\n#### :green[1.2 visitor details dataframe]")
                        vis_df = pd.DataFrame()
                        vis_df['visitor_name'] = [visitor_name]
                        vis_df['visitor_age'] = [visitor_age]
                        vis_df['visitor_address'] = [visitor_address]
                        vis_df['visitor_problem'] = [visitor_problem]
                        vis_df['gen_book_slot'] = [gen_book_slot]
                        st.dataframe(vis_df)
                        
                        #) previous visit:
                        prev_visit = st.date_input("Enter previous visited date")

                        #) current visit
                        today = datetime.now().date()
                        current_visit = st.date_input("Enter the date", value = today, min_value = today)
                        
                        #) how many days between previous visit and current visit?
                        #) visitor details df
                        st.markdown("\n#### :green[1.3 doctor fee]")
                        delta = current_visit - prev_visit
                        #) visit gap
                        st.write(":blue[- visit gap in number of days:] ")
                        delta.days
                        if delta.days < 10:
                             st.write(":violet[10 percent fee reduction is applicable] ")
                             st.code ("doctor fee is 500")
                        elif delta.days < 15:
                             st.write(":green[5 percent fee reduction is applicable] ")
                             st.code ("doctor fee is 600")
                        else:
                             st.code ("doctor fee is 750")

                        #) remaining slots available
                        st.markdown("\n#### :red[1.4 remaining general doctor available slots:]")
                        del gen_slot_dic[gen_book_slot]
                        remain_gen_df = pd.DataFrame()
                        remain_gen_df = [gen_slot_dic]
                        st.dataframe(remain_gen_df)

                    else:
                        st.error('- you have not  preferred the slot to visit')
                else:
                    st.error('- you have not entered your problem')
            else:
                    st.error('- you have not entered your address')
        else:
            st.error('- you have not entered your age')
    else:
            st.error('- you have not entered name')
