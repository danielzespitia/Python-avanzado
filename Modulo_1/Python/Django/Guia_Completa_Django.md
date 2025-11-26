# Guía Completa y Detallada de Django

## 1. ¿Qué es Django?

Django es un framework web de alto nivel escrito en Python que fomenta el desarrollo rápido y el diseño limpio y pragmático. Fue creado originalmente para gestionar sitios web de noticias de alto tráfico (como el Lawrence Journal-World) y fue liberado como código abierto en 2005.

Su filosofía principal es **"Don't Repeat Yourself" (DRY)**, que significa evitar la duplicación de código y patrones. Django se encarga de gran parte de la complejidad del desarrollo web, permitiéndote concentrarte en escribir tu aplicación sin tener que reinventar la rueda.

### Filosofía "Baterías Incluidas"

Django se describe a menudo como un framework con "baterías incluidas". Esto significa que viene con una amplia gama de funcionalidades integradas que los desarrolladores web necesitan comúnmente, como:

- Autenticación de usuarios.
- Panel de administración.
- Mapas del sitio (Sitemaps).
- RSS Feeds.
- Manejo de formularios.
- Seguridad contra ataques comunes (SQL Injection, XSS, CSRF).

## 2. ¿Para qué sirve Django?

Django es extremadamente versátil y se utiliza para construir todo tipo de sitios web, desde simples blogs hasta complejas aplicaciones empresariales. Es ideal para:

1. **Sistemas de Gestión de Contenidos (CMS):** Gracias a su potente panel de administración automático.
2. **Redes Sociales y Plataformas de Comunicación:** Maneja bien grandes volúmenes de datos y usuarios.
3. **Sitios de Comercio Electrónico:** Su seguridad y manejo de bases de datos lo hacen robusto para transacciones.
4. **APIs RESTful:** Con el complemento _Django REST Framework_, es uno de los estándares de la industria para crear backends de aplicaciones móviles y SPAs (Single Page Applications).
5. **Plataformas de Computación Científica:** Al ser Python, se integra nativamente con bibliotecas como NumPy, Pandas y Scikit-learn.

**Empresas que usan Django:** Instagram, Pinterest, Mozilla, Spotify, National Geographic.

## 3. Arquitectura MVT (Modelo-Vista-Template)

A diferencia del patrón MVC (Modelo-Vista-Controlador) tradicional, Django utiliza una variación llamada **MVT**.

### M (Modelo - Model)

Es la capa de acceso a datos. Define la estructura de la base de datos.

- En Django, un modelo es una clase de Python que representa una tabla en la base de datos.
- Django incluye un **ORM (Object-Relational Mapper)** que te permite interactuar con la base de datos usando código Python en lugar de escribir SQL.

### V (Vista - View)

Es la capa de lógica de negocio.

- Una "Vista" en Django es una función o clase que recibe una petición web (Request) y devuelve una respuesta (Response).
- Aquí es donde procesas los datos, aplicas filtros, validas permisos y decides qué plantilla mostrar.
- _Nota: Esto suele confundir a los que vienen de MVC, ya que la "Vista" de Django hace el trabajo del "Controlador" en MVC._

### T (Template - Plantilla)

Es la capa de presentación.

- Define cómo se muestran los datos al usuario (HTML, CSS).
- Django tiene su propio lenguaje de plantillas (DTL) que permite insertar lógica básica (bucles, condicionales) dentro del HTML para mostrar datos dinámicos.

## 4. Flujo de una Petición en Django

1. **URL Dispatcher (urls.py):** El usuario entra a una URL (ej. `/blog/articulo/1`). Django busca en su lista de patrones de URL para ver cuál coincide.
2. **View (views.py):** Si encuentra coincidencia, llama a la función de la Vista asociada.
3. **Model (models.py):** La Vista puede consultar el Modelo para obtener datos de la base de datos (ej. "Dame el artículo con ID 1").
4. **Template (templates/\*.html):** La Vista pasa los datos a una Plantilla HTML.
5. **Response:** Django renderiza el HTML final y lo envía de vuelta al navegador del usuario.

## 5. Estructura de Archivos Típica

Cuando creas un proyecto (`django-admin startproject mi_proyecto`), obtienes:

- **manage.py:** Una utilidad de línea de comandos para interactuar con el proyecto (correr el servidor, crear migraciones, etc.).
