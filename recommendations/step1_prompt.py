class Step1Prompt:
    def __init__(self, grounding_data):
        self.max_output_tokens = 4096
        self.system_instruction_message = """Instructions:
  1. Read the list of recommendations Title and Descriptions carefully. List of recommendations are provided between [LIST START] and [LIST END] tags as a markdown table. Let us refer to this table as RecommendationsTable.
  2. Read the user query provided between [QUERY START] and [QUERY END] tags. Let us refer to this query as UserQuestion.
  3. For each row in RecommendationsTable, do the following:
    3.1 Check if the text in the Description column is a good mitigation for the UserQuestion. Do not use your own knowledge, only use the text in the Description column to make your decision.
    3.2 If it is a good mitigation, add the Title of the recommendation to output_list.
  4. Return output_list as a json object.
  """
        self.system_general_message = "Context: You are a Senior Cyber security expert at Microsoft. You are very good at identifying the best recommendation action for a given security attack."
        self.system_constraint_message = "Constraint: Only provide recommendations from the list between [LIST START] and [LIST END] tags."
        self.system_grounding_message = "[LIST START]\n" + grounding_data + "[LIST END]\n"
        self.user_example_message = ""
        self.system_response_message = ""
        self.prompt_prefix = """Output as a json object using the format {"output_list": ["title1", "title2", ...]} User Question:\n"""
        self.deployment_id = "gpt-4o"
        self.temperature = 0.0
        self.top_p = 1.0
        self.response_format = "json_object"
        self.optimize = True
