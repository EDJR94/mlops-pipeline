# 1)
# logar no gcloud
gcloud auth login

# nome do projeto como env
export PROJECT_ID=$(gcloud config get-value project)
echo $PROJECT_ID

# configurar docker
gcloud auth configure-docker

# buildar e subir o docker para artifcat registry
gcloud builds submit --tag gcr.io/$PROJECT_ID/mlops-model:latest .

