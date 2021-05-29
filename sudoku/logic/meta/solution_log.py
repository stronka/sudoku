from collections import defaultdict


class SolutionLog(object):
    __slots__ = ['_steps', '_query']

    def __init__(self):
        self._steps = defaultdict(list)
        self._query = []

    def add_step(self, cell, action, reason):
        self._steps[cell].append({
            'action': action,
            'reason': reason
        })

    @property
    def where(self):
        self._query = []
        return self

    def query(self, condition=None):
        if condition:
            self._query.append(condition)
        return self

    def get_steps(self):
        steps = defaultdict(list)

        for cell, cell_steps in self._steps.items():
            for step in cell_steps:
                valid = True

                action = step['action']
                reason = step['reason']

                for condition in self._query:
                    valid = valid and eval(condition)

                if valid:
                    steps[cell].append({
                        'action': action,
                        'reason': reason
                    })

        return steps
