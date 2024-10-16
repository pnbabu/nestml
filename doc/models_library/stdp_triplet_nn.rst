stdp_triplet_nn
###############


stdp_triplet_nn - Synapse type with triplet spike-timing dependent plasticity

Description
+++++++++++

A connection with spike time dependent plasticity accounting for spike triplet effects (as defined in [1]_).

Nearest-neighbour variant of pre- and postsynaptic spike coupling.


References
++++++++++
.. [1] Pfister JP, Gerstner W (2006). Triplets of spikes in a model
       of spike timing-dependent plasticity.  The Journal of Neuroscience
       26(38):9673-9682. DOI: https://doi.org/10.1523/JNEUROSCI.1425-06.2006



Parameters
++++++++++


.. csv-table::
    :header: "Name", "Physical unit", "Default value", "Description"
    :widths: auto

    
    "d", "ms", "1ms", "Synaptic transmission delay"    
    "tau_plus", "ms", "16.8ms", "time constant for tr_r1"    
    "tau_x", "ms", "101ms", "time constant for tr_r2"    
    "tau_minus", "ms", "33.7ms", "time constant for tr_o1"    
    "tau_y", "ms", "125ms", "time constant for tr_o2"    
    "A2_plus", "real", "7.5e-10", ""    
    "A3_plus", "real", "0.0093", ""    
    "A2_minus", "real", "0.007", ""    
    "A3_minus", "real", "0.00023", ""    
    "Wmax", "nS", "100nS", ""    
    "Wmin", "nS", "0nS", ""


State variables
+++++++++++++++

.. csv-table::
    :header: "Name", "Physical unit", "Default value", "Description"
    :widths: auto

    
    "w", "nS", "1nS", "Synaptic weight"    
    "tr_r1", "real", "0.0", ""    
    "tr_r2", "real", "0.0", ""    
    "tr_o1", "real", "0.0", ""    
    "tr_o2", "real", "0.0", ""
Source code
+++++++++++

.. code-block:: nestml

   synapse stdp_triplet_nn:
     state:
       w nS = 1nS # Synaptic weight
       tr_r1 real = 0.0
       tr_r2 real = 0.0
       tr_o1 real = 0.0
       tr_o2 real = 0.0
     end
     parameters:
       d ms = 1ms @nest::delay # Synaptic transmission delay
       tau_plus ms = 16.8ms # time constant for tr_r1
       tau_x ms = 101ms # time constant for tr_r2
       tau_minus ms = 33.7ms # time constant for tr_o1
       tau_y ms = 125ms # time constant for tr_o2
       A2_plus real = 7.5e-10
       A3_plus real = 0.0093
       A2_minus real = 0.007
       A3_minus real = 0.00023
       Wmax nS = 100nS
       Wmin nS = 0nS
     end
     equations:
       tr_r1'=-tr_r1 / tau_plus
       tr_r2'=-tr_r2 / tau_x
       tr_o1'=-tr_o1 / tau_minus
       tr_o2'=-tr_o2 / tau_y
     end

     input:
       pre_spikes real <-spike
       post_spikes real <-spike
     end

     output: spike

     onReceive(post_spikes):
       # increment post trace values
       tr_o1 += 1
       tr_o2 += 1
       # potentiate synapse
       #w_ nS = Wmax * ( w / Wmax + tr_r1 * ( A2_plus + A3_plus * tr_o2 ) )
       w_ nS = w + tr_r1 * (A2_plus + A3_plus * tr_o2)
       w = min(Wmax,w_)
     end

     onReceive(pre_spikes):
       # increment pre trace values
       tr_r1 += 1
       tr_r2 += 1
       # depress synapse
       #w_ nS = Wmax * ( w / Wmax  -  tr_o1 * ( A2_minus + A3_minus * tr_r2 ) )
       w_ nS = w - tr_o1 * (A2_minus + A3_minus * tr_r2)
       w = max(Wmin,w_)
       # deliver spike to postsynaptic partner
       deliver_spike(w,d)
     end

   end



Characterisation
++++++++++++++++

.. include:: stdp_triplet_nn_characterisation.rst


.. footer::

   Generated at 2023-03-02 18:49:47.357670