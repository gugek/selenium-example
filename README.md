# Selenium Example

Selenium example using Python bindings.

`$ python example.py [url]`


# Setup & Provision

## Development

- Use a vagrant environment for a RHEL7 machine
- `$ vagrant up`
- Return to host shell and then run: `$ vagrant provision`

### Deployment

On the development environment

In the `/vagrant/provisioning/` directory.

`$ ansible-playbook -vvv -i production site.yml`

# Command Line Help

```
# python example.py --help
usage: example.py [-h] [-v] [-d] [-l LOGFILE] [-L LOGLEVEL] [-p PAUSE] url

Selenium example

positional arguments:
  url                   website to scrape

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         verbose output
  -d, --debug           debug output
  -l LOGFILE, --logfile LOGFILE
                        Log file name
  -L LOGLEVEL, --loglevel LOGLEVEL
                        Python logging levels
  -p PAUSE, --pause PAUSE
                        delay in seconds for clicks
```
