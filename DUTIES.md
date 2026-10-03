# Duties and Responsibilities for Ultra-Low Latency FPGA Feed Handler Agent

## Dual-Control Architecture
Maker:
rtl-pipeline-generator

Checker:
timing-closure-checker

## Operational Workflow
1. The Maker (rtl-pipeline-generator) analyzes incoming telemetry, context, and requirements.
2. The Maker synthesizes a draft operational execution plan with supporting data.
3. The Checker (timing-closure-checker) independently verifies all assumptions and constraints.
4. If validation passes, the plan is signed, logged, and committed.
5. All actions are appended to the immutable governance audit trail.
