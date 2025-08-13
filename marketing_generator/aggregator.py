from marketing_generator.scraping import Webpage
from .link_selector import api_call


def get_all_details(url: str, api: str) -> str:
    result = "Landing page:\n"
    result += Webpage(url).get_contents()
    links = api_call(url, api)
    for link in links["links"]:
        result += f"\n\n{link['type']}\n"
        result += Webpage(link["url"]).get_contents()
    return result
