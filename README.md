# 🥗 What2Eat

다이어트 단계별 허용식품 안내 & AI 다이어트 어시스턴트

> 다이어트 시작 체중·체지방·근육량을 기반으로 현재 다이어트 단계를 자동 계산하고, 해당 단계에 맞는 허용식품 질문에 답변해주는 챗봇 기반 서비스입니다.

<!-- 배포 링크 / 데모 영상 / 대표 스크린샷을 이 자리에 추가하세요 -->
<!-- 🔗 Demo: https://... -->
<!-- 📹 Demo Video: https://... -->

---

## 핵심 기능

- **다이어트 단계 자동 계산**: 시작일, 시작 체중/체지방/근육량을 입력하면 현재 다이어트 단계를 자동으로 산출
- **단계별 맞춤 허용식품 안내**: 계산된 단계를 기준으로 허용/비허용 식품 기준 제공
- **AI 다이어트 챗봇**: GPT 기반 대화형 인터페이스로 다이어트 관련 질문에 실시간 답변
- **진행 상태 시각화**: 체중·체지방 변화를 그래프로 확인
- **다이어트 진행 알림**: 단계 변화 및 목표 관리 알림 기능

---

## 🛠 기술 스택

| 분야 | 기술 |
|---|---|
| **Frontend** | React, Tailwind CSS |
| **Backend** | Python, Flask |
| **AI / LLM** | OpenAI GPT-3.5-turbo API |
| **Data** | 허용식품 성분 데이터 수집·정제, 규칙 기반 비교 로직 |
| **Infra** | AWS, CI/CD Pipeline |

---

## 🏗 시스템 구조

```
[사용자 입력: 체중/체지방/근육량/시작일]
              │
              ▼
   [Backend: 다이어트 단계 계산 로직]
              │
       ┌──────┴──────┐
       ▼             ▼
[규칙 기반 허용식품 비교]   [GPT-3.5 다이어트 챗봇]
       │             │
       └──────┬──────┘
              ▼
     [React Frontend: 결과/그래프 표시]
```

- AI 응답은 순수 생성형 답변 대신, 다이어트 기본 정보(식사 원칙·권장 식품·주의사항)를 컨텍스트로 구성한 프롬프트 + 규칙 기반 비교 로직을 결합해 답변 정확도를 확보

---

## 👥 팀 구성

| 파트 | 역할 |
|---|---|
| Backend | 서버·DB 설계, API 개발, 다이어트 단계 계산 로직 |
| Frontend | 입력 폼 UI, 결과/그래프 화면, 반응형 디자인 |
| AI | GPT API 연동, 챗봇 프롬프트 설계 |
| Data Analysis | 허용식품 데이터 수집·정제, 다이어트 허용 기준 정립 |

<!-- 팀원 이름과 GitHub 링크를 이 자리에 추가하세요 -->

---

## 🚀 실행 방법

### Backend
```bash
pip install flask flask-cors openai
python app.py
# http://localhost:5000
```

### Frontend
```bash
npx create-react-app chatbot-frontend
cd chatbot-frontend
npm install tailwindcss
npm start
# http://localhost:3000
```

### 환경 변수
```
OPENAI_API_KEY=your-api-key
```

---

## 📁 폴더 구조

```
What2Eat/
├── backend/
│   ├── app.py
│   ├── models/
│   └── data/
│       └── diet_info.txt
├── frontend/
│   ├── src/
│   │   ├── App.js
│   │   └── components/
│   └── public/
└── README.md
```

---

## 🗓 개발 기간

7주 (기획·설계 → 기능 개발 → 통합 테스트 → AWS 배포)

| 주차 | 주요 내용 |
|---|---|
| 1주 | 서버·DB·API 구조 설계, 와이어프레임 제작, 데이터 수집 |
| 2주 | 사용자 관리 API, 입력폼 UI, 허용/비허용 규칙 정리 |
| 3주 | 허용식품 API·질의처리 로직, 기본 화면 구현 |
| 4주 | 알림·진행상태 API, 다이어트 계획 화면 |
| 5주 | 텍스트 처리 API, 결과 화면 최적화 |
| 6주 | 백엔드·프론트 통합 테스트, 반응형 디자인 |
| 7주 | AWS 배포, CI/CD 파이프라인 구축, 최종 검토 |
