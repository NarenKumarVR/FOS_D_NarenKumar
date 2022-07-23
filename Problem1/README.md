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
