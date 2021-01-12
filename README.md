# Respuestas 2 y 3


## Instalacion
1. Clonado:

   
    `git clone https://github.com/mangelrivasm/Codigorespuestas2-3.git`
    
    
2. Crear Entorno Virtual (Recommended)<br/> 
    - `pip install virtualenv`
    - `virtualenv .venv`  
    
3. Activar entorno virtual
    - `source .venv/bin/activate`

4. Instalar dependencias
    - `pip install -r requirements.txt`

5. Intalar Chrome Web Driver
    - `wget https://chromedriver.storage.googleapis.com/x.xx/chromedriver_linux64.zip` <br>
    Controlador de Chrome reciente on https://sites.google.com/a/chromium.org/chromedriver/downloads <br /> <br />
    Incluirlo en el path del sistema

## Correr respuesta de instagram
1. Incluir en el codigo fuente de scraper.py, el usuario y la contrasena
	- `Linea 29 usuario, Linea 31 password`
2. Guardar
3. Ejecutar
    - `python scraper.py`

## Correr respuesta de Facebook

1. Ejecutar
    - `python facebookMark.py user password link` 

## License
This project is under the [MIT License](https://github.com/AgiMaulana/instagram-comments-scraper/blob/master/LICENSE.md)
