# Generador de Presentaciones de IA

El Generador de Presentaciones de IA es una aplicación web que utiliza ChatGPT para crear presentaciones de PowerPoint simples basadas en la entrada del usuario. Los usuarios pueden ingresar una palabra o frase junto con la cantidad deseada de diapositivas, y la aplicación genera las diapositivas de presentación utilizando contenido generado por IA.

## Características

- Genera presentaciones de PowerPoint con contenido generado por IA.
- Número personalizable de diapositivas.
- Interfaz web fácil de usar.

## Cómo funciona

1. Visita el sitio web del Generador de Presentaciones de IA.
2. Ingresa una palabra o frase en el campo de entrada.
3. Especifica la cantidad de diapositivas que deseas en tu presentación.
4. Haz clic en el botón "Generar".
5. El sistema impulsado por IA generará el contenido para la cantidad especificada de diapositivas.
6. Se descargará la presentación de PowerPoint y podrás explorar las diapositivas generadas.

## Tecnologías utilizadas

- Frontend: HTML, CSS, JavaScript
- Backend: Python, Flask
- Modelo de IA: ChatGPT (GPT-3.5 de OpenAI)


## Instalaciónes
# Metodo 1: Clonando el repositorio

Para ejecutar el Generador de Presentaciones de IA localmente, sigue estos pasos:

1. Clona este repositorio: `git clone https://github.com/your-username/ai-presentation-generator.git`
2. Navega hasta el directorio del proyecto: `cd ai-presentation-generator`
3. Instala las dependencias necesarias: `pip install -r requirements.txt`
4. Ejecuta la aplicación: `python app.py`
5. Abre tu navegador web y visita `http://localhost:5000` para acceder a la aplicación.

# Metodo 2: Ejecución con Docker

También puedes ejecutar la aplicación utilizando Docker. Sigue los siguientes pasos:

1. Asegúrate de tener Docker instalado en tu sistema.
2. Ejecuta el siguiente comando en la terminal:

```bash
docker run -p 5000:5000 jorgesotoaudelo/ai_presentation_generator:latest

3. Abre tu navegador web y visita `http://localhost:5000` para acceder a la aplicación.

## Como conseguir tu API KEY

1. Crea una cuenta de OpenAI (Si usas ChatGPT, significa que ya tienes una)
2. [Accede a la pagina de Api Keys de OpenAI aqui](https://platform.openai.com/account/api-keys)
3. Genera tu apikey, copea y pega en la pagina