# DSA210Project
NBA Fantasy Team Performance Analysis

Project Objective
This project, undertaken as part of the DSA210 course in the Fall 2024 semester, seeks to enhance my NBA Fantasy team's performance by systematically evaluating the effects of weekly roster adjustments. By leveraging matchup data from my ESPN Fantasy account, the project examines player acquisitions, their contributions based on position eligibility (PG, SG, SF, PF, C), and overall team impact. Through the analysis of weekly trends and performance variations, the project aims to provide a structured, data-driven approach to optimizing fantasy points and improving strategic decision-making throughout the season.

Hypothesis
I propose that optimizing NBA Fantasy roster changes by strategically selecting players based on position-specific performance trends can lead to a measurable improvement in team success. By systematically identifying which positions yield the highest fantasy points and evaluating the effect of newly acquired players on matchup outcomes, I expect to develop an evidence-based strategy that minimizes uncertainty in roster management. The goal is to transition from intuitive selections to a structured, data-driven approach that ensures sustained competitiveness in the fantasy league.

Dataset
The dataset is sourced from my ESPN Fantasy account and is refined through systematic weekly analysis. Key components include:

1. Weekly Player Additions 
   - List of players added to my roster.
   - Their position eligibility (PG, SG, SF, PF, C).
   - Fantasy points they contributed in the first week after being added.

2. Player Performance within My Team  
   - Total fantasy points earned by newly added players.
   - Breakdown of their contribution by position (e.g., SG, PF).

3. Positional Analysis  
   - Aggregated impact of acquired players categorized by position.
   - Identification of positions that yield the highest fantasy points.

4. Visualization of Weekly Performance  
   - Graphs displaying contributions of newly acquired players per position.
   - Visual summaries stored in a designated directory for trend analysis.

5. Trend Evaluation  
   - Long-term analysis of position-specific performance over multiple weeks.
   - Insights into which positions (e.g., SF, C) are most valuable for optimizing fantasy points.

This dataset serves as the foundation for assessing the impact of roster modifications and refining team management strategies for future weeks.

Motivation
Managing an NBA Fantasy team involves strategic decision-making within the constraints of limited weekly player acquisitions. This project focuses on examining the effectiveness of these decisions by analyzing the performance of newly added players. By incorporating data science techniques, I aim to bridge my passion for basketball with quantitative analysis, ultimately refining my approach to fantasy team management. Beyond enhancing my personal fantasy league strategy, this project also provides valuable experience in data collection, visualization, and decision-making, reinforcing the practical application of data analysis in sports.

Project Plan

1. Data Collection and Structuring  
   - Gather weekly matchup and performance data via the ESPN API.
   - Identify newly added players and classify them by position.
   - Record their fantasy point contributions and categorize them accordingly.

2. Exploratory Data Analysis (EDA)  
   - Compare week-to-week roster changes and their impact.
   - Determine trends in player contributions by position.
   - Identify positions that consistently generate high fantasy points.

3. Position-Based Performance Assessment  
   - Group new acquisitions by their eligible positions.
   - Aggregate position-based contributions over multiple weeks.
   - Identify the most valuable positions for long-term success.

4. Data Visualization  
   - Create bar charts to illustrate weekly contributions by position.
   - Store visualizations in a dedicated directory for future analysis.
   - Develop cumulative visualizations highlighting trends over time.

5. Insights and Strategy Implementation  
   - Synthesize findings to optimize future player acquisitions.
   - Develop a framework for making data-informed roster decisions.
   - Utilize insights to maximize fantasy points and improve strategic planning.

Areas for Improvement

- Enhancing Data Accuracy:  
  - Integrate mid-week transactions to capture more precise player movements.
  - Improve classification of hybrid positions (e.g., G/F, F/C) to refine analysis.

- Expanding the Dataset: 
  - Incorporate data from previous fantasy seasons to detect long-term trends.
  - Compare results across multiple seasons for deeper insights.

Future Enhancements

1. Automated Data Processing:  
   - Streamline the collection and visualization process for efficiency.
   - Implement automatic updates to reduce manual data handling.

2. Interactive Tool Development:  
   - Create a web-based tool for users to input their fantasy team data.
   - Provide personalized recommendations based on historical trends.

Predictive Modeling for Player Selection

Overview
To improve decision-making, I developed a predictive model using a Decision Tree algorithm. This model evaluates free agent statistics and historical performance to recommend optimal player acquisitions based on fantasy point projections.

Key Methodology

1. Data Collection:  
   - Retrieve available free agent statistics, including rebounds, assists, and blocks.
   - Incorporate historical performance data for model training.

2. Position-Based Prioritization:  
   - Identify key positions based on past team performance trends.
   - Adjust player rankings accordingly to maximize fantasy points.

3. Model Training:  
   - Train a Decision Tree Regressor to predict fantasy point contributions.
   - Utilize key statistical metrics and positional insights for accurate forecasting.

4. Player Recommendations:  
   - Rank available free agents based on expected fantasy point contributions.
   - Generate a list of the top five recommended players to enhance team performance.

By integrating data analysis with predictive modeling, this project aims to refine NBA Fantasy team management, making strategic decisions more data-driven and efficient.

Data Analysis and Hypothesis Testing

After collecting player performance data using the ESPN Fantasy API, I conducted a systematic analysis to validate the project hypothesis: that player positions significantly influence fantasy point contributions.

The process included:

Data Cleaning: Removing incomplete records, ensuring only players with defined positions and fantasy points were considered.
Exploratory Data Analysis (EDA): Calculating and visualizing the average fantasy points contributed by each position (PG, SG, SF, PF, C) across multiple weeks.
Visualization: A bar chart was created to visually compare average fantasy contributions between positions. The graph was saved as figure/position_avg_points.png.
Hypothesis Testing:
A one-way ANOVA test was conducted to determine if the differences in mean fantasy points across player positions were statistically significant.
The ANOVA test returned, strongly rejecting the null hypothesis (H0).
This result supports the alternative hypothesis (H1), confirming that player position significantly affects fantasy point contributions in my NBA Fantasy team.

Evaluation Methods

Statistical Test Used: One-way ANOVA, appropriate for comparing mean values across multiple independent groups (positions).
Data Validity: Real weekly data from ESPN Fantasy ensured authentic, gameplay-driven insights.
Visualization Support: Data-driven bar chart analysis visually reinforced the statistical findings.
Reproducibility: All data collection and analysis steps were automated and reproducible with updated ESPN Fantasy data.
By integrating real-world data with statistical evaluation, this project successfully bridged theoretical hypothesis and practical fantasy team optimization strategies.

