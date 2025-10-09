# qa-ui-smoke-shop

Suite de **pruebas automatizadas (UI + API)** para un e‑commerce ficticio. Proyecto pensado para portfolio: simple, claro y con CI/CD.

> **Tecnologías**: Python · Pytest · Playwright · Requests · Pytest‑html (o Allure) · GitHub Actions · Docker (opcional) · MySQL (opcional)

---

## 🎯 Objetivos del proyecto
- Practicar automatización **UI** con Page Object Model (POM).
- Agregar **tests de API** sencillos para validar flujos clave.
- Ejecutar la suite en **CI/CD (GitHub Actions)** y publicar reportes.
- Opcional: validar datos en **BD** y contenedores **Docker**.

---

## 🧱 Estructura sugerida
```
qa-ui-smoke-shop/
├─ src/
│  ├─ pages/              # Page Objects (HomePage, LoginPage, ProductPage, CartPage)
│  ├─ components/         # Elementos reutilizables (headers, modales)
│  └─ api/                # Clientes API simples (auth, products, cart)
├─ tests/
│  ├─ ui/                 # Tests de interfaz (smoke + regression)
│  └─ api/                # Tests de API (smoke)
├─ data/                  # Datos de prueba (CSV/JSON)
├─ reports/               # Reportes generados por CI
├─ conftest.py            # Fixtures (browser, base_url, usuarios, etc.)
├─ requirements.txt
├─ pytest.ini
├─ README.md
└─ .gitignore
```

---

## 🚀 Puesta en marcha (local)

### 1) Requisitos
- Python 3.10+
- Git
- (Opcional) Docker

### 2) Crear entorno e instalar dependencias
```bash
python -m venv .venv
# Windows:
.\.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

pip install -r requirements.txt

# Instalar navegadores de Playwright
python -m playwright install
```

### 3) Variables de entorno (opcional)
Crea un archivo `.env` o exporta variables:
```
BASE_URL=https://www.saucedemo.com  # o tu sitio demo
USER_STD=standard_user
PASS_STD=secret_sauce
```

### 4) Correr tests
```bash
# UI
pytest -m ui --maxfail=1 -q

# API
pytest -m api -q

# Con reporte HTML (pytest-html)
pytest --html=reports/report.html --self-contained-html -q
```

> **Tip:** Para Allure, reemplazar por: `pytest --alluredir=reports/allure && allure serve reports/allure`

---

## 🧪 Alcance mínimo (Smoke UI)
1. Login válido/ inválido
2. Búsqueda / listado de productos
3. Agregar 1–2 productos al carrito
4. Verificar carrito y precios
5. Logout

**API Smoke**: `GET /products`, `POST /login`, `POST /cart` (mock o endpoint público de prueba).

---

## 🧩 Buenas prácticas clave
- **POM** para separar lógica de UI.
- **Datos desacoplados** en `data/` (CSV/JSON).
- **Fixtures reutilizables** en `conftest.py`.
- **Asserts claros y mensajes útiles**.
- **Linting** (opcional: `ruff` o `flake8`).

---

## 🔁 CI/CD con GitHub Actions (pipeline ejemplo)
Agrega `.github/workflows/tests.yml` con contenido similar:
```yaml
name: tests
on:
  push:
  pull_request:

jobs:
  ui-api-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - name: Install deps
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      - name: Install browsers
        run: python -m playwright install --with-deps
      - name: Run tests (HTML report)
        run: pytest --html=reports/report.html --self-contained-html -q
      - name: Upload report
        uses: actions/upload-artifact@v4
        with:
          name: html-report
          path: reports/report.html
```

---

## 🧰 requirements.txt (sugerido)
```
pytest>=8.0.0
playwright>=1.46.0
pytest-html>=4.1.1
python-dotenv>=1.0.1
requests>=2.32.0
# opcional
# allure-pytest>=2.13.5
# ruff>=0.6.0
```

---

## ✅ Criterios de aceptación (MVP)
- [ ] 5–10 tests UI (smoke) estables.
- [ ] 3–5 tests API.
- [ ] POM implementado.
- [ ] Pipeline en GitHub Actions que suba el reporte como artefacto.
- [ ] README con pasos claros para ejecutar.

---

## 📊 Métricas útiles
- Tiempo total de suite (objetivo < 3 min smoke).
- % de tests flakey (objetivo ~0% en smoke).
- Cobertura de flujos críticos (login, carrito, logout).

---

## 🧭 Roadmap corto
- v0.1: Smoke UI + API + pipeline CI (este repo).
- v0.2: Datos en BD + Docker compose.
- v0.3: Allure + dashboards rápidos (history, trends).
- v1.0: Suite estable + documentación completa + demo grabada.