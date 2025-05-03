# Airline Overbooking Analysis & Revenue Maximization

## Project Summary

This project analyzes airline overbooking strategies to maximize revenue while considering factors such as passenger compensation, customer loyalty, and flight characteristics. The primary goal was to develop mathematical models to determine optimal overbooking rates for both domestic and international flights, aiming to enhance airline revenue. The analysis dives into compensation strategies for bumped passengers (both voluntary and involuntary), models potential revenue under various overbooking scenarios, and assesses the impact on overall profit.

## Key Areas of Analysis

1.  **Compensation Modeling:**
    * Developed models to estimate short-term costs associated with bumping passengers, considering legal requirements (Denied Boarding Compensation) and negotiated compensations (vouchers, meals, etc.)[cite: 471, 475, 494, 501].
    * Modeled long-term implications using Customer Lifetime Value (CLV) and logistic curves to quantify potential revenue loss due to decreased customer loyalty resulting from bumping[cite: 478, 575, 594].
    * Distinguished between costs for voluntarily and involuntarily bumped passengers, recognizing that voluntary bumping is generally preferable for airlines[cite: 5, 6, 65].
    * Calculated comprehensive expected compensation values per bumped passenger: approximately \$1802.52 for domestic and \$5936.91 for international flights[cite: 105, 108].

2.  **Revenue Modeling & Optimization:**
    * Utilized Monte Carlo simulations to model airline revenue under different overbooking levels (from conservative 0% to extra aggressive 10-15%)[cite: 112, 138, 141].
    * Incorporated key variables like flight capacity (assumed 200 domestic, 400 international), seat class distribution (Economy, Business), ticket prices, and estimated no-show rates (4% domestic, 7.5% international)[cite: 115, 123, 129, 130, 131, 134].
    * Determined optimal overbooking rates under baseline assumptions:
        * **Domestic:** 2.5% overbooking (booking 205 passengers for 200 seats), maximizing revenue at \$62,564.67 per flight[cite: 10, 168].
        * **International:** 6.25% overbooking (booking 425 passengers for 400 seats), maximizing revenue at \$340,641.28 per flight[cite: 10, 170].

3.  **Sensitivity Analysis:**
    * Examined how changes in no-show rates and compensation costs affect the optimal overbooking strategy and maximum revenue[cite: 12, 185].
    * Found that the no-show rate significantly influences the optimal overbooking percentage, while compensation costs have a lesser impact on the optimal rate itself, though they do affect overall profitability[cite: 13, 197, 198].

4.  **Profitability Analysis:**
    * Estimated flight operating costs (fuel, labor, maintenance, fees, etc.) to analyze the impact of overbooking strategies on profit per passenger[cite: 266, 269, 271, 289].
    * Demonstrated how even small differences in revenue gained through optimized overbooking can significantly impact profitability[cite: 15, 16, 300].

## Methodology

* **Probabilistic Modeling:** Used triangular distributions to model passenger wait times when bumped[cite: 510, 513].
* **Customer Lifetime Value (CLV):** Estimated long-term revenue loss based on flyer type (occasional, moderate, frequent) and loyalty duration[cite: 575, 587].
* **Logistic Regression:** Modeled the probability of loyalty loss based on delay duration and bump type (voluntary/involuntary)[cite: 594, 599].
* **Monte Carlo Simulation:** Simulated thousands of flights to assess revenue outcomes under uncertainty (passenger no-shows) for various booking levels[cite: 138, 141, 143].
* **Optimization:** Identified booking levels that yielded the maximum average revenue per flight across simulations[cite: 168, 170].
* **Cost Estimation:** Aggregated various airline operating cost components to provide context for profitability[cite: 271, 289].

## Key Findings & Recommendations

* Overbooking is a viable strategy to maximize revenue, but the optimal rate depends on factors like no-show probability and flight type[cite: 3, 470].
* The optimal baseline rates found were 2.5% (Domestic) and 6.25% (International)[cite: 10, 324].
* Airlines should consider **situational overbooking**, adjusting rates based on specific flight characteristics (e.g., holiday travel, time of day) where no-show rates might differ from the average[cite: 322, 323].
* Managing compensation effectively involves balancing immediate costs with long-term customer retention. Encouraging voluntary bumping, potentially with generous offers, can mitigate negative loyalty impacts[cite: 328, 329, 331].
* There's a trade-off between maximizing revenue through higher overbooking and maintaining customer satisfaction[cite: 315, 332].

## Code & Implementation

The analysis was performed using Python, leveraging libraries such as NumPy, Pandas, and Matplotlib for simulation, data handling, and visualization[cite: 342, 405]. Key code components include:
* Compensation cost simulation (Short-term & Long-term/Loyalty Loss) [cite: 340, 348]
* Monte Carlo simulation for revenue modeling under different strategies [cite: 349]
* Revenue maximization analysis to find optimal booking levels [cite: 383]
* Sensitivity analysis for no-show rates and compensation costs [cite: 399, 404]
* Profitability analysis plotting profit per passenger against costs [cite: 406]

*(Note: Consider adding a direct link to your GitHub repository or specific code files here if applicable, as mentioned in the document [cite: 348, 404])*

## Assumptions & Limitations

* Assumed constant no-show rates (4% domestic, 7.5% international) and compensation costs for baseline analysis, though sensitivity analysis explored variations[cite: 115, 117, 119, 303].
* Used fixed flight capacities and seat class distributions; results are scalable, but absolute revenue figures depend on actual aircraft configurations[cite: 123, 124, 304].
* Relied on average CLV estimations and modeled loyalty loss; actual passenger behavior varies[cite: 576, 592].
* Cost estimations are based on industry averages and simplified models[cite: 267, 270].

---

Feel free to modify this draft to better suit your specific project structure and emphasis on GitHub. Let me know if you'd like any sections expanded or adjusted!
