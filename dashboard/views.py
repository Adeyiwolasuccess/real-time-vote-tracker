from django.shortcuts import redirect, render

from .forms import SubmissionForm


def home(request):
    return render(request, "dashboard/home.html")


def submit_result(request):
    if request.method == "POST":
        form = SubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.submitted_by = request.user
            submission.save()
            return redirect("home")
    else:
        form = SubmissionForm()

    return render(request, "dashboard/submit_result.html", {"form": form})
