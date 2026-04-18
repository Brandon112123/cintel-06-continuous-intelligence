"""
continuous_intelligence_custom.py - Custom continuous intelligence project.

Author: Brandon Smith
Date: 2026-04

System Metrics Data

- Data represents recent observations from a monitored system.
- Each row represents one observation of system activity.

- The CSV file includes these columns:
  - requests: number of requests handled
  - errors: number of failed requests
  - total_latency_ms: total response time in milliseconds

Purpose

- Read system metrics from a CSV file.
- Apply continuous intelligence techniques to a custom problem.
- Create monitoring signals such as error rate and average latency.
- Add rolling monitoring with rolling latency.
- Create a health score for each observation.
- Label each row as HEALTHY or WARNING.
- Add a simple latency trend label.
- Save detailed and summary outputs.
- Create a chart to visualize system health trends.

Paths (relative to repo root)

    INPUT FILE: data/system_metrics_custom.csv
    DETAIL FILE: artifacts/system_monitoring_details_custom.csv
    SUMMARY FILE: artifacts/system_assessment_custom.csv
    CHART FILE: artifacts/system_health_chart_custom.png

Terminal command to run this file from the root project folder

    uv run python -m cintel.continuous_intelligence_custom
"""

# === DECLARE IMPORTS ===

import logging
from pathlib import Path
from typing import Final

import matplotlib.pyplot as plt
import polars as pl
from datafun_toolkit.logger import get_logger, log_header, log_path

# === CONFIGURE LOGGER ===

LOG: logging.Logger = get_logger("P6", level="DEBUG")

# === DEFINE GLOBAL PATHS ===

ROOT_DIR: Final[Path] = Path.cwd()
DATA_DIR: Final[Path] = ROOT_DIR / "data"
ARTIFACTS_DIR: Final[Path] = ROOT_DIR / "artifacts"

DATA_FILE: Final[Path] = DATA_DIR / "system_metrics_custom.csv"
DETAIL_FILE: Final[Path] = ARTIFACTS_DIR / "system_monitoring_details_custom.csv"
SUMMARY_FILE: Final[Path] = ARTIFACTS_DIR / "system_assessment_custom.csv"
CHART_FILE: Final[Path] = ARTIFACTS_DIR / "system_health_chart_custom.png"

# === DEFINE THRESHOLDS ===

MAX_ERROR_RATE: Final[float] = 0.03
MAX_AVG_LATENCY: Final[float] = 30.0

# === DEFINE THE MAIN FUNCTION ===


def main() -> None:
    """Run the custom continuous intelligence pipeline."""
    log_header(LOG, "CINTEL")

    LOG.info("========================")
    LOG.info("START main()")
    LOG.info("========================")

    log_path(LOG, "ROOT_DIR", ROOT_DIR)
    log_path(LOG, "DATA_FILE", DATA_FILE)
    log_path(LOG, "DETAIL_FILE", DETAIL_FILE)
    log_path(LOG, "SUMMARY_FILE", SUMMARY_FILE)
    log_path(LOG, "CHART_FILE", CHART_FILE)

    # Ensure artifacts directory exists
    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)

    # ----------------------------------------------------
    # STEP 1: READ SYSTEM METRICS
    # ----------------------------------------------------
    df = pl.read_csv(DATA_FILE)

    LOG.info(f"STEP 1. Loaded {df.height} system records")

    # ----------------------------------------------------
    # STEP 2: DESIGN SIGNALS
    # ----------------------------------------------------
    LOG.info("STEP 2. Designing signals from raw metrics...")

    df = df.with_columns(
        [
            (pl.col("errors") / pl.col("requests")).alias("error_rate"),
            (pl.col("total_latency_ms") / pl.col("requests")).alias("avg_latency_ms"),
        ]
    )

    # ----------------------------------------------------
    # STEP 3: ADD ROLLING MONITORING AND HEALTH SCORE
    # ----------------------------------------------------
    LOG.info("STEP 3. Adding rolling latency and health score...")

    df = df.with_columns(
        [
            pl.col("avg_latency_ms")
            .rolling_mean(window_size=3)
            .alias("rolling_latency"),
            (100 - (pl.col("error_rate") * 500) - pl.col("avg_latency_ms")).alias(
                "health_score"
            ),
        ]
    )

    # ----------------------------------------------------
    # STEP 4: LABEL ROW LEVEL STATUS
    # ----------------------------------------------------
    LOG.info("STEP 4. Labeling each row with status and latency trend...")

    df = df.with_columns(
        [
            pl.when(
                (pl.col("error_rate") > MAX_ERROR_RATE)
                | (pl.col("avg_latency_ms") > MAX_AVG_LATENCY)
            )
            .then(pl.lit("WARNING"))
            .otherwise(pl.lit("HEALTHY"))
            .alias("status"),
            pl.when(pl.col("rolling_latency") > pl.col("avg_latency_ms"))
            .then(pl.lit("RISING"))
            .otherwise(pl.lit("STEADY"))
            .alias("latency_trend"),
        ]
    )

    # ----------------------------------------------------
    # STEP 5: SUMMARIZE CURRENT SYSTEM STATE
    # ----------------------------------------------------
    LOG.info("STEP 5. Summarizing monitored system state...")

    summary_df = df.select(
        [
            pl.col("requests").mean().alias("avg_requests"),
            pl.col("errors").mean().alias("avg_errors"),
            pl.col("error_rate").mean().alias("avg_error_rate"),
            pl.col("avg_latency_ms").mean().alias("avg_latency_ms"),
            pl.col("health_score").mean().alias("avg_health_score"),
        ]
    )

    warning_count = df.filter(pl.col("status") == "WARNING").height

    summary_df = summary_df.with_columns(
        [
            pl.lit(warning_count).alias("warning_count"),
            pl.when(pl.lit(warning_count > 0))
            .then(pl.lit("DEGRADED"))
            .otherwise(pl.lit("STABLE"))
            .alias("system_state"),
        ]
    )

    LOG.info("STEP 5. System assessment completed")

    # ----------------------------------------------------
    # STEP 6: SAVE DETAILED AND SUMMARY OUTPUTS
    # ----------------------------------------------------
    df.write_csv(DETAIL_FILE)
    summary_df.write_csv(SUMMARY_FILE)

    LOG.info(f"STEP 6. Wrote detail file: {DETAIL_FILE}")
    LOG.info(f"STEP 6. Wrote summary file: {SUMMARY_FILE}")

    # ----------------------------------------------------
    # STEP 7: CREATE VISUALIZATION
    # ----------------------------------------------------
    plt.figure(figsize=(10, 6))
    plt.plot(df["avg_latency_ms"].to_list(), label="Avg Latency")
    plt.plot(df["rolling_latency"].fill_null(0).to_list(), label="Rolling Latency")
    plt.plot(df["health_score"].to_list(), label="Health Score")
    plt.title("System Health Trend")
    plt.xlabel("Observation")
    plt.ylabel("Value")
    plt.legend()
    plt.tight_layout()
    plt.savefig(CHART_FILE)
    plt.close()

    LOG.info(f"STEP 7. Wrote chart file: {CHART_FILE}")

    LOG.info("========================")
    LOG.info("Pipeline executed successfully!")
    LOG.info("========================")
    LOG.info("END main()")


# === CONDITIONAL EXECUTION GUARD ===

if __name__ == "__main__":
    main()
