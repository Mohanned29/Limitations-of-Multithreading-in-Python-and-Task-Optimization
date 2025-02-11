from .task_manager import TaskManager
from .performance_analyzer import analyze_task
from .logger import get_logger
import concurrent.futures

logger = get_logger("Core")

task_manager = TaskManager()
def run(task, *args, **kwargs):
    logger.info("Exécution de la tâche demandée avec SmartExecutor.")
    
    task_type = analyze_task(task, *args, **kwargs)
    logger.info(f"Type de tâche détecté: {task_type}")

    future = (task_manager.submit_cpu_task(task, *args, **kwargs) if task_type == "cpu"
              else task_manager.submit_io_task(task, *args, **kwargs))

    try:
        result = future.result(timeout=5)  # ⏳ Add timeout here (5s max)
        logger.info("Tâche exécutée avec succès.")
    except concurrent.futures.TimeoutError:
        logger.error("Timeout: La tâche a pris trop de temps.")
        raise TimeoutError("Task timed out")
    except Exception as e:
        logger.error("Erreur lors de l'exécution de la tâche: " + str(e))
        raise e

    return result

