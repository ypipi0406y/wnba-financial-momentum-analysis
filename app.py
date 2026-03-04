import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="WNBA Salary Cap Analysis", layout="wide")

# -----------------------------
# Load Data
# -----------------------------
team = pd.read_csv("WNBA_team_cap_summary_2021_2025.csv")
cba = pd.read_csv("WNBA_key_cba_numbers_2021_2025.csv")
momentum = pd.read_csv("WNBA_league_momentum_2021_2025.csv")

# Clean team data
team["Total_Salaries"] = pd.to_numeric(team["Total_Salaries"], errors="coerce")
team["Total_Players"] = pd.to_numeric(team["Total_Players"], errors="coerce")
team["Cap_Room"] = pd.to_numeric(team["Cap_Room"], errors="coerce")
team["Guaranteed_Salaries"] = pd.to_numeric(team["Guaranteed_Salaries"], errors="coerce")

# Clean CBA data
cba["Value_Numeric"] = pd.to_numeric(cba["Value"], errors="coerce")

# Clean momentum data
momentum["Total_Attendance"] = pd.to_numeric(momentum["Total_Attendance"], errors="coerce")
momentum["Average_Attendance"] = pd.to_numeric(momentum["Average_Attendance"], errors="coerce")
momentum["TV_Average_Viewers"] = pd.to_numeric(momentum["TV_Average_Viewers"], errors="coerce")
momentum["Social_Video_Views"] = pd.to_numeric(momentum["Social_Video_Views"], errors="coerce")

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("WNBA Project")
page = st.sidebar.radio(
    "Navigate",
    ["Overview", "League Momentum", "Team Cap Analysis", "CBA Trend", "Insight"]
)

# -----------------------------
# Overview
# -----------------------------
if page == "Overview":
    st.title("WNBA Financial & Momentum Analysis")
    st.subheader("A league-level and team-level view of WNBA growth from 2021 to 2025")

    st.markdown("""
    This project analyzes WNBA league momentum and team salary cap structure from 2021 to 2025.
    It combines attendance and audience growth indicators with team payroll, cap room,
    and guaranteed salary data to better understand how league growth and financial structure evolved over time.
    """)

    col1, col2, col3 = st.columns(3)
    col1.metric("Years Covered", int(momentum["Year"].nunique()))
    col2.metric("Teams per Season", int(team["Team"].nunique()))
    col3.metric("Team Records", len(team))

    st.markdown("## Project Objective")
    st.write("""
    This website explores two levels of WNBA growth:

    **League Level**
    - Total Attendance
    - Average Attendance
    - TV Audience Growth
    - Social / Digital Visibility

    **Team Level**
    - Total Salaries
    - Cap Room
    - Guaranteed Salaries
    - Salary Cap Structure
    """)

    st.markdown("## Data Scope")
    st.write("""
    The current version uses:
    - **2021–2025 League Momentum Data**
    - **2021–2025 Team Cap Summary**
    - **2021–2025 Key CBA Numbers**

    This allows the project to connect broad league momentum with team-level financial structure.
    """)

    st.markdown("## Why This Matters")
    st.write("""
    League growth is often discussed through attendance, TV ratings, and social visibility.
    However, financial structure also matters. Team payroll allocation, cap room, and guaranteed commitments
    provide a second lens for understanding how growth may or may not translate into long-term organizational stability.
    """)

# -----------------------------
# League Momentum
# -----------------------------
elif page == "League Momentum":
    st.title("League Momentum")

    st.write("""
    This section tracks league-level momentum using attendance, audience, and visibility indicators from 2021 to 2025.
    Attendance is the most directly comparable metric across all five years.
    TV and digital metrics are included as additional signals, though their exact reporting scope varies by year.
    """)

    st.markdown("## Total Attendance Over Time")
    fig1, ax1 = plt.subplots(figsize=(8, 4))
    ax1.plot(momentum["Year"], momentum["Total_Attendance"], marker="o")
    ax1.set_title("WNBA Total Attendance (2021–2025)")
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Total Attendance")
    st.pyplot(fig1)

    st.markdown("## Average Attendance Over Time")
    fig2, ax2 = plt.subplots(figsize=(8, 4))
    ax2.plot(momentum["Year"], momentum["Average_Attendance"], marker="o")
    ax2.set_title("WNBA Average Attendance (2021–2025)")
    ax2.set_xlabel("Year")
    ax2.set_ylabel("Average Attendance")
    st.pyplot(fig2)

    st.markdown("## TV Audience Growth")
    fig3, ax3 = plt.subplots(figsize=(8, 4))
    ax3.plot(momentum["Year"], momentum["TV_Average_Viewers"], marker="o")
    ax3.set_title("WNBA TV Audience Metric (2021–2025)")
    ax3.set_xlabel("Year")
    ax3.set_ylabel("Average Viewers")
    st.pyplot(fig3)

    st.markdown("## League Momentum Data")
    st.dataframe(momentum[[
        "Year",
        "Total_Attendance",
        "Average_Attendance",
        "TV_Average_Viewers",
        "TV_Metric_Type",
        "Social_Video_Views"
    ]], use_container_width=True)

    st.markdown("## Initial Interpretation")
    st.write("""
    Attendance growth shows the clearest long-term momentum trend in the data.
    TV audience growth also appears strong, but metric definitions vary somewhat by year.
    Together, these indicators suggest that league-wide visibility and audience demand expanded meaningfully from 2021 to 2025.
    """)

