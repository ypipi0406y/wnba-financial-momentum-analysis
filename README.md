# WNBA Financial & Momentum Analysis

A Streamlit project analyzing WNBA league momentum and team salary cap structure from 2021 to 2025.
https://wnba-financial-momentum-analysis-nq9dgqktostsjnqdryfqln.streamlit.app/
## Project Overview

This project explores WNBA growth from two levels:

### League Level
- Total Attendance
- Average Attendance
- TV Audience Growth
- Social / Digital Visibility

### Team Level
- Total Salaries
- Cap Room
- Guaranteed Salaries
- Salary Cap Structure

The goal is to better understand how league-wide momentum and team-level financial structure evolved over time.

## Research Focus

This project is built around the following questions:

- How has WNBA league momentum changed from 2021 to 2025?
- How have team payroll structures changed across the same period?
- What differences can be observed across teams in salary commitment, cap flexibility, and guaranteed salaries?
- How can league growth and financial structure be analyzed together?

## Data Sources

This project uses three main datasets:

1. **WNBA League Momentum Data (2021–2025)**
   - Total Attendance
   - Average Attendance
   - TV Audience Metrics
   - Social Video Views

2. **WNBA Team Cap Summary (2021–2025)**
   - Team
   - Total Salaries
   - Total Players
   - Cap Room
   - Guaranteed Salaries

3. **WNBA Key CBA Numbers (2021–2025)**
   - Salary Cap
   - Player Supermaximum
   - Player Maximum
   - Player Minimum
   - Roster Size Requirement

## Project Structure

```text
.
├── app.py
├── requirements.txt
├── WNBA_league_momentum_2021_2025.csv
├── WNBA_team_cap_summary_2021_2025.csv
└── WNBA_key_cba_numbers_2021_2025.csv
