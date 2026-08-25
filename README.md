# AI Resume Analyzer & ATS Scoring System

An AI-powered resume analysis platform that evaluates resumes against job descriptions using **ATS scoring, skill matching, semantic similarity, resume structure analysis, career-readiness assessment, and recruiter-oriented ranking**.

The application is built with **Python and Streamlit** and provides actionable feedback to help candidates identify skill gaps and improve their resumes for specific job descriptions.

---

## 🚀 Project Overview

Applicant Tracking Systems (ATS) are widely used by recruiters to screen resumes before human evaluation. A resume may contain relevant experience but still receive a low ATS match because of missing keywords, weak skill alignment, poor structure, or insufficiently relevant content.

This project addresses these challenges by analyzing a resume against a target job description and generating a comprehensive candidate evaluation.

The system combines **rule-based analysis, weighted scoring, NLP-based semantic matching, skill extraction, and recruiter-oriented analytics** into a single interactive platform.

---

## ✨ Key Features

### 1. Resume & Job Description Processing

* Upload resumes in PDF format.
* Extract text from resumes using PDF parsing.
* Accept job descriptions through text input or PDF upload.
* Clean and preprocess extracted text before analysis.

### 2. ATS Score

Calculates an overall ATS compatibility score using multiple components rather than relying only on keyword matching.

The analysis considers:

* Skill matching
* Keyword relevance
* Semantic similarity
* Resume structure
* Resume quality
* Career and experience indicators
* Education
* Achievement impact

### 3. Weighted ATS Scoring

Skills and job requirements are assigned different levels of importance to provide a more realistic assessment of candidate-job alignment.

The system identifies:

* Matched skills
* Missing skills
* Important missing skills
* Critical missing skills
* Overall skill alignment

### 4. Skill Extraction & Analysis

Automatically extracts technical skills from resumes and job descriptions.

The system performs:

* Skill extraction
* Skill normalization
* Skill categorization
* Skill matching
* Missing-skill detection
* Skill importance analysis

### 5. Semantic Matching

Uses the **all-MiniLM-L6-v2** sentence-transformer model to compare the semantic meaning of the resume and job description.

This helps identify relevant experience even when the exact job-description keywords are not present.

### 6. Resume Quality & Structure Analysis

Evaluates the organization and completeness of a resume.

The system detects sections such as:

* Contact information
* Summary
* Education
* Skills
* Experience
* Projects
* Achievements

It provides:

* Section completeness analysis
* Missing-section detection
* Structure score
* Structure recommendations
* Resume quality assessment

### 7. Resume Content Analysis

The platform analyzes important resume components including:

**Projects**

* Project detection
* Project relevance analysis
* Project scoring
* Project feedback

**Experience**

* Experience detection
* Experience scoring
* Career-readiness analysis

**Achievements**

* Achievement detection
* Achievement count
* Impact analysis
* Action-verb analysis
* Achievement quality assessment

**Education**

* Education detection
* Education scoring
* CGPA detection
* CGPA-based assessment

### 8. Keyword & Content Analysis

Analyzes the usage of important terms throughout the resume.

Includes:

* Keyword frequency
* Keyword density
* Top skills
* Keyword stuffing detection
* Resume content statistics

### 9. AI Feedback & Recommendations

Generates personalized feedback based on the resume and target job description.

The system provides:

* Resume improvement recommendations
* ATS optimization suggestions
* Skill-gap recommendations
* Semantic matching feedback
* Overall candidate feedback
* Score explanation

### 10. Candidate Profile & SWOT Analysis

Generates a recruiter-oriented candidate profile based on the analysis.

Includes:

* Candidate strengths
* Candidate weaknesses
* Technical score
* SWOT analysis
* Recruiter summary

### 11. Career Readiness & Hiring Recommendation

Combines multiple resume indicators to estimate candidate readiness and provide a recruiter-oriented assessment.

The system generates:

* Career readiness score
* Candidate ranking
* Hiring recommendation
* Final candidate profile

### 12. Multiple Resume Analysis

The application can analyze multiple resumes and compare candidates against the same job description.

Features include:

* Batch resume analysis
* Candidate comparison
* Candidate ranking
* Leaderboard visualization
* Shortlisting support

### 13. Recruiter Dashboard

Provides visual insights into candidate performance and recruitment-related metrics.

The dashboard helps compare candidates across multiple evaluation criteria.

### 14. PDF Report Generation

Generates a downloadable PDF report containing the candidate's analysis and evaluation results.

---

## 🔄 System Workflow

