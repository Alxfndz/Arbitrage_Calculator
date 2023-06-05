import streamlit as st

def arbitrage_calculator(original_bet_odds, hedge_bet_odds, desired_win_amount):
    original_bet_probability = 1 / original_bet_odds
    hedge_bet_probability = 1 / hedge_bet_odds
    total_probability = original_bet_probability + hedge_bet_probability
    return original_bet_probability,hedge_bet_probability,total_probability
    
def add_background_image():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images.unsplash.com/photo-1552749412-02bd58bcff5f?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )


def main():
    st.title('💰Arbitrage Calculator')
    st.write('Use this arbitrage calculator to work out how to guarantee profit in a two-way market.')
    st.write("Enter the odds of your original bet and the odds for the alternative outcome. The calculator will tell you if you've found an arbitrage opportunity and how much to bet on each outcome.")
    
    original_bet_odds = st.number_input('Enter the odds of the original bet: ', min_value=1.00, max_value=1000.00, value=1.00,)
    hedge_bet_odds = st.number_input('Enter the odds of the hedge bet: ', min_value=1.00, max_value=1000.00, value=1.00,)
    desired_win_amount = st.number_input('Enter your desired win amount: ',min_value=1,max_value=1000000,value=1000)
    original_bet_probability,hedge_bet_probability,total_probability = arbitrage_calculator(original_bet_odds, hedge_bet_odds, desired_win_amount)
    calculate_button = st.button('Test For Arbitrage')
    
    if calculate_button:
        if total_probability < 1:
            st.write("You've found an arbitrage opportunity!")
            original_bet_amount = desired_win_amount / original_bet_odds
            hedge_bet_amount = desired_win_amount / hedge_bet_odds
            total_bet_amount = original_bet_amount + hedge_bet_amount
            profit = desired_win_amount - total_bet_amount
            roi = (profit / total_bet_amount) * 100
            
            st.write("The amount to bet on the original bet is: ", round(original_bet_amount,2))
            st.write("The amount to bet on the hedge bet is: ", round(hedge_bet_amount,2))
            st.write("The total amount of the bet is: ", round(total_bet_amount,2))
            st.write("The profit is: ", round(profit,2))
            st.write("The ROI is: ", round(roi,2), "%")
            
        else:
            st.write("No arbitrage opportunity found.")


if __name__ == "__main__":
    add_background_image()
    main()