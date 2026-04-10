# 🐍 Django Base Project (ejemploIW)

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.x-green.svg)](https://www.djangoproject.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)

Plantilla base y proyecto funcional Django con arquitectura modular. Este repositorio está estructurado para gestionar múltiples entidades de negocio (mascotas, sedes, productos, proveedores, etc.) y está preparado para desarrollo con contenedores Docker.

## 📁 Estructura del Proyecto

El proyecto sigue una estructura modular, separando la lógica de negocio en distintas aplicaciones Django:

*   `mascotas/` - Gestión de mascotas y los tipos de mascotas(CRUD).
*   `encuentros/` - Registro de interacciones entre mascotas-usuarios (CRUD).
*   `user/` - Modelo de usuario personalizado.
*   `ejemploIW/` - Carpeta principal del proyecto (settings, urls raíz, wsgi/asgi).

## 🚀 Características Principales (v1.0)

*   **Arquitectura Modular:** Apps Django desacopladas para facilitar el mantenimiento.
*   **Docker Ready:** Incluye `dockerfile` y `compose.yml` para levantar el entorno de desarrollo con un solo comando.
*   **Variables de Entorno:** Configuración segura mediante archivo `.env` (no incluido en el repo por seguridad).
*   **API Testing:** Incluye una **Postman Collection** (`ejemploIW.postman_collection.json`) para probar los endpoints rápidamente.

## ⚙️ Requisitos Previos

*   [Docker](https://docs.docker.com/get-docker/) y Docker Compose (Recomendado)
*   *Alternativa sin Docker:* Python 3.10+ y pip.

## 🛠️ Instalación y Primeros Pasos

Sigue estos pasos para tener el proyecto corriendo en tu máquina local.

### 1. Clonar el repositorio
```bash
git clone https://github.com/alvaromendoooo/django-base.git
cd django-base
```
### 2. Levantar la aplicación y su base de datos asociada mediante docker
```bash
docker compose up -d
```
Con el comando indicado, se levanta el gestor visual de PostgreSQL, la base de datos PostgreSQL asociada a la aplicación django y la aplicación Django.