```text
                 ┌─────────────────────┐
                 │  Upload Resume PDF   │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │   Extract Resume    │
                 │       Text          │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Text Cleaning &     │
                 │ Preprocessing       │
                 └──────────┬──────────┘
                            │
             ┌──────────────┴──────────────┐
             ▼                             ▼
   ┌──────────────────┐          ┌──────────────────┐
   │ Resume Analysis  │          │ Job Description  │
   │                  │          │ Analysis         │
   └────────┬─────────┘          └────────┬─────────┘
            │                             │
            └──────────────┬──────────────┘
                           ▼
                 ┌─────────────────────┐
                 │ Skill & Keyword     │
                 │ Matching            │
                 └──────────┬──────────┘
                            ▼
                 ┌─────────────────────┐
                 │ Semantic Matching   │
                 └──────────┬──────────┘
                            ▼
                 ┌─────────────────────┐
                 │ Weighted ATS Score  │
                 └──────────┬──────────┘
                            ▼
        ┌────────────────────────────────────┐
        │ Resume Quality & Career Analysis   │
        └────────────────┬───────────────────┘
                         ▼
                 ┌─────────────────────┐
                 │ Recommendations &   │
                 │ Candidate Feedback  │
                 └──────────┬──────────┘
                            ▼
                 ┌─────────────────────┐
                 │ Ranking / Hiring    │
                 │ Recommendation      │
                 └──────────┬──────────┘
                            ▼
                 ┌─────────────────────┐
                 │ PDF Report /        │
                 │ Dashboard           │
                 └─────────────────────┘
```

---

## 🧠 ATS Scoring Approach

Instead of evaluating a resume using a single keyword count, the system combines multiple signals to produce a more comprehensive candidate evaluation.

Major components include:

* **Keyword & Skill Matching**
* **Weighted Skill Importance**
* **Semantic Similarity**
* **Resume Structure**
* **Resume Quality**
* **Project Analysis**
* **Experience Analysis**
* **Achievement Impact**
* **Education**
* **Career Readiness**

The final evaluation is used to generate an overall candidate score and supporting explanations.

---

## 🤖 Semantic Matching

The project uses the **Sentence Transformers** framework with the `all-MiniLM-L6-v2` model.

The resume and job description are converted into vector representations and compared using semantic similarity.

This allows the system to identify conceptually relevant content even when the wording between the resume and job description differs.

---

## 📊 Candidate Evaluation

The platform provides a detailed candidate profile containing:

| Analysis          | Output                            |
| ----------------- | --------------------------------- |
| ATS Compatibility | Overall ATS score                 |
| Skill Matching    | Matched and missing skills        |
| Skill Importance  | Important and critical skills     |
| Semantic Matching | Resume-JD similarity              |
| Resume Structure  | Section completeness              |
| Resume Quality    | Quality assessment                |
| Projects          | Project score and feedback        |
| Experience        | Experience score                  |
| Achievements      | Impact and achievement analysis   |
| Education         | Education score and CGPA analysis |
| Career Readiness  | Readiness score                   |
| Candidate Ranking | Comparative ranking               |
| Hiring Decision   | Recruiter-oriented recommendation |

---

## 🛠️ Technology Stack

### Programming

* Python

### Application

* Streamlit

### Data Processing

* Pandas
* NumPy

### Natural Language Processing

* Sentence Transformers
* `all-MiniLM-L6-v2`

### Machine Learning / Analysis

* Scikit-learn

### PDF Processing

* pdfplumber
* ReportLab

### Visualization

* Plotly

### Development

* Jupyter Notebook
* VS Code
* Git & GitHub

---

## 📁 Project Structure

```text
ATS-Resume-Analyzer/
│
├── data/
│   └── Project data and configuration files
│
├── tests/
│   ├── test.py
│   ├── test_education.py
│   ├── test_keywords.py
│   ├── test_loader.py
│   ├── test_pdf.py
│   ├── test_project.py
│   ├── test_report.py
│   ├── test_sections.py
│   ├── test_semantic.py
│   ├── test_skills.py
│   └── test_weighted.py
│
├── utils/
│   ├── PDF parsing
│   ├── text cleaning
│   ├── skill extraction
│   ├── ATS scoring
│   ├── semantic matching
│   ├── resume analysis
│   ├── recommendations
│   ├── candidate ranking
│   └── report generation
│
├── .gitignore
├── README.md
├── app.py
└── requirements.txt
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/harikamodem/ATS-Resume-Analyzer.git
cd ATS-Resume-Analyzer
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
streamlit run app.py
```

The application will open in the browser through the Streamlit local server.

---

## 📌 Example Use Case

A candidate can:

1. Upload their resume.
2. Enter or upload a target job description.
3. Run the resume analysis.
4. View the overall ATS score.
5. Identify matched and missing skills.
6. Review semantic similarity with the job description.
7. Analyze resume structure and content quality.
8. Review project, experience, education, and achievement analysis.
9. Receive personalized recommendations.
10. Generate a downloadable analysis report.

Recruiters can also use the multi-resume functionality to compare candidates against a common job description.

---

## 🔮 Future Improvements

Potential extensions include:

* Integration with live job portals and job-description APIs.
* Advanced transformer-based resume understanding.
* Automatic resume rewriting based on identified skill gaps.
* Job recommendation based on candidate skills.
* Cloud deployment for public access.
* Persistent candidate dashboards.
* Explainable AI visualizations for scoring decisions.

---
