#!/usr/bin/env python

"""
Perform some test of the calculate_rmsd function
Needs to be expanded
by: Maximilian Peters (lastNameDotFirstNameATgmail)
project: https://github.com/charnley/rmsd
license: https://github.com/charnley/rmsd/blob/master/LICENSE

"""

import calculate_rmsd

def test_all(threshold=0.001):
    """
    Some very basic functional tests
    :return: True if all test passed
    """

    print('Testing PDB RMSD')
    if not test_pdb(threshold=threshold):
        return False
    else:
        print('Passed')

    print('Testing xyz RMSD')
    if not test_xyz(threshold=threshold):
        return False
    else:
        print('Passed')

    print('\nPassed all tests')

    return True

def test_xyz(threshold=0.001):
    """
    A simple test for the xyz functionality
    :return: True if all test passed 
    """

    p_atoms, P = calculate_rmsd.get_coordinates('examples/ethane.xyz', 'xyz')
    q_atoms, Q = calculate_rmsd.get_coordinates('examples/ethane.xyz', 'xyz')

    n_rmsd = calculate_rmsd.rmsd(P, Q)
    Pc = calculate_rmsd.centroid(P)
    Qc = calculate_rmsd.centroid(Q)
    P -= Pc
    Q -= Qc

    k_rmsd = calculate_rmsd.kabsch_rmsd(P, Q)
    q_rmsd = calculate_rmsd.quaternion_rmsd(P, Q)

    if abs(n_rmsd) > threshold:
        print('Failed to calculate normal RMSD, result: {0}'.format(n_rmsd))
        return False
    if abs(k_rmsd) > threshold:
        print('Failed to calculate Kabsch RMSD, result: {0}'.format(k_rmsd))
        return False
    if abs(q_rmsd) > threshold:
        print('Failed to calculate quaternion RMSD, result: {0}'.format(q_rmsd))
        return False
    if abs(q_rmsd - k_rmsd) > threshold ** 2:
        print('Failed to yield similar Kabsch and quaternion RMSD, result: {0} vs {1}'.format(k_rmsd, q_rmsd))
        return False
    return True

def test_pdb(threshold=0.001):
    """
    A simple test for the PDB functionality
    :return: True if all test passed
    """
    p_atoms, P = calculate_rmsd.get_coordinates('examples/ci2_1.pdb', 'pdb')
    q_atoms, Q = calculate_rmsd.get_coordinates('examples/ci2_2.pdb', 'pdb')

    n_rmsd = calculate_rmsd.rmsd(P, Q)
    Pc = calculate_rmsd.centroid(P)
    Qc = calculate_rmsd.centroid(Q)
    P -= Pc
    Q -= Qc

    k_rmsd = calculate_rmsd.kabsch_rmsd(P, Q)
    q_rmsd = calculate_rmsd.quaternion_rmsd(P, Q)

    if abs(n_rmsd - 26.975) > threshold:
        print('Failed to calculate normal RMSD, result: {0}'.format(n_rmsd))
        return False
    if abs(k_rmsd - 11.777) > threshold:
        print('Failed to calculate Kabsch RMSD, result: {0}'.format(k_rmsd))
        return False
    if abs(q_rmsd - 11.777) > threshold:
        print('Failed to calculate quaternion RMSD, result: {0}'.format(q_rmsd))
        return False
    if abs(q_rmsd - k_rmsd) > threshold ** 2:
        print('Failed to yield similar Kabsch and quaternion RMSD, result: {0} vs {1}'.format(k_rmsd, q_rmsd))
        return False
    return True

if __name__ == '__main__':
    test_all()