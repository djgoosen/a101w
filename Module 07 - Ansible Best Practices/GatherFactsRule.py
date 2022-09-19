#!/usr/bin/env python3

from ansiblelint import AnsibleLintRule


class GatherFactsRule(AnsibleLintRule):
    id = 'ANSIBLE1313'
    shortdesc = 'DevOps team rule: gather_facts should never be set to True'
    description = 'Check if gather_facts: True'
    tags = {'resources'}

    def match(self, file, line):
        return 'gather_facts: True' in line
