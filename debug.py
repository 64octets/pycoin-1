import eventlet
from eventlet import backdoor
import signal, code, traceback
import threading
DEBUG_BACKDOOR = True
DEBUG_SIGINT = False

debug_locals = {}

if DEBUG_BACKDOOR:
    backdoor_th = threading.Thread(target=backdoor.backdoor_server, args=(eventlet.listen(('localhost', 3000)), debug_locals))
    backdoor_th.daemon = True
    backdoor_th.start()
    
def signal_handler( signal_number ):
    """
    A decorator to set the specified function as handler for a signal.
    This function is the 'outer' decorator, called with only the (non-function) 
    arguments
    """
    
    # create the 'real' decorator which takes only a function as an argument
    def __decorator( function ):
        signal.signal( signal_number, function )
        return function
    
    return __decorator
    
if DEBUG_SIGINT:
    @signal_handler(signal.SIGINT)
    def debug_handler(sig, frame):
        """Interrupt running process, and provide a python prompt for
        interactive debugging."""
        debug_locals["_frame"] = frame         # Allow access to frame object.
        
        i = code.InteractiveConsole(debug_locals)
        message  = "Signal recieved : entering python shell.\nTraceback:\n"
        message += ''.join(traceback.format_stack(frame))
        i.interact(message)
    
