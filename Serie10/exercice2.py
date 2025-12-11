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

def afficher_resume_posts(posts, n=5):
    for i in range(min(n, len(posts))):
        post = posts[i]
        print(f"Post #{post['id']} de l'utilisateur {post['userId']} : {post['title']}")

if __name__ == "__main__":
    posts = recuperer_posts()
    
    print(f"Il y a {len(posts)} posts au total")
    print("\nAperçu des 5 premiers posts")
    afficher_resume_posts(posts, 5)

