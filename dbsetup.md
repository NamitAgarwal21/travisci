# travisci

Access db from local terminal  
- open https://cloud.google.com/sdk/docs/install
- Download for your platform and put in home directory
- From terminal navigate to home directory and run the following command
- ./google-cloud-sdk/install.sh
- Do you want to help improve the Google Cloud SDK (y/N)?  N
- Do you want to continue (Y/n)?  Y
- Open new terminal
- gcloud init
- You must log in to continue. Would you like to log in (Y/n)?  Y
- it would redirect to browser
- login and allow   

Pick cloud project to use: 
 [1] travis-ci-staging-services-1
 [2] Create a new project
Please enter numeric choice or text value (must exactly match list 
item):  1
- gcloud components install kubectl
-  gcloud container clusters get-credentials travis-ci-services-1 --region us-east4 --project travis-ci-staging-services-1
- kubectl config use-context gke_travis-ci-staging-services-1_us-east4_travis-ci-services-1
- kubectl -n gce-staging-pro-services-1 exec -it travis-pro-billing-v2-db8f9dc7c-8cw96 env | grep DATABASE
-  gcloud components install cloud_sql_proxy