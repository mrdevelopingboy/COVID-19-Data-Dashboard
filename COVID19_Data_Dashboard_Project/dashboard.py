from pathlib import Path
import pandas as pd
import streamlit as st
import plotly.express as px

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "covid19_sample_data.csv"

st.set_page_config(page_title="COVID-19 Data Dashboard", page_icon="🦠", layout="wide")
st.title("🦠 COVID-19 Data Dashboard")
st.caption("Interactive dashboard with country, region, date, and metric filters.")
st.info("Data note: this is synthetic sample data created for practice, not official public-health data.")

@st.cache_data
def load_data():
    return pd.read_csv(DATA_FILE, parse_dates=["Date"])

df = load_data()
min_date, max_date = df.Date.min().date(), df.Date.max().date()

with st.sidebar:
    st.header("Dashboard Filters")
    regions = sorted(df.Region.unique().tolist())
    selected_regions = st.multiselect("Select region(s)", regions, default=regions)
    possible = sorted(df[df.Region.isin(selected_regions)].Country.unique().tolist())
    selected_countries = st.multiselect("Select country/countries", possible, default=possible)
    dates = st.date_input("Select date range", value=(min_date, max_date), min_value=min_date, max_value=max_date)
    metric = st.selectbox("Trend metric", ["New_Cases","New_Deaths","Cumulative_Cases","Cumulative_Deaths","Cumulative_Recovered"])

if not selected_countries:
    st.warning("Please select at least one country.")
    st.stop()
if isinstance(dates, (tuple,list)) and len(dates)==2:
    start_date,end_date=dates
else:
    start_date,end_date=min_date,max_date

filtered=df[df.Region.isin(selected_regions) & df.Country.isin(selected_countries) &
            (df.Date.dt.date>=start_date) & (df.Date.dt.date<=end_date)].copy()
if filtered.empty:
    st.warning("No data matches these filters. Change the filters and try again.")
    st.stop()

latest=filtered.sort_values("Date").groupby("Country",as_index=False).tail(1)
a,b,c,d=st.columns(4)
a.metric("Cumulative cases",f"{int(latest.Cumulative_Cases.sum()):,}")
b.metric("Cumulative deaths",f"{int(latest.Cumulative_Deaths.sum()):,}")
c.metric("Cumulative recovered",f"{int(latest.Cumulative_Recovered.sum()):,}")
d.metric("Average vaccination rate",f"{latest.Vaccination_Rate.mean()*100:.1f}%")

st.subheader("Trend over time")
trend=filtered.groupby(["Date","Country"],as_index=False)[metric].sum()
fig=px.line(trend,x="Date",y=metric,color="Country",markers=True,title=metric.replace("_"," ")+" over time")
fig.update_layout(hovermode="x unified")
st.plotly_chart(fig,use_container_width=True)

left,right=st.columns(2)
with left:
    comparison=latest.sort_values("Cumulative_Cases",ascending=False)
    fig2=px.bar(comparison,x="Country",y="Cumulative_Cases",color="Region",title="Cumulative cases by country")
    st.plotly_chart(fig2,use_container_width=True)
with right:
    region_summary=latest.groupby("Region",as_index=False).Cumulative_Cases.sum()
    fig3=px.pie(region_summary,names="Region",values="Cumulative_Cases",title="Cases share by region")
    st.plotly_chart(fig3,use_container_width=True)

st.subheader("Vaccination rate by country")
fig4=px.bar(latest.sort_values("Vaccination_Rate",ascending=False),x="Country",y="Vaccination_Rate",
            color="Region",title="Vaccination rate (sample data)")
fig4.update_yaxes(tickformat=".0%")
st.plotly_chart(fig4,use_container_width=True)

with st.expander("View filtered data table"):
    st.dataframe(filtered.sort_values(["Date","Country"]),use_container_width=True)
    st.download_button("Download filtered data as CSV",filtered.to_csv(index=False).encode("utf-8"),
                       "filtered_covid19_data.csv","text/csv")
st.caption(f"Showing {len(filtered):,} rows for {len(selected_countries)} selected countries.")
