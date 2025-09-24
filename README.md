# Web Scraping en Python: Tres formas diferentes

Este proyecto muestra cómo hacer **web scraping** en Python utilizando tres métodos distintos: Requests, Beautiful Soup y Playwright.

## 1. Requests

**Ventajas:**
- Muy rápido
- Muy sencillo de implementar

**Desventajas:**
- No permite saltarse paywalls ni captchas
- Solo agarra el HTML crudo del DOM
- Muy manual para filtrar lo que buscamos (uso de regex)

---

## 2. Beautiful Soup

**Ventajas:**
- Rápido
- Extremadamente sencillo de implementar
- Fácil encontrar elementos, atributos y filtrar
- Se puede usar regex para una limpieza de los datos

**Desventajas:**
- Igual que Requests: no se pueden saltar paywalls ni captchas
- No permite seguir el flujo de URLs, al ser estático

---

## 3. Playwright

**Ventajas:**
- Permite simular un usuario end-to-end
- Capturas de pantalla
- Carga el JS de la página
- Dinámico
- Funciona con SPAs
- Posible saltarse paywalls o captchas

**Desventajas:**
- Más lento que los métodos estáticos

---

## Requisitos / Dependencias

Para instalar dependencias, se utilizó **uv** como gestor de paquetes:
```bash
uv init name_your_project
```
Puedes hacer Fork o clonar el proyecto
```bash
git clone https://github.com/ycaballero12315/scrapping-requests-amazon.git
```
```bash
uv install playwright beautifulsoup4 requests
uv install asyncio  # para la versión asíncrona de Playwright, debes instalarlo porque Playwright es asincrono
