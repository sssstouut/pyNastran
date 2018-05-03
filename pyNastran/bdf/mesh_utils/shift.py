"""
defines:
 - model = shift(bdf_filename, dxyz, bdf_filename_out=None)
"""
from __future__ import print_function
from six import iteritems
import numpy as np

from pyNastran.bdf.mesh_utils.internal_utils import get_bdf_model


def shift(bdf_filename, dxyz, bdf_filename_out=None):
    """shifts the model by some amount"""
    if isinstance(dxyz, list):
        dxyz = np.array(dxyz)
    assert isinstance(dxyz, np.ndarray), dxyz
    print("dxyz = %s" % dxyz)

    model = get_bdf_model(bdf_filename, xref=True, log=None, debug=True)
    for unused_nid, node in iteritems(model.nodes):
        xyz = node.get_position() + dxyz
        node.set_position(model, xyz, cid=0, xref=True)

    for unused_caero_id, caero in iteritems(model.caeros):
        caero.shift(dxyz)

    if bdf_filename_out:
        model.write_bdf(bdf_filename_out)
    return model
