```
$ vagrant provision
==> machine1: Running provisioner: ansible...
ANSIBLE_FORCE_COLOR=true ANSIBLE_HOST_KEY_CHECKING=false PYTHONUNBUFFERED=1 ansible-playbook --private-key=/Users/matt/.vagrant.d/insecure_private_key --user=vagrant --limit='machine1' --inventory-file=/Users/matt/Workspaces/ansible-bug/.vagrant/provisioners/ansible/inventory -v test.yml

PLAY [all] ********************************************************************

GATHERING FACTS ***************************************************************
ok: [machine1]

TASK: [myrole | template src=template.j2 dest=/tmp/something] *****************
fatal: [machine1] => {'msg': "AnsibleError: file: /Users/matt/Workspaces/ansible-bug/myrole/templates/template.j2, line number: 1, error: no filter named 'to_lua'", 'failed': True}
fatal: [machine1] => {'msg': "AnsibleError: file: /Users/matt/Workspaces/ansible-bug/myrole/templates/template.j2, line number: 1, error: no filter named 'to_lua'", 'failed': True}

FATAL: all hosts have already failed -- aborting

PLAY RECAP ********************************************************************
           to retry, use: --limit @/Users/matt/test.retry

machine1                   : ok=1    changed=0    unreachable=1    failed=0

Ansible failed to complete successfully. Any error output should be
visible above. Please fix these errors and try again.
```
