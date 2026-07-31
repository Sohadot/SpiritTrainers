# SECURITY_POLICY.md

> The asset's attack surface is small by design, but a category asset's real
> security concern is not only servers — it is the integrity of the *name and
> the claim*. This policy covers both.

---

## 1. Threat model

This is a static asset with no accounts, no user data, no database, and no
server-side code. That removes most conventional web risk. What remains:

- **Supply-chain risk** in any third-party code the site might load.
- **Content integrity** — unauthorized changes to the name, meaning, or claim.
- **Impersonation** — others misusing the name or the thesis.
- **Availability** — the domain and hosting themselves.

## 2. No third-party runtime dependencies

The site is self-contained:

- **No external scripts, fonts, stylesheets, trackers, or analytics** loaded at
  runtime. Everything ships from the asset's own files.
- No CDN calls, no remote embeds, no fetch to third-party hosts.
- This is both a privacy stance and a supply-chain defense: there is no external
  code path an attacker can compromise to reach a visitor.

Any proposal to add a runtime dependency is a Tier 2 change and must justify why
the value outweighs re-introducing supply-chain risk.

**Social share cards** (`assets/og/*.png`, referenced by `og:image` /
`twitter:image`) are self-hosted and fetched by social crawlers only — they are
never loaded into the page at runtime. They therefore introduce no runtime
external request and stay within this policy.

## 3. Content integrity is a security property

For a category asset, an unauthorized edit to `CANONICAL_MEANING.md` or
`CLAIM_BOUNDARY.md` is a security incident, not just an editorial one — it can
silently break the thesis or introduce a liability (a medical/religious claim).

Protections:

- `main` is protected; changes arrive only through `CHANGE_CONTROL.md`.
- Tier 1 files cannot be self-approved.
- Git history is the tamper-evident record; force-pushes to `main` are
  prohibited.

## 4. Secrets

There are, by design, **no secrets in this repository** — no API keys, tokens,
credentials, or private endpoints, because the asset needs none. Any secret found
in the repo is itself the incident: rotate it, remove it from history, and log
it. `run_secret_scanning` (or equivalent) should pass clean at all times.

## 5. Domain & hosting security

The most valuable component of the asset is the **domain registration itself.**
Practical safeguards for the owner:

- Registrar-lock the domain; enable two-factor auth on the registrar account.
- Keep registration well ahead of expiry; a lapse is the single largest risk to
  the asset's value.
- Serve over HTTPS only; redirect HTTP → HTTPS.
- Set a minimal, static-appropriate security header set (CSP that forbids
  external origins, `X-Content-Type-Options: nosniff`, a strict referrer policy).

## 6. Reporting

Security concerns — a leaked secret, an integrity question, a domain issue — are
handled privately by the asset owner, not through public issues. Do not disclose
a suspected domain or registrar vulnerability in a public channel.

## 7. Review cadence

- On every change: G4/G5 build checks and secret scan (`QUALITY_GATE.md`).
- Periodically: confirm no runtime dependency has crept in, confirm domain
  registrant/expiry/lock status, confirm HTTPS and headers.
