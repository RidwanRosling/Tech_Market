import json
from difflib import get_close_matches
import os

# Fungsi untuk memuat file JSON
def load_knowledge_base(file_path: str) -> dict:
    # Membuka file menggunakan `with` agar otomatis ditutup setelah selesai
    with open(file_path, 'r') as file:
        # Membaca isi file JSON dan mengonversinya menjadi dictionary
        data: dict = json.load(file)
    # Mengembalikan dictionary yang berisi data dari file JSON
    return data

def find_best_match(user_question: str, questions: list[str]) -> str | None:
    try:
        matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
        return matches[0] if matches else None
    except Exception:
        return None

def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]

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
    file_path = 'ours/pc_recommendations.json'
    data = load_pc_recommendations(file_path)
    return data  # Data berisi semua rekomendasi PC dari file JSON

def get_bot_response(user_input: str) -> str:
    knowledge_base: dict = load_knowledge_base('ours/knowledge_base.json')
    best_match: str | None = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])
    
    if best_match:
        answer: str = get_answer_for_question(best_match, knowledge_base)
        return answer
    else:
        return "Maaf, saya tidak mengerti pertanyaan Anda. Silakan coba pertanyaan lain."