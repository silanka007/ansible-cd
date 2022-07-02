# commands

- aws ec2 describe-instances \
  \
   --query 'Reservations[*].Instances[*].PublicIpAddress' \
   --filters "Name=tag:Project,Values=Ansible CICD" \
   --output text >> inventory
