# Sistema experto de recomendación de herramientas de inteligencia artificial

## Descripción
Sistema que permite a los usuarios obtener recomendaciones de herramientas de inteligencia artificial que se ajusten a sus necesidades. Cuenta con un motor de inferencia que permite obtener recomendaciones de herramientas de inteligencia artificial basadas en las respuestas proporcionadas por el usuario.

## Tecnologías

- Frontend desarrollado en React.js 18.2.0
- Backend desarrollado en FastAPI 0.110.0
- Web scraping con BeautifulSoup 4.12.3 y extraído desde [aifindy](https://aifindy.com/)

## Instalación
### Frontend
```
cd frontend
npm install
npm run dev
```
### Backend
```
python -m .venv venv
.venv\Scripts\activate
pip install -r requirements.txt
cd backend
uvicorn main:app --reload
```

### Requisitos
- Python 3.12
- Node.js 20.11.1
- npm 10.2.4

## Uso
1. Ingresar a la [aplicación web](http://localhost:5173/)
2. Responder las preguntas que se presentan
3. Obtener las recomendaciones de herramientas de inteligencia artificial