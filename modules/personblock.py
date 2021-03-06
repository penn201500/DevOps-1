# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Author Yo
# Email YoLoveLife@outlook.com
from collections import namedtuple

from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.inventory import Inventory
from ansible.parsing.dataloader import DataLoader
from ansible.playbook.play import Play
from ansible.vars import VariableManager
from callback import ResultCallback

HOST_LIST='/tmp/ansible.host'
class PersonBlock():
    def __init__(self):
        Options = namedtuple('Options',
                             ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check'])
        self.options = Options(connection='smart', module_path='', forks=100, become=None, become_method='sudo',
                          become_user=None, check=False)

        self.variable_manager = VariableManager()
        self.loader = DataLoader()
        self.passwords = dict(vault_pass='')
        self.results_callback = ResultCallback()
        self.inventory = Inventory(loader=self.loader, variable_manager=self.variable_manager, host_list=HOST_LIST)
        self.variable_manager.set_inventory(self.inventory)
        self.tqm=TaskQueueManager(inventory=self.inventory,
              variable_manager=self.variable_manager,
              loader=self.loader,
              options=self.options,
              passwords=self.passwords,
              stdout_callback=self.results_callback,)
        #self.play = Play().load(self.play_source, variable_manager=self.variable_manager, loader=self.loader)

    def add_extendvars(self,newext):
        #print(newext)
        #ext=self.variable_manager.extra_vars.copy()
        #self.variable_manager.extra_vars=ext.update(newext)
        self.variable_manager.extra_vars=newext


    def set_playbook(self,pb):
        self.playbook=pb

    def run_block(self):
        try:
            result =self.tqm.run(Play().load(self.playbook.push_playbook(),variable_manager=self.variable_manager,loader=self.loader))
        finally:
            if self.tqm is not None:
                self.tqm.cleanup()

