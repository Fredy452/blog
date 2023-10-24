# Backend de la Aplicación Web de blogs

## Descripción 
Desde el backend de la aplicación web de blogs, los usuarios pueden realizar las siguientes acciones:

- **Registro e Inicio de Sesión de Usuarios:** Los usuarios pueden registrarse en el sistema e iniciar sesión en la aplicación.
- **Creación de Catetgorias:** Los usuarios pueden crear categorias para los posts.
- **Creación de Etiquetas:** Los usuarios pueden crear entradas etiquetas para los posts
- **Creacin de Posts:** Los usuarios pueden crear posts con categorias, etiquetas he imagenes.
- **Edición de Posts:** Los usuarios pueden editar los posts que han creado.
- **Eliminación de Posts:** Los usuarios pueden eliminar los posts que han creado.
- **Búsqueda de Posts:** Los usuarios tienen a su disposición una interfaz para buscar posts según su nombre.

## Instalación de la Aplicación Web 

### Pasos para configurar el entorno virtual, instalar Django y las dependencias desde el archivo `requirements.txt`:
- Inicializar el entorno virtual:
```bash
python3 -m venv venv
```
- Activar el entorno virtual:
```bash
source venv/bin/activate
```
- Instalar Django:
```bash
pip install django
```
- Instalar las dependencias del proyecto:
```bash
pip install -r requeriments.txt
```

## Estructura del Proyecto


- `apps/`: Directorio que contiene las aplicaciones Django.
- `config/`: Directorio que contiene la configuración principal de Django.
- `media/`: Directorio para archivos multimedias como imagenes, videos, etc.
- `static/`: Directorio para archivos estáticos como CSS, JavaScript, etc.
- `templates/`: Directorio para las plantillas HTML utilizadas en la aplicación.
- `tests/`: Directorio para archivos de pruebas.
- `LICENSE`: Archivo de licencia del proyecto.
- `Makefile`: Archivo con lista de comandos a ejecutarse con `make`
- `manage.py`: El archivo de gestión de Django para realizar tareas administrativas.
- `README.md`: Este archivo, que proporciona información sobre el proyecto.
- `requeriments.txt`: Archivo que lista las dependencias necesarias para el proyecto.

# Que mas puedo agregar a este proyecto?
- [ ] Implementar un sistema de comentarios para los posts.
- [ ] Implementar un sistema de likes para los posts.
- [ ] Implementar un sistema de seguidores para los usuarios.
- [ ] Implementar un sistema de notificaciones para los usuarios.
- [ ] Implementar un sistema de mensajes para los usuarios.
