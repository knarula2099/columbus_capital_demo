import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

# Set page configuration
st.set_page_config(
    page_title="PropertyPulse AI - Columbus Capital",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1E88E5;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.5rem;
        font-weight: 600;
        color: #333;
        margin-top: 1rem;
    }
    .card {
        padding: 1.5rem;
        border-radius: 0.5rem;
        background-color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
    }
    .metric-value {
        font-size: 2rem;
        font-weight: 700;
        color: #1E88E5;
    }
    .metric-label {
        font-size: 1rem;
        color: #555;
    }
    .alert-high {
        padding: 0.75rem;
        border-radius: 0.25rem;
        background-color: rgba(255, 99, 71, 0.1);
        border-left: 4px solid tomato;
        margin-bottom: 0.5rem;
    }
    .alert-medium {
        padding: 0.75rem;
        border-radius: 0.25rem;
        background-color: rgba(255, 165, 0, 0.1);
        border-left: 4px solid orange;
        margin-bottom: 0.5rem;
    }
    .alert-low {
        padding: 0.75rem;
        border-radius: 0.25rem;
        background-color: rgba(30, 144, 255, 0.1);
        border-left: 4px solid dodgerblue;
        margin-bottom: 0.5rem;
    }
    .innovation-card {
        padding: 1rem;
        border-radius: 0.25rem;
        background-color: white;
        border: 1px solid #ddd;
        margin-bottom: 0.5rem;
    }
    .innovation-year {
        display: inline-block;
        padding: 0.25rem 0.5rem;
        border-radius: 0.25rem;
        background-color: rgba(30, 144, 255, 0.1);
        color: dodgerblue;
        font-size: 0.8rem;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# Sample data generation functions
def generate_maintenance_data():
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"]
    predicted = [12, 15, 10, 8, 14, 16, 18]
    actual = [15, 14, 11, 8, 0, 0, 0]
    urgent = [3, 2, 1, 0, 0, 0, 0]
    future = [False, False, False, False, True, True, True]
    
    return pd.DataFrame({
        "month": months,
        "predicted": predicted,
        "actual": actual,
        "urgent": urgent,
        "future": future
    })

def generate_energy_data():
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"]
    standard = [45000, 42000, 44000, 46000, 48000, 52000, 54000]
    optimized = [45000, 40000, 38000, 37000, 36000, 35000, 34000]
    future = [False, False, False, False, True, True, True]
    
    return pd.DataFrame({
        "month": months,
        "standard": standard,
        "optimized": optimized,
        "future": future
    })

def generate_tenant_satisfaction_data():
    quarters = ["Q1", "Q2", "Q3", "Q4"]
    scores = [76, 82, 89, 94]
    future = [False, False, False, True]
    
    return pd.DataFrame({
        "quarter": quarters,
        "score": scores,
        "future": future
    })

def generate_cost_savings_data():
    categories = ["Maintenance", "Energy", "Staffing", "Operations"]
    values = [32, 45, 15, 8]
    
    return pd.DataFrame({
        "category": categories,
        "value": values
    })

def generate_alerts():
    return [
        {"property": "Los Altos Ranch Market", "issue": "HVAC system predicted failure within 14 days", "priority": "High"},
        {"property": "San Isidro Plaza", "issue": "Energy usage 15% above optimal levels", "priority": "Medium"},
        {"property": "Coronado Building", "issue": "Elevator maintenance recommended", "priority": "Low"}
    ]

def generate_properties():
    return [
        "All Properties",
        "San Isidro Plaza",
        "Los Altos Ranch Market",
        "Three Amigos",
        "Santa Fe Building 440",
        "1651 Galisteo",
        "Coronado Building",
        "Imaging Center",
        "Granada Square",
        "San Ignacio Apartments",
        "San Isidro Apartments",
        "Target Store",
        "Whole Foods"
    ]

def generate_future_innovations():
    return [
        {
            "name": "Autonomous Building Systems",
            "description": "Self-regulating energy, water, and climate systems with zero human intervention needed.",
            "year": 2027
        },
        {
            "name": "Predictive Tenant Matching",
            "description": "AI algorithms that predict tenant-property fit with 98% accuracy, optimizing community ecosystem.",
            "year": 2028
        },
        {
            "name": "Digital Twin Integration",
            "description": "Complete virtual replicas of properties for scenario testing and optimization.",
            "year": 2029
        },
        {
            "name": "Blockchain Leasing",
            "description": "Smart contracts for all tenant relationships with automated enforcement and payments.",
            "year": 2030
        },
        {
            "name": "Community AI Concierge",
            "description": "AI-based community management system that handles tenant requests and fosters relationships.",
            "year": 2031
        },
        {
            "name": "Autonomous Infrastructure Repair",
            "description": "Robotic systems that automatically repair building issues without human intervention.",
            "year": 2033
        }
    ]

# Main dashboard content
def main():
    # --- SIDEBAR ---
    with st.sidebar:
        st.image("https://via.placeholder.com/150x80?text=Columbus+Capital", width=150)
        st.markdown("### PropertyPulse AI")
        
        properties = generate_properties()
        selected_property = st.selectbox("Select Property", properties)
        
        st.markdown("---")
        st.markdown("### Dashboard Options")
        view_type = st.radio("View Type", ["Overview", "Maintenance", "Energy", "Tenant Experience", "Financial Impact"])
        
        st.markdown("---")
        st.markdown("### Future Focus")
        time_horizon = st.slider("Time Horizon (Years)", 1, 10, 5)
        
        st.markdown("---")
        st.markdown("### About")
        st.markdown("PropertyPulse AI is a forward-looking dashboard demonstrating how AI can transform property management for Columbus Capital.")
        st.markdown("Created by Karan Narula")
    
    # --- MAIN CONTENT ---
    if view_type == "Overview":
        show_overview(selected_property)
    elif view_type == "Maintenance":
        show_maintenance(selected_property)
    elif view_type == "Energy":
        show_energy(selected_property)
    elif view_type == "Tenant Experience":
        show_tenant(selected_property)
    elif view_type == "Financial Impact":
        show_financial(selected_property)

def show_overview(selected_property):
    st.markdown(f'<h1 class="main-header">PropertyPulse AI Dashboard: {selected_property}</h1>', unsafe_allow_html=True)
    
    # Top metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<p class="metric-label">AI Health Score</p>', unsafe_allow_html=True)
        st.markdown('<p class="metric-value">87%</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<p class="metric-label">Projected Annual Savings</p>', unsafe_allow_html=True)
        st.markdown('<p class="metric-value">$247,500</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<p class="metric-label">Tenant Satisfaction</p>', unsafe_allow_html=True)
        st.markdown('<p class="metric-value">89%</p>', unsafe_allow_html=True)
        st.markdown('<p>+18% YoY with AI Optimization</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Alerts
    st.markdown('<h2 class="sub-header">AI-Generated Alerts</h2>', unsafe_allow_html=True)
    alerts = generate_alerts()
    
    for alert in alerts:
        priority_class = f"alert-{alert['priority'].lower()}"
        st.markdown(f"""
        <div class="{priority_class}">
            <strong>{alert['property']}:</strong> {alert['issue']}
            <span style="float: right; font-weight: 600;">{alert['priority']}</span>
        </div>
        """, unsafe_allow_html=True)
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<h2 class="sub-header">Predictive Maintenance</h2>', unsafe_allow_html=True)
        maintenance_data = generate_maintenance_data()
        
        fig = px.bar(maintenance_data, x="month", y=["predicted", "actual", "urgent"],
                    title="Maintenance Issues by Month",
                    labels={"value": "Number of Issues", "variable": "Type"},
                    color_discrete_sequence=["#8884d8", "#82ca9d", "#ff7300"])
        
        # Add a vertical line to separate past from future predictions
        future_start_index = maintenance_data[maintenance_data["future"] == True].index[0]
        future_start_month = maintenance_data.iloc[future_start_index]["month"]
        
        fig.add_vline(x=future_start_month, line_dash="dash", line_color="grey")
        fig.add_annotation(x=future_start_month, y=max(maintenance_data["predicted"]), 
                          text="AI Predictions", showarrow=True, arrowhead=1)
        
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("AI prediction accuracy: 93% over last 12 months")
    
    with col2:
        st.markdown('<h2 class="sub-header">Energy Optimization</h2>', unsafe_allow_html=True)
        energy_data = generate_energy_data()
        
        fig = px.line(energy_data, x="month", y=["standard", "optimized"],
                     title="Energy Usage: Standard vs. AI-Optimized",
                     labels={"value": "Energy (kWh)", "variable": "Type"},
                     color_discrete_sequence=["#ff7300", "#00C49F"])
        
        # Add a vertical line to separate past from future predictions
        future_start_index = energy_data[energy_data["future"] == True].index[0]
        future_start_month = energy_data.iloc[future_start_index]["month"]
        
        fig.add_vline(x=future_start_month, line_dash="dash", line_color="grey")
        fig.add_annotation(x=future_start_month, y=max(energy_data["standard"]), 
                          text="AI Projections", showarrow=True, arrowhead=1)
        
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("Projected annual savings: $125,000 (28% reduction)")
    
    # Future innovations
    st.markdown('<h2 class="sub-header">Future AI Innovations (2025-2035)</h2>', unsafe_allow_html=True)
    
    innovations = generate_future_innovations()
    cols = st.columns(3)
    
    for i, innovation in enumerate(innovations):
        col = cols[i % 3]
        with col:
            st.markdown(f"""
            <div class="innovation-card">
                <h3>{innovation['name']}</h3>
                <p>{innovation['description']}</p>
                <span class="innovation-year">Estimated {innovation['year']}</span>
            </div>
            """, unsafe_allow_html=True)

def show_maintenance(selected_property):
    st.markdown(f'<h1 class="main-header">Predictive Maintenance: {selected_property}</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        maintenance_data = generate_maintenance_data()
        
        # Create a more detailed maintenance visualization
        fig = make_subplots(rows=2, cols=1, 
                           subplot_titles=("Monthly Maintenance Issues", "AI Detection Efficiency"))
        
        # Bar chart of maintenance issues
        fig.add_trace(
            go.Bar(x=maintenance_data["month"], y=maintenance_data["predicted"], name="AI Predicted",
                  marker_color="#8884d8"),
            row=1, col=1
        )
        
        fig.add_trace(
            go.Bar(x=maintenance_data["month"], y=maintenance_data["actual"], name="Actual",
                  marker_color="#82ca9d"),
            row=1, col=1
        )
        
        fig.add_trace(
            go.Bar(x=maintenance_data["month"], y=maintenance_data["urgent"], name="Urgent",
                  marker_color="#ff7300"),
            row=1, col=1
        )
        
        # Line chart showing detection efficiency over time
        months = maintenance_data["month"][:4]  # Only use past months
        efficiency = [85, 89, 92, 95]  # Sample efficiency percentages
        
        fig.add_trace(
            go.Scatter(x=months, y=efficiency, mode="lines+markers", name="AI Detection Efficiency",
                      line=dict(color="#1E88E5", width=3)),
            row=2, col=1
        )
        
        fig.update_layout(height=600, title_text="AI-Powered Maintenance Analysis")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown('<h2 class="sub-header">Maintenance Insights</h2>', unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card">
            <h3>Cost Reduction</h3>
            <p class="metric-value">38%</p>
            <p>Decrease in maintenance costs through AI prediction</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card">
            <h3>Emergency Repairs</h3>
            <p class="metric-value">-74%</p>
            <p>Reduction in emergency repair situations</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card">
            <h3>Equipment Lifespan</h3>
            <p class="metric-value">+32%</p>
            <p>Increase in average equipment lifespan</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<h2 class="sub-header">How AI Transforms Maintenance</h2>', unsafe_allow_html=True)
    st.markdown("""
    * **Early Detection**: AI identifies subtle patterns in sensor data to predict failures 3-6 weeks before conventional methods
    * **Optimal Scheduling**: Maintenance is scheduled during optimal times to minimize tenant disruption
    * **Resource Optimization**: Predictive maintenance reduces parts inventory needs by 25% while improving availability
    * **Automatic Dispatching**: The system automatically dispatches appropriate technicians based on issue complexity
    """)
    
    st.markdown('<h2 class="sub-header">Predicted Maintenance Timeline</h2>', unsafe_allow_html=True)
    
    # Create a custom timeline of upcoming maintenance
    timeline_data = [
        {"task": "HVAC Compressor Replacement", "property": "Los Altos Ranch Market", "due": "14 days", "severity": "High"},
        {"task": "Parking Lot Lighting Upgrade", "property": "San Isidro Plaza", "due": "21 days", "severity": "Medium"},
        {"task": "Elevator Annual Maintenance", "property": "Coronado Building", "due": "30 days", "severity": "Low"},
        {"task": "Roof Inspection", "property": "Granada Square", "due": "45 days", "severity": "Medium"},
        {"task": "Plumbing System Check", "property": "San Ignacio Apartments", "due": "60 days", "severity": "Low"}
    ]
    
    for item in timeline_data:
        severity_color = "tomato" if item["severity"] == "High" else "orange" if item["severity"] == "Medium" else "dodgerblue"
        st.markdown(f"""
        <div class="card" style="margin-bottom: 0.5rem; border-left: 4px solid {severity_color};">
            <div style="display: flex; justify-content: space-between;">
                <div>
                    <h3>{item["task"]}</h3>
                    <p>Location: {item["property"]}</p>
                </div>
                <div>
                    <p style="font-weight: 600; color: {severity_color};">{item["severity"]}</p>
                    <p>Due in: {item["due"]}</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

def show_energy(selected_property):
    st.markdown(f'<h1 class="main-header">Energy Optimization: {selected_property}</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        energy_data = generate_energy_data()
        
        fig = px.line(energy_data, x="month", y=["standard", "optimized"],
                     title="Energy Usage Optimization",
                     labels={"value": "Energy (kWh)", "variable": "Type"},
                     color_discrete_sequence=["#ff7300", "#00C49F"])
        
        # Add projected savings annotation
        monthly_savings = []
        for i, row in energy_data.iterrows():
            if i > 0:  # Skip first month as there were no savings
                monthly_savings.append(row["standard"] - row["optimized"])
        
        avg_monthly_saving = sum(monthly_savings) / len(monthly_savings)
        annual_saving = avg_monthly_saving * 12
        
        fig.add_annotation(
            x=energy_data["month"].iloc[-1],
            y=energy_data["optimized"].iloc[-1],
            text=f"Projected Annual Savings: ${annual_saving:,.0f}",
            showarrow=True,
            arrowhead=1
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown('<h2 class="sub-header">Energy Stats</h2>', unsafe_allow_html=True)
        
        # Calculate stats
        total_reduction_pct = ((energy_data["standard"].sum() - energy_data["optimized"].sum()) / 
                              energy_data["standard"].sum() * 100)
        
        st.markdown(f"""
        <div class="card">
            <h3>Energy Reduction</h3>
            <p class="metric-value">{total_reduction_pct:.1f}%</p>
            <p>Overall reduction in energy usage</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card">
            <h3>Carbon Offset</h3>
            <p class="metric-value">162 tons</p>
            <p>Annual CO₂ emissions reduction</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card">
            <h3>ROI Timeline</h3>
            <p class="metric-value">1.8 years</p>
            <p>For AI energy system implementation</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<h2 class="sub-header">AI Energy Optimization Technologies</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="card">
            <h3>Predictive Climate Control</h3>
            <p>AI adjusts HVAC settings based on weather forecasts, occupancy patterns, and tenant preferences, reducing energy waste by 22%.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card">
            <h3>Smart Lighting Systems</h3>
            <p>Automated lighting adjusts based on natural light availability and occupancy, with machine learning that adapts to usage patterns over time.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="card">
            <h3>Load Balancing & Demand Response</h3>
            <p>AI shifts energy usage to off-peak hours and negotiates with utility providers for optimal rates based on predictive usage models.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Add an interactive element
    st.markdown('<h2 class="sub-header">Energy Savings Calculator</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        property_size = st.slider("Property Size (sq ft)", 5000, 100000, 25000, 1000)
        current_energy_cost = st.slider("Current Monthly Energy Cost ($)", 1000, 50000, 15000, 500)
        optimization_level = st.select_slider("AI Optimization Level", options=["Basic", "Standard", "Advanced"])
    
    with col2:
        # Calculate estimated savings based on inputs
        if optimization_level == "Basic":
            savings_pct = 0.18
        elif optimization_level == "Standard":
            savings_pct = 0.25
        else:
            savings_pct = 0.32
        
        monthly_savings = current_energy_cost * savings_pct
        annual_savings = monthly_savings * 12
        
        st.markdown(f"""
        <div class="card">
            <h3>Estimated Results</h3>
            <p class="metric-value">${annual_savings:,.0f}/year</p>
            <p>Projected savings with {optimization_level} AI optimization</p>
            <p>Implementation cost: ${property_size * 1.8:,.0f}</p>
            <p>ROI period: {(property_size * 1.8 / annual_savings):.1f} years</p>
        </div>
        """, unsafe_allow_html=True)

def show_tenant(selected_property):
    st.markdown(f'<h1 class="main-header">Tenant Experience: {selected_property}</h1>', unsafe_allow_html=True)
    
    tenant_data = generate_tenant_satisfaction_data()
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        fig = px.line(tenant_data, x="quarter", y="score",
                     title="Tenant Satisfaction Score Trend",
                     labels={"score": "Satisfaction Score (0-100)"},
                     line_shape="spline")
        
        fig.update_traces(line=dict(color="#8884d8", width=3), mode="lines+markers", marker=dict(size=10))
        
        # Add a vertical line to separate past from future predictions
        future_start_index = tenant_data[tenant_data["future"] == True].index[0]
        future_start_quarter = tenant_data.iloc[future_start_index]["quarter"]
        
        fig.add_vline(x=future_start_quarter, line_dash="dash", line_color="grey")
        fig.add_annotation(x=future_start_quarter, y=tenant_data["score"].max(), 
                          text="AI Projection", showarrow=True, arrowhead=1)
        
        # Add benchmark lines
        fig.add_shape(type="line", 
                     x0=tenant_data["quarter"].iloc[0], y0=75, 
                     x1=tenant_data["quarter"].iloc[-1], y1=75,
                     line=dict(color="green", width=1, dash="dot"))
        
        fig.add_annotation(x=tenant_data["quarter"].iloc[0], y=75,
                          text="Industry Average", showarrow=False,
                          xanchor="left", yanchor="bottom")
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown('<h2 class="sub-header">Tenant Metrics</h2>', unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card">
            <h3>Renewal Rate</h3>
            <p class="metric-value">94%</p>
            <p>+12% after AI implementation</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card">
            <h3>Response Time</h3>
            <p class="metric-value">1.2 hours</p>
            <p>-68% with AI-enabled communication</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card">
            <h3>Service Tickets</h3>
            <p class="metric-value">-32%</p>
            <p>Reduction in service requests</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<h2 class="sub-header">AI-Enhanced Tenant Experience</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="card">
            <h3>24/7 AI Concierge</h3>
            <p>Tenants interact with an AI assistant that handles requests, provides information, and coordinates services with human-like understanding.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card">
            <h3>Personalized Environments</h3>
            <p>AI learns tenant preferences and automatically adjusts lighting, temperature, and amenity access based on individual profiles.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="card">
            <h3>Predictive Amenities</h3>
            <p>The system anticipates community needs and proactively schedules events, services, and amenity availability.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Tenant feedback analysis
    st.markdown('<h2 class="sub-header">AI Sentiment Analysis: Tenant Feedback</h2>', unsafe_allow_html=True)
    
    # Create a sample sentiment analysis visualization
    sentiment_data = pd.DataFrame({
        "category": ["Maintenance", "Amenities", "Location", "Value", "Security", "Staff"],
        "positive": [78, 85, 92, 68, 75, 88],
        "neutral": [15, 10, 6, 22, 15, 9],
        "negative": [7, 5, 2, 10, 10, 3]
    })
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        y=sentiment_data["category"],
        x=sentiment_data["positive"],
        name="Positive",
        orientation="h",
        marker=dict(color="#4CAF50")
    ))
    
    fig.add_trace(go.Bar(
        y=sentiment_data["category"],
        x=sentiment_data["neutral"],
        name="Neutral",
        orientation="h",
        marker=dict(color="#FFC107")
    ))
    
    fig.add_trace(go.Bar(
        y=sentiment_data["category"],
        x=sentiment_data["negative"],
        name="Negative",
        orientation="h",
        marker=dict(color="#F44336")
    ))
    
    fig.update_layout(
        barmode="stack",
        title="Tenant Sentiment Analysis by Category",
        xaxis_title="Percentage",
        yaxis_title="Category",
        legend_title="Sentiment"
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
    **AI Insights:** Sentiment analysis reveals strongest positive feedback for location and staff interactions. 
    The system has identified value perception as an opportunity area and recommends targeted improvements to 
    amenities that tenants rate most highly for their impact on perceived value.
    """)

def show_financial(selected_property):
    st.markdown(f'<h1 class="main-header">Financial Impact: {selected_property}</h1>', unsafe_allow_html=True)
    
    # Key financial metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="card">
            <h3>Annual Cost Savings</h3>
            <p class="metric-value">$247,500</p>
            <p>Through AI-driven optimizations</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card">
            <h3>5-Year Projection</h3>
            <p class="metric-value">$1.24M</p>
            <p>Cumulative savings with AI systems</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="card">
            <h3>Property Value Impact</h3>
            <p class="metric-value">+8.2%</p>
            <p>Estimated increase in property values</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Cost savings breakdown
    st.markdown('<h2 class="sub-header">AI-Driven Cost Savings Breakdown</h2>', unsafe_allow_html=True)
    
    cost_data = generate_cost_savings_data()
    
    fig = px.pie(cost_data, values="value", names="category",
                title="Cost Savings Distribution",
                color_discrete_sequence=px.colors.qualitative.Set3)
    
    fig.update_traces(textposition="inside", textinfo="percent+label")
    
    st.plotly_chart(fig, use_container_width=True)
    
    # ROI analysis
    st.markdown('<h2 class="sub-header">AI Implementation ROI Analysis</h2>', unsafe_allow_html=True)
    
    # Create sample ROI data
    years = list(range(2025, 2030))
    investment = [350000, 75000, 50000, 50000, 25000]
    returns = [247500, 320000, 382500, 420000, 475000]
    cumulative_roi = [
        (returns[0] - investment[0]) / investment[0] * 100
    ]
    
    for i in range(1, len(years)):
        total_investment = sum(investment[:i+1])
        total_returns = sum(returns[:i+1])
        cumulative_roi.append((total_returns - total_investment) / total_investment * 100)
    
    roi_data = pd.DataFrame({
        "year": years,
        "investment": investment,
        "returns": returns,
        "cumulative_roi": cumulative_roi
    })
    
    # Create a subplot with 2 y-axes
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    # Add bar charts for investment and returns
    fig.add_trace(
        go.Bar(x=roi_data["year"], y=roi_data["investment"], name="Investment", marker_color="#E57373"),
        secondary_y=False
    )
    
    fig.add_trace(
        go.Bar(x=roi_data["year"], y=roi_data["returns"], name="Returns", marker_color="#81C784"),
        secondary_y=False
    )
    
    # Add line chart for cumulative ROI
    fig.add_trace(
        go.Scatter(x=roi_data["year"], y=roi_data["cumulative_roi"], name="Cumulative ROI %", 
                  mode="lines+markers", marker=dict(size=8), line=dict(width=2, color="#5C6BC0")),
        secondary_y=True
    )
    
    # Update layout
    fig.update_layout(
        title_text="AI Technology Investment ROI Analysis",
        barmode="group"
    )
    
    fig.update_xaxes(title_text="Year")
    fig.update_yaxes(title_text="Amount ($)", secondary_y=False)
    fig.update_yaxes(title_text="ROI (%)", secondary_y=True)
    
    st.plotly_chart(fig, use_container_width=True)
    
    # AI value proposition
    st.markdown('<h2 class="sub-header">AI Value Beyond Direct Savings</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="card">
            <h3>Tenant Premium</h3>
            <p>Higher quality tenants willing to pay 5-7% premium for AI-enhanced properties with improved experience metrics.</p>
        </div>
        
        <div class="card" style="margin-top: 1rem;">
            <h3>Resale Value</h3>
            <p>Properties with documented AI systems and efficiency metrics command higher valuations (average +8.2% in comparable markets).</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card">
            <h3>Financing Benefits</h3>
            <p>Financial institutions offer improved terms for properties with AI management systems due to reduced risk profiles and improved cash flow visibility.</p>
        </div>
        
        <div class="card" style="margin-top: 1rem;">
            <h3>Brand Premium</h3>
            <p>Columbus Capital's reputation as an innovation leader in property development creates marketing advantages and tenant preference.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Implementation cost calculator
    st.markdown('<h2 class="sub-header">AI Implementation Cost Calculator</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        num_properties = st.slider("Number of Properties", 1, 20, 5)
        implementation_level = st.select_slider(
            "Implementation Level", 
            options=["Basic (Monitoring)", "Standard (Monitoring + Automation)", "Advanced (Full AI Integration)"]
        )
        existing_systems = st.selectbox(
            "Existing Building Management Systems",
            options=["None/Minimal", "Standard", "Modern/Advanced"]
        )
    
    with col2:
        # Calculate implementation costs
        base_cost_per_property = {
            "Basic (Monitoring)": 45000,
            "Standard (Monitoring + Automation)": 75000,
            "Advanced (Full AI Integration)": 120000
        }
        
        existing_discount = {
            "None/Minimal": 0,
            "Standard": 0.15,
            "Modern/Advanced": 0.30
        }
        
        # Calculate totals
        base_cost = base_cost_per_property[implementation_level] * num_properties
        discount = base_cost * existing_discount[existing_systems]
        total_cost = base_cost - discount
        
        annual_savings_per_property = {
            "Basic (Monitoring)": 35000,
            "Standard (Monitoring + Automation)": 55000,
            "Advanced (Full AI Integration)": 85000
        }
        
        annual_savings = annual_savings_per_property[implementation_level] * num_properties
        roi_period = total_cost / annual_savings
        
        st.markdown(f"""
        <div class="card">
            <h3>Implementation Analysis</h3>
            <p><strong>Total Implementation Cost:</strong> ${total_cost:,.0f}</p>
            <p><strong>Annual Projected Savings:</strong> ${annual_savings:,.0f}</p>
            <p><strong>ROI Period:</strong> {roi_period:.2f} years</p>
            <p><strong>5-Year Net Benefit:</strong> ${(annual_savings * 5) - total_cost:,.0f}</p>
        </div>
        """, unsafe_allow_html=True)
        
        if roi_period < 1.5:
            st.success("This implementation has an excellent ROI timeframe!")
        elif roi_period < 3:
            st.info("This implementation has a solid ROI timeframe.")
        else:
            st.warning("Consider phased implementation to improve ROI timeframe.")

# Run the app
if __name__ == "__main__":
    main()