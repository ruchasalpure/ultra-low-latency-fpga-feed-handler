from crewai import Agent

ultra_low_latency_fpga_feed_handler = Agent(
    role="Ultra Low Latency Fpga Feed Handler",
    goal="Deliver high-precision autonomous Ultra Low Latency Fpga Feed Handler operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)
