```markdown
# TECH SPEC: Lang Sync

## Overview

**Lang Sync** is a tool designed to manage translated files within a version-controlled repository. It ensures consistency, synchronization, and proper handling of localization assets across different languages and branches. This tool integrates seamlessly with Git workflows and supports automated synchronization of translation files while maintaining version control integrity.

---

## Architecture Overview

The architecture of Lang Sync is modular and follows a client-server pattern where:

- **Client**: The CLI tool used by developers to interact with the system.
- **Server**: A lightweight service that handles coordination between Git repositories and translation file management.
- **Git Integration Layer**: Manages interactions with Git repositories including cloning, committing, pushing, and pulling changes.
- **Translation File Manager**: Parses, validates, and synchronizes translation files across languages.
- **Configuration Engine**: Reads configuration from `.langs.yml` or similar files to define sync rules and policies.

### High-Level Flow

1. User triggers Lang Sync via CLI (`lang-sync sync`).
2. CLI communicates with the Lang Sync server over HTTP/JSON.
3. Server fetches latest translations from configured sources.
4. Translation files are parsed and validated against schema.
5. Conflicts are detected and resolved based on policy.
6. Updated files are committed and pushed back to the Git repository.

---

## Components

| Component | Description |
|----------|-------------|
| **CLI Tool** | Command-line interface for triggering sync operations. |
| **Core Service** | RESTful API backend responsible for coordinating sync logic. |
| **Git Adapter** | Wrapper around Git commands to handle repository operations. |
| **Translation Parser** | Parses various formats (e.g., JSON, YAML, PO) into internal structures. |
| **Conflict Resolver** | Detects and resolves merge conflicts during sync. |
| **Validator** | Ensures translation files conform to expected schemas. |
| **Config Loader** | Loads configuration from `.langs.yml` or environment variables. |

---

## Data Model

### Translation Entry

Each translation entry represents a single localized string.

```json
{
  "key": "greeting.hello",
  "source": "Hello",
  "translations": {
    "en": "Hello",
    "fr": "Bonjour",
    "de": "Hallo"
  },
  "last_modified": "2025-04-05T14:30:00Z"
}
```

### Repository State

Represents the current state of the repository including tracked files and metadata.

```json
{
  "repo_path": "/path/to/repo",
  "branch": "main",
  "files": [
    {
      "path": "locales/en.json",
      "sha": "abc123def456...",
      "modified_at": "2025-04-05T14:30:00Z"
    }
  ]
}
```

### Sync Configuration

Configuration defines how Lang Sync should operate.

```yaml
# .langs.yml
sync_rules:
  - source_format: json
    target_formats:
      - json
      - yaml
    locales:
      - en
      - fr
      - de
    output_dir: ./locales
    conflict_resolution: 'keep_newest'
```

---

## Key APIs / Interfaces

### Core Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST   | `/api/v1/sync` | Initiates a synchronization process. |
| GET    | `/api/v1/status` | Returns the status of the last sync operation. |
| POST   | `/api/v1/validate` | Validates a set of translation files. |
| GET    | `/api/v1/config` | Retrieves current configuration settings. |

### CLI Interface

```bash
lang-sync sync --config-path .langs.yml --dry-run
lang-sync validate --input-file ./locales/en.json
lang-sync status
```

---

## Tech Stack

| Category | Technology |
|---------|------------|
| Language | Go (for performance and concurrency) |
| Web Framework | Gin |
| ORM | GORM |
| Git Integration | libgit2 (via go-git) |
| Configuration | Viper |
| Testing | testify, ginkgo |
| Logging | Zap |
| CI/CD | GitHub Actions |
| Deployment | Docker, Helm Charts |

---

## Dependencies

### External Libraries

| Library | Purpose |
|--------|---------|
| [go-git](https://github.com/go-git/go-git) | Git operations |
| [viper](https://github.com/spf13/viper) | Configuration management |
| [zap](https://github.com/uber-go/zap) | Structured logging |
| [gin](https://github.com/gin-gonic/gin) | Web framework |
| [gorm](https://github.com/go-gorm/gorm) | ORM for database interaction |
| [testify](https://github.com/stretchr/testify) | Testing utilities |

### Internal Modules

| Module | Description |
|--------|-------------|
| `pkg/git` | Git interaction layer |
| `pkg/parser` | Translation file parsing logic |
| `pkg/validator` | Validation rules enforcement |
| `pkg/conflict` | Conflict resolution strategies |
| `cmd/lang-sync` | CLI entrypoint |

---

## Deployment

### Containerization

Lang Sync will be containerized using Docker. The image will include:

- Built binary
- Required runtime libraries
- Default configuration file

Example Dockerfile:

```dockerfile
FROM alpine:latest
RUN apk add --no-cache ca-certificates
WORKDIR /app
COPY lang-sync .
COPY .langs.yml .
CMD ["./lang-sync"]
```

### Kubernetes Deployment

For production environments, Lang Sync can be deployed using Helm charts:

```yaml
# values.yaml
replicaCount: 1
image:
  repository: ghcr.io/arkashira/lang-sync
  tag: latest
service:
  type: ClusterIP
  port: 8080
```

---

## Security Considerations

- All communication between CLI and server must be secured using TLS.
- Secrets (like tokens) should be stored securely using Kubernetes secrets or equivalent.
- Input validation prevents injection attacks.
- Access controls may be added in future versions to restrict who can trigger syncs.

---

## Future Enhancements

- Support for more translation formats (e.g., XLIFF, Android strings).
- Web UI for monitoring and managing sync jobs.
- Integration with translation platforms like Crowdin or Transifex.
- Automated pull request creation for sync updates.
```
