COVID-19 DATA DASHBOARD — BEGINNER PROJECT

IMPORTANT: This project uses synthetic sample data for practice. It is NOT official COVID-19 data and should not be used for health decisions.

FILES
- dashboard.py: interactive Streamlit dashboard
- data/covid19_sample_data.csv: 10 countries, monthly data from 2020 through 2023
- requirements.txt: Python packages
- README.txt: instructions

FEATURES
- Region, country, and date-range filters
- Selectable trend metric
- Summary metrics for cases, deaths, recovered, and vaccination rate
- Interactive trend line chart
- Country comparison bar chart
- Region share pie chart
- Vaccination rate chart
- Filtered data table and CSV download

RUN ON WINDOWS / VS CODE
1. Extract the ZIP file.
2. Open the extracted COVID19_Data_Dashboard_Project folder in VS Code.
3. Choose Terminal > New Terminal.
4. Install packages:
   py -m pip install -r requirements.txt
5. Run the dashboard:
   py -m streamlit run dashboard.py
6. A browser should open. If not, open the Local URL shown in the terminal, usually http://localhost:8501.
7. Use the filters on the left to interact with the dashboard.

SUBMISSION
Upload the complete ZIP file to the assignment portal (maximum 10 MB).
Suggested note:
Built an interactive COVID-19 Data Dashboard using Python, Pandas, Plotly, and Streamlit. It includes region, country, and date filters, summary metrics, trend analysis, country and region comparisons, vaccination visualization, and a filtered data table.

PROJECT STRUCTURE
COVID19_Data_Dashboard_Project/
  dashboard.py
  requirements.txt
  README.txt
  data/
    covid19_sample_data.csv
