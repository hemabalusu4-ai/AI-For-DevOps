# Project: Gen-AI Assisted DevOps Pipeline  
**Purpose:** Use a Generative AI model + DevOps pipeline to automate code review, deployment, monitoring & remediation.  
**Difficulty:** Intermediate → Advanced  
**Stack:**  
- Repository + CI/CD: GitHub & GitHub Actions  
- GenAI: (e.g., OpenAI API / Azure OpenAI)  
- Infrastructure/Deployment: (e.g., Docker → Kubernetes or Cloud Run)  
- Monitoring: Logs & Metrics → Anomaly Detection  
- Remediation: Automated workflow triggered on anomaly or GenAI decision  

## Setup & Run  
1. Clone this repo into your portal under `projects/project-005-genai-devops/`.  
2. In `instrumentation/`, deploy or set up your sample service.  
3. Configure logs & metrics ingestion in `logs-metrics/`.  
4. In `genai-analysis/`, adapt the model and scripts for code review or alert analysis.  
5. In `remediation/`, set up scripts or workflows that get triggered on analysis results.  
6. Push code → triggers `genai-devops-pipeline.yml` → runs CI/CD + GenAI step + deployment + monitoring + remediation.  

## Folder Overview  
- `instrumentation/` → Code for service(s) you’ll manage  
- `logs-metrics/` → Setup for collecting operational data  
- `genai-analysis/` → GenAI logic (prompts, scripts, model)  
- `remediation/` → Auto-heal scripts or workflows  
- `infra/` → Infrastructure as Code (IaC) definitions  
- `.github/workflows/` → Pipeline definition  
## Future Enhancements  
- Expand GenAI to auto-generate pipeline definitions  
- Integrate more monitoring sources (traces, events)  
- UI/dashboard for GenAI decisions and remediation history  
