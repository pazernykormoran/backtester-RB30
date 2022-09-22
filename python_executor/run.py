from os import getenv
from libs.utils.module_loaders import import_executor_module
strategy_path = getenv('STRATEGY_PATH')
from libs.utils.run_service import run_service
microservice_name = 'python_executor'
module = import_executor_module(strategy_path)
run_service(microservice_name, module.TradeExecutor)