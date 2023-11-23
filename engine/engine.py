from models.models import RuleSet, RuleInputType


class AlertEngine:
    _instance = None
    _variables = dict()

    def __init__(self):
        # load all rules
        print('alert engine init')

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def execute(self, rule_set: RuleSet):
        for rule in rule_set.rules:
            function = rule.function
            inputs = self.preprocess_inputs(rule.inputs)
            # this only works for single output for now
            output = self.preprocess_outputs(rule.outputs)

            self._variables[output] = function(*inputs)

    def preprocess_inputs(self, raw_inputs):
        inputs = []
        if len(raw_inputs) > 0:
            # process inputs
            for raw_input in raw_inputs:
                if raw_input.type == RuleInputType.VALUE:
                    inputs.append(raw_input.value)
                if raw_input.type == RuleInputType.REFERENCE:
                    if raw_input.value in self._variables:
                        inputs.append(self._variables.get(raw_input.value))
                    else:
                        raise AttributeError('Missing variable: ' + raw_input.value)
        return inputs

    def preprocess_outputs(self, raw_outputs):
        if len(raw_outputs) > 0:
            for raw_output in raw_outputs:
                if raw_output.value not in self._variables:
                    self._variables[raw_output.value] = None
                    return raw_output.value
