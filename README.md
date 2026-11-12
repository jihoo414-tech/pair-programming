# Progressive Pair Programming

AI가 개발을 대신하는 범위와 개발자가 직접 학습·구현하는 범위를 작업마다 정하는 페어 프로그래밍 스킬입니다. 개발자가 이해하지 못한 채 구현이 끝나는 상황을 줄이고, 역량이 쌓이면 근거를 확인하며 위임 범위를 조정하도록 설계했습니다.

**한국어로 작성된 스킬**이며, Claude Code와 Codex에서 명시적으로 호출해 사용할 수 있습니다. 스킬은 대화와 작업 기록을 바탕으로 협업 방식을 조정합니다. 역량이나 학습 효과를 자동으로 측정하거나 보장하지 않습니다.

## 어떻게 동작하나요?

1. 작업 목표와 개발자·AI가 각각 구현할 범위, 검증 방법을 정합니다.
2. 구체적인 작업 영역마다 협업 수준을 선택합니다. 새로운 학습 영역에는 L0를 제안하며, 사용자가 결정합니다.
3. 사용자가 직접 구현하는 영역에서는 질문부터 시작해 요청에 따라 단계적으로 힌트를 제공합니다. AI에 위임한 영역에서는 합의된 범위를 구현하고 검증 근거를 설명합니다.
4. 작업을 마칠 때 수행 범위와 테스트 결과, 남은 과제를 기록합니다. 레벨 변경은 근거를 제시하고 사용자가 승인한 경우에만 반영합니다.

| 수준 | 협업 방식 |
| --- | --- |
| L0 | 개발자가 설계·테스트·핵심 구현을 주도하고 AI는 질문과 리뷰로 지원 |
| L1 | 개발자가 핵심 로직을 주도하고 AI가 합의된 부분을 지원 |
| L2 | 개발자가 요구사항과 검증 기준을 정하고 AI 구현을 검토 |
| L3 | AI가 합의된 범위의 설계·구현·검증을 진행하고 개발자가 검수 |

수준은 사람 전체의 능력 점수가 아니라 **특정 작업의 소유권과 위임 범위**입니다. 영역마다 다르게 적용하고 언제든 변경할 수 있습니다. TDD는 사용자가 선택할 때만 적용합니다.

## 빠르게 사용해 보기

### 1. 저장소 내려받기

```bash
git clone https://github.com/jihoo414-tech/pair-programming.git
```

### 2. 스킬 설치

Claude Code에서 특정 프로젝트에 설치하려면 해당 프로젝트 루트에서 실행합니다. 아래 `PAIR_REPO`는 위에서 내려받은 저장소의 절대 경로입니다.

```bash
PAIR_REPO="/path/to/pair-programming"
mkdir -p .claude/skills
cp -R "$PAIR_REPO/skills/progressive-pair-programming" .claude/skills/
```

Codex에 사용자 범위로 설치하려면:

```bash
PAIR_REPO="/path/to/pair-programming"
mkdir -p ~/.codex/skills
cp -R "$PAIR_REPO/skills/progressive-pair-programming" ~/.codex/skills/
```

Windows PowerShell의 경우 `PAIR_REPO`를 실제 경로로 바꾼 뒤 실행합니다.

```powershell
$PAIR_REPO = 'C:\path\to\pair-programming'
New-Item -ItemType Directory -Force "$HOME\.codex\skills" | Out-Null
Copy-Item -Recurse "$PAIR_REPO\skills\progressive-pair-programming" "$HOME\.codex\skills\"
```

Claude Code 프로젝트 설치 시 대상 경로는 해당 프로젝트의 `.claude\skills\`입니다. 기존에 같은 이름의 스킬이 있다면 먼저 내용을 확인하세요. 설치 후 도구가 스킬을 인식하지 못하면 세션을 새로 시작합니다.

### 3. 명시적으로 호출

```text
Claude Code: /progressive-pair-programming
Codex: $progressive-pair-programming
```

이어서 다음과 같이 작업 범위를 전달할 수 있습니다.

```text
좌석 선점 API를 개선하고 싶어. 동시성 테스트는 내가 직접 작성하고,
AI가 기존 구현을 분석해줘. 테스트의 정답 코드는 먼저 보여주지 말아줘.
```

위는 동작을 보여주기 위한 예시이며 실제 세션 기록이 아닙니다. 스킬은 작업 목표, 각자의 구현 범위, 수준과 진행 방식을 확인한 뒤 시작합니다. 사용자가 소유한 구현은 느리다는 이유만으로 대신 수정하지 않습니다.

## 기록과 개인정보

스킬은 **작업 대상 프로젝트**의 `docs/learning/capability-map.md`와 `docs/learning/session-log.md`를 확인합니다. 처음에는 파일이 없어도 됩니다. 작업 종료 시 세션 로그를 만들거나 기존 로그에 추가하고, 레벨을 저장하기로 승인한 경우에만 Capability Map을 만듭니다. 기록을 원하지 않으면 시작할 때 알려주세요. 파일 대신 대화에 요약합니다.

기록은 해당 프로젝트에 저장되며 이 저장소로 자동 전송되지 않습니다. 사용자 자신의 작업 기록에 민감한 정보가 포함되지 않도록 확인한 뒤 커밋하거나 공유하세요. 이 공개 저장소에는 개인 학습 기록을 포함하지 않았습니다.

## 구성

```text
skills/progressive-pair-programming/
├── SKILL.md                         # 시작, 소유권, 진행 및 기록
├── agents/openai.yaml               # Codex 명시적 호출 설정
├── evals/                           # 행동 평가 케이스 5개
└── references/
    ├── capability-levels.md         # L0–L3와 승급 근거
    ├── coaching-rules.md            # H1–H5 힌트, 막혔을 때 대응, 파일 소유권
    ├── competency-check.md          # 역량 검증 요청 시 절차
    └── record-format.md             # session-log·Capability Map 기록 형식
```

`evals/`의 케이스는 `skills/progressive-pair-programming/`에서 `claude plugin eval . --scaffold --allow-tools Write,Edit,Bash`로 실행할 수 있습니다. 실제 모델 호출이라 비용이 듭니다. 이 평가는 스킬이 규칙대로 행동하는지 확인할 뿐, 학습 효과를 측정하지는 않습니다.

이 스킬은 TicketFlow 프로젝트에서 AI와의 협업 과정을 관리하기 위해 작성한 스킬을 다른 프로젝트에서도 사용할 수 있도록 정리한 것입니다.
