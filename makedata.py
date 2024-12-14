import re
from transformers import pipeline

# 요약 모델 로드
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# 텍스트 파일 읽기
with open("diet_info.txt", "r", encoding="utf-8") as file:
    raw_text = file.read()

# 데이터 분리
entries = raw_text.strip().split("\n")
  # 빈 줄을 기준으로 나눔
print("Entries 리스트 확인:", entries)

# 긴 텍스트를 분할하는 함수
def split_text(text, chunk_size=1024):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

# 요약 생성 함수
def summarize_text(text, chunk_size=1024, batch_size=4):
    chunks = split_text(text, chunk_size)
    summaries = []
    for i in range(0, len(chunks), batch_size):
        batch = chunks[i:i+batch_size]
        try:
            # 배치 요약 수행
            batch_summaries = summarizer(batch, max_length=150, min_length=50, do_sample=False)
            summaries.extend([summary["summary_text"] for summary in batch_summaries])
        except Exception as e:
            print(f"요약 중 오류 발생: {e}")
            summaries.extend(batch)  # 오류 발생 시 원본 유지
    return " ".join(summaries)

# 결과 저장할 리스트
qa_pairs = []
# qa_pairs가 비어있는 경우 확인
if not qa_pairs:
    print("qa_pairs 리스트가 비어있습니다. 데이터 처리에 문제가 있습니다.")
    
for entry in entries:
    # 제목과 내용 분리
    match = re.match(r"영상제목:(.+)\nTranscript:(.+)", entry, re.DOTALL)
    if not match:
        continue

    title = match.group(1).strip()
    transcript = match.group(2).strip()

    # 질문 생성
    question = f"{title}에 대해 무엇을 배울 수 있나요?"

    # 긴 텍스트 요약
    answer = summarize_text(transcript)

    # 질문-답변 저장
    qa_pairs.append({"question": question, "answer": answer})

# 결과 저장 및 출력
with open("qa_formatted_data.txt", "w", encoding="utf-8") as file:
    for pair in qa_pairs:
        file.write(f"질문: {pair['question']}\n")
        file.write(f"답변: {pair['answer']}\n\n")

# 결과 확인
for pair in qa_pairs:
    print(f"질문: {pair['question']}")
    print(f"답변: {pair['answer']}\n")

# qa_pairs 내용 확인
for pair in qa_pairs:
    print(f"질문: {pair['question']}")
    print(f"답변: {pair['answer']}\n")


