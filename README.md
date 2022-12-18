[![Build Status](https://travis-ci.com/wadobo/decide.svg?branch=master)](https://travis-ci.com/wadobo/decide) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/94a85eaa0e974c71af6899ea3b0d27e0)](https://www.codacy.com/app/Wadobo/decide?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=wadobo/decide&amp;utm_campaign=Badge_Grade) [![Codacy Badge](https://api.codacy.com/project/badge/Coverage/94a85eaa0e974c71af6899ea3b0d27e0)](https://www.codacy.com/app/Wadobo/decide?utm_source=github.com&utm_medium=referral&utm_content=wadobo/decide&utm_campaign=Badge_Coverage)


DECIDE-SINGLE-SALARES-1
===========================

Integrantes del grupo
-------------------------
* García Quijada, José Mª
* Gaviro Martínez, Miguel
* Graván Bru, Víctor
* Moreno Dominguez, Eloy
* Stefan, Bodgan Marian
* Zuleta de Reales Toro, Santiago

Plataforma voto electrónico educativa
----------------------------------

El objetivo de este proyecto es implementar una plataforma de voto
electrónico seguro, que cumpla una serie de garantías básicas, como la
anonimicidad y el secreto del voto.

Se trata de un proyecto educativo, pensado para el estudio de sistemas de
votación, por lo que prima la simplicidad por encima de la eficiencia
cuando sea posible. Por lo tanto se asumen algunas carencias para permitir
que sea entendible y extensible.


Subsistemas, apps y proyecto base
---------------------------------

El proyecto se divide en subsistemas, los cuales estarán desacoplados
entre ellos. Para conseguir esto, los subsistemas se conectarán entre si mediante API y necesitamos un proyecto base donde configurar las ruts de estas API.

Este proyecto Django estará dividido en apps (subsistemas y proyecto base), donde cualquier app podrá ser reemplazada individualmente.

Subsistemas implementados
---------------------------------

Para cumplir el objetivo de mejorar el proyecto base Decide, hemos contribuido a él complementándolo con los siguientes subsistemas del ámbito visual:
* **Visualización de resultados:** Este subsistema se basa en la creación de gráficos asociados a los resultados de las votaciones, para ello hemos cumplido los diferentes incrementos. 
    * Pintado de gráficas y estudio de datos. **(Eloy Moreno)**
    * Mostrar información relevante en tiempo real, como el número de
        votos, porcentaje del censo, estadísticas de votantes, según
         perfiles, etc. **(Bogdan Marian y Víctor Graván)**
    * Implementar visualizaciones para la plataforma de Telegram a través de un bot. **(Eloy Moreno)**

* **Traducciones:** Como su nombre indica, aquí se trata de traducir las diferentes vistas de la aplicación a diferentes idiomas. En nuestro caso, hemos traducido la interfaz a los idiomas inglés y alemán, además de al español claro. Sus incrementos on los siguientes.
    * Hacer la interfaz traducible. **(Santiago Zuleta de Reales y Miguel Gaviro)**
    * Traducir la interfaz al español. **(Santiago Zuleta de Reales y Miguel Gaviro)**
    * Traducir la interfaz a otros idiomas. **(Santiago Zuleta de Reales y Miguel Gaviro)**

* **Diseño y usabilidad**: Finalmente, hemos implementado una mejora en el diseño y la interfaz a través de elementos JavaScript y Css para ampliar el uso de la página a personas con diferentes problemas de salud. En este caso nos hemos centrado en problemas de visión implementando una sección de accesibilidad donde se pueden ajustar los diferentes filtros de luz (modo noche, escala de grises y alto contraste) además de una personalización completa de tamaño de fuente e interlineado. Los subsistemas que lo componen son.
    * Estudiar la usabilidad y definir una nueva interfaz usable, con
  componentes css. **(José Mª García)**
    * Hacer la interfaz responsive, para que funcione en móviles. **(José Mª García)**
    * Estudiar la accesibilidad de la interfaz y hacerla accesible. **(José Mª García)**

Configurar y ejecutar el proyecto
---------------------------------

Para configurar el proyecto, podremos crearnos un fichero local_settings.py basado en el
local_settings.example.py, donde podremos configurar la ruta de nuestras apps o escoger que módulos
ejecutar.

Una vez hecho esto, será necesario instalar las dependencias del proyecto, las cuales están en el
fichero requirements.txt:

    pip install -r requirements.txt

Tras esto tendremos que crearnos nuestra base de datos con postgres:

    sudo su - postgres
    psql -c "create user decide with password 'decide'"
    psql -c "create database decide owner decide"

Entramos en la carpeta del proyecto (cd decide) y realizamos la primera migración para preparar la
base de datos que utilizaremos:

    ./manage.py migrate

Por último, ya podremos ejecutar el módulos o módulos seleccionados en la configuración de la
siguiente manera:

    ./manage.py runserver



Ejecutar con vagrant 
------------------------------

Existe una configuración de vagrant que crea una máquina virtual con todo
lo necesario instalado y listo para funcionar. La configuración está en
vagrant/Vagrantfile y por defecto utiliza Virtualbox, por lo que para
que esto funcione debes tener instalado en tu sistema vagrant y Virtualbox.

Crear la máquina virtual con vagrant:

    $ cd vagrant
    $ vagrant up

Una vez creada podremos acceder a la web, con el usuario admin/admin:

http://localhost:8080/admin

Acceder por ssh a la máquina:

    $ vagrant ssh

Esto nos dará una consola con el usuario vagrant, que tiene permisos de
sudo, por lo que podremos acceder al usuario administrador con:

    $ sudo su

Parar la máquina virtual:

    $ vagrant stop

Una vez parada la máquina podemos volver a lanzarla con `vagrant up`.

Eliminar la máquina virtual:

    $ vagrant destroy


