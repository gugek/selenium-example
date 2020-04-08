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
$ python example.py --help
```
