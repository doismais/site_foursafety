# AGENTS.md Lite - Project Workspace Context
## Project Identity: 4safety (NEØ PROTOCOL)

- **Master Workspace**: Refer to [Master AGENTS.md](../../AGENTS.md) for global orchestration and protocols.
- **Safety Standard**: Adhere to the HTML validation and code check rules defined in `scripts/check.sh`.
- **Git Protocol**: Always follow the NΞØ Protocol (Security -> Build -> Conventional Commits -> Push).
- **Core Mission**: Safety and compliance monitoring.

### Dependency Management:
- **Project Structure**: Purely static (HTML/CSS/JS). No local dev dependencies for tools.
- **Vercel CLI**: Always use the **Global CLI** to prevent `tar` and `path-to-regexp` vulnerabilities (which are blocked by pnpm audit).
- **Environment**: Managed via `pnpm` but configured to ignore `EPERM` on global configs when possible.

### Critical Note:
Never modify architectural settings without verifying the Master Orquestrador in the root.
