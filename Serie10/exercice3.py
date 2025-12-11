import requests

def recuperer_posts():
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
        if response.status_code == 200:
            return response.json()
        else:
            return []
    except Exception as e:
        print(f"Oups, problème de connexion : {e}")
        return []

if __name__ == "__main__":
    posts = recuperer_posts()
    
    stats_par_user = {}
    
    for post in posts:
        user_id = post["userId"]
        
        if user_id not in stats_par_user:
            stats_par_user[user_id] = {"nb_posts": 0, "longueur_moyenne_titre": 0, "total_longueur": 0}
        
        stats_par_user[user_id]["nb_posts"] += 1
        stats_par_user[user_id]["total_longueur"] += len(post["title"])
    
    for user_id in stats_par_user:
        nb_posts = stats_par_user[user_id]["nb_posts"]
        total_longueur = stats_par_user[user_id]["total_longueur"]
        stats_par_user[user_id]["longueur_moyenne_titre"] = total_longueur / nb_posts
    
    liste_users = []
    for user_id, stats in stats_par_user.items():
        liste_users.append({
            "user_id": user_id,
            "nb_posts": stats["nb_posts"],
            "longueur_moyenne_titre": stats["longueur_moyenne_titre"]
        })
    
    liste_users_triee = sorted(liste_users, key=lambda x: x["nb_posts"], reverse=True)
    
    print("Top 3 des utilisateurs les plus actifs")
    for i in range(min(3, len(liste_users_triee))):
        user = liste_users_triee[i]
        print(f"L'utilisateur {user['user_id']} a fait {user['nb_posts']} posts, la longueur moyenne des titres est {user['longueur_moyenne_titre']:.1f} caractères")

