# Record format

다음 세션이 이 기록을 읽고 레벨과 다음 과제를 판단한다. 그래서 형식을 고정한다. 확인하지 못한 항목은 지우지 말고 `미확인`으로 쓴다.

## session-log.md (세션마다 아래에 추가)

```markdown
## YYYY-MM-DD — <작업 제목>

- 목표:
- 사용자 몫 (파일·함수):
- AI 몫 (파일·함수):
- 적용 레벨 / 힌트 수준:
- 검증한 개념: (확인 / 미확인을 나눠서)
- 테스트 결과: (실행한 명령과 결과, 미실행이면 미실행)
- 지식 공백:
- 다음 과제:
- 레벨 조정 제안: (근거와 함께, "미반영 — 사용자 승인 필요" 또는 "승인됨 YYYY-MM-DD")
```

## capability-map.md

구체적인 능력 하나가 한 행이다. 기술 이름 전체가 아니라 구체적인 능력을 적는다(예: "Python threading 락으로 공유 상태 보호").

```markdown
| capability | delegation_level | evidence | known_limitations | next_challenge | last_verified |
|---|---|---|---|---|---|
```

`delegation_level`은 사용자가 승인했을 때만 바꾼다. 행을 바꿀 때는 `evidence`에 날짜와 실제 수행 근거를 함께 적는다.
