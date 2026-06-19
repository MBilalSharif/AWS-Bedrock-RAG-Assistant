import boto3

client = boto3.client(
    service_name="bedrock-agent-runtime",
    region_name="us-east-1"
)

kb_id = "######"

questions = [
    "How many days of maternity leave does the company offer?"

]


response = bedrock.invoke_model(
    modelId="anthropic.claude-3-haiku-20240307-v1:0",
    body={"prompt": "What is the company's leave policy?"}
)



for input_text in questions:
    print(f"\n=== QUESTION ===\n{input_text}")
    try:
        response = client.retrieve_and_generate(
            input={
                "text": input_text
            },
            retrieveAndGenerateConfiguration={
                "type": "KNOWLEDGE_BASE",
                "knowledgeBaseConfiguration": {
                    "knowledgeBaseId": kb_id,
                    "modelArn": "arn:aws:bedrock:us-east-1::foundation-model/anthropic.claude-3-haiku-20240307-v1:0",
                      "generationConfiguration": {
                        "promptTemplate": {
                            "textPromptTemplate": (
                                "You are a strict assistant. ONLY use the information "
                                "in the search results below to answer.\n"
                                "If the search results do not contain enough information "
                                "to answer the question, respond exactly with: "
                                "\"I don't know based on the provided documents.\"\n"
                                "Do NOT use any outside knowledge, even if you know the answer.\n\n"
                                "<search_results>\n$search_results$\n</search_results>\n\n"
                                "Question: $query$"
                            )
                        }
                      }
                }
            }
        )

        answer = response["output"]["text"]
        print("\n=== ANSWER ===")
        print(answer)

      
    except Exception as e:
        print(f"Error: {e}")





