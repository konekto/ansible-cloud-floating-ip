Ansible cloud floating ip
=========

This role can set the floating ip of a Hetzner cloud server. It creates the network script and restarts the server.

See the Hetzner wiki for more details: https://wiki.hetzner.de/index.php/Cloud_floating_IP_persistent/en

Role Variables
--------------

* floating_ip - The floating ip for the server. (mandatory)

Example Playbook
----------------

Here a simple example for a playbook

    - name: Add floating ip to all cloud servers
      hosts: all
      roles:
        - role: ansible-cloud-floating-ip
          vars:
            floating_ip: 8.8.8.8

License
-------

MIT

Author Information
------------------

the team of konek.to. http://konek.to 2018

