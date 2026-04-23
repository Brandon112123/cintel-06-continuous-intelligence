# Continuous Intelligence Portfolio

**Brandon D. Smith**
**2026-04**

This page summarizes my work on **continuous intelligence** projects.

## 1. Professional Project

### Repository Link
[GitHub Repository](https://github.com/Brandon112123/cintel-01-getting-started)

### Brief Overview of Project Tools and Choices
This project was my starting point for continuous intelligence in Python. I used it to set up the environment, run the project, and learn the basic structure of a professional Python repo. It uses folders like `src` and `docs` and tools like `uv`, `ruff`, and `zensical` to keep the project organized and clean.

## 2. Anomaly Detection

### Repository Link
[GitHub Repository](https://github.com/Brandon112123/cintel-02-static-anomalies)

### Techniques
This project detected anomalies by flagging values outside the normal range. My custom version focused on suicide rate data and highlighted unusually high values that stood out from the rest.

### Artifacts
[Artifacts Folder](https://github.com/Brandon112123/cintel-02-static-anomalies/tree/main/artifacts)

The artifacts include a CSV file with anomaly results and a chart showing the top anomalies. These files made it easier to find unusual data points quickly.

### Insights
This analysis showed which suicide rate values were much higher than expected. That helps point out possible outliers or areas that may need more attention.

## 3. Signal Design

### Repository Link
[GitHub Repository](https://github.com/Brandon112123/cintel-03-signal-design)

### Signals
In this project, I created custom signals from alcohol consumption data. My signals focused on beer share, spirit share, total selected drinks, and total drink levels so the raw data would be easier to understand.

### Artifacts
[Artifacts Folder](https://github.com/Brandon112123/cintel-03-signal-design/tree/main/artifacts)

The artifacts include a CSV with the signal data and a chart showing the trends. This helped turn the original data into something more useful and easier to read.

### Insights
The signals showed differences in how beer and spirits contributed to total alcohol consumption. This made the trends clearer than just looking at the raw numbers alone.

## 4. Rolling Monitoring

### Repository Link
[GitHub Repository](https://github.com/Brandon112123/cintel-04-rolling-monitoring)

### Techniques
This project used rolling averages to track changes in requests, errors, and latency over time. Rolling windows helped smooth out short-term spikes and made the overall trends easier to see.

### Artifacts
[Artifacts Folder](https://github.com/Brandon112123/cintel-04-rolling-monitoring/tree/main/artifacts)

The artifacts include rolling metrics files that show how the system changed over time after the rolling calculations were applied.

### Insights
This project helped show longer-term patterns in system behavior. Instead of only seeing random ups and downs, I could better see whether the system was improving, staying stable, or getting worse.

## 5. Drift Detection

### Repository Link
[GitHub Repository](https://github.com/Brandon112123/cintel-05-drift-detection)

### Techniques
This project compared a reference period to a current period to detect drift. I looked at changes in orders processed, failed orders, and fulfillment time to see if the system behavior had shifted.

### Artifacts
[Artifacts Folder](https://github.com/Brandon112123/cintel-05-drift-detection/tree/main/artifacts)

The artifacts include result files that compare the earlier period and later period. These outputs help show whether the system changed enough to be considered drift.

### Insights
This project showed whether the system stayed consistent or started to shift over time. That is useful because drift can be an early warning sign that performance is changing.

## 6. Continuous Intelligence Pipeline

### Repository Link
[GitHub Repository](https://github.com/Brandon112123/cintel-06-continuous-intelligence)

### Techniques
This project combined signals, monitoring, and assessment into one full pipeline. It turned raw system data into useful measures like error rate and latency, then used those results to check system health.

### Artifacts
[Artifacts Folder](https://github.com/Brandon112123/cintel-06-continuous-intelligence/tree/main/artifacts)

The artifacts include monitoring details, a system assessment file, and a health chart. Together, these outputs give both detailed results and a summary of system condition.

### Assessment
The pipeline gives an overall view of the system state. It helps show whether the system looks healthy, stable, or in need of attention based on error rate, latency, and trend patterns.
