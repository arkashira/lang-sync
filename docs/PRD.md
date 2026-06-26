# Product Requirements Document – Lang Sync

---

## 1. Problem Statement

Software projects that support multiple locales often store translated assets (JSON, YAML, PO, XLIFF, etc.) alongside source code in a Git repository.  
Typical pain points:

| Pain | Impact |
|------|--------|
| **Manual sync** – Translators must copy files into the repo, merge conflicts arise, and version history is lost. | Delays releases, increases QA effort. |
| **Inconsistent naming & structure** – Different teams use different folder layouts or file prefixes, causing confusion. | Hard to discover translations, increases onboarding time. |
| **Missing translations** – No automated way to detect untranslated strings or stale keys. | Poor user experience, higher support tickets. |
| **Security & compliance** – Sensitive strings may be accidentally committed or exposed. | Risk of data leaks, regulatory violations. |

> **Bottom line:** Developers and localization teams need a single, automated, Git‑centric workflow that guarantees consistency, traceability, and minimal friction.

---

## 2. Target Users

| Persona | Role | Pain Points | How Lang Sync Helps |
|---------|------|-------------|---------------------|
| **DevOps / Release Engineer** | Maintains repo structure | Manual merge conflicts, time‑consuming release prep | Automated pull‑requests, conflict detection |
| **Localization Engineer** | Manages translation files | Inconsistent file formats, missing keys | Validation, linting, auto‑generation |
| **Product Manager** | Tracks feature readiness | Uncertain translation coverage | Coverage dashboards, alerts |
| **QA Engineer** | Tests UI in multiple locales | Manual verification, flaky tests | Automated diff checks, CI integration |

---

## 3. Goals & Success Metrics

| Goal | Success Metric | Target |
|------|----------------|--------|
| **Reduce merge conflicts** | % of PRs with translation conflicts | < 5 % |
| **Improve translation coverage** | % of UI strings translated | ≥ 95 % |
| **Speed up release cycle** | Avg. time from PR merge to release | ≤ 2 days |
| **Ensure compliance** | Number of accidental commits of sensitive strings | 0 |
| **Increase developer satisfaction** | NPS for localization workflow | ≥ 8/10 |

---

## 4. Key Features (Prioritized)

| # | Feature | Description | Priority |
|---|---------|-------------|----------|
| 1 | **Git‑Based Sync CLI** | `lang-sync sync` pulls latest translations, merges changes, and pushes a PR with diff. Supports multiple file formats (JSON, YAML, PO, XLIFF). | Must‑Have |
| 2 | **Schema Validation** | Enforces consistent folder layout (`/locales/<lang>/`, file naming convention). Lints for missing keys, duplicate entries, and invalid JSON/YAML. | Must‑Have |
| 3 | **Coverage Dashboard** | Web UI (or CLI output) showing translation coverage per locale, per file, and per feature flag. | Must‑Have |
| 4 | **Auto‑Generation of Missing Keys** | Detects new source strings, auto‑creates empty entries in all locales with placeholders. | Must‑Have |
| 5 | **Conflict Resolver** | Interactive CLI tool that highlights conflicts and suggests merge strategies (keep source, keep translation, manual edit). | Should‑Have |
| 6 | **Sensitive String Masking** | Configurable regex to detect and redact sensitive data before commit. | Should‑Have |
| 7 | **CI/CD Integration** | GitHub Actions template that runs `lang-sync` on push, fails build on validation errors. | Should‑Have |
| 8 | **Localization API** | REST/GraphQL endpoint to fetch translations at runtime, with caching. | Nice‑To‑Have |
| 9 | **Plugin System** | Allow custom format adapters (e.g., Android XML, iOS Strings). | Nice‑To‑Have |
| 10 | **Analytics & Alerts** | Slack/Email notifications for low coverage or failed syncs. | Nice‑To‑Have |

---

## 5. Scope

### In‑Scope

- CLI tool (`lang-sync`) with subcommands: `sync`, `lint`, `coverage`, `conflict`.
- Support for JSON, YAML, PO, XLIFF (v2) files.
- GitHub Actions workflow template.
- Basic web dashboard (React + Node) for coverage.
- Documentation (README, usage guide, contribution guide).
- Unit & integration tests covering 90 % of core logic.

### Out‑of‑Scope

- Native integration with external LSPs or IDEs.
- Full‑blown translation memory or CAT tool.
- Real‑time translation API (beyond the optional API endpoint).
- Mobile app or desktop GUI.

---

## 6. Technical Constraints & Decisions

| Decision | Rationale |
|----------|-----------|
| **Language**: Rust (CLI) + TypeScript (Dashboard) | Rust gives fast, safe CLI; TypeScript ensures maintainable web UI. |
| **Version Control**: Git | Existing repo structure; no need for alternative VCS. |
| **File Formats**: JSON, YAML, PO, XLIFF | Most common in open‑source and enterprise. |
| **CI Platform**: GitHub Actions | Highest adoption; easy to ship template. |
| **Data Storage**: Local file system + SQLite for metadata | No external DB needed for small to medium repos. |

---

## 7. Dependencies

- **Git** (native CLI)
- **Node.js** (≥ 18) for dashboard
- **Rust** (≥ 1.70) for CLI
- **Python** (optional) for helper scripts
- **OpenAPI** for optional API

---

## 8. Milestones

| Milestone | Deliverable | Target Date |
|-----------|-------------|-------------|
| 1 | CLI core (`sync`, `lint`) + basic tests | 2026‑07‑15 |
| 2 | Coverage dashboard + CI template | 2026‑08‑01 |
| 3 | Conflict resolver + masking | 2026‑08‑20 |
| 4 | Documentation + example repo | 2026‑09‑01 |
| 5 | Beta release & community feedback | 2026‑09‑15 |

---

## 9. Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| **Complex merge conflicts** | High | Provide interactive resolver, fallback to manual PR review. |
| **Format drift** | Medium | Strict schema validation, auto‑format on commit. |
| **Performance on large repos** | Medium | Lazy loading, incremental sync, benchmark tests. |
| **Security of sensitive strings** | High | Regex masking, audit logs, optional encryption. |

---

## 10. Success Criteria

- 90 % of participating projects adopt `lang-sync` in CI.
- 95 % reduction in translation‑related PR conflicts within 3 months.
- Positive NPS (> 8) from localization engineers after 6 months.

---

## 11. Appendices

### 11.1 Example Workflow

```bash
# Pull latest translations and create PR
lang-sync sync

# Lint all translation files
lang-sync lint

# View coverage report
lang-sync coverage
```

### 11.2 Contribution Guidelines

- Follow Rust style guidelines (rustfmt, clippy).
- Write tests for every new feature.
- Submit PRs to `main` branch; CI must pass.

---

**Prepared by:**  
Senior Product/Engineering Lead – Axentx  
Date: 2026‑06‑26

---
