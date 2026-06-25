from autotrans_ci import AutoTransCI, TranslationJob
import pytest

def test_trigger_translation_job():
    autotrans_ci = AutoTransCI()
    job = autotrans_ci.trigger_translation_job(1)
    assert job.id == 1
    assert job.code_merge_id == 1
    assert job.status == "pending"

def test_get_translation_job():
    autotrans_ci = AutoTransCI()
    job = autotrans_ci.trigger_translation_job(1)
    retrieved_job = autotrans_ci.get_translation_job(job.id)
    assert retrieved_job.id == job.id
    assert retrieved_job.code_merge_id == job.code_merge_id
    assert retrieved_job.status == job.status

def test_update_translation_job_status():
    autotrans_ci = AutoTransCI()
    job = autotrans_ci.trigger_translation_job(1)
    autotrans_ci.update_translation_job_status(job.id, "success")
    retrieved_job = autotrans_ci.get_translation_job(job.id)
    assert retrieved_job.status == "success"

def test_list_available_actions():
    autotrans_ci = AutoTransCI()
    actions = autotrans_ci.list_available_actions()
    assert "autotrans-ci" in actions

def test_execute_autotrans_ci_action():
    autotrans_ci = AutoTransCI()
    result = autotrans_ci.execute_autotrans_ci_action(1)
    assert result["status"] == "success"
    assert result["job_id"] == "1"

def test_execute_autotrans_ci_action_invalid_code_merge_id():
    autotrans_ci = AutoTransCI()
    with pytest.raises(ValueError):
        autotrans_ci.get_translation_job(1)
