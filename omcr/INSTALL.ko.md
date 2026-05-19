# OMCR 설치 가이드 (opioid PR 프로젝트)

## 두 저장소 역할

| 저장소 | 역할 |
|--------|------|
| [opioid-model_wiki](https://github.com/limserenahansol/opioid-model_wiki) | **AMM 수학 모델** (`model/`), Eli와 공유하는 스펙 |
| [opioidaddiction-matlab](https://github.com/limserenahansol/opioidaddiction-matlab) | **MATLAB 파이프라인** (step01–07, 종단 CSV) |

OMCR = [oh-my-claudecode-research](https://github.com/youngeun1209/oh-my-claudecode-research) — **Claude Code 전용** (Cursor와 별개).

## 설치 (Claude Code에서 한 줄씩)

```
/plugin marketplace add https://github.com/youngeun1209/oh-my-claudecode-research
```

```
/plugin install oh-my-claudecode-research
```

## 프로젝트별 초기화

1. GitHub에서 repo clone
2. Claude Code로 해당 폴더 열기
3. `/omcr-setup` (인프라 생성)
4. `/start-research` (인터뷰 — root `CLAUDE.md` 이미 채워져 있으면 확인만)

**wiki repo:** 모델·피팅·논문 초안  
**matlab repo:** pupil, lick, motivation, QC 스크립트

## 프리셋

`examples/opioid-pr-behavior/memory-templates/` → `.claude/agent-memory/*/MEMORY.md` 복사 (opioid PR 맥락).

## 자주 쓰는 에이전트

- `@analysis-implementer` — M0/M1 Python, MNLE, JSON
- `@supervisor` — Tier 1–4 우선순위, 가설
- `@paper-writer` — grant / methods
- `@reviewer` — passive PIT 표현 등 검토

## 진실 소스

모델 규칙은 **항상** wiki의 `model/07`, `model/08`을 따릅니다. OMCR는 그걸 읽고 코드/글을 씁니다.

English: [INSTALL.md](./INSTALL.md)
