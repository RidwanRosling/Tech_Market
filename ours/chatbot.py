import json
from difflib import get_close_matches
import pandas as pd
import os

# Fungsi untuk memuat file JSON
def load_knowledge_base(file_path: str) -> dict:
    # Membuka file menggunakan `with` agar otomatis ditutup setelah selesai
    """Penulisan data: dict menggunakan titik dua (:) adalah bagian dari type hinting di Python, seperti yang dijelaskan sebelumnya. Berikut adalah penjelasan rinci mengapa ditulis seperti itu dan apa fungsinya.
    
    1. Apa itu Type Hinting?
    Type hinting adalah fitur Python untuk memberikan informasi tentang tipe data yang diharapkan oleh variabel atau fungsi. Ini diperkenalkan secara resmi di Python 3.5 melalui modul typing.
    Pada kode di atas, data: dict adalah cara untuk menunjukkan bahwa variabel data diharapkan memiliki tipe data dict (dictionary)."""
    with open(file_path, 'r') as file:
        # Membaca isi file JSON dan mengonversinya menjadi dictionary
        data: dict = json.load(file)
    # Mengembalikan dictionary yang berisi data dari file JSON
    return data

# save the knowledge base to a json
def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def find_best_match(user_question: str, questions: list[str]) -> str | None:
    try:
        matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
        return matches[0] if matches else None
    except Exception:
        return None

    return matches[0] if matches else None

def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]

def chat_bot():
    knowledge_base: dict = load_knowledge_base('knowledge_base.json')

    while True:
        user_input: str = input('You: ')

        if user_input.lower() == 'quit':
            break
        best_match: str | None = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])

        if best_match:
            answer: str = get_answer_for_question(best_match, knowledge_base)
            print(f'Bot: {answer}')
        else:
            print('Bot: I don\'t know the answer. Can you teach me?')
            new_answer: str = input('Type the answer or "skip" to skip: ')

            if new_answer.lower() != 'skip':
                knowledge_base["questions"].append({"question": user_input, "answer": new_answer})
                save_knowledge_base('knowledge_base.json', knowledge_base)
                print('Bot: Thank you! I learned a new response!')

def load_pc_recommendations(file_path: str) -> dict:
    # Pastikan path file yang dimasukkan sesuai dengan lokasi
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    else:
        raise FileNotFoundError(f"File {file_path} tidak ditemukan.")
    
# Fungsi untuk mendapatkan rekomendasi PC
def get_pc_recommendation():
    file_path = 'ours/pc_recommendations.json'  # pastikan path ini sesuai
    try:
        data = load_pc_recommendations(file_path)
        return data  # Data berisi semua rekomendasi PC dari file JSON
    except FileNotFoundError as e:
        print(e)
        return None

def get_bot_response(user_input: str) -> str:
    knowledge_base: dict = load_knowledge_base('ours/knowledge_base.json')
    
    best_match: str | None = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])
    
    if best_match:
        answer: str = get_answer_for_question(best_match, knowledge_base)
        return answer
    else:
        return "Maaf, saya tidak mengerti pertanyaan Anda. Silakan coba pertanyaan lain."




if __name__ == '__main__':
    chat_bot()