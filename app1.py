import streamlit as st
import random
def play(userchoice):
    result=""
    points=0
    computerchoice= random.randint(0,2)
    if userchoice==computerchoice:
        result="Bad Choice"
    elif userchoice==3:
        result="The Game is over"
    else:
        if userchoice==0 and computerchoice==1:
            result="you lose"
        elif userchoice==1 and computerchoice==2:
            result="you lose"
        elif userchoice==2 and computerchoice==0:
            result="you lose"
        else:
            result="you win"
            points=points+1
    return result,computerchoice,points

def main():
    st.title("FUN ZONE")
    html_temp="""
        <div style="background-color:tomato;padding:10px">
            <h2 style="color:white;text-align:center;">STONE PAPER SCISSOR</h2>
        </div>
        """
    st.markdown(html_temp,unsafe_allow_html=True)
    st.header(" 0:STONE, 1:PAPER, 2:SCISSOR, 3:QUIT")
    userchoice= st.selectbox("choice:",["0","1","2","3"])
    st.write("Your Choice Is:",userchoice)
    if "total_points" not in st.session_state:
        st.session_state.total_points = 0
    if st.button("PLAY"):
        result,computerchoice,points=play(int(userchoice))
        st.success(result)
        st.success(computerchoice)
        st.session_state.total_points += points
        st.info(f"Points this round: {points}")
        st.success(f"🎯 Total Score: {st.session_state.total_points}")
        
    
    if st.button("About"):
        st.text("Lets Learn")
        st.text("Built With Streamlit")


if __name__ == '__main__':
    main()
    
