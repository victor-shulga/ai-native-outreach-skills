#!/usr/bin/env python3
"""Copy the course skills from their pack repos into week folders.

The pack repos are the source of truth. This repo is a by-week mirror for the participants of
«AI-native аутріч для агенцій»: one folder per week, every skill of that week inside it, so a
participant installs a week with one command.

    python3 sync.py            # clone every source repo fresh, rebuild week-*/skills/, write READMEs
    python3 sync.py --check    # rebuild into a temp dir and report what would change, write nothing

Edit weeks.json to move a skill between weeks. Never edit a copied SKILL.md here: fix it in the
pack repo and re-run sync.py, or the next sync overwrites the edit.
"""
import filecmp
import json
import re
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
CFG = json.load(open(os.path.join(HERE, "weeks.json"), encoding="utf-8"))
OWNER = CFG["owner"]
CHECK = "--check" in sys.argv


def clone_all():
    tmp = tempfile.mkdtemp(prefix="course-sync-")
    repos = sorted({s[1] for w in CFG["weeks"] for s in w["skills"]})
    for r in repos:
        subprocess.run(["git", "clone", "-q", "--depth", "1", f"https://github.com/{OWNER}/{r}.git",
                        os.path.join(tmp, r)], check=True)
    return tmp


def week_readme(w):
    rows = "\n".join(f"| `{n}` | {why} | `npx skills add {OWNER}/{n if r == n and not p else r + '/' + p}` |"
                     for n, r, p, why in w["skills"])
    return f"""# {w['title']}

Уроки: {w['lessons']}.

## Встановити весь тиждень

```bash
npx skills add {OWNER}/ai-native-outreach-skills/{w['dir']}
```

Без терміналу: завантажте теку `{w['dir']}/skills/<скіл>` як ZIP і в Claude Desktop: Settings → Capabilities → Skills → Upload a skill.

## Скіли тижня

| Скіл | Навіщо на цьому тижні | Окремо, з основного паку |
|---|---|---|
{rows}

Копії взято з основних паків. Оновлення приходять туди першими; ця тека синхронізується скриптом `sync.py`.
"""


PLUGIN_REF = re.compile(r"\$\{CLAUDE_PLUGIN_ROOT\}/reference/([A-Za-z0-9._-]+)")


def vendor_pack_refs(skill_dir, repo_dir):
    """A pack skill may read `${CLAUDE_PLUGIN_ROOT}/reference/<file>` from its pack. A lone copy has
    no pack around it, so copy those files into the skill and point the text at the local copy."""
    md = os.path.join(skill_dir, "SKILL.md")
    text = open(md, encoding="utf-8").read()
    files = sorted(set(PLUGIN_REF.findall(text)))
    if not files:
        return
    os.makedirs(os.path.join(skill_dir, "reference"), exist_ok=True)
    for f in files:
        src = os.path.join(repo_dir, "reference", f)
        if not os.path.isfile(src):
            sys.exit(f"{md} reads reference/{f}, which the pack does not ship")
        shutil.copy2(src, os.path.join(skill_dir, "reference", f))
    open(md, "w", encoding="utf-8").write(PLUGIN_REF.sub(r"reference/\1", text))


def build(dst_root, src_root):
    for w in CFG["weeks"]:
        wdir = os.path.join(dst_root, w["dir"])
        sk_root = os.path.join(wdir, "skills")
        if os.path.isdir(sk_root):
            shutil.rmtree(sk_root)
        os.makedirs(sk_root)
        for name, repo, path, _ in w["skills"]:
            src = os.path.join(src_root, repo, path) if path else os.path.join(src_root, repo)
            if not os.path.isfile(os.path.join(src, "SKILL.md")):
                # entry repos (max) keep the skill in a same-named subfolder
                alt = os.path.join(src, name)
                if os.path.isfile(os.path.join(alt, "SKILL.md")):
                    src = alt
                else:
                    sys.exit(f"no SKILL.md for {name} in {repo}/{path}")
            dst = os.path.join(sk_root, name)
            shutil.copytree(src, dst,
                            ignore=shutil.ignore_patterns(".git", ".github", "*.bak*", "__pycache__", ".DS_Store"))
            vendor_pack_refs(dst, os.path.join(src_root, repo))
        with open(os.path.join(wdir, "README.md"), "w", encoding="utf-8") as f:
            f.write(week_readme(w))


def diff(a, b):
    changed = []
    cmp = filecmp.dircmp(a, b, ignore=[".git"])
    def walk(c, rel=""):
        for n in c.left_only + c.right_only + c.diff_files:
            changed.append(os.path.join(rel, n))
        for n, sub in c.subdirs.items():
            walk(sub, os.path.join(rel, n))
    walk(cmp)
    return changed


src = clone_all()
if CHECK:
    out = tempfile.mkdtemp(prefix="course-check-")
    for w in CFG["weeks"]:
        if os.path.isdir(os.path.join(HERE, w["dir"])):
            shutil.copytree(os.path.join(HERE, w["dir"]), os.path.join(out, w["dir"]))
    build(out, src)
    ch = [c for w in CFG["weeks"] for c in diff(os.path.join(HERE, w["dir"]), os.path.join(out, w["dir"]))] \
        if all(os.path.isdir(os.path.join(HERE, w["dir"])) for w in CFG["weeks"]) else ["(weeks missing)"]
    print("up to date" if not ch else "would change:\n  " + "\n  ".join(ch))
    sys.exit(1 if ch else 0)

build(HERE, src)
total = sum(len(w["skills"]) for w in CFG["weeks"])
print(f"synced {total} skills into {len(CFG['weeks'])} weeks")
