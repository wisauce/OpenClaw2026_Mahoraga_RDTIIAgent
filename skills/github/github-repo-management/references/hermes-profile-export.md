# Reinitializing a repository from a Hermes profile directory

Use this when a user asks to push/export a Hermes profile such as `~/.hermes/profiles/<name>` into a GitHub repository. Treat profile directories as sensitive runtime state, not normal source trees.

## Safe export pattern

1. Clone the target repo into a temporary directory.
2. Remove the old working tree contents while preserving `.git/`.
3. Create a profile-aware `.gitignore` before copying files.
4. Copy the profile with explicit exclusions for secrets, runtime state, logs, sessions, caches, locks, and local config.
5. Commit a redacted `config.example.yaml` instead of the real `config.yaml`.
6. If the exported profile is meant to be a domain-specific agent, update `SOUL.md` and `README.md` to state the agent identity/domain, and add a README "Skills" note distinguishing the profile's unique domain skill directory from bundled Hermes skills.
7. Run a staged-file secret scan before committing.
8. Push only after verifying the sensitive files are not tracked.

## Important `.gitignore` entries

```gitignore
# Hermes secrets / credentials
.env
.env.*
auth.json
auth.lock
**/*token*
**/*secret*
**/*credential*

# Runtime state / databases / locks
state.db*
*.db
*.sqlite
*.sqlite3
*.lock
*.pid
*.sock

# Logs and session transcripts
logs/
*.log
sessions/
*.jsonl
.hermes_history

# Caches / generated runtime files
cache/
audio_cache/
video_cache/
image_cache/
tmp/
temp/
__pycache__/
*.py[cod]
*.bak*
.update_check
.skills_prompt_snapshot.json
context_length_cache.yaml
models_dev_cache.json
ollama_cloud_models_cache.json
gateway_state.json
channel_directory.json
cron/.tick.lock

# Local config: publish a redacted example instead
config.yaml
config.yaml.bak*

# Local machine/editor noise
.DS_Store
Thumbs.db
.vscode/
.idea/
```

## `rsync` exclusions

```bash
rsync -a "$PROFILE"/ ./ \
  --exclude '.env' \
  --exclude 'auth.json' \
  --exclude 'auth.lock' \
  --exclude 'state.db*' \
  --exclude 'logs/' \
  --exclude 'sessions/' \
  --exclude 'cache/' \
  --exclude 'audio_cache/' \
  --exclude 'video_cache/' \
  --exclude 'image_cache/' \
  --exclude '*.lock' \
  --exclude '*.pid' \
  --exclude '.hermes_history' \
  --exclude '.update_check' \
  --exclude '.skills_prompt_snapshot.json' \
  --exclude 'context_length_cache.yaml' \
  --exclude 'models_dev_cache.json' \
  --exclude 'ollama_cloud_models_cache.json' \
  --exclude 'gateway_state.json' \
  --exclude 'channel_directory.json' \
  --exclude 'config.yaml' \
  --exclude 'config.yaml.bak*'
```

## README and persona notes for domain-specific exports

When the target repository represents a named/domain-specific Hermes profile, make the identity explicit in committed docs:

- `SOUL.md`: define the agent name, domain, scope, operating style, and any non-legal/non-medical/etc. disclaimer relevant to the domain.
- `README.md`: explain that this is a sanitized Hermes profile export, describe the domain purpose, and include a **Skills** section.
- In the README **Skills** section, call out the one unique domain skill directory (for example `skills/RDTIIAnalyzer/`) and state that the rest of the checked-in skills are bundled Hermes skills included for general capability, not agent-specific domain logic.

## Redacted config example

```bash
python3 - <<'PY'
from pathlib import Path
import re
src = Path(PROFILE) / 'config.yaml'
out = Path('config.example.yaml')
if src.exists():
    text = src.read_text(errors='ignore')
    text = re.sub(
        r'(?im)^(\s*(?:api_key|token|secret|password|client_secret|access_token|refresh_token)\s*:\s*).+$',
        r'\1"<REDACTED>"',
        text,
    )
    text = re.sub(r'gh[pousr]_[A-Za-z0-9_]+', '<REDACTED_GITHUB_TOKEN>', text)
    text = re.sub(r'sk-[A-Za-z0-9_-]+', '<REDACTED_API_KEY>', text)
    out.write_text(text)
PY
```

## Staged-file secret scan

Use hard credential patterns, not generic words like `api_key`, because skills and documentation commonly contain placeholder key names.

```bash
python3 - <<'PY'
import pathlib, re, subprocess, sys
files = subprocess.check_output(['git', 'diff', '--cached', '--name-only'], text=True).splitlines()
secret_patterns = [
    re.compile(r'gh[pousr]_[A-Za-z0-9_]{30,}'),
    re.compile(r'github_pat_[A-Za-z0-9_]{40,}'),
    re.compile(r'sk-[A-Za-z0-9_-]{32,}'),
    re.compile(r'-----BEGIN (?:RSA |OPENSSH |EC |DSA )?PRIVATE KEY-----'),
]
bad = []
for f in files:
    p = pathlib.Path(f)
    if not p.is_file() or p.stat().st_size > 5_000_000:
        continue
    text = p.read_text(errors='ignore')
    if any(pattern.search(text) for pattern in secret_patterns):
        bad.append(f)
if bad:
    print('Refusing to commit likely hard secrets in:', '\n'.join(bad[:50]), file=sys.stderr)
    sys.exit(2)
print(f'Secret scan passed for {len(files)} staged paths')
PY
```

## Verification

```bash
git status --short
git rev-parse --short HEAD
git ls-remote --heads origin main
for f in .env auth.json state.db logs/gateway.log sessions/sessions.json config.yaml; do
  if git ls-files --error-unmatch "$f" >/dev/null 2>&1; then
    echo "TRACKED:$f"
  else
    echo "ignored-or-absent:$f"
  fi
done
```
