from .task_manager import TaskManager
from .performance_analyzer import analyze_task
from .logger import get_logger

logger = get_logger("Core")

task_manager = TaskManager()

def run(task, *args, **kwargs):
    logger.info("Exécution de la tâche demandée avec SmartExecutor.")
    
    task_type = analyze_task(task, *args, **kwargs)
    logger.info(f"Type de tâche détecté: {task_type}")

    if task_type == "cpu":
        future = task_manager.submit_cpu_task(task, *args, **kwargs)
    else:
        future = task_manager.submit_io_task(task, *args, **kwargs)

    try:
        result = future.result()
        logger.info("Tâche exécutée avec succès.")
    except Exception as e:
        logger.error("Erreur lors de l'exécution de la tâche: " + str(e))
        raise e

    return result
