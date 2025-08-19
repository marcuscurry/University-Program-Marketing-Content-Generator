from marketing_generator.scraping import Webpage
from .link_selector import api_call

def get_all_details(url: str, api: str) -> str:
    result = ""

    # 1. Add Landing Page Content
    try:
        result += "Landing page:\n"
        result += Webpage(url).get_contents()
    except Exception as e:
        print(f"[WARN] Failed to load landing page {url}: {e}")
        result += "[Landing page failed to load]\n"

    # 2. Fetch relevant links via API call
    try:
        links = api_call(url, api)
    except Exception as e:
        print(f"[ERROR] Failed to fetch selected links: {e}")
        return result + "\n[No additional pages fetched due to link selection error]"

    # 3. Loop through selected links
    for link in links.get("links", []):
        try:
            label = link.get("type", "Extra Info")
            page_url = link.get("url")

            if not page_url:
                print(f"[WARN] Skipping malformed link (missing 'url'): {link}")
                result += f"\n[Skipped a link due to missing URL]\n"
                continue

            result += f"\n\n{label}\n"
            result += Webpage(page_url).get_contents()

        except Exception as e:
            fallback_url = link.get("url", "[unknown URL]")
            fallback_label = link.get("type", "Unknown Section")
            print(f"[WARN] Skipping URL {fallback_url} due to error: {e}")
            result += f"\n[Failed to load {fallback_label} page at {fallback_url}]\n"

    return result
