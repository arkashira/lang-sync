import json
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class TranslationJob:
    id: int
    code_merge_id: int
    status: str

class AutoTransCI:
    def __init__(self):
        self.translation_jobs = []

    def trigger_translation_job(self, code_merge_id: int) -> TranslationJob:
        job = TranslationJob(id=len(self.translation_jobs) + 1, code_merge_id=code_merge_id, status="pending")
        self.translation_jobs.append(job)
        return job

    def get_translation_job(self, job_id: int) -> TranslationJob:
        for job in self.translation_jobs:
            if job.id == job_id:
                return job
        raise ValueError("Job not found")

    def update_translation_job_status(self, job_id: int, status: str) -> None:
        for job in self.translation_jobs:
            if job.id == job_id:
                job.status = status
                return
        raise ValueError("Job not found")

    def list_available_actions(self) -> List[str]:
        return ["autotrans-ci"]

    def execute_autotrans_ci_action(self, code_merge_id: int) -> Dict[str, str]:
        job = self.trigger_translation_job(code_merge_id)
        self.update_translation_job_status(job.id, "success")
        return {"status": "success", "job_id": str(job.id)}
