try:
    from comet_ml import Experiment
    comet_installed = True
except:
    comet_installed = False


class CometLogger():
    def __init__(self):
        global comet_installed
        self._logging = False
        if comet_installed:
            try:
                self._experiment = Experiment(auto_metric_logging=False,
                                              display_summary_level=0)
                self._logging = True
            except:
                print("Comet not configured properly")
        else:
            print("Comet is not installed")
    
    def log_metric(self, name, value, step=None, epoch=None):
        if self._logging:
            self._experiment.log_metric(name, value, step=step,
                                        epoch=epoch)
    
    def log_parameters(self, dic):
        if self._logging:
            self._experiment.log_parameters(dic)

    def log_parameter(self, name, value):
        if self._logging:
            self._experiment.log_parameter(name, value)
    
    def end(self):
        if self._logging:
            self._experiment.end()
