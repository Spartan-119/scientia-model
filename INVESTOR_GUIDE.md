# 📊 Investor Guide: How to Use the Scientia Projections Tool

Welcome! This interactive tool allows you to explore Scientia's financial projections and test different scenarios.

## What You'll See

### 1. **Key Metrics Dashboard** (Top)
Five key outcomes for the 24-month projection:
- **Final ARR**: Total annual recurring revenue after 2 years
- **Free Users**: Active freemium users
- **Paid Users**: Individual paying subscribers
- **Enterprise Seats**: Total enterprise licenses sold
- **Conversion Rate**: Percentage of free users converting to paid

### 2. **MRR Growth Chart**
Visual representation of monthly recurring revenue split between:
- 🔵 **B2C MRR** (Individual subscriptions)
- 🟢 **Enterprise MRR** (Enterprise deals)
- 🟣 **Total MRR** (Combined revenue)

### 3. **User Funnel Chart**
Bar chart showing the growth of:
- 🟠 Free users (top of funnel)
- 🔵 Paid users (converted individuals)
- 🟢 Enterprise seats (B2B sales)

### 4. **Detailed Table**
Month-by-month breakdown of all metrics for deep analysis

### 5. **Analysis Sections**
- Path to market (SOM analysis)
- Explanation of model assumptions

## How to Explore Different Scenarios

### Left Sidebar Controls

Adjust any parameter in real-time to see immediate impact:

#### **B2C Freemium Section**
- **Paid Price**: Monthly subscription price per user
- **Initial Free Users**: Waitlist size at launch
- **New Free Users/Month**: Organic acquisition rate
- **Viral Growth Multiplier**: How fast user acquisition accelerates
- **Conversion Rate %**: Free-to-paid conversion
- **Paid User Churn %**: Monthly subscriber loss rate

#### **Enterprise Section**
- **Price (per seat)**: Enterprise license cost per user
- **Launch Month**: When enterprise sales begin
- **Avg Seats/Deal**: Typical enterprise deal size
- **Initial Deals/Month**: Starting sales velocity
- **Deal Growth %**: Month-over-month sales increase
- **Enterprise Churn %**: Enterprise customer retention

## Recommended Scenarios to Explore

### 🎯 **Base Case** (Current Settings)
The default values represent a realistic projection based on industry benchmarks.

### 📊 **Conservative Case**
Try adjusting:
- Conversion Rate: 2%
- Viral Growth Multiplier: 1.05
- Deal Growth Rate: 15%

This shows "worst case" while still being viable.

### 🚀 **Optimistic Case**
Try adjusting:
- Conversion Rate: 5%
- Viral Growth Multiplier: 1.15
- Deal Growth Rate: 30%
- Paid User Churn: 3%

This shows "best case" with strong product-market fit.

### 🏢 **Enterprise-First Strategy**
Try adjusting:
- Enterprise Launch Month: 3
- Avg Seats/Deal: 50
- Enterprise Price: £20

This shows what happens if we focus heavily on enterprise.

## Key Questions This Tool Answers

1. **What's the revenue potential?**
   - Look at Final ARR metric and Total MRR chart

2. **How important is user conversion?**
   - Adjust Conversion Rate % and watch ARR change

3. **When do we reach profitability?**
   - Compare monthly MRR to your expected operating costs

4. **What drives growth more: B2C or Enterprise?**
   - Compare the blue vs green lines in the MRR chart

5. **How sensitive is the model to churn?**
   - Adjust churn rates and see impact on final metrics

6. **What if viral growth is stronger/weaker?**
   - Modify the Viral Growth Multiplier

## Understanding the Model

### Key Assumptions

1. **Freemium Funnel**
   - Users start free
   - Convert to paid monthly at a steady rate
   - Converted users leave the free pool
   - Some paid users churn each month

2. **Viral Growth**
   - Each month, new user acquisition accelerates
   - Models word-of-mouth and network effects
   - Growth multiplier compounds monthly

3. **Enterprise Sales**
   - Launches after B2C proves product-market fit
   - Sales-driven (not viral)
   - Larger deals, lower churn
   - More predictable revenue

4. **Realistic Benchmarks**
   - 2-5% conversion is typical for SaaS freemium
   - 5-7% monthly churn is average for B2C SaaS
   - 2-3% annual churn is typical for enterprise

## Tips for Your Analysis

✅ **Do:**
- Test multiple scenarios
- Look for tipping points (when does growth accelerate?)
- Consider which levers you can actually control
- Think about resource allocation (B2C vs Enterprise focus)

❌ **Don't:**
- Cherry-pick only the highest numbers
- Ignore churn rates (they significantly impact outcomes)
- Forget that assumptions compound over time
- Overlook the timing of enterprise launch

## Questions for Discussion

After exploring the tool, consider:

1. Which scenario seems most achievable given the team and market?
2. What are the biggest risks to these projections?
3. What would need to be true for the optimistic case?
4. How does this compare to the TAM/SAM/SOM analysis?
5. What milestones would validate these assumptions?

## Technical Notes

- All calculations happen in real-time in your browser
- No data is stored or transmitted
- Results update instantly as you adjust inputs
- You can screenshot any view for your records

---

**Ready to explore?** Start by adjusting one parameter at a time and watching how it affects the final ARR!

