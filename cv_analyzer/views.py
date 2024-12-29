from django.shortcuts import render, redirect
from .models import CV, JobRequirement
from .forms import CVUploadForm, JobRequirementForm
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def home(request):
    return render(request, 'cv_analyzer/home.html')

def upload_cv(request):
    if request.method == 'POST':
        form = CVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('compare_cvs')
    else:
        form = CVUploadForm()
    return render(request, 'cv_analyzer/upload_cv.html', {'form': form})

def compare_cvs(request):
    if request.method == 'POST':
        form = JobRequirementForm(request.POST)
        if form.is_valid():
            job_requirements = form.save(commit=False)
            
            # Get the two most recent CVs
            cvs = CV.objects.all().order_by('-uploaded_at')[:2]
            
            if len(cvs) < 2:
                return render(request, 'cv_analyzer/compare_cvs.html', {
                    'form': form,
                    'error': 'Please upload at least two CVs'
                })
            
            rankings = []
            for cv in cvs:
                # Calculate skills similarity
                vectorizer = CountVectorizer()
                vectors = vectorizer.fit_transform([
                    cv.skills.lower(),
                    job_requirements.required_skills.lower()
                ])
                skill_similarity = cosine_similarity(vectors)[0][1] * 100
                
                # Calculate title similarity
                title_vectorizer = CountVectorizer()
                title_vectors = title_vectorizer.fit_transform([
                    cv.title.lower(),
                    job_requirements.title.lower()
                ])
                title_similarity = cosine_similarity(title_vectors)[0][1] * 100
                
                # Calculate experience score (assuming more experience is better, up to 10 years)
                exp_score = min(cv.experience / 10.0, 1.0) * 100
                
                # Calculate total score with weights
                total_score = (
                    skill_similarity * 0.5 +  # Skills are 50% of total score
                    exp_score * 0.3 +        # Experience is 30% of total score
                    title_similarity * 0.2    # Title match is 20% of total score
                )
                
                rankings.append({
                    'cv': cv,
                    'scores': {
                        'total_score': total_score,
                        'skill_score': skill_similarity,
                        'experience_score': exp_score,
                        'title_relevance': title_similarity
                    }
                })
            
            # Sort by total score
            rankings.sort(key=lambda x: x['scores']['total_score'], reverse=True)
            
            return render(request, 'cv_analyzer/results.html', {
                'rankings': rankings,
                'job_title': job_requirements.title
            })
    else:
        form = JobRequirementForm()
    
    return render(request, 'cv_analyzer/compare_cvs.html', {'form': form})
