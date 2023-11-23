from datetime import datetime

import jsonpickle

from engine.engine import AlertEngine
from models.models import RuleSet, Rule, Methods, RuleInput, RuleOutput, UtilityType, RuleInputType, \
    ConsumptionIntervalType

# test rule set
rule_set = RuleSet()

# load consumption time series data from db
rule1 = Rule(Methods.load_consumption_range)
rule1.inputs.append(RuleInput(10))
rule1.inputs.append(RuleInput(UtilityType.WATER))
rule1.inputs.append(RuleInput(datetime.now()))
rule1.inputs.append(RuleInput(datetime.now()))
rule1.inputs.append(RuleInput(ConsumptionIntervalType.HOURLY))
# save data into variable
rule1.outputs.append(RuleOutput('consumption_result'))
rule_set.rules.append(rule1)

# find max consumption value in data
rule2 = Rule(Methods.find_max_consumption)
rule2.inputs.append(RuleInput('consumption_result', RuleInputType.REFERENCE))
rule2.outputs.append(RuleOutput('max_result'))
rule_set.rules.append(rule2)

# consumption max is greater than limit
rule3 = Rule(Methods.greater_than)
rule3.inputs.append(RuleInput('max_result', RuleInputType.REFERENCE))
rule3.inputs.append(RuleInput(30))
rule3.outputs.append(RuleOutput('result'))
rule_set.rules.append(rule3)

# evaluate result
# responsible to handle alert creation
rule4 = Rule(Methods.evaluate_result)
rule4.inputs.append(RuleInput('result', RuleInputType.REFERENCE))
rule_set.rules.append(rule4)

# TODO load all rule_sets from db at startup
print(jsonpickle.encode(rule_set))


if __name__ == '__main__':
    engine = AlertEngine()
    engine.execute(rule_set)
