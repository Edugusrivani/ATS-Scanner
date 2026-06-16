📄 ATS Resume Scanner 🚀 | AICTE Virtual Internship 2026

### 🎯 Project Title
**Automated Applicant Tracking System** using Python, SQL & Power BI

---

### 📝 About The Project
Recruiters receive **1000+ resumes** 📥 for a single job posting. Manual screening = ⏰ Time waste + 😵 Human error.

This ATS Scanner automates everything:
1. 📤 **Extracts text** from PDF resumes using `pdfplumber`
2. 🔍 **Matches keywords** between resume & Job Description  
3. 📊 **Calculates ATS Score** 0-100% using smart algorithm
4. ⚠️ **Shows missing skills** to improve resume

🏆 Built for **AICTE Virtual Internship 2026** by **Edunet Foundation** 🇮🇳

---

### ✨ Key Features
- 📄 **PDF Text Extraction**: Auto read resume content
- 🎯 **Keyword Matching**: Regex-based smart comparison
- 📊 **ATS Scoring**: `Score = Matched/Total × 100`
- 🗄️ **SQLite Database**: Fast & lightweight storage
- 📊 **Excel Export**: Download results in `.xlsx`
- 📈 **Power BI Dashboard**: Visual analytics

---

### 🛠️ Tech Stack
| 🧩 Component | 💻 Technology |
|-----------|--------------|
| 🐍 Language | Python 3.10+ |
| 📚 Libraries | pdfplumber, pandas, sqlite3, re |
| 🗄️ Database | SQLite3 |
| 📊 Visualization | Power BI, Excel |

---

### 🚀 How to Run
1. **Clone the repository** 📥
```bash
git clone https://github.com/your-username/ATS-Scanner.git
cd ATS-ScannerInstall dependencies 📦bashpip install -r requirements.txtRun the scanner ▶️bashpython ats_scanner.py📸 Sample OutputjavascriptEnter Job Description: Python Developer with SQL, Flask, AWS
Enter Resume Path: sri_resume.pdf

✅ Result:
Matched Keywords: Python, SQL, Flask
Missing Keywords: AWS, Docker
🎯 ATS Score: 80%
✅ Status: Recommended for Interview📊 Results Table📄 Resume Name🎯 ATS Score🔑 Matched Skills✅ Statussri_resume.pdf80% 🟢Python, SQL, Pandas, FlaskGood Matchjohn_resume.pdf72% 🟡Python, SQLNeeds Improvementpriya_resume.pdf68% 🔴Java, SQLLow Match🌍 Social Impact
🎓 For Students: Know what recruiters want, improve resumes⏱️ For HR: Reduce screening time 90% ⚡⚖️ For Companies: Skill-based hiring, reduce bias📁 Project StructurejavascriptATS-Scanner/
├── ats_scanner.py          # 🐍 Main Python code
├── ats_scanner.db          # 🗄️ SQLite database
├── requirements.txt        # 📦 Dependencies
├── README.md              # 📝 Documentation
└── screenshots/           # 📸 Output screenshots🔮 Future Improvements

