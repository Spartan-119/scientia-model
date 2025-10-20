# Scientia Financial Projections App 📊

An interactive financial forecasting application built with Streamlit to showcase Scientia's 24-month revenue projections to investors. The app models a dual-revenue strategy: B2C Freemium + Enterprise.

## Features

- 🎛️ **Interactive Assumptions**: Adjust all key business assumptions in real-time
- 📈 **Dynamic Charts**: Visual representations of MRR growth and user funnel
- 📊 **Detailed Breakdown**: Month-by-month data table with all key metrics
- 💡 **Investor-Ready**: Professional design suitable for investor presentations

## Quick Start

### Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

### Run Locally

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## Deployment Options

### Option 1: Streamlit Community Cloud (Recommended - Free)

1. Push this repository to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with GitHub
4. Click "New app" and select your repository
5. Set main file path to `app.py`
6. Click "Deploy"

Your app will be live at `https://[your-app-name].streamlit.app`

### Option 2: Other Platforms

- **Heroku**: Follow [Streamlit's Heroku deployment guide](https://docs.streamlit.io/knowledge-base/tutorials/deploy/heroku)
- **AWS/GCP/Azure**: Deploy as a containerized application
- **Railway/Render**: Simple git-based deployment

## How to Use

1. **Adjust Assumptions**: Use the sidebar to modify:
   - B2C pricing and user acquisition parameters
   - Enterprise pricing and sales metrics
   - Growth rates and churn rates

2. **View Results**: The main panel shows:
   - Key 24-month outcome metrics
   - MRR growth visualization
   - User funnel breakdown
   - Detailed month-by-month projections

3. **Scenario Planning**: Test different scenarios by adjusting assumptions to show:
   - Conservative case (lower growth rates)
   - Base case (current assumptions)
   - Optimistic case (higher conversion, lower churn)

## Key Metrics Explained

- **ARR** (Annual Recurring Revenue): Total MRR × 12
- **MRR** (Monthly Recurring Revenue): Predictable monthly revenue
- **Conversion Rate**: % of free users who convert to paid
- **Churn Rate**: % of users lost each month
- **Viral Growth Multiplier**: Month-over-month increase in new user acquisition

## Model Assumptions

### B2C Freemium
- Starts with waitlist users
- Organic growth accelerates monthly (viral effect)
- 3% monthly conversion rate (industry standard: 2-5%)
- Converted users move from free to paid pool

### Enterprise
- Launches after B2C establishes product-market fit
- Multi-seat deals with lower churn
- Sales-driven growth model
- Higher per-seat value

## Tips for Investor Presentations

1. **Start with base case**: Show realistic, achievable numbers
2. **Demonstrate sensitivity**: Show how key levers impact outcomes
3. **Explain assumptions**: Use the built-in explanations section
4. **Compare scenarios**: Prepare 3 scenarios (conservative/base/optimistic)
5. **Share the link**: Deploy and share the live app for interactive exploration

## Customization

To customize for your business:

1. Edit the default values in `app.py` (sidebar inputs)
2. Modify the calculation logic in `calculate_projections()` function
3. Adjust colors and styling in the CSS section
4. Add/remove metrics as needed

## Support

For issues or questions, please contact the development team.

---

**Built with ❤️ using Streamlit**

