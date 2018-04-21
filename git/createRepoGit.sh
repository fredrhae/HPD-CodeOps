#!/bin/bash

echo "Criando pasta principal..."

mkdir HPD-CodeOps
cd HPD-CodeOps

echo "Criando diretórios das aulas..."
mkdir linux
mkdir git
mkdir ruby
mkdir python
mkdir docker
mkdir chef
mkdir ansible
mkdir gitlab
mkdir jenkins
mkdir prometheus
mkdir beat
mkdir markdown
mkdir graylog

echo "Criando arquivos ocultos pra diretórios vazios..."
touch linux/.hold
touch git/.hold
touch ruby/.hold
touch python/.hold
touch docker/.hold
touch chef/.hold
touch ansible/.hold
touch gitlab/.hold
touch jenkins/.hold
touch prometheus/.hold
touch beat/.hold
touch markdown/.hold
touch graylog/.hold

echo "Inicializando arquivos git..."

git init
read -p "Entre com a url do repositório git: " repo
git remote add origin $repo
git pull origin master
git add .
git commit -m "Commit arquivos iniciais..."
git push -u origin master
