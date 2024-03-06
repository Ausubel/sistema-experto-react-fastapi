# Sistema experto de recomendación de herramientas de inteligencia artificial

## Descripción
Sistema que permite a los usuarios obtener recomendaciones de herramientas de inteligencia artificial que se ajusten a sus necesidades. Cuenta con un motor de inferencia que permite obtener recomendaciones de herramientas de inteligencia artificial basadas en las respuestas proporcionadas por el usuario.

- Frontend desarrollado en React.js 18.2.0
- Backend desarrollado en FastAPI 0.110.0
- Web scraping para obtener información de las herramientas de inteligencia artificial desde: [https://aifindy.com/](aifindy.com)

## Instalación
### Frontend
1. Instalar dependencias
```bash
npm install
```
2. Iniciar el servidor
```bash
npm dev
```
### Backend
1. Crear un entorno virtual
```bash
python -m .venv venv
```
2. Activar el entorno virtual
#### Linux
```bash
source .venv/bin/activate
```
#### Windows
```bash
.venv\Scripts\activate
```
3. Instalar dependencias
```bash
pip install -r requirements.txt
```
4. Iniciar el servidor
```bash
uvicorn main:app --reload
```

### Requisitos
- Python 3.12
- Node.js 20.11.1
- npm 10.2.4

## Uso
1. Ingresar a la aplicación web
2. Responder las preguntas que se presentan
3. Obtener las recomendaciones de herramientas de inteligencia artificial