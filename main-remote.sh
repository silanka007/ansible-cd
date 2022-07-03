#!/bin/bash
ansible-playbook main-remote.yml -i inventory --private-key "./ansible-cicd-uswest2.pem"