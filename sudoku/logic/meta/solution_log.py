from collections import defaultdict


class SolutionLog(object):
    __slots__ = ['_steps', '_query', '_transaction_active', '_transaction_steps']

    def __init__(self):
        self._steps = []
        self._query = []

        self._transaction_active = False
        self._transaction_steps = []

    def begin_transaction(self):
        self.commit()
        self._transaction_active = True

    def commit(self):
        self._steps.extend(self._transaction_steps)
        self._end_transaction()

    def rollback(self):
        self._end_transaction()

    def _end_transaction(self):
        self._transaction_steps = []
        self._transaction_active = False

    def add_step(self, cell, action, reason):
        if self._transaction_active:
            self._transaction_steps.append({'cell': cell, 'action': action, 'reason': reason})
        else:
            self._steps.append({'cell': cell, 'action': action, 'reason': reason})

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
