from lagom.integrations.fast_api import FastApiIntegration
from src.di import ContainerBuilder

container = FastApiIntegration(ContainerBuilder.get_container())
