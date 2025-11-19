from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def mind_home(request):
    flashcards = []

    if request.method == "POST":
        text = request.POST.get("topic_text", "").strip()

        if text:
            # SIMPLE, CLEAN, OFFLINE AI-LIKE FLASHCARD GENERATION
            sentences = [s.strip() for s in text.replace("\n", " ").split(".") if s.strip()]
            points = []

            for s in sentences:
                parts = s.replace(":", "-").split("-")
                if len(parts) >= 2:
                    q = parts[0].strip()
                    a = "-".join(parts[1:]).strip()
                    points.append((q, a))
                else:
                    if len(s.split()) > 4:
                        q = s[:40].strip() + "…?"
                        a = s
                        points.append((q, a))

            # Convert to flashcards list
            for q, a in points:
                flashcards.append({"question": q, "answer": a})

    return render(request, "mindgarden/mindgarden.html", {"flashcards": flashcards})
