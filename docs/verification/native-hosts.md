# Native host verification

Date: 2026-09-13 (Asia/Jakarta). Both host adapters were installed into an isolated temporary project from the actual package source. No global rules or skills were installed. All installed Codex skill bytes were compared to source after the runs and matched. The scenario was read-only: no downstream UI application was built.

## Codex CLI 0.147.0

Natural-language invocation completed with exit code 0. The prompt described a vague new operational dashboard and a backend-only logging fix without naming the router. The host read the temporary project's `ui-ux/SKILL.md` and linked discovery/style/prototype/plan instructions. It selected the full UI route for the dashboard, left high-impact product decisions unresolved, and excluded the backend-only task.

Explicit `$ui-ux` invocation also completed with exit code 0 and returned the correct installed path and image/visual approval/HTML/interaction approval/production plan sequence. The host received only a short read-only smoke prompt for this explicit check.

Command shape, run from a temporary installed project (prompts piped through stdin):

```sh
codex exec --ignore-user-config --ignore-rules --ephemeral --skip-git-repo-check --sandbox read-only -C <temporary-project> --json -
```

Exact prompts, observed file-read commands and final answers are retained in [codex-smoke.json](codex-smoke.json). Non-fatal host warnings about the local model cache and PowerShell shell snapshot did not prevent completion. This proves the observed discovery/invocation and decision behavior, not deterministic selection on every future task.

## Claude Code 2.1.263

The native startup `system/init` event reported all six package skills in both its `skills` and `slash_commands` lists. Discovery therefore succeeded in the isolated project. The subsequent API request failed with HTTP 403 / `oauth_org_not_allowed`: the organization has disabled subscription access for Claude Code.

The first explicit `/ui-ux` attempt returned that same access error before model execution. A separate stream-json startup check collected the discovery list; it was not an attempt to bypass the access restriction. No credentials or authentication settings were changed. **Automatic selection and explicit execution in Claude remain unverified.**

Command shape used for the startup evidence:

```sh
claude -p --output-format stream-json --verbose --no-session-persistence --setting-sources project --strict-mcp-config --mcp-config '{"mcpServers":{}}' --tools Read,Skill --allowedTools Read,Skill --permission-mode dontAsk
```

The sanitized discovery/error fields are in [claude-discovery.json](claude-discovery.json). To finish this check later, use an authorized Claude Code account/API setup and rerun the explicit and natural-language smoke prompts from [the test guide](../testing.md). There is no package code change that can resolve an organization access restriction.
