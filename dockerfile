# Usar una imagen base de Python 3.12
FROM python:3.12.7-alpine3.20

# Establecer el directorio de trabajo
WORKDIR /usr/app/

# Instalar dependencias de Python
RUN apk update && \
    apk add --no-cache gcc musl-dev libffi-dev postgresql-dev && \
    pip install --upgrade pip

# Instalar Node.js y npm
RUN apk add --no-cache nodejs npm

# Copiar y instalar las dependencias de Python
COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copiar y instalar las dependencias de Node.js
COPY ./package.json ./package-lock.json ./
RUN npm install

# Copiar el resto del código de la aplicación
COPY ./ ./

# Exponer el puerto en el que correrá la aplicación
EXPOSE 8000