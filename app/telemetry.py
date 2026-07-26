import os

from dotenv import load_dotenv

load_dotenv()

from azure.monitor.opentelemetry.exporter import AzureMonitorTraceExporter
from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor


def configure_telemetry():

    connection_string = os.getenv("APPLICATIONINSIGHTS_CONNECTION_STRING")

    print(f"Connection string found: {bool(connection_string)}")

    if not connection_string:
        print("No Application Insights connection string found. Telemetry is disabled.")
        return

    resource = Resource.create({
        "service.name": "hello-fastapi",
        "service.version": "1.0.0",
    })

    provider = TracerProvider(resource=resource)

    exporter = AzureMonitorTraceExporter(
        connection_string=connection_string
    )

    processor = BatchSpanProcessor(exporter)

    provider.add_span_processor(processor)

    trace.set_tracer_provider(provider)

    print("OpenTelemetry configured successfully.")