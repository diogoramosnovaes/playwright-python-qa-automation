## How to help in this repository

This repo is a Playwright + Pytest automation framework using a Page Object Model (POM).
Focus on actionable, repository-specific guidance below — follow existing patterns.

- **Big picture:** tests are split under `tests/ui` and `tests/api`. Page objects live in `pages/` and fixtures are defined in `conftest.py`.
- **Key files:** `conftest.py` (fixtures: `browser`, `page`, `api_request_context`), `config.py` (`get_base_url()` / `get_api_url()`), `pages/*` (POM classes), `tests/ui/test_saucedemo.py` (example flows), `.github/workflows/ci.yml` (CI commands).

- **Async patterns:** the test-suite uses async Playwright fixtures and `@pytest.mark.asyncio`. Tests call page-object methods with `await`. Prefer implementing or adapting functions as `async` when they call Playwright async APIs so tests remain consistent with `conftest.py`.

- **Running tests locally:** mirror CI steps from `.github/workflows/ci.yml`:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m playwright install --with-deps
pytest tests/api -q
pytest tests/ui -q
```

- **Useful quick commands:** run a single test:

```bash
pytest tests/ui/test_saucedemo.py::test_login_sucesso -q
```

- **Artifacts & failure handling:** screenshots are saved by the `pytest_runtest_makereport` hook into `screenshots/` on failure. CI also uploads artifacts under `test-results/` (see workflow).

- **API tests:** use the Playwright request fixture `api_request_context` (base URL from `config.get_api_url()`). Look at `tests/api` for examples.

- **Coding conventions & patterns observed:**
  - Page objects instantiate `locator`s in `__init__` and expose small actions (e.g., `login`, `add_product`, `fill_form`). See `pages/login_page.py` and `pages/products_page.py`.
  - Tests expect page-object methods to be awaitable; keep async/await consistent with Playwright's async API.
  - Keep selectors using `data-test` attributes where present (e.g., `[data-test="username"]`). Prefer these stable attributes over fragile CSS paths.

- **When changing tests or page objects:**
  - Run the relevant tests locally and ensure screenshots are produced for failures.
  - Update `requirements.txt` if adding packages and ensure `python -m playwright install` still works.

- **References/examples to inspect when unsure:** `conftest.py`, `pages/login_page.py`, `tests/ui/test_saucedemo.py`, `.github/workflows/ci.yml`, `requirements.txt`, `config.py`.

If anything here is unclear or you want the guidance in Portuguese, tell me which sections to expand or correct.
