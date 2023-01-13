import logging
import termcolor

class DefaultFormatter(logging.Formatter):

    mformat = "[{asctime}] {coloredlevel} @{filename}:{lineno:<4d}: {message}"

    def get_colored_level(self, level, levelname) :
        if(level <= logging.DEBUG):
            return termcolor.colored(" {:8s} ".format(levelname), "grey")
        elif(level <= logging.INFO):
            return termcolor.colored(" {:8s} ".format(levelname), "green")
        elif(level <= logging.WARNING):
            return termcolor.colored(" {:8s} ".format(levelname), "black", "on_yellow")
        elif(level <= logging.ERROR):
            return termcolor.colored(" {:8s} ".format(levelname), "black", "on_light_red")
        elif(level <= logging.CRITICAL):
            return termcolor.colored(" {:8s} ".format(levelname), "white", "on_red")

    def format(self, record):
        record.coloredlevel=self.get_colored_level(record.levelno, record.levelname) 
        formatter = logging.Formatter(self.mformat, style='{')
        return formatter.format(record)

def create_logger(name : str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(0)
    ch.setFormatter(DefaultFormatter())
    logger.addHandler(ch)
    return logger

logger = create_logger(__name__)