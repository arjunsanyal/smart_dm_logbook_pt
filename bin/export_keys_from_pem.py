#!/usr/bin/env python
#
# Run from top-level dir like
#
# $ bin/export_keys_from_pem
#
# A utility script to display public and private keys from a .pem
# file for copy-and-paste into a django settings.py file.
#
# Arjun Sanyal (arjun.sanyal@childrens.harvard.edu)
#
# todo: add fingerprint:
# $ openssl x509 -inform DER -in cert.cer -fingerprint -noout
# SHA1 Fingerprint=06:55:AB:19:2E:95:BC:35:F9:61:28:FF:F9:F5:29:D6:FD:02:06:EF

import os
import subprocess
import tempfile

cert_dir = './certs/'
keyfilename = 'key.pem'
filename = cert_dir + 'keys_for_settings.txt'

if __name__ == "__main__":
    proc = subprocess.Popen(['openssl rsa -text -noout -in '
                             + cert_dir
                             + keyfilename],
                            stdout=subprocess.PIPE,
                            shell=True)
    out_str = (proc.communicate()[0]).replace(':', '').replace('\n', '').replace(' ', '')

    # output the keys as hex strings in settings.py variables
    keys_str = "APP_PUBLIC_KEY = '0x" \
        + out_str.partition('modulus')[2].partition('publicExponent')[0] \
        + "'" \
        + "\n" \
        + "APP_PRIVATE_KEY = '0x" \
        + out_str.partition('privateExponent')[2].partition('prime1')[0] \
        + "'\n"

    # print keys_str
    temp = tempfile.NamedTemporaryFile(
        suffix='.tmp',
        dir=cert_dir,
        delete=False)
    temp.write(keys_str)
    temp.flush()
    try:
        os.unlink(filename)
    except:
        pass
    os.rename(temp.name, filename)
    temp.close()

    print """\nDone.. Add certs/keys_for_settings.py file to settings.py
And don\'t forget to check the APP_THUMBPRINT too!\n"""
