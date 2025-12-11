import requests

class JsonPlaceholderClient:
    def __init__(self, base_url="https://jsonplaceholder.typicode.com"):
        self.base_url = base_url
    
    def _get(self, endpoint):
        url = self.base_url + endpoint
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                return response.json()
            else:
                return None
        except Exception as e:
            print(f"Oups, problème de connexion : {e}")
            return None
    
    def get_posts(self):
        return self._get("/posts")
    
    def get_post(self, post_id):
        return self._get(f"/posts/{post_id}")

if __name__ == "__main__":
    client = JsonPlaceholderClient()
    
    posts = client.get_posts()
    if posts:
        print(f"Il y a {len(posts)} posts au total")
    
    post_1 = client.get_post(1)
    if post_1:
        print(f"\nVoici le post #1")
        print(f"Le titre est {post_1['title']}")
        print(f"Le contenu est {post_1['body']}")

