import inspect
import time
import types
from .logger import get_logger

logger = get_logger("PerformanceAnalyzer")

def analyze_source(task) -> str:
    """
    Analyse statique du code source de la fonction pour déterminer s'il s'agit d'une tâche CPU-bound ou I/O-bound.
    Retourne "cpu" ou "io".
    """
    try:
        source = inspect.getsource(task)
    except Exception as e:
        logger.warning("Impossible d'analyser le code source, défaut d'analyse statique. Par défaut, utilisation de CPU-bound.")
        return "cpu"

    io_keywords = ['sleep', 'socket', 'recv', 'send', 'read', 'write', 'urlopen', 'select', 'poll']
    source_lower = source.lower()
    for kw in io_keywords:
        if kw in source_lower:
            logger.debug(f"Mot-clé I/O détecté dans le code source: {kw}")
            return "io"
    return "cpu"

def micro_profile(task, *args, **kwargs) -> str:
    
    start_wall = time.time()
    start_cpu = time.process_time()
    try:
        result = task(*args, **kwargs)
        if isinstance(result, types.GeneratorType):
            try:
                next(result)
            except StopIteration:
                pass
    except Exception as e:
        logger.debug("Micro-profilage échoué avec exception: " + str(e))
    end_wall = time.time()
    end_cpu = time.process_time()

    wall_time = end_wall - start_wall
    cpu_time = end_cpu - start_cpu

    ratio = cpu_time / wall_time if wall_time > 0 else 0
    if ratio > 0.8:
        logger.debug(f"Profilage: wall_time={wall_time:.4f}, cpu_time={cpu_time:.4f}, ratio={ratio:.2f} -> CPU-bound")
        return "cpu"
    else:
        logger.debug(f"Profilage: wall_time={wall_time:.4f}, cpu_time={cpu_time:.4f}, ratio={ratio:.2f} -> I/O-bound")
        return "io"

def analyze_task(task, *args, **kwargs) -> str:
    """
    Analyse combinée : utilise l'analyse statique du code source et le micro-profilage.
    Retourne "cpu" ou "io".
    """
    source_analysis = analyze_source(task)
    logger.debug(f"Analyse statique du code source: {source_analysis}")
    
    profile_analysis = micro_profile(task, *args, **kwargs)
    logger.debug(f"Analyse micro-profilage: {profile_analysis}")
    
    if source_analysis == profile_analysis:
        return source_analysis
    else:
        logger.debug("Divergence entre analyse statique et micro-profilage, utilisation de l'analyse statique.")
        return source_analysis
