# -*- coding: utf-8 -*-
#
# nest_multithreading_test.py
#
# This file is part of NEST.
#
# Copyright (C) 2004 The NEST Initiative
#
# NEST is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# NEST is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with NEST.  If not, see <http://www.gnu.org/licenses/>.
import os
import unittest

from pynestml.frontend.pynestml_frontend import to_nest, install_nest
import nest


class NestMultithreadingTest(unittest.TestCase):

    def test_nest_multithreading(self):
        input_path = os.path.join(os.path.realpath(
            os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 'models', 'iaf_psc_exp.nestml')))
        nest_path = nest.ll_api.sli_func("statusdict/prefix ::")
        target_path = 'target_t'
        logging_level = 'INFO'
        module_name = 'names_module'
        store_log = False
        suffix = '_nestml'
        dev = True
        to_nest(input_path, target_path, logging_level, module_name, store_log, suffix, dev)
        install_nest(target_path, nest_path)

        nest.Install(module_name)
        nest.SetKernelStatus({"local_num_threads": 2})
        neurons = nest.Create('iaf_psc_exp_nestml', 2)
        st = list(nest.GetStatus(neurons, 'vp'))
        print(st)
        mm = nest.Create('multimeter', {"record_from": ["V_abs"]})
        nest.Connect(mm, neurons[0])
        nest.Simulate(100.)

        v_m = mm.get("events")["V_abs"]
        print(v_m)
