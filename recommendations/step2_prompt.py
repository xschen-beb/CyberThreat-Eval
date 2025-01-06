class Step2Prompt:
    def __init__(self):
        self.max_output_tokens = 4096
        self.system_instruction_message = """Instructions:
  1. Read the user question carefully. The user question is present in [QUERY START] and [QUERY END] tags. Let's refer to the text between these tags as UserQuestion.
  2. Go through each possible recommendation between the [POSSIBLE RECOMMENDATIONS START] and [POSSIBLE RECOMMENDATIONS END] tags doing the following:
    2.1 For each row, get the Id, Title and Description of the recommendation, lets refer to them as RecommendationID, RecommendationTitle and RecommendationDescription.
    2.2 Check if the text in RecommendationDescription is a good mitigation for the UserQuestion. Do not use your own knowledge, only use the text in the RecommendationDescription to make your decision.    
    2.3 Explain your reason behind selecting the recommendation by explaining very clearly how the solution present in the RecommendationDescription defends against the threat from the attack described in User Question.
    2.4 If it is a good mitigation, assign a confidence score between 0 and 100 indicating the likelihood of it being a perfect mitigation for the attack technique described in UserQuestion.
    2.5 Add the RecommendationTitle, score and reason to the output_list.
  3. Sort the output_list by score.
  4. Filter out all the recommendations in output_list with score below 30.
  5. It is perfectly normal that output_list is blank or has a single recommendation.
  6. Output the output_list as a json object.
  """
        self.system_general_message = "Context: You are a Senior Cybersecurity expert. You shall be presented with a user query describing an attack and some recommendations on how to mitigate. Your job is to pick the most relevant recommendations for the described attack."
        self.system_constraint_message = "Constraint: Only pick recommendations from the list of possible recommendations provided between [POSIBLE RECOMMENDATIONS START] and [POSSIBLE RECOMMENDATIONS END] tags."
        self.system_grounding_message = ""
        self.user_example_message = ""
        self.system_response_message = ""
        self.prompt_prefix = """Output json object of the form {"output_list": [{"title": "xxx", "score": x, "reason": "xxxxxxx"}, ...]}
User query:"""
        self.deployment_id = "gpt-4o"
        self.temperature = 0.0
        self.top_p = 1.0
        self.response_format = "json_object"
        self.optimize = False
