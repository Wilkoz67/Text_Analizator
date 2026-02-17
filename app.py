from flask import Flask, render_template, request, session, redirect, url_for
from analyzer import TextAnalyzer
from sorting import bubble_sort
from io_utils import *
from translations import translations

app = Flask(__name__)
app.secret_key = "secret123"


def load_stopwords():
    try:
        with open("stopwords.txt", "r", encoding="utf-8") as f:
            return [w.strip() for w in f.readlines()]
    except:
        return []


@app.route("/lang/<code>")
def set_lang(code):
    if code in ["en", "pl", "ru"]:
        session["lang"] = code
    return redirect(url_for("index"))


@app.route("/", methods=["GET", "POST"])
def index():
    error = None
    lang = session.get("lang", "en")
    t = translations[lang]

    if request.method == "POST":
        try:
            # === TEXT INPUT ===
            text = request.form.get("text", "")
            session["last_text"] = text  # zapis tekstu do powrotu

            # === FILE INPUT ===
            if "file" in request.files and request.files["file"].filename != "":
                text = request.files["file"].read().decode("utf-8")
                session["last_text"] = text  # zapis tekstu z pliku

            # === EMPTY CHECK ===
            if text.strip() == "":
                raise Exception(t["error"])

            # === FORM OPTIONS ===
            minlen = int(request.form.get("minlen", 1))
            sortby = request.form.get("sort")
            search = request.form.get("search", "")

            # === ANALYSIS ===
            stopwords = load_stopwords()
            ta = TextAnalyzer(text, stopwords)

            stats = {
                "words": ta.word_count(),
                "chars": ta.char_count(),
                "sentences": ta.sentence_count(),
                "paragraphs": ta.paragraph_count(),
                "avgw": ta.avg_word_len(),
                "avgs": ta.avg_sentence_len()
            }

            freq = ta.frequency()
            freq = [f for f in freq if len(f[0]) >= minlen]

            # === SORTING ===
            if sortby == "alpha":
                freq = bubble_sort(freq, 0)
            else:
                freq = bubble_sort(freq, 1, True)

            # === SEARCH ===
            if search:
                word_count = ta.search_word(search)
                phrase_count = ta.search_phrase(search)
            else:
                word_count = None
                phrase_count = None

            # 🔥 WAŻNE: wracamy do results.html (nie index!)
            return render_template(
                "results.html",
                stats=stats,
                freq=freq,
                query=search,
                search_word=word_count,
                search_phrase=phrase_count,
                t=t
            )

        except Exception as e:
            error = str(e)

    # GET + powrót z przyciskiem BACK (zachowuje tekst)
    return render_template(
        "index.html",
        error=error,
        t=t,
        last_text=session.get("last_text", "")
    )


# ⬇ MUSI BYĆ NA KOŃCU BEZ WCIĘĆ ⬇
if __name__ == "__main__":
    app.run(debug=True)
