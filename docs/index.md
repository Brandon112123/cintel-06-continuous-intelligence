# Continuous Intelligence

This site provides documentation for this project.
Use the navigation to explore module-specific materials.

## How-To Guide

Many instructions are common to all our projects.

See
[⭐ **Workflow: Apply Example**](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/)
to get these projects running on your machine.

## Project Documentation Pages (docs/)

- **Home** - this documentation landing page
- **Project Instructions** - instructions specific to this module
- **Glossary** - project terms and concepts

## Additional Resources

- [Suggested Datasets](https://denisecase.github.io/pro-analytics-02/reference/datasets/cintel/)

## Custom Project

### Dataset
I used a custom system metrics dataset in `data/system_metrics_custom.csv`. Each row shows requests, errors, and total latency. I chose this dataset because it matches the topic of the project and shows changes over time.

### Signals
The main signals I used were `error_rate` and `avg_latency_ms`. I also added `rolling_latency` and `health_score`. I used `status` to label rows as `HEALTHY` or `WARNING`.

### Experiments
I changed the project by lowering the thresholds and adding more signals. I changed `MAX_ERROR_RATE` from `0.05` to `0.03` and `MAX_AVG_LATENCY` from `40.0` to `30.0`. I also added a chart and a detailed output file.

### Results
The project ran successfully and created new output files. The results showed that as errors and latency went up, the system looked less healthy.

### Interpretation
This means the system performance got worse over time. The project helped show how monitoring signals can be used to spot problems early.
