./GenRandNum.sh n #commandto run

where n is the number of times the loop has to run 

!! Not able to run the docker.

Commands used:
 - docker run -d fosfordevops/csvgenerator --platform linux/amd64
 - docker run -d fosfordevops/csvgenerator

Errors got:
WARNING: The requested image's platform (linux/amd64) does not match the detected host platform (linux/arm64/v8) and no specific platform was requested
89be5a14840984ec860686bc9bbf6f1034827404f14894953727bef825e810c3
docker: Error response from daemon: failed to create shim task: OCI runtime create failed: runc create failed: unable to start container process: exec: "--platform": executable file not found in $PATH: unknown.

PART 1:
After running docker run:
console curl -o ./part-1-output http://localhost:9393/raw 
^ IF THIS FAILS
wget -O ./part-1-output http://localhost:9393/raw
console docker logs [container_id] >& part-1-logs

PART 2:
Create docker-compose.yaml file
docker-compose up


PART 3:
Add Prometheus container prom/prometheus:v2.22.0

Prometheus configuration is YAML. The Prometheus download comes with a sample configuration in a file called prometheus.yml that is a good place to get started.

We've stripped out most of the comments in the example file to make it more succinct (comments are the lines prefixed with a #).

#inside the file
global:
  scrape_interval:     15s
  evaluation_interval: 15s

rule_files:
  # - "first.rules"
  # - "second.rules"

scrape_configs:
  - job_name: prometheus
    static_configs:
      - targets: ['localhost:9090']