# -----------------------------
# Team Cap Analysis
# -----------------------------
elif page == "Team Cap Analysis":
    st.title("Team Cap Analysis")

    # -----------------------------
    # Part 1: Single-Year Team Comparison
    # -----------------------------
    st.markdown("## Yearly Team Comparison")

    selected_year = st.selectbox(
        "Select a year",
        sorted(team["Year"].unique())
    )

    filtered_team = team[team["Year"] == selected_year].copy()

    st.dataframe(filtered_team, use_container_width=True)

    st.markdown("### Total Salaries by Team")
    fig4, ax4 = plt.subplots(figsize=(10, 5))
    ax4.bar(filtered_team["Team"], filtered_team["Total_Salaries"])
    ax4.set_title(f"Total Salaries by Team ({selected_year})")
    ax4.set_ylabel("Total Salaries")
    plt.xticks(rotation=45, ha="right")
    st.pyplot(fig4)

    st.markdown("### Cap Room by Team")
    fig5, ax5 = plt.subplots(figsize=(10, 5))
    ax5.bar(filtered_team["Team"], filtered_team["Cap_Room"])
    ax5.set_title(f"Cap Room by Team ({selected_year})")
    ax5.set_ylabel("Cap Room")
    plt.xticks(rotation=45, ha="right")
    st.pyplot(fig5)

    st.markdown("### Guaranteed Salaries by Team")
    fig6, ax6 = plt.subplots(figsize=(10, 5))
    ax6.bar(filtered_team["Team"], filtered_team["Guaranteed_Salaries"])
    ax6.set_title(f"Guaranteed Salaries by Team ({selected_year})")
    ax6.set_ylabel("Guaranteed Salaries")
    plt.xticks(rotation=45, ha="right")
    st.pyplot(fig6)

    st.markdown("## Initial Interpretation")
    st.write("""
    This view compares team payroll structure within a single season.
    It helps show which teams are operating with higher salary commitment,
    lower cap flexibility, or stronger guaranteed salary pressure.
    """)

    # -----------------------------
    # Part 2: Team Trend View
    # -----------------------------
    st.markdown("---")
    st.markdown("## Team Trend View")

    selected_team = st.selectbox(
        "Select a team",
        sorted(team["Team"].unique())
    )

    team_trend = team[team["Team"] == selected_team].copy()

    st.dataframe(team_trend, use_container_width=True)

    st.markdown(f"### Total Salaries Over Time: {selected_team}")
    fig7, ax7 = plt.subplots(figsize=(8, 4))
    ax7.plot(team_trend["Year"], team_trend["Total_Salaries"], marker="o")
    ax7.set_title(f"{selected_team} Total Salaries (2021–2025)")
    ax7.set_xlabel("Year")
    ax7.set_ylabel("Total Salaries")
    st.pyplot(fig7)

    st.markdown(f"### Cap Room Over Time: {selected_team}")
    fig8, ax8 = plt.subplots(figsize=(8, 4))
    ax8.plot(team_trend["Year"], team_trend["Cap_Room"], marker="o")
    ax8.set_title(f"{selected_team} Cap Room (2021–2025)")
    ax8.set_xlabel("Year")
    ax8.set_ylabel("Cap Room")
    st.pyplot(fig8)

    st.markdown(f"### Guaranteed Salaries Over Time: {selected_team}")
    fig9, ax9 = plt.subplots(figsize=(8, 4))
    ax9.plot(team_trend["Year"], team_trend["Guaranteed_Salaries"], marker="o")
    ax9.set_title(f"{selected_team} Guaranteed Salaries (2021–2025)")
    ax9.set_xlabel("Year")
    ax9.set_ylabel("Guaranteed Salaries")
    st.pyplot(fig9)

    st.markdown("## Team-Level Insight")
    st.write(f"""
    This trend view shows how {selected_team}'s payroll structure changed from 2021 to 2025.
    It provides a more detailed view of whether the team became more financially flexible,
    more committed in guaranteed salary, or more aggressive in overall payroll allocation over time.
    """)
