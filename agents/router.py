from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from agents.profile_agent import get_profile_data, get_about  # ✅ This is correct
from agents.github_agent import fetch_github_projects
from agents.docker_agent import fetch_docker_repos


# Groq LLM Setup
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key="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",
    temperature=0.0,
    max_retries=2
)

def ask_agent(query: str):
    print("📝 ask_agent received query:", query)

    # 👉 Direct answers for "who is Prajwal" type questions
    if any(phrase in query.lower() for phrase in ["who is prajwal", "tell me about prajwal", "who is he", "who is this", "who is prajwal b", "tell about him"]):
        return get_about()

    # Load dynamic context
    profile = get_profile_data()
    github_projects = fetch_github_projects()
    docker_projects = fetch_docker_repos()

    # Build the prompt
    prompt_template = PromptTemplate(
        input_variables=["profile", "github_projects", "docker_projects", "question"],
        template="""
You are Prajwal's personal AI assistant.

Important:
- The user is always asking about Prajwal B.
- If the user says "this", "he", "him", or "his", assume they are referring to Prajwal B.
- If the user provides an incomplete sentence, assume they are asking about Prajwal.
- If the user provides an email, phone number, or GitHub/DockerHub link directly, confirm it belongs to Prajwal and provide more information if possible.
- If you don't have an answer, politely say: "Sorry, no data available."

Prajwal's Profile:
{profile}

GitHub Projects:
{github_projects}

DockerHub Repositories:
{docker_projects}

User Question: {question}

Assistant:
"""
    )

    prompt = prompt_template.format(
        profile=profile,
        github_projects=github_projects,
        docker_projects=docker_projects,
        question=query
    )

    try:
        response = llm.invoke(prompt)

        # Safely handle None responses
        if response is None or response.content is None or response.content.strip() == "":
            print("⚠️ Model returned empty response.")
            return "Sorry, I couldn’t find any information to answer your question."

        print("🧠 Model response:", response.content)
        return response.content

    except Exception as e:
        print("❌ ask_agent error:", str(e))
        return f"Error: {str(e)}"
