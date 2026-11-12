#!/bin/bash
set -e

if command -v dnf >/dev/null 2>&1; then
  dnf install -y httpd
elif command -v yum >/dev/null 2>&1; then
  yum install -y httpd
fi

systemctl enable httpd
systemctl restart httpd