# -----------------------------
# CBA Trend
# -----------------------------
elif page == "CBA Trend":
    st.title("CBA Trend")

    cba_numeric = cba[cba["Value_Numeric"].notna()].copy()

    metric_choice = st.selectbox(
        "Choose a CBA metric",
        sorted(cba_numeric["Item"].unique())
    )

    filtered_cba = cba_numeric[cba_numeric["Item"] == metric_choice].copy()

    st.markdown(f"## {metric_choice} Over Time")

    fig7, ax7 = plt.subplots(figsize=(8, 4))
    ax7.plot(filtered_cba["Year"], filtered_cba["Value_Numeric"], marker="o")
    ax7.set_title(f"{metric_choice} (2021–2025)")
    ax7.set_xlabel("Year")
    ax7.set_ylabel("Value")
    st.pyplot(fig7)

    st.dataframe(filtered_cba[["Year", "Item", "Value"]], use_container_width=True)

    st.markdown("## Interpretation")
    st.write("""
    This page highlights how core CBA-related financial benchmarks changed over time.
    Tracking these values helps explain whether team payroll pressure is occurring in a context
    of rising league-wide salary limits.
    """)

# -----------------------------
# Insight
# -----------------------------
elif page == "Insight":
    st.title("Insight")

    selected_year = st.selectbox(
        "Select a year for insight review",
        sorted(team["Year"].unique()),
        key="insight_year"
    )

    filtered_team = team[team["Year"] == selected_year].copy()

    highest_salary_team = filtered_team.loc[filtered_team["Total_Salaries"].idxmax()]
    lowest_cap_team = filtered_team.loc[filtered_team["Cap_Room"].idxmin()]
    highest_guaranteed_team = filtered_team.loc[filtered_team["Guaranteed_Salaries"].idxmax()]

    st.markdown(f"## Key Takeaways for {selected_year}")

    st.write(
        f"**Highest Total Salaries:** {highest_salary_team['Team']} "
        f"with ${highest_salary_team['Total_Salaries']:,.0f}"
    )

    st.write(
        f"**Lowest Cap Room:** {lowest_cap_team['Team']} "
        f"with ${lowest_cap_team['Cap_Room']:,.0f}"
    )

    st.write(
        f"**Highest Guaranteed Salaries:** {highest_guaranteed_team['Team']} "
        f"with ${highest_guaranteed_team['Guaranteed_Salaries']:,.0f}"
    )

    latest_momentum = momentum[momentum["Year"] == momentum["Year"].max()].iloc[0]

    st.markdown("## League Context")
    st.write(
        f"In {int(latest_momentum['Year'])}, WNBA total attendance reached "
        f"{int(latest_momentum['Total_Attendance']):,} and average attendance reached "
        f"{int(latest_momentum['Average_Attendance']):,}, showing continued league-wide audience growth."
    )

    st.markdown("## Why Financial Differences Exist")

    st.write("""
    Financial differences across WNBA teams are not random. They often reflect different roster-building stages,
    different levels of guaranteed salary commitment, and different approaches to cap management. Some teams operate
    with a strong win-now mindset and spend aggressively near the cap, while others preserve more flexibility for future moves.

    At the same time, base player pay across the league remains relatively low compared with the league’s growing visibility.
    This is not explained by momentum alone. It is also shaped by the current CBA structure, fixed cap growth, and unresolved
    revenue-sharing questions.
    """)
    st.markdown("## Three Team-Level Financial Profiles")
    st.markdown("### 1. Aggressive Contenders")

    st.write("""
    These teams tend to operate with higher total salaries, lower cap room, and stronger guaranteed salary commitments.
    Their financial profile suggests a more aggressive competitive posture. Rather than preserving flexibility, they appear
    more willing to allocate resources toward immediate roster strength.

    From a business perspective, low cap room is not always a negative signal. In many cases, it reflects a stronger win-now
    approach and a greater willingness to invest in current competitiveness.
    """)
    st.markdown("### 2. Balanced Operators")

    st.write("""
    These teams appear to balance payroll commitment with a manageable degree of flexibility. Their salary structures suggest
    competitive intent, but without the same level of financial compression seen among the most aggressive teams.

    This profile may represent organizations that are trying to remain competitive while also protecting enough cap room
    to adjust their roster strategy over time.
    """)
    st.markdown("### 3. Flexible or Transitional Teams")

    st.write("""
    These teams usually show lower total salary commitment, higher cap room, or lighter guaranteed salary pressure.
    Their financial structure suggests a more flexible or transitional position.

    This does not necessarily mean they are unsuccessful. Instead, it may indicate a rebuilding phase, a more conservative
    allocation strategy, or a roster structure that leaves more room for future adjustment.
    """)
    st.markdown("## Overall Interpretation")

    st.write("""
    Team-level financial differences show that WNBA organizations do not respond to league growth in the same way.
    Some teams invest aggressively, some manage payroll more evenly, and others preserve flexibility.

    At the league level, however, base player pay still appears relatively low compared with the WNBA’s recent growth in
    attendance, audience attention, and visibility. This suggests that league momentum and salary growth are related,
    but they do not move at the same speed.
    """)
    st.write("""
    In this project, lower cap room is not treated as automatically negative. In some cases, it may reflect stronger
    competitive investment and a greater willingness to allocate resources toward roster quality.
    """)