import concurrent.futures
from .config import Config
from .logger import get_logger

logger = get_logger("TaskManager")

class TaskManager:
    def __init__(self):
        self.thread_executor = concurrent.futures.ThreadPoolExecutor(max_workers=Config.MAX_THREADS)
        self.process_executor = concurrent.futures.ProcessPoolExecutor(max_workers=Config.MAX_PROCESSES)
        logger.debug("TaskManager initialisé avec ThreadPoolExecutor et ProcessPoolExecutor.")

    def submit_io_task(self, task, *args, **kwargs):
        """
        Soumettre une tache I/O-bound au ThreadPoolExecutor.
        """
        logger.debug("Soumission d'une tâche I/O-bound.")
        return self.thread_executor.submit(task, *args, **kwargs)

    def submit_cpu_task(self, task, *args, **kwargs):
        """
        Soumettre une tâche CPU-bound au ProcessPoolExecutor.
        """
        logger.debug("Soumission d'une tâche CPU-bound.")
        return self.process_executor.submit(task, *args, **kwargs)

    def shutdown(self, wait: bool = True):
        """
        stop les deux executeurs.
        """
        logger.debug("Fermeture des exécuteurs.")
        self.thread_executor.shutdown(wait=wait)
        self.process_executor.shutdown(wait=wait)
