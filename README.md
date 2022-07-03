# commands
- aws ec2 describe-instances \
  \
   --query 'Reservations[*].Instances[*].PublicIpAddress' \
   --filters "Name=tag:Project,Values=Ansible" \
   --output text >> inventory


[comment:]: # "Assuming the udacity.pem and inventory files are present in the current directory - for setup role"
- ansible-playbook main-remote.yml -i inventory --private-key ansible-cicd-uswest2.pem