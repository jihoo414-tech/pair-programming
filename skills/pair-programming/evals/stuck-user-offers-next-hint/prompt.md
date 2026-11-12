---
tags: [skill-creator]
max_turns: 30
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

/pair-programming
(이어서 진행 중. 지난번에 동시성 부분은 내가 직접 짜기로 했고, 힌트는 질문 위주로만 달라고 했었어.)
세 번째 시도인데 아직도 실패해.

```
FAILED tests/test_concurrency.py::test_no_oversell - assert 30 == 10
```

inventory.py에 락 넣었는데 왜 안 되는지 진짜 모르겠다.

Input files: inventory.py, slug.py, tests/, docs/learning/capability-map.md
