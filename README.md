# My Tennis Club

**My Tennis Club** es una aplicación web diseñada para gestionar los miembros de un club de tenis. La aplicación permite a los usuarios ver una lista de miembros, acceder a detalles individuales de cada miembro y navegar de manera eficiente gracias a una interfaz limpia y moderna, implementada con Python y el framework Django. La interfaz está estilizada utilizando Bootstrap 5, lo que garantiza una experiencia de usuario responsiva y atractiva tanto en dispositivos de escritorio como móviles.

## Funcionalidades principales

- **Página de inicio**: Presenta información sobre el club de tenis y un acceso rápido a la lista de miembros.
- **Gestión de miembros**: Los miembros pueden ser visualizados en una lista, con información básica como nombre, apellido y un enlace a los detalles de cada uno.
- **Detalles del miembro**: Cada miembro tiene una página dedicada con su información detallada, incluyendo teléfono y fecha de incorporación al club.
- **Navegación eficiente**: Barra de navegación fija en la parte superior para un acceso rápido y constante a las secciones principales del sitio.

## Tecnologías utilizadas

- **Backend**: Python con Django, un potente framework para aplicaciones web.
- **Frontend**: HTML5, CSS3 con Bootstrap 5 para el diseño y la interfaz de usuario responsiva.
- **Base de datos**: Utiliza el sistema de base de datos integrado de Django, compatible con varias bases de datos relacionales como SQLite, PostgreSQL y MySQL.
  
## Características de la interfaz

- **Barra de navegación**: Fija y accesible desde cualquier parte del sitio.
- **Diseño limpio y moderno**: Estilizado con Bootstrap para una experiencia de usuario fluida y accesible en todos los dispositivos.
- **Accesibilidad**: Mejoras en la accesibilidad con atributos ARIA y un diseño optimizado para pantallas pequeñas.

## Cómo empezar

1. **Clonar este repositorio**:
    ```bash
    git clone https://github.com/tu-usuario/my-tennis-club.git
    ```

2. **Instalar dependencias**:
    Asegúrate de tener Python instalado, luego instala los paquetes necesarios:
    ```bash
    pip install -r requirements.txt
    ```

3. **Migrar la base de datos**:
    Ejecuta las migraciones para configurar la base de datos:
    ```bash
    python manage.py migrate
    ```

4. **Ejecutar el servidor de desarrollo**:
    Inicia el servidor de desarrollo de Django:
    ```bash
    python manage.py runserver
    ```

5. **Accede a la aplicación**:
    Abre tu navegador y visita [http://127.0.0.1:8000/](http://127.0.0.1:8000/) para ver la aplicación en acción.

## Contribuciones

¡Las contribuciones son bienvenidas! Si tienes una idea para mejorar el proyecto, abre un *issue* o crea un *pull request*. Asegúrate de seguir las buenas prácticas al hacer contribuciones al código.

## Licencia

Este proyecto está bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles.
