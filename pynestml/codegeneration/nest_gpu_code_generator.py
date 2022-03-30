# -*- coding: utf-8 -*-
#
# nest_gpu_code_generator.py
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
from typing import Sequence, Optional, Mapping, Any
from pynestml.codegeneration.nest_code_generator import NESTCodeGenerator
from pynestml.frontend.frontend_configuration import FrontendConfiguration
from pynestml.meta_model.ast_synapse import ASTSynapse
from pynestml.meta_model.ast_neuron import ASTNeuron


class NESTGPUCodeGenerator(NESTCodeGenerator):
    """
    A code generator for NEST GPU target
    """

    _default_options = {
        "neuron_parent_class": "BaseNeuron",
        "neuron_parent_class_include": "archiving_node.h",
        "preserve_expressions": False,
        "simplify_expression": "sympy.logcombine(sympy.powsimp(sympy.expand(expr)))",
        "templates": {
            "path": os.path.join(os.path.dirname(__file__), "resources_nest_gpu"),
            "model_templates": {
                "neuron": ["user_m1_iaf_psc_exp.cu.jinja2", "user_m1_iaf_psc_exp.h.jinja2",
                           "user_m1_iaf_psc_exp_kernel.h.jinja2", "user_m1_iaf_psc_exp_rk5.h.jinja2"],
            },
            "module_templates": [""]
        }
    }

    def __init__(self, options: Optional[Mapping[str, Any]] = None):
        super().__init__(options)
        self._target = "NEST_GPU"
        super(NESTGPUCodeGenerator, self).setup_template_env()
        # TODO: setup the printers and reference converters

    def generate_neuron_code(self, neuron: ASTNeuron) -> None:
        if not os.path.isdir(FrontendConfiguration.get_target_path()):
            os.makedirs(FrontendConfiguration.get_target_path())

        for _model_templ in self._model_templates["neuron"]:
            file_extension = _model_templ.filename.split(".")[-2]
            _file = _model_templ.render(self._get_neuron_model_namespace(neuron))
            suffix = ""
            if "kernel" in _model_templ.filename:
                suffix = "_kernel"
            elif "rk5" in _model_templ.filename:
                suffix = "_rk5"

            with open(str(os.path.join(FrontendConfiguration.get_target_path(),
                                       neuron.get_name())) + suffix + "." + file_extension, "w+") as f:
                f.write(str(_file))

    def generate_module_code(self, neurons: Sequence[ASTNeuron], synapses: Sequence[ASTSynapse]):
        pass

    def generate_code(self, neurons: Sequence[ASTNeuron], synapses: Sequence[ASTSynapse]) -> None:
        super(NESTGPUCodeGenerator, self).generate_code(neurons)
