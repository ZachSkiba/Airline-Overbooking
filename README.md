# Airline Overbooking Analysis & Revenue Maximization
**Collaborator:** Jake Skiba [@JakeSkiba16](https://github.com/JakeSkiba16)
 
## Project Summary

This project analyzes airline overbooking strategies to maximize revenue while considering factors such as passenger compensation, customer loyalty, and flight characteristics. The primary goal was to develop mathematical models to determine optimal overbooking rates for both domestic and international flights, aiming to enhance airline revenue. The analysis dives into compensation strategies for bumped passengers (both voluntary and involuntary), models potential revenue under various overbooking scenarios, and assesses the impact on overall profit.

## Key Areas of Analysis

1.  **Compensation Modeling:**
    * Developed models to estimate short-term costs associated with bumping passengers, considering legal requirements (Denied Boarding Compensation) and negotiated compensations (vouchers, meals, etc.).
    * Modeled long-term implications using Customer Lifetime Value (CLV) and logistic curves to quantify potential revenue loss due to decreased customer loyalty resulting from bumping.
    * Distinguished between costs for voluntarily and involuntarily bumped passengers, recognizing that voluntary bumping is generally preferable for airlines.
    * Calculated comprehensive expected compensation values per bumped passenger: approximately \$1802.99 for domestic and \$5936.91 for international flights.

2.  **Revenue Modeling & Optimization:**
    * Utilized Monte Carlo simulations to model airline revenue under different overbooking levels (from conservative 0% to extra aggressive 10-15%).
    * Incorporated key variables like flight capacity (assumed 200 domestic, 400 international), seat class distribution (Economy, Business), ticket prices, and estimated no-show rates (4% domestic, 7.5% international).
    * Determined optimal overbooking rates:
        * **Domestic:** 2.5% overbooking (booking 205 passengers for 200 seats), maximizing revenue at \$62,564.67 per flight.
        * **International:** 6.25% overbooking (booking 425 passengers for 400 seats), maximizing revenue at \$340,641.28 per flight.

3.  **Sensitivity Analysis:**
    * Examined how changes in no-show rates and compensation costs affect the optimal overbooking strategy and maximum revenue.
    * Found that the no-show rate significantly influences the optimal overbooking percentage, while compensation costs have a lesser impact on the optimal rate itself, though they do affect overall profitability.

4.  **Profitability Analysis:**
    * Estimated flight operating costs (fuel, labor, maintenance, fees, etc.) to analyze the impact of overbooking strategies on profit per passenger.
    * Demonstrated how even small differences in revenue gained through optimized overbooking can significantly impact profitability.

## Methodology

* **Probabilistic Modeling:** Used triangular distributions to model passenger wait times when bumped.
* **Customer Lifetime Value (CLV):** Estimated long-term revenue loss based on flyer type (occasional, moderate, frequent) and loyalty duration.
* **Logistic Regression:** Modeled the probability of loyalty loss based on delay duration and bump type (voluntary/involuntary).
* **Monte Carlo Simulation:** Simulated thousands of flights to assess revenue outcomes under uncertainty (passenger no-shows) for various booking levels.
* **Optimization:** Identified booking levels that yielded the maximum average revenue per flight across simulations.
* **Cost Estimation:** Aggregated various airline operating cost components to provide context for profitability.

## Key Findings & Recommendations

* Overbooking is a viable strategy to maximize revenue, but the optimal rate depends on factors like no-show probability and flight type.
* The optimal baseline rates found were 2.5% (Domestic) and 6.25% (International).
* Airlines should consider **situational overbooking**, adjusting rates based on specific flight characteristics (e.g., holiday travel, time of day) where no-show rates might differ from the average.
* Managing compensation effectively involves balancing immediate costs with long-term customer retention. Encouraging voluntary bumping, potentially with generous offers, can mitigate negative loyalty impacts.
* There's a trade-off between maximizing revenue through higher overbooking and maintaining customer satisfaction.

## Code & Implementation

The analysis was performed using Python, using libraries such as NumPy, Pandas, and Matplotlib for simulation, data handling, and visualization. Key code components include:
* Compensation cost simulation (Short-term & Long-term/Loyalty Loss) 
* Monte Carlo simulation for revenue modeling under different strategies
* Revenue maximization analysis to find optimal booking levels 
* Sensitivity analysis for no-show rates and compensation costs
* Profitability analysis plotting profit per passenger against costs


## Assumptions & Limitations

* Assumed constant no-show rates (4% domestic, 7.5% international) and compensation costs for baseline analysis, though sensitivity analysis explored variations.
* Used fixed flight capacities and seat class distributions; results are scalable, but absolute revenue figures depend on actual aircraft configurations.
* Relied on average CLV estimations and modeled loyalty loss; actual passenger behavior varies.
* Cost estimations are based on industry averages and simplified models.


