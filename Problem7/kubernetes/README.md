Create the Blue Deployment:

$ kubectl apply -f kubernetes/blue-deploy.yaml
The service is of type=LoadBalancer so it can be accessed via a Network Load Balancer on GCP. It uses the name and version labels specified in the Deployment to select the pods for the service.

Create the Service:

$ kubectl apply -f kubernetes/service.yaml

Test the Blue Deployment

$ EXTERNAL_IP=$(kubectl get svc nginx -o jsonpath="{.status.loadBalancer.ingress[*].ip}")
$ while true; do curl -s http://$EXTERNAL_IP/version | grep nginx; sleep 0.5; done

Now we are ready to deploy a new version.

Update the application
A new Deployment will be created to update the application and the Service will be updated to point at the new version. This is mostly instantaneous.

Create the Green Deployment
You can update the Blue Deployment's file directly or use a tool like sed:

Create the new Deployment:

$ sed 's/1\.10/1.11/' kubernetes/blue-deploy.yaml | kubectl apply -f -
Switch Traffic to the Green Version
We will update the Service to select pods from the Green Deployment. This will cause new requests to be set to the new pods.

You can update the file directly or use a tool like sed:

$ sed 's/1\.10/1.11/' kubernetes/service.yaml 

Update the Service:

sed 's/1\.10/1.11/' kubernetes/service.yaml | kubectl apply -f -