# Lang Sync – ROADMAP  

*Version: 0.1 – Draft (June 2026)*  

---  

## 📌 Vision  
Provide developers and localization teams with a fast, reliable, and CI‑friendly tool to keep translation files in perfect sync across branches, locales, and repositories.  

---  

## 🚀 MVP (Must‑Have for Launch) – **Critical**  

| # | Feature | Description | Acceptance Criteria |
|---|---------|-------------|----------------------|
| **MVP‑01** | **Core CLI** | `lang-sync` command‑line interface that runs inside any repo. | `lang-sync --help` displays usage; exits with status 0 on success. |
| **MVP‑02** | **Config File (`lang-sync.yml`)** | Declarative config to locate translation roots, supported locales, and file patterns. | Repo contains a valid `lang-sync.yml`; CLI reads it without error. |
| **MVP‑03** | **File‑Format Support (JSON & YAML)** | Parse, merge, and write translation files in JSON and YAML. | `lang-sync sync` correctly updates missing keys in all locales for both formats. |
| **MVP‑04** | **Missing‑Key Detection & Auto‑Placeholder Generation** | Detect keys present in a source locale but absent in others; insert placeholder (`TODO`) entries. | After `lang-sync sync`, every locale file contains all source keys; placeholders are clearly marked. |
| **MVP‑05** | **Git Integration (Add & Commit)** | Stage changed translation files and create a single commit with a conventional message. | Running `lang-sync sync --commit` results in a new commit titled `chore(i18n): sync translations`. |
| **MVP‑06** | **Safety Checks** | Dry‑run mode, conflict detection (local modifications vs. generated changes), and abort on errors. | `lang-sync sync --dry-run` prints a diff without touching the working tree; conflicts abort with a clear message. |
| **MVP‑07** | **CI Compatibility** | Exit codes and minimal output suitable for GitHub Actions / GitLab CI pipelines. | In a CI job, `lang-sync sync --ci` returns non‑zero on failure and prints a concise summary. |
| **MVP‑08** | **Documentation & Quick‑Start Guide** | README section with installation, config example, and typical workflow. | New users can follow the guide and run `lang-sync sync` on a sample repo without errors. |

**MVP Goal:** Ship a stable, single‑binary (or pip‑installable) tool that can be dropped into any repo and keep translation files synchronized with zero‑config defaults. Target release: **End of Q2 2026**.  

---  

## 🌱 Version 1 – “Polish & Extend”  

| Theme | Target Quarter | Features |
|-------|----------------|----------|
| **V1‑01** **Multi‑Format Support** | Q3 2026 | • Add PO/GETTEXT, XLIFF, and Android XML formats.<br>• Auto‑detect format per file path.<br>• Preserve comments and ordering. |
| **V1‑02** **External Translation APIs** | Q3 2026 | • Plug‑in architecture for providers (Google Translate, DeepL, OpenAI).<br>• `--auto-translate` flag to fill placeholders with machine translations.<br>• Configurable quality thresholds. |
| **V1‑03** **Enhanced Reporting** | Q4 2026 | • `lang-sync report` generates markdown/HTML summary (coverage %, missing per locale).<br>• Exportable CSV for analytics. |
| **V1‑04** **CI/CD Integration Packages** | Q4 2026 | • Official GitHub Action (`arkashira/lang-sync-action`).<br>• GitLab CI template.<br>• Environment variable support for secrets (API keys). |
| **V1‑05** **Conflict Resolution UI (CLI)** | Q4 2026 | • Interactive mode to resolve key‑level conflicts (keep, overwrite, skip).<br>• Ability to abort and stage manual fixes. |
| **V1‑06** **Versioned Schema & Migration** | Q4 2026 | • Schema version stored in `lang-sync.yml`.<br>• Migration command to upgrade older translation files. |

**Definition of Done for V1:** All V1 features pass unit‑, integration‑, and end‑to‑end tests; documentation updated; CI templates published; stable release tag `v1.0.0`.  

---  

## 🚀 Version 2 – “Enterprise & Collaboration”  

| Theme | Target Quarter | Features |
|-------|----------------|----------|
| **V2‑01** **Web Dashboard** | Q1 2027 | • Central UI to view translation health across repos.<br>• Pull‑request creation from UI for missing keys.<br>• Role‑based access (viewer, editor, admin). |
| **V2‑02** **Sync Across Multiple Repositories** | Q1 2027 | • Define “translation hub” repo; sync files to/from satellite repos
