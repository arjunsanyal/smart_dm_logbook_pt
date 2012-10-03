# smart_hv_django

Arjun Sanyal <arjun.sanyal@childrens.harvard.edu>

A Django-based app for working with Microsoft HealthVault. Part of the
SMART Project <smartplatforms.org>.


# Requirements

* The Python Cryptography Toolkit <https://www.dlitz.net/software/pycrypto/>
  * Install the easy way: `sudo pip install pycrypto`
* The `lxml` XML toolkit <http://lxml.de>
  * Python has ElementTree built in, but since much of what this
    libray does is XML manipulation, the extra features of lxml
    are quite useful


# Getting Started

## Certificate Generation

To get started, generate a new app with cert with the HV App manager
then create a additional cert with no passphrase locally below.

    $ openssl req -outform DER -new -newkey rsa:2048 -days 10000 -nodes \
          -x509 -keyout key.pem -out cert.cer

Add the `cert.cer` public certificate to your app's automatically
generated public certificate at <http://config.healthvault-ppe.com>. If
your upload was successful, you will see the certificate file's
thumbprint listed. You can also generate this with:

    $ openssl x509 -inform DER -in cert.cer -fingerprint -noout

which will output:

    SHA1 Fingerprint=06:55:AB:19:2E...............29:D6:FD:02:06:EF

this (without the colons) will match the "thumbprint" at HealthVault.

Then use the `/bin/export_keys_from_pem` script to generate the Python
variables with your public and private key data to copy-and-paste into
`settings.py`.

## Configuring settings.py

* Set your app's id, `HV_APPID`. This is in your HV App Config center
* Set you app's certificate "fingerprint" (or "thumbprint" in MS-speak)
  from above
* Set your app's public and private keys, by running the
  `export_keys_from_pem` script and adding the output file to settings.py
