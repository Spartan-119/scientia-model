import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Page configuration
st.set_page_config(
    page_title="Scientia Financial Projections",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .stMetric {
        background-color: #f0f2f6;
        padding: 10px;
        border-radius: 5px;
    }
    .big-font {
        font-size:20px !important;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# Title
st.title("📊 Scientia: Complete Financial Model (24 Months)")
st.markdown("**Revenue, Costs, Profitability & Cash**")
st.divider()

# Sidebar for assumptions
st.sidebar.header("🎯 Quick Scenario Selector")

# Preset scenarios
scenario = st.sidebar.selectbox(
    "Choose a scenario:",
    ["Base Case", "Conservative", "Optimistic", "Custom"]
)

if scenario == "Conservative":
    # Conservative defaults
    conversion_rate = 2.0
    free_user_growth_acceleration = 1.05
    deal_growth_rate = 15.0
    b2c_cac = 40
    enterprise_cac = 2500
elif scenario == "Optimistic":
    # Optimistic defaults
    conversion_rate = 5.0
    free_user_growth_acceleration = 1.15
    deal_growth_rate = 30.0
    b2c_cac = 20
    enterprise_cac = 1500
else:
    # Base case defaults (will be overridden if Custom)
    conversion_rate = 3.0
    free_user_growth_acceleration = 1.1
    deal_growth_rate = 20.0
    b2c_cac = 30
    enterprise_cac = 2000

st.sidebar.divider()

# Core assumptions (always visible)
st.sidebar.subheader("🔧 Core Assumptions")

with st.sidebar.expander("💰 Revenue Model", expanded=(scenario == "Custom")):
    indiv_price = st.number_input("B2C Price (£/month)", value=20, min_value=1, step=1)
    enterprise_price = st.number_input("Enterprise Price (£/seat/mo)", value=14, min_value=1, step=1)
    if scenario == "Custom":
        conversion_rate = st.number_input("Conversion Rate %", value=3.0, min_value=0.0, max_value=100.0, step=0.1, format="%.1f")

with st.sidebar.expander("📈 Growth Assumptions", expanded=(scenario == "Custom")):
    initial_free_users = st.number_input("Initial Free Users", value=300, min_value=0, step=50)
    monthly_free_user_growth = st.number_input("New Free Users/mo", value=200, min_value=0, step=50)
    if scenario == "Custom":
        free_user_growth_acceleration = st.number_input("Viral Growth Multiplier", value=1.1, min_value=1.0, max_value=2.0, step=0.01, format="%.2f")
    avg_seats_per_deal = st.number_input("Avg Seats/Deal", value=25, min_value=1, step=1)
    if scenario == "Custom":
        deal_growth_rate = st.number_input("Enterprise Deal Growth %", value=20.0, min_value=0.0, max_value=200.0, step=1.0, format="%.1f")

with st.sidebar.expander("💼 Operations & Costs"):
    initial_cash = st.number_input("Initial Cash (£)", value=150000, min_value=0, step=10000)
    llm_cost_per_user = st.number_input("LLM Cost/User/mo (£)", value=2.0, min_value=0.0, step=0.1, format="%.1f")
    if scenario == "Custom":
        b2c_cac = st.number_input("B2C CAC (£)", value=30, min_value=0, step=5)
        enterprise_cac = st.number_input("Enterprise CAC (£)", value=2000, min_value=0, step=100)
    marketing_spend = st.number_input("Marketing Spend (£/mo)", value=2000, min_value=0, step=500)
    
with st.sidebar.expander("👥 Team"):
    founders_count = st.number_input("Founders", value=2, min_value=0, step=1)
    founder_salary = st.number_input("Founder Salary (£/mo)", value=3000, min_value=0, step=500)
    engineers_count = st.number_input("Engineers", value=1, min_value=0, step=1)
    engineer_salary = st.number_input("Engineer Salary (£/mo)", value=5000, min_value=0, step=500)

# Hidden advanced parameters (set to defaults)
paid_user_churn = 5.0
enterprise_launch_month = 6
deals_month_1 = 1
enterprise_churn = 3.0
infrastructure_cost_base = 500
infrastructure_cost_per_user = 0.1
sales_reps_count = 0
sales_rep_salary = 4000
sales_hire_month = 6
office_and_misc = 1000

# Calculation function
def calculate_projections():
    months = []
    total_free_users = 0
    paid_users = 0
    enterprise_seats = 0
    total_enterprise_deals = 0
    monthly_new_free_users = monthly_free_user_growth
    cash_balance = initial_cash
    
    for month in range(1, 25):
        # REVENUE CALCULATIONS
        # B2C Freemium
        if month == 1:
            total_free_users = initial_free_users
        else:
            monthly_new_free_users = round(monthly_new_free_users * free_user_growth_acceleration)
            total_free_users += monthly_new_free_users
        
        new_conversions = round(total_free_users * (conversion_rate / 100))
        churned_paid_users = paid_users * (paid_user_churn / 100)
        paid_users = max(0, paid_users + new_conversions - churned_paid_users)
        total_free_users = max(0, total_free_users - new_conversions)
        
        # Enterprise
        new_deals = 0
        if month >= enterprise_launch_month:
            months_since_enterprise_launch = month - enterprise_launch_month
            new_deals = round(deals_month_1 * ((1 + deal_growth_rate / 100) ** months_since_enterprise_launch))
            
            total_enterprise_deals += new_deals
            new_seats = new_deals * avg_seats_per_deal
            churned_seats = enterprise_seats * (enterprise_churn / 100)
            enterprise_seats = enterprise_seats + new_seats - churned_seats
        
        b2c_mrr = round(paid_users * indiv_price)
        enterprise_mrr = round(enterprise_seats * enterprise_price)
        total_revenue = b2c_mrr + enterprise_mrr
        
        # COST CALCULATIONS
        # COGS
        total_active_users = paid_users + enterprise_seats + (total_free_users * 0.3)  # 30% of free users active
        llm_costs = round(total_active_users * llm_cost_per_user)
        infrastructure_costs = round(infrastructure_cost_base + (total_active_users * infrastructure_cost_per_user))
        total_cogs = llm_costs + infrastructure_costs
        
        # Customer Acquisition Costs
        b2c_acquisition_cost = round(new_conversions * b2c_cac)
        enterprise_acquisition_cost = round(new_deals * enterprise_cac) if month >= enterprise_launch_month else 0
        total_cac = b2c_acquisition_cost + enterprise_acquisition_cost
        
        # Team Costs
        sales_reps = sales_reps_count if month >= sales_hire_month else 0
        team_costs = (
            (founders_count * founder_salary) +
            (engineers_count * engineer_salary) +
            (sales_reps * sales_rep_salary)
        )
        
        # Total Operating Expenses
        total_opex = team_costs + marketing_spend + office_and_misc + total_cac
        
        # P&L
        gross_profit = total_revenue - total_cogs
        gross_margin = (gross_profit / total_revenue * 100) if total_revenue > 0 else 0
        net_income = gross_profit - total_opex
        net_burn = -net_income
        
        # Cash
        cash_balance = cash_balance + net_income
        runway = round(cash_balance / net_burn) if cash_balance > 0 and net_burn > 0 else 0
        
        months.append({
            'Month': month,
            # Users
            'Free Users': round(total_free_users),
            'Paid Users': round(paid_users),
            'Enterprise Seats': round(enterprise_seats),
            'Total Active Users': round(total_active_users),
            # Revenue
            'B2C MRR': b2c_mrr,
            'Enterprise MRR': enterprise_mrr,
            'Total Revenue': total_revenue,
            # Costs
            'LLM Costs': llm_costs,
            'Infrastructure Costs': infrastructure_costs,
            'Total COGS': total_cogs,
            'B2C Acquisition': b2c_acquisition_cost,
            'Enterprise Acquisition': enterprise_acquisition_cost,
            'Total CAC': total_cac,
            'Team Costs': team_costs,
            'Marketing Spend': marketing_spend,
            'Total Opex': total_opex,
            # P&L
            'Gross Profit': gross_profit,
            'Gross Margin': round(gross_margin, 1),
            'Net Income': round(net_income),
            'Net Burn': round(net_burn),
            # Cash
            'Cash Balance': round(cash_balance),
            'Runway': runway,
        })
    
    return pd.DataFrame(months)

# Calculate projections
df = calculate_projections()
final_month = df.iloc[-1]
break_even_month = df[df['Net Income'] >= 0]['Month'].min() if (df['Net Income'] >= 0).any() else 'Not reached'

# Display key outcomes
st.subheader("🎯 Key Metrics Dashboard")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Month 24 ARR",
        f"£{(final_month['Total Revenue'] * 12) / 1_000_000:.2f}M",
        delta=None
    )

with col2:
    st.metric(
        "Gross Margin",
        f"{final_month['Gross Margin']:.1f}%",
        delta=None
    )

with col3:
    if final_month['Net Income'] >= 0:
        st.metric(
            "Profitability",
            f"£{final_month['Net Income'] / 1000:.1f}K profit/mo",
            delta="Cash flow positive! ✅"
        )
    else:
        st.metric(
            "Monthly Burn",
            f"£{final_month['Net Burn'] / 1000:.0f}K",
            delta=None,
            delta_color="inverse"
        )

with col4:
    if final_month['Net Income'] >= 0:
        st.metric(
            "Cash Runway",
            "Self-Sustaining ♾️",
            delta="No funding needed"
        )
    else:
        runway_display = f"{final_month['Runway']}mo" if final_month['Runway'] > 0 else "Out of cash!"
        st.metric(
            "Cash Runway",
            runway_display,
            delta=None
        )

st.divider()

# Main Charts - Two key visualizations
col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Revenue Growth Path")
    fig_revenue = go.Figure()
    fig_revenue.add_trace(go.Scatter(
        x=df['Month'], 
        y=df['Total Revenue'],
        mode='lines',
        name='Total Revenue',
        line=dict(color='#8B5CF6', width=3),
        fill='tozeroy'
    ))
    fig_revenue.update_layout(
        xaxis_title="Month",
        yaxis_title="Monthly Revenue (£)",
        hovermode='x unified',
        height=350,
        showlegend=False
    )
    st.plotly_chart(fig_revenue, use_container_width=True)

with col2:
    st.subheader("💰 Cash Runway")
    fig_cash = go.Figure()
    fig_cash.add_trace(go.Scatter(
        x=df['Month'],
        y=df['Cash Balance'],
        mode='lines',
        name='Cash Balance',
        line=dict(color='#3B82F6', width=3),
        fill='tozeroy'
    ))
    fig_cash.add_hline(y=0, line_dash="dash", line_color="red", opacity=0.5)
    fig_cash.update_layout(
        xaxis_title="Month",
        yaxis_title="Cash Balance (£)",
        hovermode='x unified',
        height=350,
        showlegend=False
    )
    st.plotly_chart(fig_cash, use_container_width=True)

st.divider()

# Detailed P&L - Hidden by default
with st.expander("📊 View Detailed P&L Analysis"):
    st.subheader("Revenue vs Costs Breakdown")
    
    fig_pnl = go.Figure()
    fig_pnl.add_trace(go.Scatter(x=df['Month'], y=df['Total Revenue'], mode='lines', name='Revenue', line=dict(color='#8B5CF6', width=2)))
    fig_pnl.add_trace(go.Scatter(x=df['Month'], y=df['Total COGS'], mode='lines', name='COGS', line=dict(color='#F59E0B', width=2)))
    fig_pnl.add_trace(go.Scatter(x=df['Month'], y=df['Total Opex'], mode='lines', name='Opex', line=dict(color='#EF4444', width=2)))
    fig_pnl.add_trace(go.Scatter(x=df['Month'], y=df['Net Income'], mode='lines', name='Net Income', line=dict(color='#10B981', width=2)))
    fig_pnl.update_layout(xaxis_title="Month", yaxis_title="Amount (£)", hovermode='x unified', height=350)
    st.plotly_chart(fig_pnl, use_container_width=True)
    
    st.subheader("Monthly Burn Rate")
    fig_burn = go.Figure()
    fig_burn.add_trace(go.Bar(x=df['Month'], y=df['Net Burn'], name='Net Burn', marker_color='#EF4444'))
    fig_burn.update_layout(xaxis_title="Month", yaxis_title="Monthly Burn (£)", hovermode='x unified', height=300)
    st.plotly_chart(fig_burn, use_container_width=True)

st.divider()

# Complete P&L Table - Behind expander
with st.expander("📋 View Complete Monthly P&L Table"):
    # Create formatted P&L table
    pnl_display = pd.DataFrame({
        'Month': df['Month'],
        'Revenue': df['Total Revenue'].apply(lambda x: f"£{x/1000:.1f}K"),
        'COGS': df['Total COGS'].apply(lambda x: f"£{x/1000:.1f}K"),
        'GM%': df['Gross Margin'].apply(lambda x: f"{x:.1f}%"),
        'CAC': df['Total CAC'].apply(lambda x: f"£{x/1000:.1f}K"),
        'Team': df['Team Costs'].apply(lambda x: f"£{x/1000:.1f}K"),
        'Opex': df['Total Opex'].apply(lambda x: f"£{x/1000:.1f}K"),
        'Net Income': df['Net Income'].apply(lambda x: f"£{x/1000:.1f}K"),
        'Burn': df['Net Burn'].apply(lambda x: f"£{x/1000:.1f}K"),
        'Cash': df['Cash Balance'].apply(lambda x: f"£{x/1000:.0f}K"),
        'Runway': df['Runway'].apply(lambda x: f"{x}mo"),
    })
    
    st.dataframe(pnl_display, use_container_width=True, height=400)

st.divider()

# Key Insights - Simplified
col1, col2, col3 = st.columns(3)

with col1:
    st.info(f"""
    **🎯 Growth Trajectory**
    - Break-Even: Month {break_even_month}
    - Final ARR: £{(final_month['Total Revenue'] * 12) / 1_000_000:.2f}M
    - Gross Margin: {final_month['Gross Margin']:.1f}%
    """)

with col2:
    cash_status = "🔴 Critical" if final_month['Cash Balance'] < 0 else "🟢 Healthy" if final_month['Runway'] > 12 else "🟡 Monitor"
    st.warning(f"""
    **💰 Cash Position**
    - Status: {cash_status}
    - Balance M24: £{final_month['Cash Balance']/1000:.0f}K
    - Runway: {final_month['Runway']} months
    """)

with col3:
    st.success(f"""
    **📊 Revenue Mix (M24)**
    - B2C: £{final_month['B2C MRR']/1000:.1f}K ({(final_month['B2C MRR']/final_month['Total Revenue']*100):.0f}%)
    - Enterprise: £{final_month['Enterprise MRR']/1000:.1f}K ({(final_month['Enterprise MRR']/final_month['Total Revenue']*100):.0f}%)
    """)

# Footer
st.divider()
st.caption(f"💡 **{scenario}** scenario selected. Switch scenarios in the sidebar or choose 'Custom' to fine-tune all parameters.")

