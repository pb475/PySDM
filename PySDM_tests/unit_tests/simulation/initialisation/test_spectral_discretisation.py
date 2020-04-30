from PySDM.initialisation.spectral_sampling import *
from PySDM.initialisation.spectra import Lognormal
import numpy as np
import pytest


@pytest.mark.parametrize("discretisation", [
	pytest.param(linear),
	pytest.param(logarithmic),
	pytest.param(constant_multiplicity)
])
def test_spectral_discretisation(discretisation):
	# Arrange
	n_sd = 100
	m_mode = .5e-5
	n_part = 256*16
	s_geom = 1.5
	spectrum = Lognormal(n_part, m_mode, s_geom)
	m_range = (.1e-6, 100e-6)

	# Act
	m, n = discretisation(n_sd, spectrum, m_range)

	# Assert
	assert m.shape == n.shape
	assert n.shape == (n_sd,)
	assert np.min(m) >= m_range[0]
	assert np.max(m) <= m_range[1]
	actual = np.sum(n)
	desired = spectrum.cumulative(m_range[1]) - spectrum.cumulative(m_range[0])
	quotient = actual / desired
	# TODO relative error
	np.testing.assert_almost_equal(actual=quotient, desired=1.0, decimal=2)


# TODO test_linear()

# TODO test_logarithmic()

# TODO test_constant_multiplicity()
