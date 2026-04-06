# AGENTS.md Lite - Project Workspace Context
## Project Identity: 4safety (NEØ PROTOCOL)

- **Master Workspace**: Refer to [Master AGENTS.md](../../AGENTS.md) for global orchestration and protocols.
- **Safety Standard**: Adhere to the HTML validation and code check rules defined in `scripts/check.sh`.
- **Git Protocol**: Always follow the NΞØ Protocol (Audit -> Validation -> Commit -> Push when explicitly authorized).
- **Core Mission**: Safety and compliance monitoring.

### Dependency Management:
- **Project Structure**: Static-first site (HTML/CSS/JS) with lightweight Node tooling for validation and local automation.
- **Node Tooling**: `pnpm` is used for install, audit and HTMLHint execution. There is no frontend bundler or framework runtime in this repo.
- **Vercel CLI**: Prefer the global CLI when deployment or linking is required.

### Critical Note:
Never modify architectural settings without verifying the Master Orquestrador in the root.
