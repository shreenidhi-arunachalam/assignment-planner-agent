import os
from dotenv import load_dotenv
from google import genai

load_dotenv()


client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))


def planner_agent(text):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
You are a highly structured academic planner agent.

Your job:
- Break the assignment into clear tasks
- Create a study/execution plan
- Include realistic time estimates
- Make it specific to the assignment type

Assignment:
{text}

Return in this format:

PRIORITY TASKS:
...

PLAN:
...

TIME ESTIMATE:
...
"""
    )
    return response.text



def critic_agent(plan_text):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
You are a strict academic reviewer (critic agent).

Your job is to review the plan below and find:
- unrealistic time estimates
- missing steps
- poor structure
- weak planning assumptions
- anything a top university student would improve

Then rewrite ONLY the improved version.

PLAN TO REVIEW:
{plan_text}

Return format:

ISSUES FOUND:
...

IMPROVED PLAN:
...
"""
    )
    return response.text



def final_refiner(improved_plan):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
You are a final polish agent.

Take this improved plan and:
- make it more human
- remove repetition
- improve clarity
- keep structure clean and readable

PLAN:
{improved_plan}

Return final polished version only.
"""
    )
    return response.text


def get_plan(text):
    # Step 1: Planner
    plan = planner_agent(text)

    # Step 2: Critic
    critique_output = critic_agent(plan)

    # Split critique + improved plan
    if "IMPROVED PLAN:" in critique_output:
        improved_plan = critique_output.split("IMPROVED PLAN:")[-1]
    else:
        improved_plan = critique_output

    # Step 3: Final refinement
    final_plan = final_refiner(improved_plan)

    # Return structured output for UI
    return {
        "raw_plan": plan,
        "critique": critique_output,
        "final_plan": final_plan
    }



if __name__ == "__main__":
    print("\n AI Assignment Planner Agent (Multi-Agent System v3)\n")

    user_input = input("Enter your assignments:\n")

    print("\nGenerating plan...\n")

    result = get_plan(user_input)

    print("\n================ FINAL PLAN ================\n")
    print(result["final_plan"])

    print("\n================ CRITIC OUTPUT ================\n")
    print(result["critique"])