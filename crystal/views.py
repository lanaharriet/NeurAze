from django.shortcuts import render

def summarize_text(text):
    sentences = text.split('.')
    sentences = [s.strip() for s in sentences if s.strip()]
    return ' '.join(sentences[:3]) + '.' if sentences else ''

def simplify_text(text):
    replacements = {
        "however": "but",
        "therefore": "so",
        "utilize": "use",
        "approximately": "about",
        "complex": "hard",
        "difficult": "hard",
        "individuals": "people",
        "numerous": "many",
        "consequently": "as a result",
        "essential": "important",
    }

    simple = text.lower()
    for word, repl in replacements.items():
        simple = simple.replace(word, repl)

    return simple.capitalize()

def extract_points(text):
    sentences = [s.strip() for s in text.split('.') if s.strip()]
    return sentences[:5]

def crystal_home(request):
    summary = ""
    simplified = ""
    points = []

    if request.method == "POST":
        user_text = request.POST.get("user_text")

        summary = summarize_text(user_text)
        simplified = simplify_text(user_text)
        points = extract_points(user_text)

    return render(request, 'crystal/crystal.html', {
        'summary': summary,
        'simplified': simplified,
        'points': points,
    })
