from collections import defaultdict


class SolutionLog(object):
    __slots__ = ['_steps', '_query']

    def __init__(self):
        self._steps = []
        self._query = []

    def add_step(self, cell, action, reason):
        self._steps.append({
            'cell': cell,
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
        steps = []

        for step in self._steps:
            valid = True

            cell = step['cell']
            action = step['action']
            reason = step['reason']

            for condition in self._query:
                valid = valid and eval(condition)

            if valid:
                steps.append({
                    'cell': cell,
                    'action': action,
                    'reason': reason
                })

        return steps
