from flask import Flask, request

from utils import get_settings, get_candidates_by_cid, get_candidates, search_candidates_by_name, \
    get_candidates_by_skill

app = Flask(__name__)


@app.route("/")
def page_index():

    settings = get_settings()
    online = settings.get("online", False)
    if online:
        return "Приложение работает"
    return "Приложение не работает"


@app.route("/candidate/<int:cid>")
def page_candidates(cid):
    candidate = get_candidates_by_cid(cid)
    page_content = f"""
    <h1>{candidate["name"]}</h1>
    <p>{candidate["position"]}</p>
    <img src="{candidate["picture"]}" width=200/>
    <p>{candidate["skills"]}</p>
    """

    return page_content


@app.route("/list")
def page_list_of_candidates():
    candidates = get_candidates()

    page_content = "<h1>Все кандидаты</h1>"

    for candidate in candidates:
        page_content += f"""
            <p><a href="/candidate/{candidate["id"]}">{candidate["name"]}</a></p>
            """

    return page_content


@app.route("/search")
def page_search_by_name():

    name = request.args.get("name", "")

    candidates = search_candidates_by_name()
    candidates_count = len(candidates)

    page_content = f"<h1>Найдено кандидатов {candidates_count}</h1>"

    for candidate in candidates:
        page_content += f"""
            <p><a href="/candidate/{candidate["id"]}">{candidate["name"]}</a></p>
            """

    return page_content


@app.route("/skill/<skill_name>")
def page_search_by_skill(skill_name):

    candidates = get_candidates_by_skill(skill_name)
    candidates_count = len(candidates)

    page_content = f"<h1>Найдено кандидатов с навыком {skill_name} : {candidates_count}</h1>"

    for candidate in candidates:
        page_content += f"""
            <p><a href="/candidate/{candidate["id"]}">{candidate["name"]}</a></p>
            """

    return page_content


app.run()