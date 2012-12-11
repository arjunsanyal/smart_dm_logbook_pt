
SMART Microsoft HealthVault Patient App
---------------------------------------

Arjun Sanyal <arjun.sanyal@childrens.harvard.edu>
Josh Mandel  <Joshua.Mandel@childrens.harvard.edu>

The patient-facing app of the SMART + Microsoft HealthVault "Merge"
project.


########### Do NOW

- FIX export script for new location











# FIXME: porting to flask (0.8.1) for appfog deployment #

# AppFog - Flask deployment notes

- added requirements.txt from af flask github repo only added flask==0.8
  line (not mymongo line)
- copied their wsgi.py script verbatim
- "af push"
- works!!! "welcome to appfog"



# angular seed

- app, config, logs, scripts, test dirs from angular-seed

- manifest.yml, requirements.txt from AF








---


FIXME: update this

- Requires the `healthvault.py` library as a submodule
- Uses the [AngularJS](http://angularjs.org) framework for client-side interaction
- Uses the [D3.js](http://d3js.org) manipulation and visulation library
- Uses the Django python-based web framwork (version 1.1)

## To Run

We're running it on port 9000, but you can change this in `settings.py`
at the `APP_ACTION_URL`

    $ python manage.py runserver 9000

Go to <http://localhost:9000>

## TODO

- Local caching of glucose results


---

Angular docs

### Running unit tests

We recommend using [jasmine](http://pivotal.github.com/jasmine/) and
[Testacular](http://vojtajina.github.com/testacular/) for your unit tests/specs, but you are free
to use whatever works for you.

Requires [node.js](http://nodejs.org/), Testacular (`sudo npm install -g testacular`) and a local
or remote browser.

* start `scripts/test.sh` (on windows: `scripts\test.bat`)
  * a browser will start and connect to the Testacular server (Chrome is default browser, others can be captured by loading the same url as the one in Chrome or by changing the `config/testacular.conf.js` file)
* to run or re-run tests just change any of your source or test javascript files


### End to end testing

Angular ships with a baked-in end-to-end test runner that understands angular, your app and allows
you to write your tests with jasmine-like BDD syntax.

Requires a webserver, node.js + `./scripts/web-server.js` or your backend server that hosts the angular static files.

Check out the
[end-to-end runner's documentation](http://docs.angularjs.org/guide/dev_guide.e2e-testing) for more
info.

* create your end-to-end tests in `test/e2e/scenarios.js`
* serve your project directory with your http/backend server or node.js + `scripts/web-server.js`
* to run do one of:
  * open `http://localhost:port/test/e2e/runner.html` in your browser
  * run the tests from console with [Testacular](vojtajina.github.com/testacular) via
    `scripts/e2e-test.sh` or `script/e2e-test.bat`


### Receiving updates from upstream

When we upgrade angular-seed's repo with newer angular or testing library code, you can just
fetch the changes and merge them into your project with git.


## Directory Layout

    app/                --> all of the files to be used in production
      css/              --> css files
        app.css         --> default stylesheet
      img/              --> image files
      index.html        --> app layout file (the main html template file of the app)
      index-async.html  --> just like index.html, but loads js files asynchronously
      js/               --> javascript files
        app.js          --> application
        controllers.js  --> application controllers
        directives.js   --> application directives
        filters.js      --> custom angular filters
        services.js     --> custom angular services
      lib/              --> angular and 3rd party javascript libraries
        angular/
          angular.js        --> the latest angular js
          angular.min.js    --> the latest minified angular js
          angular-*.js      --> angular add-on modules
          version.txt       --> version number
      partials/             --> angular view partials (partial html templates)
        partial1.html
        partial2.html

    config/testacular.conf.js        --> config file for running unit tests with Testacular
    config/testacular-e2e.conf.js    --> config file for running e2e tests with Testacular

    scripts/            --> handy shell/js/ruby scripts
      e2e-test.sh       --> runs end-to-end tests with Testacular (*nix)
      e2e-test.bat      --> runs end-to-end tests with Testacular (windows)
      test.bat          --> autotests unit tests with Testacular (windows)
      test.sh           --> autotests unit tests with Testacular (*nix)
      web-server.js     --> simple development webserver based on node.js

    test/               --> test source files and libraries
      e2e/              -->
        runner.html     --> end-to-end test runner (open in your browser to run)
        scenarios.js    --> end-to-end specs
      lib/
        angular/                --> angular testing libraries
          angular-mocks.js      --> mocks that replace certain angular services in tests
          angular-scenario.js   --> angular's scenario (end-to-end) test runner library
          version.txt           --> version file
      unit/                     --> unit level specs/tests
        controllersSpec.js      --> specs for controllers
        directivessSpec.js      --> specs for directives
        filtersSpec.js          --> specs for filters
        servicesSpec.js         --> specs for services

## Contact

For more information on AngularJS please check out http://angularjs.org/
