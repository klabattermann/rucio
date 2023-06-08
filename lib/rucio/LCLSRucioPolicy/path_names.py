
import hashlib

def construct_surl_LCLS(dsn: str, scope: str, filename: str) -> str:
    """
    Defines relative SURL for replicas. This method uses the LCLS convention
    for xtc files. To be used for non-deterministic sites.

    @return: relative SURL for new replica.
    @rtype: str
    """
    if dsn == "xtc":
        if dsn == 'xtc' and filename.find('smd.xtc') > 0:
            return '/%s/%s/%s/smalldata/%s' % (scope[:3], scope, dsn, filename)
        return '/%s/%s/%s/%s' % (scope[:3], scope, dsn, filename)

    try:
        instr, expt, fld, remain = filename.split('.', 3)
    except ValueError:
        use_hash = True
    else:
        use_hash = False if fld in ('xtc', 'hdf5') else True

    if use_hash:
        md5 = hashlib.md5(filename.encode()).hexdigest()
        return '/hash/%s/%s' % (md5[:3], filename)
    else:
        if fld == 'xtc' and filename.endswith('smd.xtc'):
            return '/%s/%s/xtc/smalldata/%s' % (instr, expt, remain)
        return '/%s/%s/%s/%s' % (instr, expt, fld, remain)

