import json

from setting import CANDIDATES_PATH, SETTINGS_PATH

def get_settings():
    with open(SETTINGS_PATH, "r", encoding="UTF-8") as f:
        data_json = json.load(f)
    return data_json



def get_candidates():
    with open(CANDIDATES_PATH, "r", encoding="UTF-8") as f:
        data_json = json.load(f)
    return data_json


def get_candidates_by_cid(cid):
    candidates = get_candidates()
    for candidate in candidates:
        if candidate.get("id") == cid:
            return candidate


def search_candidates_by_name(name):

    settings = get_settings()
    case_sensitive = settings.get["case-sensitive"]

    candidates = get_candidates()
    candidates_match = []

    for candidate in candidates:

        if name in candidate.get["name"]:
            candidates_match.append(candidate)
            continue

        if not case_sensitive:
            if name.lower() in candidate.get["name"].lower():
                candidates_match.append(candidate)

    return candidates_match


def get_candidates_by_skill(skill_name):

    settings = get_settings()
    limit = settings.get("limit", 3)

    candidates = get_candidates()
    candidates_match = []

    skill_name = skill_name.lower()

    for candidate in candidates:

        skills = candidate["skills"].lower().split(", ")

        if skill_name in skills:
            candidates_match.append(candidate)


    return candidates_match[:limit]
