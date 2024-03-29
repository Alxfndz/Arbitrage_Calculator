# Arbitrage Calculator
https://alxfndz-arbitrage-calculator-app-ersfmn.streamlit.app/

## Description

This **Arbitrage Calculator** is a Python application built using the Streamlit library. It allows users to calculate and identify arbitrage opportunities in a two-way market, ensuring a guaranteed profit. By entering the odds of the original bet and the hedge bet, along with the desired total amount for the wager, the calculator determines if an arbitrage opportunity exists and provides the recommended bet amounts for each outcome.

## Features

- Calculates the probability of the original bet and hedge bet based on their odds
- Determines the total probability of both bets combined
- Identifies and notifies the user if an arbitrage opportunity is present
- Recommends the optimal bet amounts for the original bet and hedge bet to guarantee profit
- Calculates the total bet amount, profit, and return on investment (ROI) for the wager


## Usage

1. Upon launching the application, you will see the **Arbitrage Calculator** title and a brief description of its purpose.

2. Enter the odds of the original bet and the hedge bet in the corresponding input fields. The minimum and maximum values are set to 1.00 and 1000.00, respectively.

3. Specify your desired total amount for the wager using the number input field. The minimum value is 1, and the maximum value is 1,000,000. The default value is set to 1000.

4. Click on the **Test For Arbitrage** button to calculate and determine if an arbitrage opportunity exists.

5. If an arbitrage opportunity is found (total probability less than 1), the application will display the following information:

   - Confirmation message indicating the presence of an arbitrage opportunity.
   - The amount to bet on the original bet to maximize profit.
   - The amount to bet on the hedge bet to hedge against the original bet.
   - The total amount of the bet (sum of the original and hedge bets).
   - The calculated profit from the wager.
   - The return on investment (ROI) expressed as a percentage.

6. If no arbitrage opportunity is found (total probability greater than or equal to 1), the application will display a message indicating the absence of any arbitrage opportunities.

