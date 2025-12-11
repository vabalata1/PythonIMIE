def calculer_moyenne(notes: list[float]) -> float:
    return sum(notes) / len(notes)

def filtrer_notes_suffisantes(notes: list[float], seuil: float) -> list[float]:
    result = []
    for n in notes:
        if n >= seuil:
            result.append(n)
    return result

def formater_message(nom: str, moyenne: float) -> str:
    return f"L'étudiant {nom} a une moyenne de {moyenne:.2f}"

if __name__ == "__main__":
    notes = [12.5, 15.0, 8.5, 18.0, 10.5]
    
    moyenne = calculer_moyenne(notes)
    notes_suffisantes = filtrer_notes_suffisantes(notes, 10.0)
    message = formater_message("Alice", moyenne)
    
    print(f"Les notes sont {notes}")
    print(f"La moyenne est {moyenne}")
    print(f"Les notes supérieures ou égales à 10 sont {notes_suffisantes}")
    print(message)

