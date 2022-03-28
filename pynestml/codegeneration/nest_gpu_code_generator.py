# -*- coding: utf-8 -*-
#
# nest_code_generator.py
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
from typing import Sequence

from pynestml.meta_model.ast_synapse import ASTSynapse

from pynestml.codegeneration.code_generator import CodeGenerator
from pynestml.meta_model.ast_neuron import ASTNeuron


class NESTGPUCodeGenerator(CodeGenerator):
    """
    A code generator for NEST GPU target
    """

    def generate_code(self, neurons: Sequence[ASTNeuron], synapses: Sequence[ASTSynapse]) -> None:
        # TODO:
        pass
