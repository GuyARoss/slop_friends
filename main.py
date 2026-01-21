from typing import List
import random
from dataclasses import dataclass
import os

top_30_us_first_names = [
    "Liam",
    "Noah",
    "Oliver",
    "Theodore",
    "James",
    "Henry",
    "Mateo",
    "Elijah",
    "Lucas",
    "William",
    "Olivia",
    "Emma",
    "Amelia",
    "Charlotte",
    "Mia",
    "Sophia",
    "Isabella",
    "Evelyn",
    "Ava",
    "Sofia",
    "Benjamin",
    "Alexander",
    "Michael",
    "Daniel",
    "Logan",
    "Sebastian",
    "Jack",
    "Owen",
    "Ella",
    "Harper"
]


def invoke_codex(path: str, agent_info: str, prompt: str) -> str:
    import subprocess

    input_payload = f"{agent_info}\n\n{prompt}\n"

    try:
        completed = subprocess.run(
            ["codex", "exec", "--yolo", "--skip-git-repo-check", "--cd", path],
            input=input_payload,
            capture_output=True,
            text=True,
            check=True,
        )
    except FileNotFoundError as e:
        raise RuntimeError("`codex` executable not found on PATH") from e
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"codex invocation failed: {e.stderr.strip()}") from e

    return completed.stdout


project_manager = """
You are Kert a project manager of the project defined in ./project/problem.txt. Your goal is to overlook the project and ensure it is moving forward. 

You never solve the problem directly, rather manage a productive human team of subject matter experts. 
"""

project_logs = """
If you ever have any notes you need to keep solely for yourself, (to track work, remember where you are at, etx) you can keep a copy at ./project/notes/<your name>.txt

If you have larger project wide docs, you can put them in ./project/docs/
"""

project_manager_subject_mater = """
You are not a subject matter expert. You can communicate with subject matter experts on your team. 

At any time, you can find a list of subject matter experts in the project ./project/team-roles.txt file.
"""

project_manager_create_roles = """
Please take a look at the provided problem file in ./project/problem.txt. 

Your team is currently empty. You have the budget to hire 5 max subject matter experts.

Please list the subject matter experts you require for this objective in ./project/team-roles.txt and we will hire them.

Team Roles.txt should follow a bullet point structure. Where each bullet is a different role you require.
"""

chatroom = """
The chat room is a stored text file ./project/chatroom.txt where you can message and respond to your human team. 

You can always @ others if you have questions, and they will respond as soon as possible. Always make your new chat entry at the bottom of the file.

The format to send a message should be:

---

[Name] (Role): 

Message 

---

"""

pm_assess = """
Assess where your team is at with the project you are working on.

If it is complete, and can be verified, create a file ./project/results.txt that explains the details of your teams work and how it was completed.

If it is not complete, continue delegating via the chatroom what needs to be completed and why.
"""

team_hired = """
Your team just got hired. You can view your full team in ./project/team-roles.txt. Say Hello and introduce yourself in the chatroom.

You should also start designating who works on what in this chat as well. 
"""

role = """
You are a highly specialized and curious individual in your role. Working on the problem defined in ./project/problem.txt with your team defined in ./project/team-roles.txt.

There is also a chatroom for you to talk to your human team if you have any questions/comments/concerns.

Perform that tasks/duties defined by your PM in the chatroom.

If you are caught up on your work, feel free to do nothing. 
"""

@dataclass
class Position:
    name: str
    role: str
    role_full: str

    def agent_info(self) -> str:
        return f"Your name is {self.name} a {self.role}"

def read_roles(project_dir) -> List[Position]:
    if not os.path.exists(project_dir+"/project/team-roles.txt"):
        return []

    pos = []
    with open(project_dir+"/project/team-roles.txt") as f:
        for l in f.readlines():
            l = l.replace("- ", "")

            name = random.choice(top_30_us_first_names)
            pos.append(Position(name, l.split(':')[0], l))

    return pos

def main(project_dir: str):
    roles = read_roles(project_dir)

    if len(roles) == 0:
        invoke_codex(project_dir,project_manager, project_manager_create_roles)
        roles = read_roles(project_dir)

    print(roles)

    invoke_codex(project_dir, project_manager, team_hired+chatroom)

    while True:
        if os.path.exists(project_dir+"/project/results.txt"):
            break

        for r in roles:
            invoke_codex(project_dir, r.agent_info(), role+"\n"+chatroom+"\n"+project_logs)

        invoke_codex(project_dir, project_manager, pm_assess+"\n"+chatroom+"\n"+project_logs)

    pass

if __name__ == "__main__":
    import sys
    main(sys.argv[1])
