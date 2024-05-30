"""
Power series expression
"""

import numpy as np

from PySDM.physics import constants as const


class PowerSeries:  # pylint: disable=too-few-public-methods
    def __init__(self, particulator, *, prefactors=None, powers=None):
        si = const.si
        self.particulator = particulator
        prefactors = prefactors or [30.0 * si.m / si.s * si.kg ** (1 / 6)]
        self.prefactors = np.array(prefactors)
        powers = powers or [1 / 6]
        self.powers = np.array(powers)
        for i, p in enumerate(self.powers):
            self.prefactors[i] *= (4 / 3 * const.PI * 1000 * si.kg / si.m**3) ** (p)
            # self.prefactors[i] /= (1 * si.um**3) ** (p)
        assert len(self.prefactors) == len(self.powers)

    def __call__(self, output, radius):
        self.particulator.backend.power_series(
            values=output.data,
            radius=radius.data,
            num_terms=len(self.powers),
            prefactors=self.prefactors,
            powers=self.powers,
        )
