import pytest
from bs4 import BeautifulSoup


def load_html():
    with open("index.html", "r", encoding="utf-8") as file:
        return BeautifulSoup(file, "html.parser")


def test_html_requirements():
    html = load_html()
    score = 0

    # 1. Ellenőrizzük, hogy a HTML nyelve magyar
    if html.html and html.html.get("lang") == "hu":
        score += 1
        print("A HTML nyelve helyes (hu).")
    else:
        print("HIBA: A HTML nyelve nem magyar.")

    # 2. Ellenőrizzük az oldal címét
    if html.title and html.title.string.strip() == "AIX":
        score += 1
        print("Az oldal címe helyes.")
    else:
        print("HIBA: Az oldal címe nem megfelelõ.")

    # 3. Ellenőrizzük az egyes szintű címsort
    h1 = html.find("h1")
    if h1 and h1.string.strip() == "AIX":
        score += 1
        print("Az egyes szintű címsor helyes.")
    else:
        print("HIBA: Az egyes szintű címsor hibás.")

    # 4. Ellenőrizzük a három bekezdést
    paragraphs = html.find_all("p")
    if len(paragraphs) == 3:
        score += 1
        print("A bekezdések száma helyes.")
    else:
        print("HIBA: Nem megfelelő számú bekezdés.")

    # 5. Ellenőrizzük a bekezdések címeit
    headers = html.find_all("h2")
    expected_headers = ["Egy", "Kettő", "Három"]
    if [h.get_text(strip=True) for h in headers] == expected_headers:
        score += 1
        print("A bekezdések címei helyesek.")
    else:
        print("HIBA: A bekezdések címei hibásak.")

    # 6. Ellenőrizzük a félkövér Advanced Interactive eXecutive szöveget
    bold_text = html.find("b")
    if bold_text and bold_text.get_text(strip=True) == "Advanced Interactive eXecutive":
        score += 1
        print("A félkövér szöveg helyes.")
    else:
        print("HIBA: A félkövér szöveg hibás.")

    # 7. Ellenőrizzük az AIX szó kiemelését
    em_texts = html.find_all("em")
    if all(em.get_text(strip=True) == "AIX" for em in em_texts):
        score += 1
        print("Az AIX szó kiemelése helyes.")
    else:
        print("HIBA: Az AIX szó kiemelése hibás.")

    # 8. Ellenőrizzük a megjegyzést
    comments = html.find_all(string=lambda text: isinstance(text, str) and "--" in text)
    if any("nev" in comment.lower() and "202" in comment for comment in comments):
        score += 1
        print("A megjegyzés helyes.")
    else:
        print("HIBA: A megjegyzés hiányzik vagy hibás.")

    # 9. Ellenőrizzük az aix.txt tartalmát
    with open("aix.txt", "r", encoding="utf-8") as txt_file:
        aix_content = txt_file.read().strip()
    if aix_content in html.body.get_text():
        score += 1
        print("Az aix.txt tartalma helyesen szerepel az oldalon.")
    else:
        print("HIBA: Az aix.txt tartalma hiányzik.")

    # 10. Ellenőrizzük az alap HTML struktúrát
    if html.head and html.body:
        score += 1
        print("Az alap HTML struktúra megfelelő.")
    else:
        print("HIBA: Az alap HTML struktúra hibás.")

    print(f"Pontszám: {score}/10")
    assert score == 10, f"A HTML oldal csak {score}/10 pontot ért el."
