from langchain_core.prompts import ChatPromptTemplate

# Define the system prompt
system_prompt = (
    "You are an assistant for question-answering tasks. "
    "Use the following pieces of retrieved context to answer "
    "the question. If you do not know the answer, say that you "
    "do not know. Use three sentences maximum and keep the answer concise.\n\n"
    "{context}"
)

# Create the prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)
