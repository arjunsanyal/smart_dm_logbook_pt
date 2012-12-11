
SMART Glucose Logbook Patient App
=================================

Arjun Sanyal <arjun.sanyal@childrens.harvard.edu>
Josh Mandel  <Joshua.Mandel@childrens.harvard.edu>

This is the SMART patient-facing glucose logbook app. It runs as a
standalone Python WSGI app and includes metadata to make running on
[AppFog][] simple but it can be run easily on other systems. It
integrates with Microsoft [HealthVault][] for authentication and storage
of the patient's personal health data via the `healthvault_py` Python
library included as a git submodule. Both reading and writing of data to
the patient's HealthVault account is supported.

The app is written with the support of the [AngularJS][] "framework" and
the code is organized using a stripped-down version of the
[angular-seed][] sample repository. The visualization are written using
the [D3][] JavaScript visualization and interaction library.

[AppFog]: http://appfog.com
[HealthVault]: http://healthvault.com
[AngularJS]: http://angularjs.org
[angular-seed]: https://github.com/angular/angular-seed
[D3]: http://d3js.org


TODO
----
- Document HealthVault setup


Directory Structure
-------------------
- The /app, /config, /logs, /scripts, /test directories are from
  <https://github.com/angular/angular-seed>


AppFog Setup
------------
- `requirements.txt`
  - This file describes the dependecies (including versions) for this
    app. Without it AppFog's virtual server's wouldn't have the
    libraries installed that this app needs.

    flask==0.8
    pycrypto==2.6
    lxml==2.3.4

- `manifest.yml`
  - Defines the configuration parameters for the desired AppFog instance
  - Change the file for your preferred settings


Running Locally
---------------
You must have root permissions to run the app locally since it is
configured by default to listen on port 80. You can change this in the
`wsgi.py` script. To start on localhost port 80:

    $ sudo python wsgi.py


Running on AppFog
-----------------
Assuming you have the AppFog commadline app installed and are logged in
using it, updating and starting the app should be simply:

    $ af apps
    $ af push <your-app-name>
    $ af update <your-app-name> --debug
    $ af logs <your-app-name> --all
