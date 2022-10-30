#!/bin/bash
echo "Criando imagens..."

docker build ./backend/ -t hugovasc/kub-php-backend:1.0
docker build ./database/ -t hugovasc/kub-meubanco:1.0

echo "Subindo as imagens para o registry DockerHub"

docker push hugovasc/kub-php-backend:1.0
docker push hugovasc/kub-meubanco:1.0

echo "Criando servicos no cluster kubernetes..."

kubectl apply -f ./service.yml

echo "Criando os deployments..."

kubectl apply -f ./deployment.yml

echo "Deploy da aplicacao finalizado"