#!/bin/bash
sudo ipfw add fwd localhost,8080 tcp from any to 192.168.1.3 80
#sudo ipfw add fwd tcp from any,80 to me,8080
