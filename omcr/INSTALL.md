# OMCR setup — opioid PR project (two repos)

[oh-my-claudecode-research](https://github.com/youngeun1209/oh-my-claudecode-research) (OMCR) for **Claude Code**.

## Repos

| Repo | Role |
|------|------|
| [opioid-model_wiki](https://github.com/limserenahansol/opioid-model_wiki) | AMM spec (`model/`), OMCR **primary** CLAUDE.md |
| [opioidaddiction-matlab](https://github.com/limserenahansol/opioidaddiction-matlab) | MATLAB pipeline; OMCR for steps 01–07 |

## 1. Install plugin (Claude Code)

Run **one command at a time** in Claude Code:

```
/plugin marketplace add https://github.com/youngeun1209/oh-my-claudecode-research
```

```
/plugin install oh-my-claudecode-research
```

## 2. Open project & setup

**Wiki repo (modeling / Eli collaboration):**

```bash
git clone https://github.com/limserenahansol/opioid-model_wiki.git
cd opioid-model_wiki
# Open folder in Claude Code, then:
```

```
/omcr-setup
```

```
/start-research
```

When prompted, use content from root `CLAUDE.md` (already filled) or say **minimal** and edit blocks.

**MATLAB repo (analysis):**

```bash
git clone https://github.com/limserenahansol/opioidaddiction-matlab.git
cd opioidaddiction-matlab
```

Same `/omcr-setup` then `/start-research` — `CLAUDE.md` there points to this wiki as canonical model.

## 3. Apply opioid preset (optional)

After `/omcr-setup`, copy preset memories if still on template:

```bash
# From opioid-model_wiki root:
for agent in supervisor analysis-implementer paper-writer figure-descriptor reviewer literature-curator; do
  cp examples/opioid-pr-behavior/memory-templates/$agent/MEMORY.md \
     .claude/agent-memory/$agent/MEMORY.md
done
```

## 4. Daily use

```
@supervisor where are we on Tier 1 fitting?
```

```
@analysis-implementer scaffold src/ingest from model/07 lockout rules
```

## Korean summary

OMCR는 Claude Code 안에서 연구 에이전트 팀입니다. **opioid-model_wiki** = 수식·규칙, **opioidaddiction-matlab** = MATLAB 분석. 플러그인 설치 후 각 repo에서 `/omcr-setup` → `/start-research` 한 번씩 실행하세요.

See also: [INSTALL.ko.md](./INSTALL.ko.md)
