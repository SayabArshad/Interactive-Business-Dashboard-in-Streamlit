# Interactive-Business-Dashboard-in-Streamlit

## ✅ Task Objective
To design and deploy an interactive business dashboard using Streamlit and Plotly that allows users to analyze and visualize sales and profit from the Global Superstore dataset.

## 🔍 Our Approach
- Cleaned the dataset and handled missing values in key metrics like Sales and Profit.
- Built a Streamlit dashboard layout with a sidebar for filtering Region, Category, and Sub-category.
- Displayed dynamic KPIs for:
  - Total Sales
  - Total Profit
  - Total Orders
- Used Plotly Express to build:
  - Bar charts for sales and profit by category and region
  - Line charts for monthly sales trends
  - Pie charts for profit distribution
- Used caching (`@st.cache_data`) to improve performance.
- Ran and tested the app locally using the terminal command: `streamlit run Task5.py`.

## 📊 Results and Findings
- The dashboard provided real-time insights into business performance.
- Users can drill down into regional or product-level performance easily.
- The app enables non-technical stakeholders to explore data trends interactively, supporting faster decision-making.
