from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import torch

class CVAnalyzer:
    def __init__(self):
        self.model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
    
    def preprocess_text(self, text):
        """Clean and prepare text for analysis."""
        return str(text).lower().strip()
    
    def get_embeddings(self, text):
        """Get BERT embeddings for text."""
        return self.model.encode([text])[0]
    
    def calculate_skill_match(self, cv_skills, required_skills):
        """Calculate similarity between CV skills and required skills."""
        cv_skills_clean = self.preprocess_text(cv_skills)
        required_skills_clean = self.preprocess_text(required_skills)
        
        # Get embeddings
        cv_embedding = self.get_embeddings(cv_skills_clean)
        required_embedding = self.get_embeddings(required_skills_clean)
        
        # Calculate cosine similarity
        similarity = cosine_similarity(
            cv_embedding.reshape(1, -1),
            required_embedding.reshape(1, -1)
        )[0][0]
        
        return similarity * 100
    
    def analyze_cv(self, cv, job_requirements):
        """Analyze a CV against job requirements."""
        # Calculate skill match
        skill_score = self.calculate_skill_match(cv.skills, job_requirements.required_skills)
        
        # Calculate experience weight (assuming more experience is better, up to 10 years)
        exp_weight = min(cv.experience / 10.0, 1.0) * 0.3
        
        # Calculate title relevance
        title_similarity = cosine_similarity(
            self.model.encode([cv.title.lower()]),
            self.model.encode([job_requirements.title.lower()])
        )[0][0] * 0.2
        
        # Final weighted score
        final_score = (skill_score * 0.5) + (exp_weight * 100) + (title_similarity * 100)
        
        return {
            'total_score': final_score,
            'skill_score': skill_score,
            'experience_score': exp_weight * 100,
            'title_relevance': title_similarity * 100
        }

    def rank_cvs(self, cvs, job_requirements):
        """Rank multiple CVs against job requirements."""
        rankings = []
        for cv in cvs:
            scores = self.analyze_cv(cv, job_requirements)
            rankings.append({
                'cv': cv,
                'scores': scores
            })
        
        # Sort by total score
        rankings.sort(key=lambda x: x['scores']['total_score'], reverse=True)
        return rankings
