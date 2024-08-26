def count_vowels(s: str) -> int:  # функция считает количество гласных в строке
    vowels = "aeiouAEIOU"  # список гласных как строчных и прописных
    return sum(1 for char in s if char in vowels)  # суммируем количество гласных
