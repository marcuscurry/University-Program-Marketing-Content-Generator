import requests
from bs4 import BeautifulSoup
from marketing_generator.config import headers


class Webpage:
    def __init__(self, url: str):
        resp = requests.get(url, headers=headers, timeout=30)
        self.soup = BeautifulSoup(resp.text, "html.parser")
        self.url = url
        self.title = self.soup.title.string if self.soup.title is not None else ""
        if self.soup.body:
            for irrelevant in self.soup.body(["script", "style", "img", "input"]):
                irrelevant.decompose()
            self.text = self.soup.body.get_text(separator="\n", strip=True)
        else:
            self.text = ""
        links = [link.get("href") for link in self.soup.find_all("a")]
        self.links = [link for link in links if link]

    def get_contents(self) -> str:
        return f"Webpage Title:\n{self.title}\nWebpage Contents:\n{self.text}\n\n"
