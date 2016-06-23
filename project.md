### 1) Crear en "Sesame" un nuevo repositorio llamado “SocialNetwork”

    - En una ventana del navegador web:

        - Entrar en la página web del cliente "openrdf-workbench" instalado para nuestro servidor "Sesame" local:
            - http://localhost:8080/openrdf-workbench/

        - Pulsar el enlace "New Repository" del menú.

        - En la ventana que se abre:
            - Seleccionar:
                - Type: In Memory Store
                - ID: "SocialNetwork"
                - Title: "..."
            - Pulsar el botón [Next]

        - En la nueva ventana:
            - Seleccionar:
                - Persist: Yes
            - Pulsar el botón [Create]

        - Si todo ha ido bien aparecerá la pantalla con los datos del sumario del nuevo repositorio.

### 2) Añadir el fichero “Entidades.n3” al repositorio “SocialNetwork”

    - En la misma ventana del navegador web anterior:

        - Pulsar en el menú "Repositories"
            - En la pantalla de listado que se abre, seleccionar el repositorio "SocialNetwork".

        - Pulsar en el menú "Modify > Add" y en el nuevo formulario
            - Seleccionar:
                - RDF Data File: ... buscar y seleccionar el fichero "Entities_2v0.n3" proporcionado con el ejercicio ...
                - Data format: N3
            - Pulsar el botón [Upload]

        - Si todo ha ido bien aparecerá la pantalla con los datos del sumario del nuevo repositorio.

### 3) Enriquecer la instancia 2

Para la instancia 2 se procederá a enriquecer la información con información embebida en páginas HTML. Partiendo de la información que se habrá recopilado en el archivo “manuChao.n3”, proceder a volcarlo en el repositorio de SocialNetwork y hacer una query que liste los “MusicRecording”.


    1) Buscar una página web con información de Manu Chao en el sitio web de la BBC:

    - En otra ventana del navegador web:

    	- Entrar en la web de la BBC:
    		- http://www.bbc.com/

    	- Usar el búscador para localizar "Manu Chao":
    		- http://www.bbc.co.uk/search?q=Manu%20Chao

    	- Acceder a la sección de "Music":
    		- http://www.bbc.co.uk/search?q=Manu+Chao&filter=music&suggid=

    	- Seleccionar y cargar la página correspondiente a "Manu Chao":
    		- http://www.bbc.co.uk/music/artists/7570a0dd-5a67-401b-b19a-261eee01a284

    2) Extraer la información de la página web anterior:

    - En otra ventana del navegador web:

    	- Entrar en la web de la herramienta que permite obtener tripletas codificadas en RDFa a patir de una url:
    		- http://www.w3.org/2012/pyRdfa/Overview.html

    	- En el campo "URI" del tab "Distill by URI" poner la url de Manu Chao de la BBC anterior:
    		- http://www.bbc.co.uk/music/artists/7570a0dd-5a67-401b-b19a-261eee01a284

    	- Seleccionar "Output Format: N Triples", pulsar [Go!] y guardar las tripletas encontradas en un archivo:
    		- manuChao.n3

    3) Cargar la información obtenida (fichero "manuChao.n3") en el repositorio “SocialNetwork”:

    - En la ventana del navegador con openrdf-workbench de nuestro servidor local:

        - Pulsar en el menú "Repositories"
            - En la pantalla de listado que se abre, seleccionar el repositorio "SocialNetwork".

        - Pulsar en el menú "Modify > Add" y en el nuevo formulario
            - Seleccionar:
                - RDF Data File: ... buscar y seleccionar el fichero "manuChao.n3" descargado anteriormente...
                - Data format: N3
        - Pulsar el botón [Upload]

    - Si todo ha ido bien aparecerá la pantalla con los datos del sumario del nuevo repositorio.
        - Number of Statements	198
        - Number of Labeled Contexts	2

    B) Consultar información de los "MusicRecording" en el repositorio enriquecido:







