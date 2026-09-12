# Installer development evidence

Date: 2026-09-13. Runtime: Python 3.14.7 on Windows. Implementation uses Python standard library APIs compatible with Python 3.10+; other runtime/OS combinations were not executed here.

All installation targets were disposable temporary directories. User-scope tests override the home directory and `CODEX_HOME`; no real global skill installation was performed. The source fixture contains all six skill names, references, Codex metadata, rules, and a version file.

## Observed RED → GREEN cycles

Each row records an actual run of `rtk proxy python -m unittest discover -s tests -p test_install.py -v` before and after its implementation, except the final focused RED used the additional filter `-k ascii_console`. Counts include previous regression tests; routing subtests appear as several failures within one test method.

| Behavior added | Observed RED | Observed GREEN |
|---|---|---|
| First project Codex installation | 1 test, 1 failure: `The standalone installer has not been implemented` | 1 test, OK |
| User/project and Codex/Claude/both routing; existing rules preserved | 2 tests, 6 subtest failures: missing rules or wrong platform destination | 2 tests, OK |
| Read-only dry run | 4 tests, 2 subtest failures: destination snapshot changed | 4 tests, OK |
| Idempotent reinstall and existing Claude import | 5 tests, 1 failure: existing `CLAUDE.md` was changed | 5 tests, OK |
| Versioned ownership and conflict preflight | 8 tests, 3 failures: missing manifest or changed/unowned files overwritten | 8 tests, OK |
| Safe upgrades and stale owned files | 10 tests, 2 failures: missing removal plan and edited stale file accepted | 10 tests, OK |
| Reject traversal in an ownership manifest | 11 tests, 1 failure: hostile manifest installation returned success | 11 tests, OK |
| Reject destination junction escape and incomplete six-skill source | 13 tests, 2 failures: unsafe/incomplete installation returned success | 13 tests, OK |
| Reject invalid version without echoing source content | 14 tests, 1 failure: invalid version installation returned success | 14 tests, OK |
| Report missing source metadata before mutation | 15 tests, 1 failure: missing VERSION raised an OS exception | 15 tests, OK |
| Distinguish active Claude imports from fenced/inline examples | 17 tests, 2 failures: example suppressed import; prose import was duplicated | 17 tests, OK |
| Review regressions: relocatable projects and coordinated shared-rule upgrades | 20 tests, 3 failures: renamed project rejected; partial project upgrade and newer second platform accepted | 20 tests, OK |
| Native CLI with a non-Latin path and ASCII console | 1 focused test, 1 failure: subprocess traceback raised `UnicodeEncodeError` while printing a dry-run destination | 21 tests, OK |

The final run completed 21 tests in 2.687 seconds with `OK`, including an actual Windows directory-junction fixture (not skipped). Test assertions also cover mandatory CLI arguments and invalid choices, Unicode/space paths, CRLF and unmanaged byte preservation, unchanged modification times on reinstall, custom `CODEX_HOME`, Codex-only metadata, no writes during conflicting dry runs, unrelated-file preservation, unselected-platform preservation during user-scope upgrade, and no secret file contents in conflict output. A native subprocess test sets `PYTHONIOENCODING=ascii` and uses a Chinese project-directory name, verifying both dry-run output and conflict output without console encoding crashes.

## Implementation decisions

- One manifest at `<project-or-home>/.ui-ux-workflow/install.json` tracks per-platform versions, known root locations, SHA-256 hashes of owned files, and hashes of managed blocks only. File contents are not stored in this manifest.
- All source checks, destination checks, ownership checks, and stale-file checks finish before the first write or removal. Dry run performs the same checks without creating directories or changing the manifest.
- Existing unowned files and managed blocks are conflicts, even if their contents happen to match. Edited or deleted owned files/blocks are also conflicts. Resolve the customization explicitly; there is no force-overwrite option.
- Existing unmanaged bytes remain intact. Existing active project Claude imports are reused. Codex metadata is omitted from the Claude destination.
- Upgrades remove only unchanged stale files recorded in the manifest for the selected platform. Unrelated files and empty directories remain. User-scope installations have separate rules, so other installed platforms retain their versions and owned files.
- Project platforms share `AGENTS.md`. If the resulting project installation has both platforms and its installed version differs from the source package, a partial upgrade is rejected before mutation with instructions to use `--platform both`. This also covers adding a second platform from a different package version.
- Manifest paths are restricted to the six named skill trees and fixed rule destinations. Project roots are stored relative to the checkout, making copied/renamed projects portable; destinations are always derived from allowlisted mappings, never from manifest root strings. User-scope roots retain their location-change guard, including custom `CODEX_HOME`.
- Symbolic links, Windows junctions, and other reparse points in source/destination paths are rejected conservatively. The installer does not need to create any link or request administrator rights.
- The native CLI configures stdout/stderr with `backslashreplace` where supported, so non-Latin paths remain printable under legacy console encodings. This affects displayed characters only; filesystem paths and installed bytes are preserved.
- This is preflight protection, not a multi-file filesystem transaction. A runtime I/O failure may leave a partial installation; it does not produce a success message or a false handled-conflict claim that no files changed. Concurrent installations are unsupported.

The temporary-fixture suite proves installer behavior. Live Codex/Claude discovery and the real package source still need the separate integration checks recorded by the main task.
